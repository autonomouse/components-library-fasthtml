"""Tabs component - Tabbed interface.

Uses hidden radio inputs with CSS :checked selectors for pure CSS tab switching.
"""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from fasthtml.common import Div, Input, Label

from ...design_system.tokens import Colors, Spacing, Typography
from ...utils import generate_style_string, merge_classes

colors = Colors()
spacing = Spacing()
typography = Typography()


def tab_panel(
    *content: Any,
    panel_index: int = 0,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Tab panel component (content for a tab).

    Args:
        *content: Panel content
        panel_index: Index of this panel (0-based)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with tab panel

    Example:
        >>> tab_panel(
        ...     text("Content for tab 1"),
        ...     panel_index=0,
        ... )
    """
    css_class = merge_classes("tab-panel", cls)

    panel_style = generate_style_string(
        padding=f"{spacing._6} 0",
    )

    return Div(
        *content,
        cls=css_class,
        style=panel_style,
        role="tabpanel",
        **{"data-panel-index": str(panel_index)},
        **kwargs,
    )


def tabs(
    tab_labels: list[str],
    *panels: Any,
    active_index: int = 0,
    tabs_id: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Tabs component with tab list and panels using pure CSS.

    Uses hidden radio inputs and CSS :checked selectors for tab switching
    without any JavaScript.

    Args:
        tab_labels: List of tab label texts
        *panels: Tab panels (use tab_panel() or plain Div with cls="tab-panel")
        active_index: Index of initially active tab
        tabs_id: Unique ID for this tabs group (auto-generated if not provided)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with tabs

    Example:
        >>> tabs(
        ...     ["Tab 1", "Tab 2", "Tab 3"],
        ...     tab_panel(text("Content 1"), panel_index=0),
        ...     tab_panel(text("Content 2"), panel_index=1),
        ...     tab_panel(text("Content 3"), panel_index=2),
        ... )
    """
    css_class = merge_classes("tabs", cls)

    # Generate unique ID for this tabs group
    group_id = tabs_id or f"tabs-{uuid4().hex[:8]}"

    # Styles for radio inputs (visually hidden but accessible)
    radio_style = generate_style_string(
        position="absolute",
        opacity="0",
        pointer_events="none",
    )

    # Tab label styles
    tab_style = generate_style_string(
        padding=f"{spacing._3} {spacing._4}",
        border="none",
        background="none",
        cursor="pointer",
        color=colors.text_secondary,
        font_weight=typography.font_medium,
        border_bottom="2px solid transparent",
        margin_bottom="-2px",
        transition="all 0.15s",
    )

    # Tab list styles
    tabs_list_style = generate_style_string(
        display="flex",
        border_bottom=f"2px solid {colors.border}",
        gap=spacing._1,
    )

    elements = []

    # Add hidden radio inputs first
    for idx in range(len(tab_labels)):
        radio_id = f"{group_id}-{idx}"
        is_checked = idx == active_index

        elements.append(
            Input(
                type="radio",
                name=group_id,
                id=radio_id,
                cls="tab-radio",
                style=radio_style,
                checked=is_checked,
            )
        )

    # Add tab labels (clicking these checks the corresponding radio)
    tab_labels_list = []
    for idx, label in enumerate(tab_labels):
        radio_id = f"{group_id}-{idx}"

        tab_labels_list.append(
            Label(
                label,
                fr=radio_id,
                cls="tab",
                style=tab_style,
                role="tab",
            )
        )

    elements.append(Div(*tab_labels_list, cls="tabs-list", style=tabs_list_style, role="tablist"))

    # Add panels container
    panels_style = generate_style_string(position="relative")
    elements.append(Div(*panels, cls="tabs-panels", style=panels_style))

    return Div(*elements, cls=css_class, id=group_id, **kwargs)
