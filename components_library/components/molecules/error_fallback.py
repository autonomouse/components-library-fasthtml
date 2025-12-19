"""ErrorFallback component - error state display for failed operations."""

from __future__ import annotations

from typing import Any

from fasthtml.common import H3, Div, P

from ...design_system.tokens import Colors, Spacing
from ...utils import generate_style_string, merge_classes
from ..atoms import button, vstack

colors = Colors()
spacing = Spacing()


def error_fallback(
    error: str | None = None,
    title: str = "Something went wrong",
    show_retry: bool = True,
    cls: str | None = None,
    # HTMX for retry
    hx_get: str | None = None,
    hx_post: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    ErrorFallback component for displaying error states.

    Shows a user-friendly error message with optional retry functionality.
    Use this when an operation fails and you need to show an error state.

    Args:
        error: Error message to display
        title: Title text for the error
        show_retry: Whether to show retry button
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint for retry
        hx_post: HTMX POST endpoint for retry
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        **kwargs: Additional HTML attributes

    Returns:
        Error fallback element

    Example:
        >>> error_fallback(error="Failed to load data", hx_get="/retry", hx_target="#content")
        >>> error_fallback(title="Connection Error", show_retry=False)
    """
    container_style = generate_style_string(
        padding=spacing._8,
        text_align="center",
        border_radius="0.5rem",
        border=f"1px solid {colors.error.s200}",
        background_color=colors.error.s50,
    )

    title_style = generate_style_string(
        margin_bottom=spacing._4,
        font_size="1.25rem",
        font_weight="600",
        color=colors.error.s900,
    )

    message_style = generate_style_string(
        margin_bottom=spacing._6 if show_retry else "0",
        color=colors.error.s700,
    )

    css_class = merge_classes("error-fallback", cls)

    children = [
        H3(title, style=title_style),
        P(error or "An unexpected error occurred", style=message_style),
    ]

    if show_retry and (hx_get or hx_post):
        retry_btn = button(
            "Try Again",
            variant="solid",
            color_palette="red",
            size="md",
            hx_get=hx_get,
            hx_post=hx_post,
            hx_target=hx_target,
            hx_swap=hx_swap or "outerHTML",
        )
        children.append(retry_btn)

    return Div(
        vstack(*children, gap=2, align="center"),
        cls=css_class,
        style=container_style,
        role="alert",
        **kwargs,
    )
