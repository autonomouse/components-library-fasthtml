"""Labs intro page template - landing page for Labs features."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import A, Div, NotStr

from ...design_system.tokens import Colors, Spacing
from ...utils import generate_style_string
from ..atoms import badge, button, card, heading, hstack, text, vstack
from ..organisms.header import header

# Default SVG icons
_DEFAULT_FEATURE_ICON = """<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l8.57-8.57A4 4 0 1 1 18 8.84l-8.59 8.57a2 2 0 0 1-2.83-2.83l8.49-8.48"/></svg>"""


class BadgeConfig:
    """Configuration for a status badge."""

    def __init__(
        self,
        label: str,
        variant: Literal["brand", "gray", "success", "error"] = "gray",
    ) -> None:
        self.label = label
        self.variant = variant


def labs_intro_page(
    feature_title: str,
    feature_subtitle: str,
    hero_title: str,
    descriptions: list[str],
    launch_url: str,
    launch_button_text: str = "Launch",
    breadcrumb_items: list[dict[str, str]] | None = None,
    badges: list[BadgeConfig] | None = None,
    last_update: str | None = None,
    feature_icon_svg: str | None = None,
    logo_href: str = "/",
    logout_href: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Labs intro page template for feature landing pages.

    Provides a consistent layout for Labs feature introduction pages with
    a header, hero section, and content card.

    Args:
        feature_title: Title displayed in the hero section (e.g., "Articles")
        feature_subtitle: Subtitle text below the hero title
        hero_title: Title inside the content card (e.g., "Articles Search Platform")
        descriptions: List of description paragraphs for the content card
        launch_url: URL for the launch button
        launch_button_text: Text for the launch button
        breadcrumb_items: List of breadcrumb items [{label, href}]
        badges: List of BadgeConfig objects for status badges
        last_update: Last update date string (e.g., "November 14th 2025")
        feature_icon_svg: Custom SVG string for the feature icon (uses default if None)
        logo_href: URL for the logo link
        logout_href: URL for logout action in header dropdown (if None, logout hidden)
        **kwargs: Additional HTML attributes

    Returns:
        Complete page content Div (wrap with base_page for full HTML)

    Example:
        >>> labs_intro_page(
        ...     feature_title="Articles",
        ...     feature_subtitle="Search scientific literature",
        ...     hero_title="Articles Search Platform",
        ...     descriptions=["First paragraph...", "Second paragraph..."],
        ...     launch_url="/labs/articles",
        ...     badges=[BadgeConfig("Incubating", "brand"), BadgeConfig("Beta", "gray")],
        ...     last_update="November 14th 2025",
        ... )
    """
    colors = Colors()
    spacing = Spacing()

    # Default breadcrumbs if not provided
    if breadcrumb_items is None:
        breadcrumb_items = [
            {"label": "Dashboard", "href": "/"},
        ]

    # Default badges if not provided
    if badges is None:
        badges = [
            BadgeConfig("Incubating", "brand"),
            BadgeConfig("Beta", "gray"),
        ]

    # Content container style
    content_style = generate_style_string(
        padding=f"{spacing._8} {spacing._6}",
        width="100%",
        box_sizing="border-box",
    )

    page_content = Div(
        # Header with icon logo and utility icons
        header(
            logo_icon=True,
            logo_href=logo_href,
            breadcrumb_items=breadcrumb_items,
            use_utility_icons=True,
            logout_href=logout_href,
        ),
        # Main content
        Div(
            vstack(
                # Hero section with icon and title
                _hero_section(
                    feature_title=feature_title,
                    feature_subtitle=feature_subtitle,
                    feature_icon_svg=feature_icon_svg,
                    colors=colors,
                ),
                # Content card
                _content_card(
                    hero_title=hero_title,
                    descriptions=descriptions,
                    badges=badges,
                    last_update=last_update,
                    launch_url=launch_url,
                    launch_button_text=launch_button_text,
                    colors=colors,
                    spacing=spacing,
                ),
                gap="6",
                align="stretch",
            ),
            style=content_style,
        ),
        **kwargs,
    )

    return page_content


def _hero_section(
    feature_title: str,
    feature_subtitle: str,
    feature_icon_svg: str | None,
    colors: Colors,
) -> Div:
    """Build the hero section with icon and title."""
    icon_svg = feature_icon_svg or _DEFAULT_FEATURE_ICON.format(size=32)

    icon_style = generate_style_string(
        color=colors.neutral.s600,
        display="inline-flex",
        align_items="center",
    )

    return vstack(
        hstack(
            Div(NotStr(icon_svg), style=icon_style),
            heading(feature_title, level=1),
            gap="3",
            align="center",
        ),
        text(
            feature_subtitle,
            variant="helper",
        ),
        gap="2",
        align="start",
    )


def _content_card(
    hero_title: str,
    descriptions: list[str],
    badges: list[BadgeConfig],
    last_update: str | None,
    launch_url: str,
    launch_button_text: str,
    colors: Colors,
    spacing: Spacing,
) -> Div:
    """Build the main content card."""
    # Badge elements
    badge_elements = [badge(b.label, variant=b.variant) for b in badges]

    # Date badge style (subtle gray background)
    date_style = generate_style_string(
        background_color=colors.neutral.s100,
        color=colors.neutral.s600,
        padding=f"{spacing._1} {spacing._2}",
        border_radius="4px",
        font_size="0.75rem",
    )

    # Build header row with badges and date
    header_items = [*badge_elements]
    if last_update:
        header_items.append(
            Div(last_update, style=date_style),
        )

    # Build description paragraphs
    description_elements = [text(desc, size="base") for desc in descriptions]

    # Launch button
    launch_button = A(
        button(
            launch_button_text,
            variant="solid",
            color_palette="brand",
            size="md",
        ),
        href=launch_url,
        style="text-decoration: none; display: inline-flex;",
    )

    return card(
        vstack(
            # Badges and date row
            hstack(
                *header_items,
                gap="2",
                align="center",
            ),
            # Feature title
            heading(hero_title, level=2),
            # Description paragraphs
            *description_elements,
            # Launch button
            launch_button,
            gap="4",
            align="start",
        ),
    )
