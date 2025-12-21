"""Hero Card molecule."""

from typing import Any

from fasthtml.common import A, Div, Img

from ...components.atoms import badge, card, flex, heading, text


def hero_card(
    title: str,
    image_url: str | None = None,
    subtitle: str | None = None,
    badge_text: str | None = None,
    href: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Card component with a large hero image, suitable for featuring content.

    Args:
        title: Title of the card
        image_url: URL for the cover image
        subtitle: Optional subtitle (e.g. parent location)
        badge_text: Optional text to display in a badge (e.g. "Scene Count: 5")
        href: Link URL
        cls: Additional CSS classes
    """
    from ...utils import merge_classes

    # Image area
    # Fallback gradient if no image
    img_src = image_url if image_url and image_url.strip() else ""
    bg_style = "background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);"

    if img_src:
        image_component = Img(
            src=img_src,
            alt=title,
            style="width: 100%; aspect-ratio: 16/9; object-fit: cover; border-bottom: 1px solid rgba(255,255,255,0.05);",
        )
    else:
        # Placeholder div
        image_component = Div(
            style=f"width: 100%; aspect-ratio: 16/9; {bg_style}",
        )

    # Content Body
    items = [
        heading(
            title,
            level=3,
            style="font-size: 1.1rem; font-weight: 600; color: white; margin-bottom: 0.5rem;",
        )
    ]

    if subtitle:
        items.append(
            text(
                subtitle,
                style="font-size: 0.9rem; color: var(--theme-text-muted); margin-bottom: 0.5rem;",
            )
        )

    if badge_text:
        items.append(
            badge(
                badge_text,
                variant="outline",
                style="border-color: var(--theme-accent-secondary); color: var(--theme-accent-secondary); background: rgba(121, 40, 202, 0.1);",
            )
        )

    body_content = flex(
        *items,
        direction="column",
        align="start",
        style="padding: 1rem;",
    )

    # Layout container
    layout = flex(
        image_component,
        body_content,
        direction="column",
        style="height: 100%; width: 100%;",
    )

    # Base Card styles (Deep Space Glassmorphism)
    base_style = """
        background: rgba(13, 17, 34, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        overflow: hidden;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.15);
    """

    css_class = merge_classes("hero-card hover-glow hover:translate-y-[-4px]", cls)

    card_component = card(
        layout,
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
