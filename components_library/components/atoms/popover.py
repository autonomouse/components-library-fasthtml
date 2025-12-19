"""Popover component - Floating content overlay."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...utils import merge_classes


def popover(
    trigger: Any,
    *content: Any,
    position: Literal["top", "bottom", "left", "right"] = "bottom",
    show: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Popover component with floating content.

    Note: This is a simple CSS-based popover. For better positioning
    and interactions, consider using JavaScript libraries or HTMX.

    Args:
        trigger: Element that triggers the popover
        *content: Popover content elements
        position: Popover position relative to trigger
        show: Whether popover is initially visible
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with popover structure

    Example:
        >>> popover(
        ...     button("Click me"),
        ...     heading("Popover Title", level=4),
        ...     text("This is popover content"),
        ...     position="bottom"
        ... )
    """
    css_class = merge_classes("popover-wrapper", cls)

    # Popover content
    popover_content = Div(
        *content,
        cls=f"popover popover-{position}",
        style=f"display: {'block' if show else 'none'};",
    )

    return Div(
        trigger,
        popover_content,
        cls=css_class,
        style="position: relative; display: inline-block;",
        **kwargs,
    )
