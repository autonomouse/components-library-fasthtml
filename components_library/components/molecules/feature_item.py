"""Feature Item molecule - Card displaying a feature with description and optional note."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...utils import merge_classes
from ..atoms import card, text


def feature_item(
    title: str,
    description: str,
    *children: Any,
    note: str | None = None,
    note_prefix: str = "Tip: ",
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    A card component for displaying a feature, attraction, or item with details.

    Useful for showcasing features, attractions, amenities, or any item that has
    a title, description, and optional note/tip.

    Args:
        title: The feature/item title
        description: Main description text
        *children: Additional content to display
        note: Optional note, tip, or additional info (displayed with accent styling)
        note_prefix: Prefix for the note (default: "Tip: ")
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Feature item card component

    Example:
        >>> feature_item(
        ...     "Golden Pavilion",
        ...     "Stunning temple reflected in a tranquil pond",
        ...     note="Most beautiful on clear sunny days",
        ... )
    """
    # Title style
    title_style = """
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--theme-text-primary, #1f2937);
        margin-bottom: 0.5rem;
    """

    # Description style
    desc_style = """
        color: var(--theme-text-secondary, #6b7280);
        line-height: 1.6;
        margin-bottom: 0.75rem;
    """

    # Note style (accent-colored callout)
    note_style = """
        background: rgba(var(--theme-accent-primary-rgb, 118, 75, 162), 0.1);
        padding: 0.75rem;
        border-radius: 8px;
        font-size: 0.9rem;
        color: var(--theme-accent-primary, #764ba2);
        border-left: 3px solid var(--theme-accent-primary, #764ba2);
    """

    # Build content
    content = [
        Div(title, style=title_style),
        text(description, style=desc_style),
    ]

    # Add children
    if children:
        content.extend(children)

    # Add note if provided
    if note:
        note_text = f"{note_prefix}{note}" if note_prefix else note
        content.append(Div(note_text, style=note_style))

    # Card style
    card_style = """
        background: var(--theme-card-bg, rgba(255, 255, 255, 0.95));
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    """

    css_class = merge_classes("feature-item", cls)

    # Merge any incoming style
    extra_style = kwargs.pop("style", "")
    combined_style = f"{card_style} {extra_style}".strip()

    return card(
        *content,
        cls=css_class,
        style=combined_style,
        **kwargs,
    )
