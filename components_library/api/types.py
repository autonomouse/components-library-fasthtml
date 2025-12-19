"""Shared API response types for API clients.

These types provide a consistent interface for handling API responses
across different API versions (v2, v3, etc.). All API clients should
return ApiResponse[T] for consistent error handling.

Usage:
    from components_library.api import ApiResponse, ApiSuccess, ApiFailure, ApiError

    async def fetch_data() -> ApiResponse[dict]:
        try:
            data = await client.get("/endpoint")
            return ApiSuccess(data=data)
        except Exception as e:
            return ApiFailure(error=ApiError(message=str(e), status=500))

    # Pattern matching on response
    response = await fetch_data()
    if isinstance(response, ApiSuccess):
        process(response.data)
    else:
        handle_error(response.error)
"""

from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ApiError(BaseModel):
    """API error details.

    Attributes:
        message: Human-readable error message
        status: HTTP status code (0 for network errors)
        details: Additional error details (optional)
    """

    message: str
    status: int
    details: Any | None = None


class ApiSuccess(BaseModel, Generic[T]):
    """Successful API response wrapper.

    Attributes:
        data: The response data of type T
    """

    data: T


class ApiFailure(BaseModel):
    """Failed API response wrapper.

    Attributes:
        error: The error details
    """

    error: ApiError


# Union type for API responses - use this as return type
ApiResponse = ApiSuccess[T] | ApiFailure
