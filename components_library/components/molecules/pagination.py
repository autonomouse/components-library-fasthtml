"""HTMX Pagination molecule - Navigate through paginated results with HTMX."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ..atoms import button, hstack, text


def htmx_pagination(
    current_page: int,
    total_pages: int,
    base_url: str = "",
    **kwargs: Any,
) -> Div:
    """
    HTMX-enabled pagination component for navigating through pages.

    Creates a pagination control with previous/next buttons and page numbers
    using HTMX for seamless navigation without full page reloads.
    Optimized for touch interaction with large touch targets.

    Args:
        current_page: Current page number (1-based)
        total_pages: Total number of pages
        base_url: Base URL for pagination links
        **kwargs: Additional HTML attributes

    Returns:
        Pagination component

    Example:
        >>> htmx_pagination(current_page=2, total_pages=10, base_url="/search")
    """
    if total_pages <= 1:
        return Div()  # No pagination needed

    # Calculate page range to show
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)

    # Ensure we show at least 5 pages if possible
    if end_page - start_page < 4 and total_pages >= 5:
        if start_page == 1:
            end_page = min(total_pages, start_page + 4)
        elif end_page == total_pages:
            start_page = max(1, end_page - 4)

    pages = []

    # Previous button
    if current_page > 1:
        pages.append(
            button(
                "← Previous",
                variant="outline",
                size="md",
                cls="pagination-button touch-target",
                hx_get=f"{base_url}?page={current_page - 1}",
                style="min-width: 44px; min-height: 44px;",
            )
        )
    else:
        pages.append(
            button(
                "← Previous",
                variant="outline",
                size="md",
                disabled=True,
                cls="pagination-button touch-target",
                style="min-width: 44px; min-height: 44px;",
            )
        )

    # First page if not in range
    if start_page > 1:
        pages.append(_page_button(1, current_page, base_url))
        if start_page > 2:
            pages.append(text("...", cls="pagination-ellipsis"))

    # Page numbers
    for page_num in range(start_page, end_page + 1):
        pages.append(_page_button(page_num, current_page, base_url))

    # Last page if not in range
    if end_page < total_pages:
        if end_page < total_pages - 1:
            pages.append(text("...", cls="pagination-ellipsis"))
        pages.append(_page_button(total_pages, current_page, base_url))

    # Next button
    if current_page < total_pages:
        pages.append(
            button(
                "Next →",
                variant="outline",
                size="md",
                cls="pagination-button touch-target",
                hx_get=f"{base_url}?page={current_page + 1}",
                style="min-width: 44px; min-height: 44px;",
            )
        )
    else:
        pages.append(
            button(
                "Next →",
                variant="outline",
                size="md",
                disabled=True,
                cls="pagination-button touch-target",
                style="min-width: 44px; min-height: 44px;",
            )
        )

    return hstack(
        *pages,
        gap=2,
        justify="center",
        align="center",
        cls="pagination",
        **kwargs,
    )


def _page_button(page_num: int, current_page: int, base_url: str) -> Any:
    """Create a page number button."""
    if page_num == current_page:
        return button(
            str(page_num),
            variant="solid",
            color_palette="brand",
            size="md",
            cls="pagination-button touch-target",
            style="min-width: 44px; min-height: 44px;",
        )
    else:
        return button(
            str(page_num),
            variant="outline",
            size="md",
            cls="pagination-button touch-target",
            hx_get=f"{base_url}?page={page_num}",
            style="min-width: 44px; min-height: 44px;",
        )
