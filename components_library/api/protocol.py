"""Protocol definition for API clients.

Defines the interface that all API client versions (v2, v3, etc.) must implement.
This ensures that switching between API versions is a drop-in replacement.

Usage:
    from components_library.api import ApiClientProtocol

    def my_service(client: ApiClientProtocol):
        # Works with any API version
        response = await client.get("/endpoint")
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol, runtime_checkable

if TYPE_CHECKING:
    from .types import ApiResponse


@runtime_checkable
class ApiClientProtocol(Protocol):
    """Protocol defining the interface for API clients.

    All API client versions (v2, v3, etc.) must implement this interface
    to ensure they can be used interchangeably.

    Attributes:
        base_url: The base URL for API requests
        timeout: Request timeout in seconds
    """

    base_url: str
    timeout: int

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
        ...

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
        ...

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
        ...

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
        ...
