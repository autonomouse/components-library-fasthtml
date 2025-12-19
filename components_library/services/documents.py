"""Documents service for searching articles via the API."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Literal

from pydantic import BaseModel, Field

from ..api import ApiError, ApiFailure, ApiSuccess

if TYPE_CHECKING:
    from ..api import ApiClientProtocol, ApiResponse

SourceType = Literal[
    "publications",
    "clinical-trials",
    "preprints",
    "grants",
    "drug-labels",
    "patents",
    "web-articles",
]

SortType = Literal["relevance", "published:asc", "published:desc"]


class StudyResult(BaseModel):
    """Transformed document result for UI display."""

    document_id: str | None = None
    title: str
    authors: str | None = None
    publication_date: str | None = None
    journal: str | None = None
    pmid: str | None = None
    doi: str | None = None
    abstract: str | None = None
    source: str
    relevance_score: float | None = None


class ArticleResult(BaseModel):
    """Article result formatted for components."""

    id: str
    title: str
    authors: str | None = None
    publication_date: str | None = None
    journal: str | None = None
    pmid: str | None = None
    doi: str | None = None
    abstract: str | None = None
    source: str
    relevance_score: float | None = None
    date: str | None = None
    tags: list[str] = Field(default_factory=list)


class SearchQuery(BaseModel):
    """Search query metadata."""

    tokens: list[dict[str, Any]] = Field(default_factory=list)
    filters: dict[str, Any] = Field(default_factory=dict)
    terms: list[str] = Field(default_factory=list)
    search_string: str = ""


class ArticleSearchResults(BaseModel):
    """Complete search results response."""

    query: SearchQuery
    articles: list[ArticleResult] = Field(default_factory=list)
    total_results: int = 0
    total_count: int = 0
    search_timestamp: str = ""
    sort_by: str = "relevance"


class DocumentsService:
    """Service for searching and retrieving documents from the API.

    This service provides methods for searching scientific literature including
    publications, clinical trials, preprints, grants, drug labels, patents,
    and web articles.

    Example:
        from components_library.api.v2 import ApiClient
        from components_library.services import DocumentsService

        client = ApiClient(base_url="https://api.example.com/v2")
        documents = DocumentsService(client)

        # Search for documents
        results = await documents.search(
            "BRCA1 cancer",
            access_token=token,
            sources=["publications", "clinical-trials"],
        )
        if isinstance(results, ApiSuccess):
            for doc in results.data:
                print(f"{doc.title} ({doc.source})")
    """

    DEFAULT_LIMIT: ClassVar[int] = 50
    DEFAULT_SOURCES: ClassVar[list[SourceType]] = [
        "publications",
        "clinical-trials",
        "preprints",
    ]
    DEFAULT_SORT: ClassVar[SortType] = "relevance"

    def __init__(self, client: ApiClientProtocol) -> None:
        """Initialize the documents service.

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
        sources: list[SourceType] | None = None,
        sort: SortType | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> ApiResponse[list[StudyResult]]:
        """Search for documents.

        Args:
            query: Search query string
            access_token: Bearer token for authentication
            limit: Maximum number of results
            skip: Number of results to skip
            sources: Document sources to search
            sort: Sort order
            from_date: Start date filter (YYYY-MM-DD)
            to_date: End date filter (YYYY-MM-DD)

        Returns:
            ApiResponse containing list of StudyResult or error
        """
        if not query or not query.strip():
            return ApiFailure(
                error=ApiError(
                    message="Search query cannot be empty",
                    status=400,
                )
            )

        params: dict[str, Any] = {
            "q": query.strip(),
            "limit": limit or self.DEFAULT_LIMIT,
            "skip": skip,
            "sort": sort or self.DEFAULT_SORT,
        }

        # Add sources
        source_list = sources or self.DEFAULT_SOURCES
        params["source"] = list(source_list)

        # Add date filters
        if from_date:
            params["from_date"] = from_date
        if to_date:
            params["to_date"] = to_date

        response = await self.client.get(
            "/documents",
            params=params,
            access_token=access_token,
        )

        if isinstance(response, ApiFailure):
            return response

        # Transform response data
        documents = response.data.get("data", [])
        results = [self._transform_document(doc) for doc in documents]
        return ApiSuccess(data=results)

    def _transform_document(self, doc: dict[str, Any]) -> StudyResult:
        """Transform raw API document to StudyResult."""
        # Parse authors
        authors = None
        if doc.get("authors"):
            if isinstance(doc["authors"], list):
                author_names = []
                for author in doc["authors"]:
                    if isinstance(author, dict):
                        name = author.get("name") or author.get("given_name") or str(author)
                        author_names.append(name)
                    else:
                        author_names.append(str(author))
                authors = ", ".join(author_names)
            else:
                authors = str(doc["authors"])

        # Extract identifiers from other_ids
        pmid = None
        doi = None
        other_ids = doc.get("other_ids", [])
        if isinstance(other_ids, list):
            for id_entry in other_ids:
                if isinstance(id_entry, dict):
                    id_type = id_entry.get("type") or id_entry.get("namespace")
                    if id_type == "pmid":
                        pmid = id_entry.get("value") or id_entry.get("id")
                    elif id_type == "doi":
                        doi = id_entry.get("value") or id_entry.get("id")

        return StudyResult(
            document_id=doc.get("document_id"),
            title=doc.get("title", ""),
            authors=authors,
            publication_date=doc.get("published"),
            journal=doc.get("journal"),
            pmid=pmid,
            doi=doi,
            abstract=doc.get("snippet"),
            source=doc.get("document_type", "unknown"),
            relevance_score=doc.get("relevance_score"),
        )

    def study_to_article(self, study: StudyResult, index: int = 0) -> ArticleResult:
        """Convert StudyResult to ArticleResult for UI components."""
        # Generate unique ID
        if study.pmid:
            article_id = f"pmid:{study.pmid}"
        elif study.document_id:
            article_id = f"doc:{study.document_id}"
        elif study.doi:
            article_id = f"doi:{study.doi}"
        else:
            article_id = f"doc:fallback_{index}"

        return ArticleResult(
            id=article_id,
            title=study.title,
            authors=study.authors,
            publication_date=study.publication_date,
            journal=study.journal,
            pmid=study.pmid,
            doi=study.doi,
            abstract=study.abstract,
            source=study.source,
            relevance_score=study.relevance_score,
            date=study.publication_date,
            tags=[],
        )

    @staticmethod
    def build_concept_query(
        concepts: list[dict[str, Any]],
        operators: list[str],
    ) -> str:
        """Build search query from concepts and operators.

        Args:
            concepts: List of concept dicts with 'id', 'name', 'type' keys
            operators: List of logical operators ('AND' or 'OR')

        Returns:
            Formatted search query string
        """
        if not concepts:
            return ""

        def format_concept(concept: dict[str, Any]) -> str:
            concept_id = concept.get("id", "")
            concept_type = concept.get("type", "")

            # Use concept_id() syntax for ontology concepts
            if (
                concept_id
                and ":" in concept_id
                and not concept_id.startswith("free_text:")
                and concept_type != "free_text"
            ):
                return f"concept_id({concept_id})"

            # Treat as free text
            return f'"{concept.get("name", "")}"'

        if len(concepts) == 1:
            return format_concept(concepts[0])

        # Build query with operators
        query_parts = [format_concept(concepts[0])]
        for i, concept in enumerate(concepts[1:], start=0):
            operator = operators[i] if i < len(operators) else "AND"
            query_parts.append(f" {operator} {format_concept(concept)}")

        return "".join(query_parts)
