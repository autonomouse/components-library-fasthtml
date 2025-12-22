"""REST API client.

Usage:
    from components_library.api.rest import ApiClient

    # Create client with explicit configuration (dependency injection)
    client = ApiClient(base_url="https://api.example.com", timeout=30)

    # Use in async context
    response = await client.get("/concepts", params={"q": "BRCA1"})
"""

from .client import ApiClient

__all__ = ["ApiClient"]
