"""Radio component - Radio button input with label."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Input, Label

from ...utils import merge_classes


def radio(
    name: str,
    value: str,
    label: str | None = None,
    checked: bool = False,
    disabled: bool = False,
    required: bool = False,
    cls: str | None = None,
    # HTMX attributes
    hx_get: str | None = None,
    hx_post: str | None = None,
    hx_trigger: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    **kwargs: Any,
) -> Label | Input:
    """
    Radio button input component with optional label.

    Args:
        name: Radio button name attribute (group identifier)
        value: Value of this specific radio option
        label: Label text (if provided, wraps radio in label)
        checked: Whether this radio is checked
        disabled: Whether radio is disabled
        required: Whether radio is required
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint
        hx_post: HTMX POST endpoint
        hx_trigger: HTMX trigger event (default: "change")
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        **kwargs: Additional HTML attributes

    Returns:
        Input element or Label wrapping input

    Example:
        >>> Div(
        ...     radio(name="size", value="small", label="Small"),
        ...     radio(name="size", value="medium", label="Medium", checked=True),
        ...     radio(name="size", value="large", label="Large"),
        ... )
    """
    css_class = merge_classes("radio", cls)

    attrs = {
        "type": "radio",
        "name": name,
        "value": value,
        "cls": css_class,
        "checked": checked,
        "disabled": disabled,
        "required": required,
    }

    # HTMX attributes
    if hx_get:
        attrs["hx_get"] = hx_get
    if hx_post:
        attrs["hx_post"] = hx_post
    if hx_trigger:
        attrs["hx_trigger"] = hx_trigger
    # Default trigger for radio is "change"
    elif hx_get or hx_post:
        attrs["hx_trigger"] = "change"
    if hx_target:
        attrs["hx_target"] = hx_target
    if hx_swap:
        attrs["hx_swap"] = hx_swap

    input_element = Input(**{**attrs, **kwargs})

    # If label is provided, wrap in a label element
    if label:
        return Label(
            input_element,
            label,
            cls="radio-label",
            style="display: inline-flex; align-items: center; gap: 0.5rem; cursor: pointer;",
        )

    return input_element
