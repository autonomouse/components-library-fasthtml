"""Centered content layout template - Reusable centered content container."""

from __future__ import annotations

from typing import Any

from ..atoms import vstack


def centered_content(
    *content: Any,
    max_width: str = "40rem",
    padding: str = "4rem 2rem",
    text_align: str = "center",
    gap: int = 6,
    **kwargs: Any,
) -> Any:
    """
    Centered content layout with consistent styling.

    Provides a reusable pattern for centered page content with
    configurable width, padding, and alignment.

    Args:
        *content: Content elements to display
        max_width: Maximum width of content container
        padding: Padding around content
        text_align: Text alignment (left, center, right)
        gap: Vertical gap between content elements
        **kwargs: Additional HTML attributes

    Returns:
        vstack element with centered content styling

    Example:
        >>> centered_content(
        ...     heading("Welcome", level=1),
        ...     text("This is centered content"),
        ...     max_width="50rem"
        ... )
        >>> centered_content(
        ...     *elements,
        ...     text_align="left",
        ...     padding="2rem"
        ... )
    """
    return vstack(
        *content,
        gap=gap,
        style=f"max-width: {max_width}; margin: 0 auto; padding: {padding}; text-align: {text_align};",
        **kwargs,
    )
