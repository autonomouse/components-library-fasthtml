"""API v2 client.

Usage:
    from components_library.api.v2 import ApiClient

    # Create client with explicit configuration (dependency injection)
    client = ApiClient(base_url="https://api.example.com/v2", timeout=30)

    # Use in async context
    response = await client.get("/concepts", params={"q": "BRCA1"})
"""

from .client import ApiClient

__all__ = ["ApiClient"]
