"""API client library.

Provides versioned API clients for the platform. Each API version
has its own client implementation that follows the same protocol, enabling
drop-in replacement when upgrading.

Usage:
    # Import shared types
    from components_library.api import ApiResponse, ApiSuccess, ApiFailure, ApiError

    # Import protocol for type hints
    from components_library.api import ApiClientProtocol

    # Import version-specific client
    from components_library.api.v2 import ApiClient

    # Create configured client (dependency injection)
    client = ApiClient(base_url="https://api.example.com/v2")

    # Use in services
    async def fetch_concepts(client: ApiClientProtocol, query: str):
        response = await client.get("/concepts", params={"q": query})
        if isinstance(response, ApiSuccess):
            return response.data
        raise Exception(response.error.message)

Available Versions:
    - v2: Current production API (components_library.api.v2)
    - v3: Coming soon - will be drop-in replacement for v2
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
