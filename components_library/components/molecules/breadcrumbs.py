"""Breadcrumbs molecule - Navigation breadcrumbs."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Nav, Span
from pydantic import BaseModel

from ..atoms import box, link, skeleton, text


class BreadcrumbItem(BaseModel):
    """Breadcrumb item data structure."""

    name: str
    href: str | None = None
    is_loading: bool = False


def breadcrumbs(
    items: list[BreadcrumbItem],
    max_items: int = 5,
    show_truncation: bool = True,
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Breadcrumbs molecule for navigation hierarchy.

    Displays a breadcrumb trail with automatic truncation for deep hierarchies.
    Supports loading states and accessibility features.

    Args:
        items: List of BreadcrumbItem objects
        max_items: Maximum number of visible items before truncation
        show_truncation: Whether to show "..." for truncated items
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Nav element with breadcrumb trail

    Example:
        >>> breadcrumbs([
        ...     BreadcrumbItem(name="Home", href="/"),
        ...     BreadcrumbItem(name="Products", href="/products"),
        ...     BreadcrumbItem(name="Category", href="/products/category"),
        ...     BreadcrumbItem(name="Item")
        ... ])
    """
    # Handle truncation for deep hierarchies
    display_items = items
    if show_truncation and len(items) > max_items:
        # Always show first item, ellipsis, and last 2 items
        first_item = items[0]
        last_items = items[-2:]
        display_items = [first_item, BreadcrumbItem(name="..."), *last_items]

    # Build breadcrumb content as inline elements
    breadcrumb_content = []
    for idx, item in enumerate(display_items):
        is_last = idx == len(display_items) - 1
        is_ellipsis = item.name == "..."

        # Create the item content
        if item.is_loading:
            # Loading state with skeleton
            item_content = skeleton(width="80px", height="20px", style="display: inline-block;")
        elif is_ellipsis:
            # Truncation indicator
            item_content = text(
                item.name,
                variant="caption",
                style="color: var(--color-text-muted); cursor: default; padding: 0 0.25rem;",
                title="More items in path",
            )
        elif is_last:
            # Current page - bold, not clickable
            item_content = text(
                item.name,
                style="font-size: 0.875rem; font-weight: 600; color: var(--color-primary-600); padding: 0 0.25rem;",
            )
        elif item.href:
            # Clickable ancestor
            item_content = link(
                item.name,
                href=item.href,
                style="""
                    font-size: 0.875rem;
                    color: var(--color-text-muted);
                    font-weight: 400;
                    text-decoration: none;
                    padding: 0 0.25rem;
                    border-radius: 0.125rem;
                    transition: all 0.2s;
                """,
            )
        else:
            # Non-clickable item
            item_content = Span(
                item.name,
                style="""
                    font-size: 0.875rem;
                    color: var(--color-text-muted);
                    font-weight: 400;
                    padding: 0 0.25rem;
                    cursor: default;
                """,
            )

        # Add item with proper ARIA attributes
        item_attrs = {}
        if is_last:
            item_attrs["aria-current"] = "page"

        # Wrap item in span for ARIA attributes
        if item_attrs:
            item_content = Span(item_content, **item_attrs)

        breadcrumb_content.append(item_content)

        # Add separator if not last item
        if not is_last:
            separator = Span(
                "›",
                style="""
                    font-size: 0.875rem;
                    color: var(--color-text-muted);
                    opacity: 0.6;
                    margin: 0 0.5rem;
                    display: inline;
                    vertical-align: baseline;
                """,
                **{"aria-hidden": "true"},
            )
            breadcrumb_content.append(separator)

    # Build the navigation as a single inline container
    return box(
        Nav(
            *breadcrumb_content,
            **{"aria-label": "Breadcrumb navigation"},
            style="display: inline-flex; align-items: baseline; flex-wrap: nowrap;",
        ),
        cls=cls,
        **kwargs,
    )
