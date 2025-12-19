"""ConfidenceScore component - displays confidence levels as a progress bar."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...design_system.tokens import Colors
from ...utils import generate_style_string, merge_classes

colors = Colors()


def _get_color_for_percent(percent: float) -> str:
    """Get color based on confidence percentage."""
    if percent <= 40:
        return colors.error.s500
    if percent <= 70:
        return colors.warning.s500
    return colors.success.s500


def confidence_score(
    percent: float,
    size: Literal["xs", "sm", "md", "lg"] = "xs",
    width: str = "120px",
    show_label: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    ConfidenceScore component for displaying confidence levels as a progress bar.

    Visualizes confidence percentages with color-coded progress:
    - 0-40%: Red (low confidence)
    - 41-70%: Orange (medium confidence)
    - 71-100%: Green (high confidence)

    Args:
        percent: Confidence percentage (0-100)
        size: Size variant (xs, sm, md, lg)
        width: Width of the progress bar
        show_label: Whether to show percentage label
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Confidence score progress bar element

    Example:
        >>> confidence_score(75)  # Green bar at 75%
        >>> confidence_score(35, size="md", show_label=True)  # Red bar with label
    """
    # Clamp percent to 0-100
    clamped_percent = max(0, min(100, percent))
    bar_color = _get_color_for_percent(clamped_percent)

    # Size configurations
    size_map = {
        "xs": "4px",
        "sm": "6px",
        "md": "8px",
        "lg": "12px",
    }
    bar_height = size_map[size]

    # Track styles
    track_style = generate_style_string(
        width=width,
        height=bar_height,
        background_color=colors.neutral.s200,
        border_radius="9999px",
        overflow="hidden",
    )

    # Bar styles
    bar_style = generate_style_string(
        width=f"{clamped_percent}%",
        height="100%",
        background_color=bar_color,
        border_radius="9999px",
        transition="width 0.3s ease-out",
    )

    css_class = merge_classes("confidence-score", cls)

    bar_element = Div(
        Div(style=bar_style),
        style=track_style,
    )

    if show_label:
        container_style = generate_style_string(
            display="flex",
            align_items="center",
            gap="0.5rem",
        )
        label_style = generate_style_string(
            font_size="0.75rem",
            color=colors.text_secondary,
        )
        return Div(
            bar_element,
            Div(f"{int(clamped_percent)}%", style=label_style),
            cls=css_class,
            style=container_style,
            **kwargs,
        )

    return Div(bar_element, cls=css_class, **kwargs)
