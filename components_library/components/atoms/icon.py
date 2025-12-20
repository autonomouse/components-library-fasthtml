"""Icon component - Icon wrapper."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import NotStr, Span

from ...utils import merge_classes
from .icons import ICON_REGISTRY, svg_icon


def icon(
    name: str,
    size: Literal["xs", "sm", "md", "lg", "xl"] = "md",
    color: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Span:
    """
    Icon component wrapper.

    Supports both SVG icons (from registry) and emoji/text icons.
    For SVG icons, looks up the name in ICON_REGISTRY.

    Args:
        name: Icon name (from registry) or emoji
        size: Icon size ("xs", "sm", "md", "lg", "xl")
        color: Icon color (CSS value)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Span element containing the icon
    """
    # Check if it's a known SVG icon
    if name in ICON_REGISTRY:
        # Map generic sizes to pixels for SVG
        pixel_map = {
            "xs": 12,
            "sm": 16,
            "md": 20,
            "lg": 24,
            "xl": 32,
        }
        px_size = pixel_map.get(size, 20)

        # Get formatted SVG
        svg_content = svg_icon(name, size=px_size, color=color)

        # Wrapper styles for proper alignment
        css_class = merge_classes("icon", f"icon-{size}", "svg-icon", cls)
        default_style = (
            "display: inline-flex; align-items: center; justify-content: center; line-height: 1;"
        )

        style = default_style
        if "style" in kwargs:
            style += f" {kwargs.pop('style')}"

        return Span(NotStr(svg_content), cls=css_class, style=style, **kwargs)

    # Fallback to Emoji/Text implementation
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
