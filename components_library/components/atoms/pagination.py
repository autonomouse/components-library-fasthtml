"""Pagination component - Page navigation."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Button, Div, Span

from ...utils import merge_classes


def pagination(
    current_page: int,
    total_pages: int,
    base_url: str | None = None,
    hx_get_url: str | None = None,
    hx_target: str | None = None,
    hx_swap: str = "innerHTML",
    show_first_last: bool = True,
    show_prev_next: bool = True,
    max_visible: int = 7,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Pagination component for page navigation.

    Supports two navigation modes:
    1. URL-based: Use `base_url` for standard anchor links
    2. HTMX-based: Use `hx_get_url` for dynamic partial updates

    Args:
        current_page: Current page number (1-indexed)
        total_pages: Total number of pages
        base_url: Base URL for page links (e.g., "/items?page=")
        hx_get_url: HTMX endpoint for page changes (e.g., "/items?page=")
        hx_target: HTMX target selector for response
        hx_swap: HTMX swap method (default: innerHTML)
        show_first_last: Whether to show first/last buttons
        show_prev_next: Whether to show prev/next buttons
        max_visible: Maximum number of page buttons to show
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with pagination

    Example:
        >>> pagination(current_page=3, total_pages=10, base_url="/tests?page=")
        >>> pagination(
        ...     current_page=5,
        ...     total_pages=20,
        ...     hx_get_url="/items?page=",
        ...     hx_target="#results"
        ... )
    """
    css_class = merge_classes("pagination", cls)

    elements = []

    def create_page_button(page: int, text: str | None = None, disabled: bool = False) -> Any:
        """Helper to create a page button."""
        display_text = text if text else str(page)
        is_current = page == current_page

        if disabled or is_current:
            return Span(
                display_text,
                cls="pagination-item"
                + (" pagination-item-active" if is_current else " pagination-item-disabled"),
                style="cursor: not-allowed; opacity: 0.5;" if disabled else None,
            )

        if base_url:
            return A(
                display_text,
                href=f"{base_url}{page}",
                cls="pagination-item pagination-link",
            )
        elif hx_get_url:
            # HTMX-based pagination (no JavaScript)
            hx_attrs = {
                "hx-get": f"{hx_get_url}{page}",
                "hx-swap": hx_swap,
            }
            if hx_target:
                hx_attrs["hx-target"] = hx_target
            return Button(
                display_text,
                type="button",
                cls="pagination-item pagination-link",
                **hx_attrs,
            )
        else:
            return Span(display_text, cls="pagination-item")

    # First button
    if show_first_last:
        elements.append(create_page_button(1, "«", disabled=current_page == 1))

    # Previous button
    if show_prev_next:
        elements.append(
            create_page_button(max(1, current_page - 1), "‹", disabled=current_page == 1)
        )

    # Calculate visible page range
    half_visible = max_visible // 2
    start_page = max(1, current_page - half_visible)
    end_page = min(total_pages, start_page + max_visible - 1)

    # Adjust start if end is at boundary
    if end_page == total_pages:
        start_page = max(1, end_page - max_visible + 1)

    # Ellipsis before
    if start_page > 1:
        elements.append(Span("...", cls="pagination-ellipsis"))

    # Page numbers
    for page in range(start_page, end_page + 1):
        elements.append(create_page_button(page))

    # Ellipsis after
    if end_page < total_pages:
        elements.append(Span("...", cls="pagination-ellipsis"))

    # Next button
    if show_prev_next:
        elements.append(
            create_page_button(
                min(total_pages, current_page + 1),
                "›",
                disabled=current_page == total_pages,
            )
        )

    # Last button
    if show_first_last:
        elements.append(create_page_button(total_pages, "»", disabled=current_page == total_pages))

    return Div(*elements, cls=css_class, **kwargs)
