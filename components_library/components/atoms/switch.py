"""Switch component - Toggle switch input."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Input, Label, Span

from ...utils import merge_classes


def switch(
    name: str,
    label: str | None = None,
    checked: bool = False,
    disabled: bool = False,
    cls: str | None = None,
    # HTMX attributes
    hx_get: str | None = None,
    hx_post: str | None = None,
    hx_trigger: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    **kwargs: Any,
) -> Label | Div:
    """
    Toggle switch component.

    Args:
        name: Switch name attribute
        label: Label text (if provided, adds label next to switch)
        checked: Whether switch is checked/on
        disabled: Whether switch is disabled
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint
        hx_post: HTMX POST endpoint
        hx_trigger: HTMX trigger event (default: "change")
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        **kwargs: Additional HTML attributes

    Returns:
        Label or Div containing the switch

    Example:
        >>> switch(
        ...     name="notifications",
        ...     label="Enable notifications",
        ...     checked=True
        ... )
    """
    css_class = merge_classes("switch", cls)

    attrs = {
        "type": "checkbox",
        "name": name,
        "checked": checked,
        "disabled": disabled,
    }

    # HTMX attributes
    if hx_get:
        attrs["hx_get"] = hx_get
    if hx_post:
        attrs["hx_post"] = hx_post
    if hx_trigger:
        attrs["hx_trigger"] = hx_trigger
    # Default trigger for switch is "change"
    elif hx_get or hx_post:
        attrs["hx_trigger"] = "change"
    if hx_target:
        attrs["hx_target"] = hx_target
    if hx_swap:
        attrs["hx_swap"] = hx_swap

    # Build switch structure
    switch_element = Label(
        Input(**{**attrs, **kwargs}),
        Span(cls="switch-slider"),
        cls=css_class,
    )

    # If label is provided, wrap in container with label text
    if label:
        return Div(
            switch_element,
            Span(label, style="margin-left: 0.75rem;"),
            cls="switch-container",
            style="display: inline-flex; align-items: center;",
        )

    return switch_element
