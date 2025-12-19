"""Reusable services for API interactions.

Provides service classes for common API operations that can be shared
across Labs applications.

Usage:
    from components_library.services import ConceptsService, DocumentsService
    from components_library.api.v2 import ApiClient

    # Create client with your app's settings
    client = ApiClient(base_url="https://api.example.com/v2")

    # Create service instances
    concepts = ConceptsService(client)
    documents = DocumentsService(client)

    # Use in routes
    results = await concepts.search("BRCA1", access_token=token)
"""

from .concepts import Concept, ConceptsService
from .csv_export import csv_response, generate_csv
from .documents import (
    ArticleResult,
    ArticleSearchResults,
    DocumentsService,
    SearchQuery,
    SortType,
    SourceType,
    StudyResult,
)
from .health import register_health_routes

__all__ = [
    # Documents
    "ArticleResult",
    "ArticleSearchResults",
    # Concepts
    "Concept",
    "ConceptsService",
    "DocumentsService",
    "SearchQuery",
    "SortType",
    "SourceType",
    "StudyResult",
    # CSV Export
    "csv_response",
    "generate_csv",
    # Health
    "register_health_routes",
]
