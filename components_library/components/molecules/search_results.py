"""Search results molecule - Display search results with touch optimization."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ..atoms import empty_state, hstack, text, vstack
from .result_card import result_card


def search_results(
    results: list[dict[str, Any]],
    query: str | None = None,
    result_count: int | None = None,
    item_type: str = "item",
    id_field: str = "id",
    name_field: str = "name",
    **kwargs: Any,
) -> Div:
    """
    Search results molecule displaying search results.

    Shows results in a touch-optimized format with clickable items.
    Handles empty states and provides result count information.

    Args:
        results: List of data dictionaries
        query: Search query that produced these results
        result_count: Total number of results (if different from len(results))
        item_type: Type of items being displayed (default: "item")
        id_field: Field name for item ID (default: "id")
        name_field: Field name for item name (default: "name")
        **kwargs: Additional HTML attributes

    Returns:
        Search results component

    Example:
        >>> results = [
        ...     {"id": 1, "name": "First Item"},
        ...     {"id": 2, "name": "Second Item"},
        ... ]
        >>> search_results(results, query="first")
    """
    if not results:
        return _empty_results(query, item_type)

    # Use provided count or calculate from results
    count = result_count if result_count is not None else len(results)

    return Div(
        vstack(
            # Results header
            _results_header(count, query, item_type),
            # Results grid
            _results_grid(results, id_field, name_field),
            gap=4,
        ),
        cls="search-results",
        **kwargs,
    )


def _empty_results(query: str | None = None, item_type: str = "item") -> Div:
    """Create empty results state."""
    message = f"No {item_type}s found"
    description = (
        f"No {item_type}s match your search for '{query}'"
        if query
        else f"No {item_type}s available"
    )

    return empty_state(
        message=message,
        description=description,
        cls="empty-search-results",
    )


def _results_header(count: int, query: str | None = None, item_type: str = "item") -> Div:
    """Create results header with count and query info."""
    from ..atoms import heading

    header_text = f"{count} {item_type}{'s' if count != 1 else ''} found"
    if query:
        header_text += f" for '{query}'"

    return hstack(
        heading(header_text, level=3),
        text(f"Click any {item_type} to view details", variant="helper"),
        justify="between",
        align="center",
        cls="results-header",
    )


def _results_grid(results: list[dict[str, Any]], id_field: str, name_field: str) -> Div:
    """Create responsive grid layout for search results."""
    return Div(
        *[_result_item(result, id_field, name_field) for result in results],
        cls="search-results-grid",
    )


def _result_item(data: dict[str, Any], id_field: str, name_field: str) -> Div:
    """Create individual result item."""
    item_id = data.get(id_field, "Unknown")
    item_name = data.get(name_field, "Unknown Item")
    record_id = data.get("record_id", data.get("id", 0))

    return result_card(
        item_id=item_id,
        item_name=item_name,
        record_id=record_id,
        cls="search-result-item",
    )
