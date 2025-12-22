"""API client library.

Provides API clients that follow a common protocol, enabling
consistent usage patterns across different implementations.

Usage:
    # Import shared types
    from components_library.api import ApiResponse, ApiSuccess, ApiFailure, ApiError

    # Import protocol for type hints
    from components_library.api import ApiClientProtocol

    # Import REST client
    from components_library.api.rest import ApiClient

    # Create configured client (dependency injection)
    client = ApiClient(base_url="https://api.example.com")

    # Use in services
    async def fetch_concepts(client: ApiClientProtocol, query: str):
        response = await client.get("/concepts", params={"q": query})
        if isinstance(response, ApiSuccess):
            return response.data
        raise Exception(response.error.message)

Available Clients:
    - rest: HTTP/REST client (components_library.api.rest)
"""

from .protocol import ApiClientProtocol
from .types import ApiError, ApiFailure, ApiResponse, ApiSuccess

__all__ = [
    "ApiClientProtocol",
    "ApiError",
    "ApiFailure",
    "ApiResponse",
    "ApiSuccess",
]
