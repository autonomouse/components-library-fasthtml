"""Navigation Card component."""

from typing import Any

from fasthtml.common import A, Div

from ...components.atoms.heading import heading
from ...components.atoms.text import text
from ...utils import generate_style_string


def _card_stack(images: list[str | None], names: list[str] | None = None) -> Div:
    """
    Create a featured card with smaller stacked cards beside it.

    Args:
        images: List of image URLs
        names: Optional list of names for initials fallback

    Returns:
        Div containing card layout
    """
    if names is None:
        names = []

    # Pad names to match images length
    padded_names = (names[:4] if names else []) + [None] * 4
    items = list(zip(images[:4], padded_names[:4], strict=False))

    if not items:
        return Div()

    def get_initials(name: str | None) -> str:
        if not name:
            return "?"
        parts = name.strip().split()
        return (parts[0][0] + (parts[-1][0] if len(parts) > 1 else "")).upper()

    def make_card(
        img_url: str | None, name: str | None, w: int, h: int, extra_style: str = ""
    ) -> Div:
        initials = get_initials(name)
        base = f"width: {w}px; height: {h}px; border-radius: 8px; border: 2px solid rgba(59, 130, 246, 0.5); box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4); {extra_style}"
        if img_url:
            return Div(
                style=f"{base} background-image: url('{img_url}'); background-size: cover; background-position: center;"
            )
        return Div(
            initials,
            style=f"{base} background: linear-gradient(135deg, #1e3a5f, #3b82f6); display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: {w * 0.3}px;",
        )

    # Featured card (first item) - larger
    featured_w, featured_h = 70, 90
    featured = make_card(items[0][0], items[0][1], featured_w, featured_h, "flex-shrink: 0;")

    # Smaller stacked cards on the right
    small_w, small_h = 45, 60
    stack_cards = []
    remaining = items[1:4]  # Up to 3 more cards

    for i, (img_url, name) in enumerate(remaining):
        rotation = (i - 1) * 6  # -6, 0, 6 degrees
        offset_y = 8 + i * 2
        stack_cards.append(
            make_card(
                img_url,
                name,
                small_w,
                small_h,
                f"position: absolute; left: {i * 18}px; top: {offset_y}px; transform: rotate({rotation}deg); z-index: {i + 1};",
            )
        )

    # Stack container
    stack_width = small_w + (len(remaining) - 1) * 18 + 10 if remaining else 0
    stack_container = (
        Div(
            *stack_cards,
            style=f"position: relative; width: {stack_width}px; height: {featured_h}px; margin-left: 8px;",
        )
        if stack_cards
        else None
    )

    children = [featured]
    if stack_container:
        children.append(stack_container)

    return Div(
        *children,
        style="display: flex; align-items: flex-end; margin-bottom: 0.75rem;",
    )


def nav_card(
    title: str,
    description: str,
    href: str,
    preview_images: list[str | None] | None = None,
    preview_names: list[str] | None = None,
    **kwargs: Any,
) -> Any:
    """
    A navigation card component with optional stacked preview images.

    Args:
        title: Card title
        description: Card description
        href: Link URL
        preview_images: Optional list of image URLs to show as stacked avatars
        preview_names: Optional list of names for initials fallback
        **kwargs: Additional HTML attributes

    Returns:
        Anchor component
    """
    base_style = generate_style_string(
        background="rgba(17, 24, 39, 0.4)",
        backdrop_filter="blur(12px)",
        border="1px solid rgba(55, 65, 81, 0.5)",
        border_radius="12px",
        padding="1.5rem",
        transition="all 0.3s ease",
        display="block",
        text_decoration="none",
        height="100%",
        cursor="pointer",
    )

    # Merge custom style if provided
    custom_style = kwargs.pop("style", "")
    style = f"{base_style} {custom_style}"

    content = []

    # Add fanned card stack if preview data provided
    if preview_images or preview_names:
        images = preview_images or []
        names = preview_names or []
        # Ensure we have at least placeholder data
        if not images and names:
            images = [None] * len(names)
        content.append(_card_stack(images, names))

    content.extend(
        [
            heading(
                title,
                level=3,
                style="font-size: 1.25rem; font-weight: bold; color: var(--theme-text-primary, white); margin-bottom: 0.5rem;",
            ),
            text(
                description,
                style="color: var(--theme-text-secondary, #9ca3af); font-size: 0.875rem;",
            ),
        ]
    )

    return A(
        *content,
        href=href,
        style=style,
        cls="nav-card hover:bg-white/5",
        **kwargs,
    )
