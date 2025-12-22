"""Concepts service for searching concepts via the API."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import BaseModel, Field

from ..api import ApiFailure, ApiSuccess

if TYPE_CHECKING:
    from ..api import ApiClientProtocol, ApiResponse


class Concept(BaseModel):
    """Concept from the ontology API."""

    id: str
    name: str
    type: str | None = None
    description: str | None = None
    synonyms: list[str] = Field(default_factory=list)


class ConceptsService:
    """Service for searching concepts via the API.

    This service provides methods for searching and retrieving concepts
    from the ontology API, useful for autocomplete and entity lookup.

    Example:
        from components_library.api.rest import ApiClient
        from components_library.services import ConceptsService

        client = ApiClient(base_url="https://api.example.com")
        concepts = ConceptsService(client)

        # Search for concepts
        results = await concepts.search("BRCA1", access_token=token)
        if isinstance(results, ApiSuccess):
            for concept in results.data:
                print(f"{concept.name} ({concept.type})")
    """

    DEFAULT_LIMIT: ClassVar[int] = 15
    MIN_QUERY_LENGTH: ClassVar[int] = 2

    def __init__(self, client: ApiClientProtocol) -> None:
        """Initialize the concepts service.

        Args:
            client: API client instance for making requests
        """
        self.client = client

    async def search(
        self,
        query: str,
        access_token: str | None = None,
        limit: int | None = None,
        skip: int = 0,
        concept_types: list[str] | None = None,
    ) -> ApiResponse[list[Concept]]:
        """Search for concepts matching the query.

        Args:
            query: Search query string (minimum 2 characters)
            access_token: Bearer token for authentication
            limit: Maximum number of results (default: 15)
            skip: Number of results to skip
            concept_types: Optional list of concept types to filter by

        Returns:
            ApiResponse containing list of Concept or error
        """
        # Enforce minimum query length
        if not query or len(query.strip()) < self.MIN_QUERY_LENGTH:
            return ApiSuccess(data=[])

        params: dict[str, Any] = {
            "q": query.strip(),
            "limit": limit or self.DEFAULT_LIMIT,
            "skip": skip,
        }

        # Add type filter if provided
        if concept_types:
            params["type"] = concept_types

        response = await self.client.get(
            "/concepts",
            params=params,
            access_token=access_token,
        )

        if isinstance(response, ApiFailure):
            return response

        # Transform response data
        concepts_data = response.data.get("data", [])
        concepts = [self._transform_concept(c) for c in concepts_data]
        return ApiSuccess(data=concepts)

    async def get_by_ids(
        self,
        concept_ids: list[str],
        access_token: str | None = None,
    ) -> ApiResponse[dict[str, Concept]]:
        """Look up multiple concepts by their IDs.

        Uses the /concepts endpoint with concept_id query parameter.

        Args:
            concept_ids: List of concept IDs to look up
            access_token: Bearer token for authentication

        Returns:
            ApiResponse containing dict mapping concept ID to Concept, or error
        """
        if not concept_ids:
            return ApiSuccess(data={})

        # Use the /concepts endpoint with concept_id parameter for batch lookup
        response = await self.client.get(
            "/concepts",
            params={"concept_id": concept_ids},
            access_token=access_token,
        )

        if isinstance(response, ApiFailure):
            return response

        # Transform response data to dict mapping ID to Concept
        concepts_data = response.data.get("data", [])
        concepts_map = {
            c.get("id", ""): self._transform_concept(c) for c in concepts_data if c.get("id")
        }
        return ApiSuccess(data=concepts_map)

    def _transform_concept(self, data: dict[str, Any]) -> Concept:
        """Transform raw API concept data to Concept model."""
        return Concept(
            id=data.get("id", ""),
            name=data.get("name", ""),
            type=data.get("type"),
            description=data.get("description"),
            synonyms=data.get("synonyms", []),
        )
