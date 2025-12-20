"""Entity Card molecule."""

from typing import Any

from fasthtml.common import A

from ...components.atoms import avatar, badge, flex, heading, text


def entity_card(
    title: str,
    *children: Any,
    subtitle: str | None = None,
    email: str | None = None,
    image_url: str | None = None,
    avatar_size: int | None = None,
    meta: str | None = None,
    tags: list[str] | None = None,
    href: str | None = None,
    centered: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Generic card component representing an entity (user, character, item, etc.).

    Args:
        title: Entity name/title
        *children: Additional content to display in the card body
        subtitle: Entity role/subtitle (optional)
        image_url: URL for the entity image/avatar
        meta: Meta info text to display (optional)
        tags: List of strings to display as badges (optional)
        href: Link URL (optional). If provided, card becomes an anchor.
        centered: Whether to center the content (default: False)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes
    """
    from ...components.atoms import card
    from ...utils import merge_classes

    # Avatar area
    avatar_size = avatar_size or (80 if centered else 64)
    avatar_style = "margin-bottom: 1rem; border: none; box-shadow: 0 0 15px rgba(0, 240, 255, 0.3);"

    avatar_component = avatar(
        name=title,
        email=email,
        image_url=image_url,
        size=avatar_size,
        style=avatar_style,
    )

    # Content elements
    elements = [avatar_component]

    # Tags/Badges
    if tags:
        badge_elements = [
            badge(
                tag_str,
                variant="brand",
            )
            for tag_str in tags
        ]
        elements.append(
            flex(
                *badge_elements,
                gap="0.5rem",
                justify="center" if centered else "start",
                wrap="wrap",
                style="margin-bottom: 0.5rem; width: 100%;",
            )
        )

    # Title
    elements.append(
        heading(
            title,
            level=3,
            style="font-size: 1.125rem; font-weight: 600; color: white; margin: 0 0 0.25rem 0;",
            cls="text-center" if centered else "",
        )
    )

    # Subtitle
    if subtitle:
        elements.append(
            text(
                subtitle,
                variant="caption",
                style="color: var(--theme-text-muted, #9ca3af); margin-bottom: 0.25rem;",
                cls="text-center" if centered else "",
            )
        )

    # Meta
    if meta:
        elements.append(
            text(
                meta,
                variant="caption",
                style="color: var(--theme-text-muted, #9ca3af); margin-top: auto;",
                cls="text-center" if centered else "",
            )
        )

    # Additional children
    if children:
        elements.extend(children)

    # Layout container
    content_layout = flex(
        *elements,
        direction="column",
        align="center" if centered else "start",
        gap="0.25rem",
        style="height: 100%; width: 100%;",
    )

    # Base Card styles (glassmorphism default for entities)
    base_style = """
        background: rgba(17, 24, 39, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(55, 65, 81, 0.5);
        transition: all 0.3s ease;
    """

    # Merge provided style with base style
    if "style" in kwargs:
        base_style = f"{base_style} {kwargs.pop('style')}"

    css_class = merge_classes("entity-card hover-glow", cls)

    card_component = card(
        content_layout,
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
