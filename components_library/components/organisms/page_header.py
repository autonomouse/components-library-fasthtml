"""Page header organism - Page title with breadcrumbs and actions."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ..atoms import flex, heading, hstack
from ..molecules import breadcrumbs


def page_header(
    title: str,
    breadcrumb_items: list[dict[str, str]] | None = None,
    actions: list[Any] | None = None,
    description: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Page header organism with title, breadcrumbs, and action buttons.

    Args:
        title: Page title
        breadcrumb_items: List of breadcrumb items with 'text' and 'href'
        actions: List of action buttons/components
        description: Optional page description
        **kwargs: Additional HTML attributes

    Returns:
        Page header organism

    Example:
        >>> page_header(
        ...     "Laboratory Tests",
        ...     breadcrumb_items=[
        ...         {"text": "Home", "href": "/"},
        ...         {"text": "Tests", "href": "/tests"}
        ...     ],
        ...     actions=[button("Add Test", variant="solid")]
        ... )
    """
    content = []

    # Breadcrumbs
    if breadcrumb_items:
        from ..molecules.breadcrumbs import BreadcrumbItem

        breadcrumb_objects = [
            BreadcrumbItem(name=item.get("label", ""), href=item.get("href") or item.get("url"))
            for item in breadcrumb_items
        ]
        content.append(breadcrumbs(breadcrumb_objects))

    # Title and actions
    header_content = [
        flex(
            heading(title, level=1, cls="flex-1"),
            hstack(*actions, gap=2) if actions else None,
            justify="between",
            align="center",
        )
    ]

    # Description
    if description:
        header_content.append(
            flex(
                description,
                cls="text-muted mt-2",
            )
        )

    content.extend(header_content)

    return Div(
        *content,
        cls="page-header",
        **kwargs,
    )
