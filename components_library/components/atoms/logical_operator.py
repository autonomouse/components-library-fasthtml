"""LogicalOperator component - AND/OR toggle for search queries."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Button as FtButton

from ...design_system.tokens import Colors, Typography
from ...utils import generate_style_string, merge_classes

colors = Colors()
typography = Typography()


def logical_operator(
    operator: Literal["AND", "OR", "AND NOT", "OR NOT"] = "AND",
    size: Literal["sm", "md", "lg"] = "sm",
    variant: Literal["solid", "outline", "ghost"] = "ghost",
    disabled: bool = False,
    cls: str | None = None,
    # HTMX attributes for toggling
    hx_post: str | None = None,
    hx_get: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    hx_vals: str | None = None,
    **kwargs: Any,
) -> FtButton:
    """
    LogicalOperator component for displaying and toggling between AND/OR operators.

    Used in search interfaces to switch between logical operators for combining
    search terms.

    Args:
        operator: Current operator value (AND, OR, AND NOT, OR NOT)
        size: Button size (sm, md, lg)
        variant: Visual variant (solid, outline, ghost)
        disabled: Whether the operator is disabled
        cls: Additional CSS classes
        hx_post: HTMX POST endpoint for toggling
        hx_get: HTMX GET endpoint for toggling
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        hx_vals: HTMX values to send
        **kwargs: Additional HTML attributes

    Returns:
        Logical operator button element

    Example:
        >>> logical_operator("AND", hx_post="/toggle-operator", hx_target="#search-form")
        >>> logical_operator("OR", variant="outline")
    """
    # Size configurations
    size_map = {
        "sm": {
            "font_size": typography.xs.size,
            "padding": "0.25rem 0.5rem",
            "min_height": "24px",
        },
        "md": {
            "font_size": typography.sm.size,
            "padding": "0.375rem 0.75rem",
            "min_height": "32px",
        },
        "lg": {
            "font_size": typography.base.size,
            "padding": "0.5rem 1rem",
            "min_height": "40px",
        },
    }

    config = size_map[size]

    # Variant styling
    if variant == "solid":
        bg_color = colors.neutral.s600
        text_color = "white"
        border = "none"
    elif variant == "outline":
        bg_color = "transparent"
        text_color = colors.neutral.s700
        border = f"1px solid {colors.neutral.s300}"
    else:  # ghost
        bg_color = "transparent"
        text_color = colors.neutral.s700
        border = "none"

    style = generate_style_string(
        display="inline-flex",
        align_items="center",
        justify_content="center",
        font_size=config["font_size"],
        font_weight=typography.font_semibold,
        padding=config["padding"],
        min_height=config["min_height"],
        min_width="auto",
        background_color=bg_color,
        color=text_color,
        border=border,
        border_radius="0.375rem",
        cursor="not-allowed" if disabled else "pointer",
        opacity="0.5" if disabled else "1",
        transition="background-color 0.15s ease",
    )

    css_class = merge_classes("logical-operator", f"logical-operator-{variant}", cls)

    attrs: dict[str, Any] = {
        "cls": css_class,
        "style": style,
        "disabled": disabled,
        "type": "button",
    }

    # HTMX attributes
    if hx_post:
        attrs["hx_post"] = hx_post
    if hx_get:
        attrs["hx_get"] = hx_get
    if hx_target:
        attrs["hx_target"] = hx_target
    if hx_swap:
        attrs["hx_swap"] = hx_swap
    if hx_vals:
        attrs["hx_vals"] = hx_vals

    return FtButton(operator, **{**attrs, **kwargs})
