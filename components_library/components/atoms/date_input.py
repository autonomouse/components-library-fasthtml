"""DateInput component - Date picker input."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Input

from ...utils import merge_classes


def date_input(
    name: str,
    value: str | None = None,
    min: str | None = None,
    max: str | None = None,
    size: Literal["sm", "md", "lg"] = "md",
    disabled: bool = False,
    required: bool = False,
    error: bool = False,
    cls: str | None = None,
    # HTMX attributes
    hx_get: str | None = None,
    hx_post: str | None = None,
    hx_trigger: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    **kwargs: Any,
) -> Input:
    """
    Date picker input component (HTML5 date input).

    Args:
        name: Input name attribute
        value: Selected date (YYYY-MM-DD format)
        min: Minimum selectable date (YYYY-MM-DD format)
        max: Maximum selectable date (YYYY-MM-DD format)
        size: Input size (sm, md, lg)
        disabled: Whether input is disabled
        required: Whether input is required
        error: Whether input has an error state
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint
        hx_post: HTMX POST endpoint
        hx_trigger: HTMX trigger event (default: "change")
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        **kwargs: Additional HTML attributes

    Returns:
        Input element with type="date"

    Example:
        >>> date_input(
        ...     name="birth_date",
        ...     value="1990-01-15",
        ...     min="1900-01-01",
        ...     max="2024-12-31",
        ...     required=True
        ... )
    """
    css_class = merge_classes(
        "input",
        f"input-{size}",
        "input-error" if error else None,
        cls,
    )

    attrs = {
        "type": "date",
        "name": name,
        "cls": css_class,
        "disabled": disabled,
        "required": required,
    }

    if value is not None:
        attrs["value"] = value
    if min is not None:
        attrs["min"] = min
    if max is not None:
        attrs["max"] = max

    # HTMX attributes
    if hx_get:
        attrs["hx_get"] = hx_get
    if hx_post:
        attrs["hx_post"] = hx_post
    if hx_trigger:
        attrs["hx_trigger"] = hx_trigger
    # Default trigger for date input is "change"
    elif hx_get or hx_post:
        attrs["hx_trigger"] = "change"
    if hx_target:
        attrs["hx_target"] = hx_target
    if hx_swap:
        attrs["hx_swap"] = hx_swap

    return Input(**{**attrs, **kwargs})
