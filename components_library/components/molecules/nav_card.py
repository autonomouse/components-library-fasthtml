"""Navigation Card component."""

from typing import Any

from fasthtml.common import A

from ...components.atoms.heading import heading
from ...components.atoms.text import text
from ...utils import generate_style_string


def nav_card(
    title: str,
    description: str,
    href: str,
    image_url: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    A navigation card component.

    Args:
        title: Card title
        description: Card description
        href: Link URL
        image_url: Optional background/header image URL
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

    content = [
        heading(
            title,
            level=3,
            style="font-size: 1.25rem; font-weight: bold; color: var(--theme-text-primary, white); margin-bottom: 0.5rem;",
        ),
        text(
            description, style="color: var(--theme-text-secondary, #9ca3af); font-size: 0.875rem;"
        ),
    ]

    if image_url:
        # TODO: integrate image
        pass

    return A(
        *content,
        href=href,
        style=style,
        cls="nav-card hover:bg-white/5",  # Add hover class if supported, or rely on base styles
        **kwargs,
    )
