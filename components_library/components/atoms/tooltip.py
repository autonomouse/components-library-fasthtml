"""Tooltip component - Hover information."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Span

from ...utils import merge_classes


def tooltip(
    content: Any,
    text: str,
    position: Literal["top", "bottom", "left", "right"] = "top",
    cls: str | None = None,
    **kwargs: Any,
) -> Span:
    """
    Tooltip component with hover text.

    Note: This is a simple CSS-based tooltip.

    Args:
        content: Element to wrap with tooltip
        text: Tooltip text to display on hover
        position: Tooltip position relative to element
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Span element with tooltip on hover

    Example:
        >>> tooltip("Hover me", "This is helpful info")
        >>> tooltip(button("Info"), "Click for more details", position="right")
    """
    css_class = merge_classes("tooltip-wrapper", cls)

    return Span(
        content,
        Div(text, cls=f"tooltip tooltip-{position}"),
        cls=css_class,
        style="position: relative; display: inline-block;",
        **kwargs,
    )
