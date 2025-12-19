"""Collapsible component - Expandable content section.

Uses native HTML <details>/<summary> elements for CSS-only toggle functionality.
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import Details, Div, Summary

from ...design_system.tokens import Colors, Spacing
from ...utils import generate_style_string, merge_classes

colors = Colors()
spacing = Spacing()


def collapsible(
    trigger: str | Any,
    *content: Any,
    open: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Details:
    """
    Collapsible content component using native details/summary.

    Args:
        trigger: Trigger text or element
        *content: Content to show/hide
        open: Whether initially open
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Details element with collapsible content

    Example:
        >>> collapsible(
        ...     "Click to expand",
        ...     text("This content can be toggled"),
        ...     open=False
        ... )
    """
    css_class = merge_classes("collapsible", cls)

    # Summary (trigger) styles
    summary_style = generate_style_string(
        display="flex",
        align_items="center",
        padding=spacing._3,
        cursor="pointer",
        font_weight="500",
        color=colors.text_primary,
        background_color="transparent",
        list_style="none",
    )

    # Content styles
    content_style = generate_style_string(
        padding=spacing._3,
        border_top=f"1px solid {colors.border}",
    )

    # Build trigger content
    trigger_elements = [trigger] if isinstance(trigger, str) else list(trigger)

    # Icon that rotates when open (CSS handles rotation via [open] selector)
    icon = Div(
        "▼",
        cls="collapsible-icon",
        style="margin-left: 0.5rem; transition: transform 0.2s;",
    )
    trigger_elements.append(icon)

    return Details(
        Summary(*trigger_elements, style=summary_style, cls="collapsible-trigger"),
        Div(*content, cls="collapsible-content", style=content_style),
        cls=css_class,
        open=open,
        **kwargs,
    )
