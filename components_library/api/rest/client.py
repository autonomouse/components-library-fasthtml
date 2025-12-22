"""REST API client implementation.

Provides an async HTTP client for REST APIs. The client requires
explicit configuration (base_url) following dependency injection principles -
it does not read from application settings or environment variables.

Usage:
    from components_library.api.rest import ApiClient

    # Application creates configured instance
    client = ApiClient(
        base_url="https://api.example.com",
        timeout=30,
    )

    # Make requests
    response = await client.get("/concepts", params={"q": "cancer"})
    if isinstance(response, ApiSuccess):
        concepts = response.data
    else:
        print(f"Error: {response.error.message}")
"""

from __future__ import annotations

from typing import Any

import httpx

from ..types import ApiError, ApiFailure, ApiResponse, ApiSuccess


class ApiClient:
    """Async HTTP client for REST APIs.

    This client implements the ApiClientProtocol and can be used
    with any REST API endpoint.

    Attributes:
        base_url: Base URL for API requests (required)
        timeout: Request timeout in seconds (default: 30)

    Example:
        # In your application's service layer
        from components_library.api.rest import ApiClient
        from myapp.config import settings

        client = ApiClient(
            base_url=settings.api_base_url,
            timeout=settings.api_timeout,
        )
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
    ) -> None:
        """Initialize the API client.

        Args:
            base_url: Base URL for API requests (required, no default)
            timeout: Request timeout in seconds

        Raises:
            ValueError: If base_url is empty
        """
        if not base_url:
            raise ValueError("base_url is required")

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    async def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        access_token: str | None = None,
        api_key: str | None = None,
    ) -> ApiResponse[Any]:
        """Make a GET request to the API.

        Args:
            endpoint: API endpoint path (e.g., "/concepts")
            params: Query parameters
            access_token: Bearer token for authentication (OAuth2)
            api_key: API key for authentication (X-API-Key header)

        Returns:
            ApiResponse containing data or error
        """
        return await self._request(
            "GET", endpoint, params=params, access_token=access_token, api_key=api_key
        )

    async def post(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        access_token: str | None = None,
        api_key: str | None = None,
    ) -> ApiResponse[Any]:
        """Make a POST request to the API.

        Args:
            endpoint: API endpoint path
            data: Request body data (JSON)
            params: Query parameters
            access_token: Bearer token for authentication (OAuth2)
            api_key: API key for authentication (X-API-Key header)

        Returns:
            ApiResponse containing data or error
        """
        return await self._request(
            "POST", endpoint, data=data, params=params, access_token=access_token, api_key=api_key
        )

    async def put(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        access_token: str | None = None,
        api_key: str | None = None,
    ) -> ApiResponse[Any]:
        """Make a PUT request to the API.

        Args:
            endpoint: API endpoint path
            data: Request body data (JSON)
            params: Query parameters
            access_token: Bearer token for authentication (OAuth2)
            api_key: API key for authentication (X-API-Key header)

        Returns:
            ApiResponse containing data or error
        """
        return await self._request(
            "PUT", endpoint, data=data, params=params, access_token=access_token, api_key=api_key
        )

    async def delete(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        access_token: str | None = None,
        api_key: str | None = None,
    ) -> ApiResponse[Any]:
        """Make a DELETE request to the API.

        Args:
            endpoint: API endpoint path
            params: Query parameters
            access_token: Bearer token for authentication (OAuth2)
            api_key: API key for authentication (X-API-Key header)

        Returns:
            ApiResponse containing data or error
        """
        return await self._request(
            "DELETE", endpoint, params=params, access_token=access_token, api_key=api_key
        )

    async def _request(
        self,
        method: str,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        access_token: str | None = None,
        api_key: str | None = None,
    ) -> ApiResponse[Any]:
        """Internal method to make HTTP requests.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path
            data: Request body data (JSON)
            params: Query parameters
            access_token: Bearer token for authentication (OAuth2)
            api_key: API key for authentication (X-API-Key header)

        Returns:
            ApiResponse containing data or error
        """
        url = f"{self.base_url}{endpoint}"
        headers = self._build_headers(access_token, api_key)

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.request(
                    method,
                    url,
                    json=data if data else None,
                    params=params,
                    headers=headers,
                )

                if response.status_code >= 400:
                    return self._handle_error_response(response)

                return ApiSuccess(data=response.json())

        except httpx.TimeoutException:
            return ApiFailure(
                error=ApiError(
                    message="Request timeout",
                    status=408,
                )
            )
        except httpx.RequestError as e:
            return ApiFailure(
                error=ApiError(
                    message=f"Network error: {e!s}",
                    status=0,
                    details=str(e),
                )
            )

    def _build_headers(self, access_token: str | None, api_key: str | None) -> dict[str, str]:
        """Build request headers.

        Args:
            access_token: Optional bearer token (OAuth2)
            api_key: Optional API key (X-API-Key header)

        Returns:
            Headers dictionary
        """
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if access_token:
            headers["Authorization"] = f"Bearer {access_token}"
        if api_key:
            headers["X-API-Key"] = api_key
        return headers

    def _handle_error_response(self, response: httpx.Response) -> ApiFailure:
        """Handle HTTP error responses.

        Args:
            response: The HTTP response

        Returns:
            ApiFailure with error details
        """
        try:
            error_data = response.json()
            message = error_data.get("message", f"HTTP {response.status_code}")
        except Exception:
            message = f"HTTP {response.status_code}: {response.reason_phrase}"

        return ApiFailure(
            error=ApiError(
                message=message,
                status=response.status_code,
            )
        )
