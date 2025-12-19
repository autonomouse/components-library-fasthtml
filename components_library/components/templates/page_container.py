"""PageContainer template - Full-height page layout foundation."""

from __future__ import annotations

from typing import Any

from ..atoms import box


def page_container(
    children: Any,
    background: str = "var(--color-background)",
    min_height: str = "100vh",
    padding: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Page container provides a full-height page layout with consistent background styling.

    This template component serves as the foundation for page-level layouts.

    Args:
        children: Content to be rendered inside the page container
        background: Background color for the container
        min_height: Minimum height (default: 100vh for full viewport height)
        padding: Optional padding for the container
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Box element with page container styling

    Example:
        >>> page_container(
        ...     vstack(
        ...         heading("Welcome", level=1),
        ...         text("This is your page content")
        ...     ),
        ...     background="var(--color-background-alt)"
        ... )
    """
    return box(
        box(children, padding=padding or "0"),
        background=background,
        style=f"min-height: {min_height};",
        padding="0",
        cls=cls,
        **kwargs,
    )
