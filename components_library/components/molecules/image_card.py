"""Image Card molecule - Card with prominent image header."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Div, Img

from ...utils import merge_classes
from ..atoms import badge, card, flex, heading, text


def image_card(
    title: str,
    *children: Any,
    image_url: str | None = None,
    image_alt: str | None = None,
    image_height: str = "200px",
    badge_text: str | None = None,
    badge_position: str = "top-left",
    description: str | None = None,
    href: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Card component with a prominent image header.

    A flexible card for displaying content with an image, badge, title, and description.
    Uses theme-aware styling and supports optional click navigation.

    Args:
        title: Card title
        *children: Additional content to display below the description
        image_url: URL for the header image
        image_alt: Alt text for the image (defaults to title)
        image_height: CSS height for the image (default: "200px")
        badge_text: Optional badge text (e.g., "Day 1", "Featured")
        badge_position: Badge position - "top-left", "top-right", "bottom-left", "bottom-right"
        description: Optional description text
        href: Optional link URL - makes the card clickable
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes (including hx_* for HTMX)

    Returns:
        Card component with image header

    Example:
        >>> image_card(
        ...     "Tokyo Tower",
        ...     image_url="https://example.com/tokyo.jpg",
        ...     badge_text="Day 1",
        ...     description="Visit the iconic Tokyo Tower for panoramic city views.",
        ...     href="/locations/tokyo",
        ... )
    """
    # Image section
    img_alt = image_alt or title
    if image_url:
        image_section = Div(
            Img(
                src=image_url,
                alt=img_alt,
                style=f"width: 100%; height: {image_height}; object-fit: cover;",
            ),
            style="position: relative; overflow: hidden;",
        )
    else:
        # Placeholder when no image
        image_section = Div(
            Div(
                title[0] if title else "?",
                style="font-size: 3rem; color: var(--theme-text-muted, #9ca3af);",
            ),
            style=f"""
                width: 100%;
                height: {image_height};
                background: linear-gradient(135deg,
                    var(--theme-bg-start, #1a1a2e) 0%,
                    var(--theme-bg-end, #16213e) 100%);
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
            """,
        )

    # Badge overlay
    if badge_text:
        position_styles = {
            "top-left": "top: 0.75rem; left: 0.75rem;",
            "top-right": "top: 0.75rem; right: 0.75rem;",
            "bottom-left": "bottom: 0.75rem; left: 0.75rem;",
            "bottom-right": "bottom: 0.75rem; right: 0.75rem;",
        }
        badge_style = position_styles.get(badge_position, position_styles["top-left"])

        badge_element = Div(
            badge(
                badge_text,
                variant="brand",
                style="font-weight: 600;",
            ),
            style=f"position: absolute; {badge_style} z-index: 10;",
        )

        # Wrap image with badge
        image_section = Div(
            image_section,
            badge_element,
            style="position: relative;",
        )

    # Content section
    content_items = [
        heading(
            title,
            level=3,
            style="""
                font-size: 1.25rem;
                font-weight: 600;
                color: var(--theme-text-primary, #ffffff);
                margin: 0 0 0.5rem 0;
                line-height: 1.3;
            """,
        )
    ]

    if description:
        content_items.append(
            text(
                description,
                style="""
                    color: var(--theme-text-secondary, #9ca3af);
                    line-height: 1.6;
                    margin: 0;
                """,
            )
        )

    # Additional children
    if children:
        content_items.extend(children)

    content_section = flex(
        *content_items,
        direction="column",
        gap="0.5rem",
        style="padding: 1.25rem;",
    )

    # Card wrapper
    card_style = """
        background: var(--theme-card-bg, rgba(255, 255, 255, 0.95));
        border: 1px solid var(--theme-card-border, rgba(0, 0, 0, 0.1));
        border-radius: 12px;
        overflow: hidden;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    """

    # Add hover effect via CSS class
    css_class = merge_classes("image-card", cls)

    # Merge any incoming style
    extra_style = kwargs.pop("style", "")
    combined_style = f"{card_style} {extra_style}".strip()

    card_content = card(
        flex(
            image_section,
            content_section,
            direction="column",
        ),
        style=combined_style,
        cls=css_class,
        **kwargs,
    )

    # Wrap in link if href provided
    if href and href != "#":
        return A(
            card_content,
            href=href,
            style="text-decoration: none; display: block;",
        )

    return card_content
