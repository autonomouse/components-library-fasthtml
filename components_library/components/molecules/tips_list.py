"""Tips List molecule - Styled list of tips or notes."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Li, Ul

from ...utils import merge_classes
from ..atoms import card, heading


def tips_list(
    tips: list[str],
    *,
    title: str | None = None,
    icon: str = "💡",
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    A styled list of tips, notes, or bullet points with optional icons.

    Useful for displaying travel tips, pro tips, notes, or any list of
    helpful information.

    Args:
        tips: List of tip/note strings to display
        title: Optional heading for the tips section
        icon: Icon to display next to each tip (default: "💡")
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Tips list component

    Example:
        >>> tips_list(
        ...     [
        ...         "Book tickets in advance",
        ...         "Arrive early for best experience",
        ...         "Bring comfortable shoes",
        ...     ],
        ...     title="Pro Tips",
        ...     icon="✨",
        ... )
    """
    # List container style
    list_style = """
        list-style: none;
        padding: 0;
        margin: 0;
    """

    # List item style
    item_style = """
        padding: 0.75rem 0;
        border-bottom: 1px solid var(--theme-card-border, rgba(0, 0, 0, 0.1));
        display: flex;
        align-items: flex-start;
        gap: 0.75rem;
        color: var(--theme-text-primary, #1f2937);
    """

    # Last item (no border)
    last_item_style = f"{item_style} border-bottom: none;"

    # Icon style
    icon_style = """
        color: var(--theme-accent-primary, #764ba2);
        font-size: 1.2rem;
        flex-shrink: 0;
    """

    # Build list items
    tip_items = []
    for i, tip in enumerate(tips):
        is_last = i == len(tips) - 1
        tip_items.append(
            Li(
                Div(icon, style=icon_style),
                Div(tip),
                style=last_item_style if is_last else item_style,
            )
        )

    # Card style
    card_style = """
        background: var(--theme-card-bg, rgba(255, 255, 255, 0.95));
        border-radius: 12px;
        padding: 1.5rem;
    """

    # Build content
    content = []

    if title:
        content.append(
            heading(
                title,
                level=3,
                style="color: var(--theme-accent-primary, #764ba2); margin-bottom: 1rem;",
            )
        )

    content.append(Ul(*tip_items, style=list_style))

    css_class = merge_classes("tips-list", cls)

    # Merge any incoming style
    extra_style = kwargs.pop("style", "")
    combined_style = f"{card_style} {extra_style}".strip()

    return card(
        *content,
        cls=css_class,
        style=combined_style,
        **kwargs,
    )
