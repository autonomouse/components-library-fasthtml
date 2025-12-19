"""Checkbox component - Checkbox input with label."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Input, Label

from ...utils import merge_classes


def checkbox(
    name: str,
    label: str | None = None,
    checked: bool = False,
    value: str = "on",
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
) -> Div | Input:
    """
    Checkbox input component with optional label.

    Args:
        name: Checkbox name attribute
        label: Label text (if provided, wraps checkbox in label)
        checked: Whether checkbox is checked
        value: Value when checked
        disabled: Whether checkbox is disabled
        required: Whether checkbox is required
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint
        hx_post: HTMX POST endpoint
        hx_trigger: HTMX trigger event (default: "change")
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        **kwargs: Additional HTML attributes

    Returns:
        Input element or Div with label

    Example:
        >>> checkbox(
        ...     name="accept_terms",
        ...     label="I accept the terms and conditions",
        ...     required=True
        ... )
    """
    css_class = merge_classes("checkbox", cls)

    attrs = {
        "type": "checkbox",
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
    # Default trigger for checkbox is "change"
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
            cls="checkbox-label",
            style="display: inline-flex; align-items: center; gap: 0.5rem; cursor: pointer;",
        )

    return input_element
