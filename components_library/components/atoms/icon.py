"""Icon component - Icon wrapper."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Span

from ...utils import merge_classes


def icon(
    name: str,
    size: Literal["xs", "sm", "md", "lg", "xl"] = "md",
    color: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Span:
    """
    Icon component wrapper.

    This is a simple wrapper for emoji icons or icon fonts.
    For production, integrate with an icon library like:
    - Lucide Icons
    - Heroicons
    - Font Awesome

    Args:
        name: Icon name/emoji
        size: Icon size
        color: Icon color (CSS value)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Span element with icon

    Example:
        >>> icon("🏠", size="lg")
        >>> icon("✓", color="green")
    """
    size_map = {
        "xs": "0.75rem",
        "sm": "1rem",
        "md": "1.25rem",
        "lg": "1.5rem",
        "xl": "2rem",
    }

    css_class = merge_classes("icon", f"icon-{size}", cls)

    style = f"font-size: {size_map[size]}; line-height: 1;"
    if color:
        style += f" color: {color};"

    if "style" in kwargs:
        style += f" {kwargs.pop('style')}"

    return Span(name, cls=css_class, style=style, **kwargs)
