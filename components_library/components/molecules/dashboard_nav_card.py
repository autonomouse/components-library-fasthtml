"""Dashboard Navigation Card component."""

from typing import Any

from fasthtml.common import A, Div

from ...components.atoms.heading import heading
from ...components.atoms.text import text
from ...utils import generate_style_string


def dashboard_nav_card(
    title: str,
    description: str,
    href: str,
    icon_content: Any = None,  # Can be an SVG or huge icon
    color: str = "#3b82f6",
    **kwargs: Any,
) -> Any:
    """
    A navigation card for dashboard panels (Scene Board, etc.).
    """
    # Extract style from kwargs to merge with component styles
    extra_style = kwargs.pop("style", "")

    card_style = generate_style_string(
        background="rgba(10, 10, 16, 0.6)",
        border=f"1px solid {color}",
        border_radius="16px",
        padding="1.5rem",
        display="flex",
        flex_direction="column",
        align_items="center",
        text_align="center",
        box_shadow=f"0 0 10px {color}40, inset 0 0 20px {color}10",
        transition="transform 0.2s, box-shadow 0.2s",
        height="100%",
        cursor="pointer",
        text_decoration="none",  # Ensure link doesn't underline everything
    )

    # Hover effect style injection usually handled by CSS class, but we can try inline or parent
    # For now, we rely on the class 'dashboard-nav-card' if we had global CSS,
    # but let's just make it look good static first.

    return A(
        heading(
            title,
            level=3,
            style=f"font-size: 1.25rem; font-weight: 600; color: {color}; margin-bottom: 1rem; text-shadow: 0 0 5px {color}80;",
        ),
        Div(
            icon_content,
            style="font-size: 3rem; margin-bottom: 1rem; flex-grow: 1; display: flex; align-items: center; justify_content: center;",
        )
        if icon_content
        else "",
        text(description, style="color: #94a3b8; font-size: 0.875rem; line-height: 1.4;"),
        href=href,
        style=f"{card_style} {extra_style}".strip(),
        cls="dashboard-nav-card hover:scale-105",
        **kwargs,
    )
