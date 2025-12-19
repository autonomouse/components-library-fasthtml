"""Data table organism - Complete data table with search, filters, and pagination."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from fasthtml.common import Div

from ..atoms import card, empty_state, heading, pagination, vstack
from ..molecules import filter_bar, search_bar


def data_table(
    *rows: Any,
    title: str | None = None,
    search_value: str = "",
    on_search: Callable[[str], None] | None = None,
    result_count: int = 0,
    show_filters: bool = True,
    empty_message: str = "No data available",
    empty_description: str = "Try adjusting your search or filters",
    loading: bool = False,
    **kwargs: Any,
) -> Div:
    """
    Data table organism combining search, filters, table, and pagination.

    Args:
        *rows: Table row components
        title: Optional table title
        search_value: Current search value
        on_search: Callback when search changes
        result_count: Number of results found
        show_filters: Whether to show filter controls
        empty_message: Message when no data
        empty_description: Description when no data
        loading: Whether table is loading
        **kwargs: Additional HTML attributes

    Returns:
        Complete data table organism

    Example:
        >>> data_table(
        ...     *test_rows,
        ...     title="Laboratory Tests",
        ...     search_value="glucose",
        ...     result_count=25
        ... )
    """
    content = []

    # Title
    if title:
        content.append(heading(title, level=2, cls="mb-4"))

    # Search and filters
    if show_filters:
        content.append(
            vstack(
                search_bar(
                    value=search_value,
                    on_search=on_search,
                    placeholder="Search tests...",
                    width="100%",
                ),
                filter_bar(
                    result_count=result_count,
                    on_time_period_change=lambda _: None,  # TODO: Implement
                    on_source_change=lambda _: None,  # TODO: Implement
                ),
                gap=3,
            )
        )

    # Table content
    if loading:
        content.append(
            vstack(
                "Loading...",  # TODO: Use proper loading component
                cls="text-center py-8",
            )
        )
    elif not rows:
        content.append(
            empty_state(
                message=empty_message,
                description=empty_description,
            )
        )
    else:
        # TODO: Add actual table component here
        content.append(
            vstack(
                *rows,
                gap=2,
            )
        )

    # Pagination (if needed)
    if rows and result_count > 10:  # Show pagination if more than 10 results
        content.append(
            pagination(
                current_page=1,  # TODO: Make dynamic
                total_pages=5,  # TODO: Calculate from result_count
            )
        )

    return card(
        vstack(*content, gap=4),
        cls="data-table-organism",
        **kwargs,
    )
