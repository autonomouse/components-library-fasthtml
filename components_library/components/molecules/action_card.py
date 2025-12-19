"""Action card molecule - Clickable card with icon, title, and description."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ..atoms import card, heading, text, vstack


def action_card(
    title: str,
    description: str,
    hx_get: str | None = None,
    hx_target: str = "#search-results",
    hx_swap: str = "innerHTML",
    min_height: str = "120px",
    **kwargs: Any,
) -> Div:
    """
    Action card component with title, description, and optional HTMX action.

    Creates an interactive card that can trigger HTMX requests on click.
    Features hover effects and consistent styling.

    Args:
        title: Card title text
        description: Card description text
        hx_get: Optional HTMX GET endpoint (makes card clickable)
        hx_target: HTMX target element selector
        hx_swap: HTMX swap strategy
        min_height: Minimum height of the card
        **kwargs: Additional HTML attributes

    Returns:
        Action card component

    Example:
        >>> action_card(
        ...     "Most Recent Tests",
        ...     "View your recently accessed tests",
        ...     hx_get="/recent"
        ... )
        >>> action_card(
        ...     "Info Card",
        ...     "Non-clickable information card"
        ... )
    """
    # HTMX attributes if clickable
    card_attrs: dict[str, Any] = {}
    if hx_get:
        card_attrs.update(
            {
                "hx_get": hx_get,
                "hx_target": hx_target,
                "hx_swap": hx_swap,
            }
        )

    # Combine base style with interactive style if clickable
    base_style = (
        f"min-height: {min_height}; "
        "padding: 1.5rem; "
        "box-shadow: 0 2px 4px rgba(0,0,0,0.1); "
        "border-radius: 8px; "
        "border: 1px solid #e5e7eb;"
    )
    if hx_get:
        base_style += " cursor: pointer; transition: all 0.2s;"

    return card(
        vstack(
            heading(
                title,
                level=4,
                style="font-size: 1.125rem; font-weight: 600; color: #1f2937; margin-bottom: 0.5rem;",
            ),
            text(
                description,
                variant="caption",
                style="color: #6b7280; font-size: 0.875rem; line-height: 1.4;",
            ),
            gap=2,
        ),
        style=base_style,
        **{**card_attrs, **kwargs},
    )
