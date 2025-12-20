"""Character Card molecule."""

from typing import Any

from fasthtml.common import A

from ...components.atoms import avatar, badge, flex, heading, text
from ...utils import generate_style_string


def character_card(
    name: str,
    role: str | None = None,
    story_count: int = 0,
    href: str = "#",
    **kwargs: Any,
) -> Any:
    """
    Card component representing a character.

    Args:
        name: Character name
        role: Character role (e.g. Protagonist)
        story_count: Number of stories character appears in
        href: Link to character detail page
        **kwargs: Additional HTML attributes

    Returns:
        Anchor component wrapping the card
    """
    # Card container style
    container_style = generate_style_string(
        display="flex",
        flex_direction="column",
        background="rgba(17, 24, 39, 0.6)",  # Surface color
        backdrop_filter="blur(12px)",
        border="1px solid rgba(55, 65, 81, 0.5)",
        border_radius="16px",
        padding="1.5rem",
        transition="all 0.3s ease",
        text_decoration="none",
        height="100%",
        cursor="pointer",
        position="relative",
        overflow="hidden",
    )

    # Hover effect style (applied via class in CSS usually, but here inline for simplicity/portability)
    # Note: Complex hover states in inline styles are tricky. relying on class `character-card` for hover usually best.
    # We will verify styles via `component_styles` if needed.

    # Avatar area
    avatar_component = avatar(
        name=name,
        size=64,  # lg size
        style="margin-bottom: 1rem; border: 2px solid var(--theme-accent-primary, #00f0ff); box-shadow: 0 0 15px rgba(0, 240, 255, 0.3);",
    )

    # Content
    role_badge = (
        badge(
            role,
            variant="brand",
            style="margin-bottom: 0.5rem; align-self: flex-start;",
        )
        if role
        else None
    )

    name_heading = heading(
        name,
        level=3,
        style="font-size: 1.125rem; font-weight: 600; color: white; margin: 0 0 0.25rem 0;",
    )

    stats = text(
        f"Appears in {story_count} stor{'y' if story_count == 1 else 'ies'}",
        variant="caption",
        style="color: var(--theme-text-muted, #9ca3af); margin-top: auto;",
    )

    card_content = flex(
        avatar_component,
        role_badge if role_badge else "",
        name_heading,
        stats,
        direction="column",
        align="start",
        gap="0.25rem",
        style="height: 100%; width: 100%;",
    )

    return A(
        card_content,
        href=href,
        style=container_style,
        cls="character-card hover-glow",  # generic hover class
        **kwargs,
    )
