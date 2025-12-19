"""Spinner component - Loading indicator."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...utils import merge_classes


def spinner(
    size: Literal["sm", "md", "lg"] = "md",
    color: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Loading spinner component.

    Args:
        size: Spinner size (sm, md, lg)
        color: Custom color (overrides theme color)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with spinner animation

    Example:
        >>> spinner()
        >>> spinner(size="lg")
        >>> spinner(size="sm", color="#ff0000")
    """
    css_class = merge_classes("spinner", f"spinner-{size}", cls)

    style = ""
    if color:
        style = f"border-top-color: {color};"

    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    return Div(cls=css_class, style=style if style else None, role="status", **kwargs)
