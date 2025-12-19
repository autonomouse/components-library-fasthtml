"""Enhanced item details molecule - Display item information with improved aesthetics."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...design_system.tokens import BorderRadius, Colors, Shadows, Spacing, Transitions, Typography
from ..atoms import card, hstack, text, vstack


def item_details(
    details: list[tuple[str, str]],
    **kwargs: Any,
) -> Any:
    """
    Enhanced item details molecule for displaying structured information.

    A visually appealing component that displays item details with improved aesthetics,
    better typography, icons, and visual hierarchy. Takes full advantage of the design system.

    Args:
        details: List of (label, value) tuples to display
        **kwargs: Additional HTML attributes

    Returns:
        Enhanced item details section component

    Example:
        >>> item_details([
        ...     ("ID", "12345"),
        ...     ("Name", "Example Item"),
        ...     ("Category", "General"),
        ...     ("Location", "Warehouse A"),
        ...     ("Notes", "Handle with care")
        ... ])
    """
    colors = Colors()
    spacing = Spacing()
    typography = Typography()
    shadows = Shadows()
    radius = BorderRadius()
    transitions = Transitions()

    if not details:
        return vstack(gap=3, **kwargs)

    # Create enhanced detail rows with icons and better styling
    detail_cards = []

    for _i, (label, value) in enumerate(details):
        # Determine icon based on label type
        icon_name = _get_icon_for_label(label)

        # Create enhanced detail card
        detail_card = _create_enhanced_detail_card(
            label=label,
            value=value,
            icon_name=icon_name,
            colors=colors,
            spacing=spacing,
            typography=typography,
            shadows=shadows,
            radius=radius,
            transitions=transitions,
        )

        detail_cards.append(detail_card)

    return vstack(
        *detail_cards,
        gap=4,
        cls="enhanced-item-details",
        style=f"""
            background: linear-gradient(135deg, {colors.background} 0%, {colors.neutral.s50} 100%);
            border-radius: {radius.xl};
            padding: {spacing._6};
            box-shadow: {shadows.lg};
            border: 1px solid {colors.border};
        """,
        **kwargs,
    )


def _get_icon_for_label(label: str) -> str:
    """Get appropriate icon for label type."""
    label_lower = label.lower()

    # Icon mapping based on label keywords
    icon_mapping = [
        (["id"], "🔑"),
        (["name", "title"], "📋"),
        (["type", "category"], "🏷️"),
        (["location", "place"], "📍"),
        (["notes", "description", "special"], "📝"),
        (["time", "duration", "date"], "⏱️"),
        (["cost", "price"], "💰"),
        (["status"], "📊"),
        (["email", "contact"], "📧"),
        (["phone"], "📞"),
    ]

    for keywords, icon in icon_mapping:
        if any(keyword in label_lower for keyword in keywords):
            return icon

    return "ℹ️"


def _create_enhanced_detail_card(
    label: str,
    value: str,
    icon_name: str,
    colors: Colors,
    spacing: Spacing,
    typography: Typography,
    shadows: Shadows,
    radius: BorderRadius,
    transitions: Transitions,
) -> Div:
    """Create an enhanced detail card with icon and improved styling."""

    return card(
        hstack(
            # Icon section
            Div(
                text(
                    icon_name,
                    cls="detail-icon",
                    style=f"""
                        font-size: 1.5rem;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        width: 48px;
                        height: 48px;
                        background: linear-gradient(135deg, {colors.primary.s100} 0%, {colors.primary.s200} 100%);
                        border-radius: {radius.lg};
                        border: 2px solid {colors.primary.s200};
                        transition: all {transitions.base} {transitions.ease_in_out};
                    """,
                ),
                cls="detail-icon-container",
            ),
            # Content section
            vstack(
                text(
                    label,
                    variant="label",
                    weight="semibold",
                    cls="detail-label",
                    style=f"""
                        color: {colors.text_secondary};
                        font-size: {typography.sm.size};
                        text-transform: uppercase;
                        letter-spacing: 0.05em;
                        margin-bottom: {spacing._1};
                    """,
                ),
                text(
                    value,
                    variant="body",
                    weight="medium",
                    cls="detail-value",
                    style=f"""
                        color: {colors.text_primary};
                        font-size: {typography.base.size};
                        line-height: 1.6;
                        word-wrap: break-word;
                        overflow-wrap: break-word;
                    """,
                ),
                gap=2,
                cls="detail-content",
                style="flex: 1;",
            ),
            gap=4,
            align="start",
            cls="enhanced-detail-row",
            style=f"""
                padding: {spacing._4};
                background: {colors.background};
                border-radius: {radius.lg};
                border: 1px solid {colors.border};
                transition: all {transitions.base} {transitions.ease_in_out};
                position: relative;
                overflow: hidden;
            """,
        ),
        cls="enhanced-detail-card",
        style=f"""
            background: {colors.background};
            border: 1px solid {colors.border};
            border-radius: {radius.lg};
            box-shadow: {shadows.sm};
            transition: all {transitions.base} {transitions.ease_in_out};
            position: relative;
            overflow: hidden;
        """,
    )
