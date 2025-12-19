"""TokenPill component - removable token/tag for search interfaces."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Span
from pydantic import BaseModel

from ...design_system.tokens import Colors, Spacing, Typography
from ...utils import generate_style_string, merge_classes

colors = Colors()
spacing = Spacing()
typography = Typography()


class Token(BaseModel):
    """Represents a token/concept for search interfaces."""

    id: str
    name: str
    type: str | None = None
    description: str | None = None


def token_pill(
    token: Token | dict[str, Any],
    size: Literal["sm", "md", "lg"] = "md",
    variant: Literal["solid", "subtle", "outline"] = "subtle",
    color_palette: Literal["brand", "gray", "blue", "green"] = "brand",
    closable: bool = True,
    disabled: bool = False,
    cls: str | None = None,
    # HTMX for removal
    hx_delete: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    hx_confirm: str | None = None,
    **kwargs: Any,
) -> Span:
    """
    TokenPill component representing a selected token/concept as a removable pill.

    Used in search interfaces to display selected search terms that can be removed.

    Args:
        token: Token data (Token dataclass or dict with id, name)
        size: Pill size (sm, md, lg)
        variant: Visual variant (solid, subtle, outline)
        color_palette: Color scheme (brand, gray, blue, green)
        closable: Whether to show close button
        disabled: Whether the pill is disabled
        cls: Additional CSS classes
        hx_delete: HTMX DELETE endpoint for removal
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        hx_confirm: HTMX confirmation message
        **kwargs: Additional HTML attributes

    Returns:
        Token pill element

    Example:
        >>> token_pill(Token(id="1", name="Aspirin"))
        >>> token_pill({"id": "2", "name": "Cancer"}, color_palette="blue")
    """
    # Handle both Token dataclass and dict
    if isinstance(token, dict):
        token_name = token.get("name", "")
        token_id = token.get("id", "")
    else:
        token_name = token.name
        token_id = token.id

    # Size configurations
    size_map = {
        "sm": {
            "font_size": typography.xs.size,
            "padding": f"{spacing._1} {spacing._2}",
            "gap": spacing._1,
        },
        "md": {
            "font_size": typography.sm.size,
            "padding": f"{spacing._1_5} {spacing._2_5}",
            "gap": spacing._1_5,
        },
        "lg": {
            "font_size": typography.base.size,
            "padding": f"{spacing._2} {spacing._3}",
            "gap": spacing._2,
        },
    }

    config = size_map[size]

    # Color configurations
    color_map = {
        "brand": {
            "solid": {
                "bg": colors.primary.s600,
                "color": "white",
                "border": "none",
            },
            "subtle": {
                "bg": colors.primary.s100,
                "color": colors.primary.s800,
                "border": "none",
            },
            "outline": {
                "bg": "transparent",
                "color": colors.primary.s700,
                "border": f"1px solid {colors.primary.s300}",
            },
        },
        "gray": {
            "solid": {
                "bg": colors.neutral.s600,
                "color": "white",
                "border": "none",
            },
            "subtle": {
                "bg": colors.neutral.s100,
                "color": colors.neutral.s800,
                "border": "none",
            },
            "outline": {
                "bg": "transparent",
                "color": colors.neutral.s700,
                "border": f"1px solid {colors.neutral.s300}",
            },
        },
        "blue": {
            "solid": {
                "bg": colors.primary.s600,
                "color": "white",
                "border": "none",
            },
            "subtle": {
                "bg": colors.primary.s100,
                "color": colors.primary.s800,
                "border": "none",
            },
            "outline": {
                "bg": "transparent",
                "color": colors.primary.s700,
                "border": f"1px solid {colors.primary.s300}",
            },
        },
        "green": {
            "solid": {
                "bg": colors.success.s600,
                "color": "white",
                "border": "none",
            },
            "subtle": {
                "bg": colors.success.s100,
                "color": colors.success.s800,
                "border": "none",
            },
            "outline": {
                "bg": "transparent",
                "color": colors.success.s700,
                "border": f"1px solid {colors.success.s300}",
            },
        },
    }

    color_config = color_map[color_palette][variant]

    style = generate_style_string(
        display="inline-flex",
        align_items="center",
        gap=config["gap"],
        padding=config["padding"],
        font_size=config["font_size"],
        font_weight=typography.font_medium,
        background_color=color_config["bg"],
        color=color_config["color"],
        border=color_config["border"],
        border_radius="9999px",
        white_space="nowrap",
        opacity="0.6" if disabled else "1",
    )

    css_class = merge_classes(
        "token-pill",
        f"token-pill-{variant}",
        f"token-pill-{color_palette}",
        cls,
    )

    # Build children
    children: list[Any] = [token_name]

    if closable and not disabled:
        close_style = generate_style_string(
            display="inline-flex",
            align_items="center",
            justify_content="center",
            width="1rem",
            height="1rem",
            border_radius="9999px",
            cursor="pointer",
            font_size="0.75rem",
            line_height="1",
            opacity="0.7",
            transition="opacity 0.15s",
        )

        close_attrs: dict[str, Any] = {
            "style": close_style,
            "cls": "token-pill-close",
            "aria-label": f"Remove {token_name}",
        }

        if hx_delete:
            close_attrs["hx_delete"] = hx_delete
            close_attrs["hx_target"] = hx_target or "closest .token-pill"
            close_attrs["hx_swap"] = hx_swap or "outerHTML"
            if hx_confirm:
                close_attrs["hx_confirm"] = hx_confirm

        close_button = Span("×", **close_attrs)
        children.append(close_button)

    return Span(
        *children,
        cls=css_class,
        style=style,
        data_token_id=token_id,
        **kwargs,
    )
