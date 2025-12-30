"""Info Panel molecule - Styled container for informational content."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...utils import merge_classes
from ..atoms import card, heading, vstack


def info_panel(
    *children: Any,
    title: str | None = None,
    variant: Literal["default", "info", "success", "warning", "highlight"] = "default",
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Styled container for displaying informational content.

    A flexible panel component for tips, warnings, highlights, or general
    information blocks. Supports multiple visual variants.

    Args:
        *children: Content to display in the panel
        title: Optional heading for the panel
        variant: Visual style variant
            - "default": Neutral card styling
            - "info": Blue-tinted for informational content
            - "success": Green-tinted for positive messages
            - "warning": Yellow-tinted for cautions/tips
            - "highlight": Accent-colored for featured content
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Info panel component

    Example:
        >>> info_panel(
        ...     text("Pro Tip: Book tickets in advance!"),
        ...     title="Travel Tips",
        ...     variant="highlight",
        ... )
    """
    # Variant styles
    variant_styles = {
        "default": """
            background: var(--theme-card-bg, rgba(255, 255, 255, 0.95));
            border: 1px solid var(--theme-card-border, rgba(0, 0, 0, 0.1));
        """,
        "info": """
            background: rgba(59, 130, 246, 0.1);
            border: 1px solid rgba(59, 130, 246, 0.3);
        """,
        "success": """
            background: rgba(34, 197, 94, 0.1);
            border: 1px solid rgba(34, 197, 94, 0.3);
        """,
        "warning": """
            background: rgba(234, 179, 8, 0.1);
            border: 1px solid rgba(234, 179, 8, 0.3);
        """,
        "highlight": """
            background: rgba(var(--theme-accent-primary-rgb, 121, 40, 202), 0.1);
            border: 1px solid rgba(var(--theme-accent-primary-rgb, 121, 40, 202), 0.3);
        """,
    }

    title_colors = {
        "default": "var(--theme-text-primary, #1f2937)",
        "info": "#2563eb",
        "success": "#16a34a",
        "warning": "#ca8a04",
        "highlight": "var(--theme-accent-primary, #7928ca)",
    }

    base_style = f"""
        {variant_styles.get(variant, variant_styles["default"])}
        border-radius: 12px;
        padding: 1.5rem;
    """

    # Build content
    content_items = []

    if title:
        content_items.append(
            heading(
                title,
                level=3,
                style=f"""
                    font-size: 1.25rem;
                    font-weight: 600;
                    color: {title_colors.get(variant, title_colors["default"])};
                    margin: 0 0 1rem 0;
                """,
            )
        )

    content_items.extend(children)

    css_class = merge_classes("info-panel", cls)

    # Merge any incoming style
    extra_style = kwargs.pop("style", "")
    combined_style = f"{base_style} {extra_style}".strip()

    return card(
        vstack(
            *content_items,
            gap=3,
            style="align-items: stretch;",
        ),
        cls=css_class,
        style=combined_style,
        **kwargs,
    )


def highlight_text(
    text_content: str,
    variant: Literal["yellow", "blue", "green", "purple"] = "yellow",
    **kwargs: Any,
) -> Div:
    """
    Inline highlight for emphasizing text within content.

    Args:
        text_content: Text to highlight
        variant: Color variant for the highlight
        **kwargs: Additional HTML attributes

    Returns:
        Highlighted text span

    Example:
        >>> P("Total budget: ", highlight_text("$5,000", variant="yellow"))
    """
    from fasthtml.common import Span

    variant_styles = {
        "yellow": "background: rgba(253, 224, 71, 0.5); color: #713f12;",
        "blue": "background: rgba(147, 197, 253, 0.5); color: #1e40af;",
        "green": "background: rgba(134, 239, 172, 0.5); color: #14532d;",
        "purple": "background: rgba(216, 180, 254, 0.5); color: #581c87;",
    }

    style = f"""
        {variant_styles.get(variant, variant_styles["yellow"])}
        padding: 0.125rem 0.5rem;
        border-radius: 4px;
        font-weight: 600;
    """

    return Span(text_content, style=style, **kwargs)
