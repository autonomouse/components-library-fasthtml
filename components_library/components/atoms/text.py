"""Text component - text with variants and styling."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Span

from ...design_system.tokens import Colors, Typography
from ...utils import generate_style_string, merge_classes

colors = Colors()
typography = Typography()


def text(
    content: str,
    variant: Literal["body", "caption", "label", "helper", "error"] = "body",
    size: Literal["xs", "sm", "base", "lg", "xl", "xl2"] | None = None,
    weight: Literal[
        "thin", "extralight", "light", "normal", "medium", "semibold", "bold", "extrabold", "black"
    ]
    | None = None,
    color: str | None = None,
    truncate: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Span:
    """
    Text component with predefined variants and styling.

    Args:
        content: Text content
        variant: Text variant (body, caption, label, helper, error)
        size: Font size override
        weight: Font weight override
        color: Text color override
        truncate: Truncate text with ellipsis
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Span element with styled text

    Example:
        >>> text("This is body text")
        >>> text("Small caption", variant="caption")
        >>> text("Error message", variant="error")
        >>> text("Bold text", weight="bold")
    """
    # Variant configurations
    variant_config = {
        "body": {
            "size": typography.base,
            "weight": typography.font_normal,
            "color": colors.text_primary,
        },
        "caption": {
            "size": typography.sm,
            "weight": typography.font_normal,
            "color": colors.text_secondary,
        },
        "label": {
            "size": typography.sm,
            "weight": typography.font_medium,
            "color": colors.text_primary,
        },
        "helper": {
            "size": typography.sm,
            "weight": typography.font_normal,
            "color": colors.text_secondary,
        },
        "error": {
            "size": typography.sm,
            "weight": typography.font_medium,
            "color": colors.error.s600,
        },
    }

    config = variant_config[variant]

    # Override with explicit parameters
    if size:  # noqa: SIM108
        font_size = getattr(typography, size)
    else:
        font_size = config["size"]

    weight_map = {
        "thin": typography.font_thin,
        "extralight": typography.font_extralight,
        "light": typography.font_light,
        "normal": typography.font_normal,
        "medium": typography.font_medium,
        "semibold": typography.font_semibold,
        "bold": typography.font_bold,
        "extrabold": typography.font_extrabold,
        "black": typography.font_black,
    }

    font_weight = weight_map[weight] if weight else config["weight"]
    text_color = color if color else config["color"]

    style_props = {
        "font_size": font_size.size,
        "line_height": font_size.line_height,
        "font_weight": font_weight,
        "color": text_color,
    }

    if truncate:
        style_props.update(
            {
                "overflow": "hidden",
                "text_overflow": "ellipsis",
                "white_space": "nowrap",
            }
        )

    style = generate_style_string(**style_props)

    css_class = merge_classes(f"text text-{variant}", cls)

    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    return Span(content, cls=css_class, style=style if style else None, **kwargs)
