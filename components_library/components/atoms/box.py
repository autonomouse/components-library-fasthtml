"""Box component - generic container with styling."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...utils import generate_style_string, merge_classes


def box(
    *children: Any,
    padding: str | None = None,
    margin: str | None = None,
    background: str | None = None,
    border: str | None = None,
    border_radius: str | None = None,
    width: str | None = None,
    height: str | None = None,
    display: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Generic container component with flexible styling.

    Args:
        *children: Child elements to render inside the box
        padding: CSS padding value
        margin: CSS margin value
        background: Background color
        border: Border style
        border_radius: Border radius
        width: Width value
        height: Height value
        display: CSS display property
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with applied styles

    Example:
        >>> box("Content", padding="1rem", background="#f5f5f5")
    """
    style = generate_style_string(
        padding=padding,
        margin=margin,
        background=background,
        border=border,
        border_radius=border_radius,
        width=width,
        height=height,
        display=display,
    )

    css_class = merge_classes("box", cls)

    # Merge inline style with any existing style in kwargs
    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    return Div(*children, cls=css_class, style=style if style else None, **kwargs)
