"""Skeleton component - Loading placeholder."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...utils import merge_classes


def skeleton(
    variant: Literal["text", "circular", "rectangular"] = "text",
    width: str | None = None,
    height: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Skeleton loading placeholder component.

    Args:
        variant: Skeleton shape (text, circular, rectangular)
        width: Custom width (CSS value)
        height: Custom height (CSS value)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with skeleton animation

    Example:
        >>> skeleton()  # Default text line
        >>> skeleton(variant="circular", width="3rem", height="3rem")
        >>> skeleton(variant="rectangular", width="100%", height="12rem")
    """
    css_class = merge_classes("skeleton", f"skeleton-{variant}", cls)

    # Default dimensions based on variant
    default_dimensions = {
        "text": {"width": "100%", "height": "1rem"},
        "circular": {"width": "2.5rem", "height": "2.5rem"},
        "rectangular": {"width": "100%", "height": "8rem"},
    }

    dimensions = default_dimensions[variant]

    style_parts = []
    style_parts.append(f"width: {width or dimensions['width']};")
    style_parts.append(f"height: {height or dimensions['height']};")

    if variant == "circular":
        style_parts.append("border-radius: 50%;")

    style = " ".join(style_parts)

    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    return Div(cls=css_class, style=style, **kwargs)
