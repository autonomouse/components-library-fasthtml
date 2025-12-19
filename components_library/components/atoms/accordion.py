"""Accordion component - Collapsible content sections.

Uses native HTML <details>/<summary> elements for CSS-only toggle functionality.
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import Details, Div, Summary

from ...design_system.tokens import Colors, Spacing
from ...utils import generate_style_string, merge_classes

colors = Colors()
spacing = Spacing()


def accordion_item(
    title: str,
    *content: Any,
    open: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Details:
    """
    Accordion item component using native details/summary.

    Args:
        title: Item title/header
        *content: Item content (shown when expanded)
        open: Whether item is initially open
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Details element with accordion item

    Example:
        >>> accordion_item(
        ...     "Section 1",
        ...     text("Content for section 1"),
        ...     open=True
        ... )
    """
    css_class = merge_classes("accordion-item", cls)

    # Summary (trigger) styles
    summary_style = generate_style_string(
        display="flex",
        align_items="center",
        justify_content="space-between",
        padding=spacing._4,
        cursor="pointer",
        font_weight="500",
        color=colors.text_primary,
        background_color="transparent",
        border="none",
        width="100%",
        list_style="none",
    )

    # Content styles
    content_style = generate_style_string(
        padding=f"0 {spacing._4} {spacing._4}",
        color=colors.text_secondary,
    )

    # Icon that rotates when open (CSS handles rotation via [open] selector)
    icon = Div(
        "▼",
        cls="accordion-icon",
        style="transition: transform 0.2s;",
    )

    return Details(
        Summary(title, icon, style=summary_style, cls="accordion-trigger"),
        Div(*content, cls="accordion-content", style=content_style),
        cls=css_class,
        open=open,
        **kwargs,
    )


def accordion(*items: Any, cls: str | None = None, **kwargs: Any) -> Div:
    """
    Accordion container component.

    Args:
        *items: Accordion items (use accordion_item())
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with accordion

    Example:
        >>> accordion(
        ...     accordion_item("Section 1", text("Content 1"), open=True),
        ...     accordion_item("Section 2", text("Content 2")),
        ...     accordion_item("Section 3", text("Content 3")),
        ... )
    """
    css_class = merge_classes("accordion", cls)
    return Div(*items, cls=css_class, **kwargs)
