"""Dashboard Stat Card component."""

from typing import Any

from fasthtml.common import Div

from ...components.atoms.heading import heading
from ...utils import generate_style_string


def dashboard_stat_card(
    label: str,
    value: str | int,
    total: str | int | None = None,
    icon: Any = None,
    progress_value: int | None = None,
    gradient_start: str = "#22d3ee",
    gradient_end: str = "#a855f7",
    **kwargs: Any,
) -> Any:
    """
    A neon-styled stat card with progress bar for the dashboard.
    """
    # Extract style from kwargs to merge with component styles
    extra_style = kwargs.pop("style", "")

    # Neon glow effect
    box_style = generate_style_string(
        background="rgba(10, 10, 16, 0.6)",
        border=f"1px solid {gradient_start}",
        border_radius="16px",
        padding="1.5rem",
        display="flex",
        flex_direction="column",
        justify_content="space-between",
        box_shadow=f"0 0 10px {gradient_start}40, inset 0 0 20px {gradient_start}10",
        min_height="140px",
        position="relative",
        overflow="hidden",
    )

    header = Div(
        heading(
            label, level=3, style="font-size: 1.1rem; font-weight: 500; color: #e2e8f0; margin: 0;"
        ),
        Div(icon, style=f"color: {gradient_start}; font-size: 1.5rem;") if icon else "",
        style="display: flex; justify_content: space-between; align-items: flex-start; width: 100%; margin-bottom: 1rem;",
    )

    value_text = f"{value}"
    if total:
        value_text += f" / {total}"

    content = Div(
        heading(
            value_text,
            level=2,
            style="font-size: 1.8rem; font-weight: 700; color: #fff; margin: 0; margin-bottom: 0.5rem;",
        ),
    )

    progress_bar = ""
    if progress_value is not None:
        # Use HTML5 progress or custom div
        progress_bar = Div(
            Div(
                style=f"width: {progress_value}%; height: 100%; background: linear-gradient(90deg, {gradient_start}, {gradient_end}); border-radius: 4px; box-shadow: 0 0 8px {gradient_start};"
            ),
            style="width: 100%; height: 6px; background: #1e293b; border-radius: 4px; margin-top: auto;",
        )

    # Merge component style with any extra style passed in
    combined_style = f"{box_style} {extra_style}".strip()

    return Div(header, content, progress_bar, style=combined_style, **kwargs)
