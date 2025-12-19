"""EmptyState component - Empty/no data state indicator."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...design_system.tokens import Colors, Spacing
from ...utils import generate_style_string, merge_classes

colors = Colors()
spacing = Spacing()


def empty_state(
    message: str,
    icon: str | None = "📭",
    title: str | None = None,
    action: Any = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Empty state component for no data scenarios.

    Args:
        message: Description message
        icon: Optional icon (emoji or text)
        title: Optional heading
        action: Optional action element (button, link, etc.)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with empty state

    Example:
        >>> empty_state("No tests found", title="Get Started")
        >>> empty_state(
        ...     "No results match your search",
        ...     icon="🔍",
        ...     action=button("Clear Filters", variant="outline")
        ... )
    """
    css_class = merge_classes("empty-state", cls)

    elements = []

    # Icon
    if icon:
        elements.append(
            Div(
                icon,
                style=generate_style_string(font_size="4rem", margin_bottom=spacing._4),
            )
        )

    # Title
    if title:
        elements.append(
            Div(
                title,
                style=generate_style_string(
                    font_size="1.25rem",
                    font_weight="600",
                    color=colors.text_primary,
                    margin_bottom=spacing._2,
                ),
            )
        )

    # Message
    elements.append(
        Div(
            message,
            style=generate_style_string(
                font_size="1rem",
                color=colors.text_secondary,
                margin_bottom=spacing._4 if action else "0",
            ),
        )
    )

    # Action
    if action:
        elements.append(Div(action))

    return Div(
        *elements,
        cls=css_class,
        style=generate_style_string(
            display="flex",
            flex_direction="column",
            align_items="center",
            justify_content="center",
            text_align="center",
            padding=f"{spacing._12} {spacing._6}",
        ),
        **kwargs,
    )
