"""Progress component - Progress bar indicator."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...utils import merge_classes


def progress(
    value: float | int,
    max_value: float | int = 100,
    show_label: bool = False,
    label: str | None = None,
    aria_label: str | None = None,
    color: str | None = None,
    height: str = "0.5rem",
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Progress bar component.

    Args:
        value: Current progress value
        max_value: Maximum value (default: 100)
        show_label: Whether to show percentage label
        label: Custom label text (overrides percentage)
        aria_label: Accessible label for screen readers (auto-generated if not provided)
        color: Custom progress bar color
        height: Progress bar height (CSS value)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with progress bar

    Example:
        >>> progress(75)
        >>> progress(45, show_label=True)
        >>> progress(30, max_value=50, label="30/50 complete")
        >>> progress(50, aria_label="Upload progress")
    """
    # Calculate percentage
    percentage = min((value / max_value) * 100, 100)

    # Generate aria-label if not provided
    if not aria_label:
        aria_label = f"Progress: {int(percentage)}%"

    css_class = merge_classes("progress", cls)

    # Progress bar style
    bar_style = f"width: {percentage}%;"
    if color:
        bar_style += f" background-color: {color};"

    elements = []

    # Optional label above progress bar
    if show_label or label:
        label_text = label if label else f"{int(percentage)}%"
        elements.append(
            Div(
                label_text,
                style="margin-bottom: 0.25rem; font-size: 0.875rem; font-weight: 500;",
            )
        )

    # Progress container and bar
    elements.append(
        Div(
            Div(cls="progress-bar", style=bar_style),
            cls=css_class,
            style=f"height: {height};",
            role="progressbar",
            **{
                "aria-label": aria_label,
                "aria-valuenow": str(value),
                "aria-valuemin": "0",
                "aria-valuemax": str(max_value),
            },
            **kwargs,
        )
    )

    return Div(*elements) if len(elements) > 1 else elements[0]
