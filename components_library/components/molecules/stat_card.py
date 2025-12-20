"""Stat Card component."""

from typing import Any

from fasthtml.common import Div

from ...components.atoms.heading import heading
from ...components.atoms.text import text
from ...utils import generate_style_string


def stat_card(
    label: str,
    value: str | int,
    icon: str | None = None,
    gradient_start: str = "#22d3ee",
    gradient_end: str = "#a855f7",
    **kwargs: Any,
) -> Any:
    """
    A glass-styled stat card displaying a single metric.

    Args:
        label: Label for the statistic
        value: Value to display
        icon: Optional icon character or HTML
        gradient_start: Start color for the value gradient
        gradient_end: End color for the value gradient
        **kwargs: Additional HTML attributes

    Returns:
        Div component
    """
    base_style = generate_style_string(
        background="rgba(17, 24, 39, 0.4)",
        backdrop_filter="blur(12px)",
        border="1px solid rgba(55, 65, 81, 0.5)",
        border_radius="12px",
        padding="1.5rem",
        display="flex",
        flex_direction="column",
        align_items="center",
        justify_content="center",
        transition="all 0.3s ease",
        min_width="200px",
    )

    # Merge custom style if provided
    custom_style = kwargs.pop("style", "")
    style = f"{base_style} {custom_style}"

    return Div(
        Div(
            icon,
            style="font-size: 2rem; margin-bottom: 0.5rem; color: var(--theme-accent-primary, #00f0ff);",
        )
        if icon
        else None,
        heading(
            str(value),
            level=2,
            style=f"font-size: 2.5rem; font-weight: bold; background: linear-gradient(to right, {gradient_start}, {gradient_end}); -webkit-background-clip: text; color: transparent;",
        ),
        text(
            label,
            style="color: var(--theme-text-secondary, #9ca3af); font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.05em;",
        ),
        style=style,
        cls="stat-card",
        **kwargs,
    )
