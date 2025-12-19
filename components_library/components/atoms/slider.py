"""Slider component - Range slider input."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Input, Label, Span

from ...utils import merge_classes


def slider(
    name: str,
    value: float | int = 50,
    min: float | int = 0,
    max: float | int = 100,
    step: float | int = 1,
    label: str | None = None,
    show_value: bool = True,
    disabled: bool = False,
    cls: str | None = None,
    # HTMX attributes
    hx_get: str | None = None,
    hx_post: str | None = None,
    hx_trigger: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Range slider component.

    Args:
        name: Slider name attribute
        value: Current slider value
        min: Minimum value
        max: Maximum value
        step: Step increment
        label: Label text
        show_value: Whether to display current value
        disabled: Whether slider is disabled
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint
        hx_post: HTMX POST endpoint
        hx_trigger: HTMX trigger event (default: "change")
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        **kwargs: Additional HTML attributes

    Returns:
        Div containing slider and optional label/value display

    Example:
        >>> slider(
        ...     name="volume",
        ...     value=75,
        ...     min=0,
        ...     max=100,
        ...     label="Volume",
        ...     show_value=True
        ... )
    """
    css_class = merge_classes("slider", cls)

    attrs = {
        "type": "range",
        "name": name,
        "value": value,
        "min": min,
        "max": max,
        "step": step,
        "disabled": disabled,
        "cls": "input",
    }

    # HTMX attributes
    if hx_get:
        attrs["hx_get"] = hx_get
    if hx_post:
        attrs["hx_post"] = hx_post
    if hx_trigger:
        attrs["hx_trigger"] = hx_trigger
    # Default trigger for slider can be "change" or "input"
    elif hx_get or hx_post:
        attrs["hx_trigger"] = "change"  # Use "input" for real-time updates
    if hx_target:
        attrs["hx_target"] = hx_target
    if hx_swap:
        attrs["hx_swap"] = hx_swap

    elements = []

    # Optional label
    if label:
        elements.append(
            Label(
                label,
                style="display: block; margin-bottom: 0.5rem; font-weight: 500;",
            )
        )

    # Container for slider and value
    slider_container = []
    slider_container.append(Input(**{**attrs, **kwargs}))

    # Optional value display
    if show_value:
        slider_container.append(
            Span(
                str(value),
                id=f"{name}-value",
                style="margin-left: 0.75rem; font-weight: 500; min-width: 3ch;",
            )
        )

    elements.append(
        Div(
            *slider_container,
            style="display: flex; align-items: center; gap: 0.5rem;",
        )
    )

    return Div(*elements, cls=css_class)
