"""Icon Card molecule."""

from typing import Any

from fasthtml.common import A, Div

from ...components.atoms import badge, card, flex, heading, icon, text
from ...utils import merge_classes


def icon_card(
    title: str,
    description: str,
    icon_name: str,
    href: str | None = None,
    icon_color: str = "var(--theme-accent-primary, #00f0ff)",
    badge_text: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Card component with a glowing icon, title, and description.

    Args:
        title: Title of the card
        description: Description text
        icon_name: Name of the icon (e.g. lucide icon name)
        href: Link URL
        icon_color: Color of the icon and its glow
        badge_text: Optional badge text to display
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes
    """
    # Icon with glow
    # Using a container for the glow effect
    icon_container_style = f"""
        color: {icon_color};
        filter: drop-shadow(0 0 8px {icon_color});
        margin-bottom: 1rem;
    """

    icon_component = Div(
        icon(name=icon_name, size="lg", stroke_width=1.5), style=icon_container_style
    )

    # Badge (optional)
    badge_component = (
        badge(badge_text, color_palette="accent", size="sm", style="margin-bottom: 0.5rem;")
        if badge_text
        else ""
    )

    # Content
    content = flex(
        icon_component,
        badge_component,
        heading(
            title,
            level=3,
            style="font-size: 1.1rem; font-weight: 600; color: white; margin-bottom: 0.5rem;",
        ),
        text(
            description,
            style="font-size: 0.9rem; color: var(--theme-text-muted); line-height: 1.5;",
        ),
        direction="column",
        align="start",
        style="height: 100%;",
    )

    # Base Card styles
    base_style = """
        background: rgba(13, 17, 34, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        height: 100%;
    """

    css_class = merge_classes("icon-card hover-glow hover:translate-y-[-4px]", cls)

    card_component = card(
        content,
        style=base_style,
        cls=css_class,
        **kwargs,
    )

    if href and href != "#":
        return A(
            card_component,
            href=href,
            style="text-decoration: none; display: block; height: 100%;",
        )

    return card_component
