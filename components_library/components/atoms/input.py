"""Input component - Text input with variants."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Input as FtInput

from ...design_system.tokens import Colors
from ...utils import merge_classes

colors = Colors()


def input(
    name: str,
    value: str | None = None,
    placeholder: str | None = None,
    type: Literal["text", "email", "password", "number", "tel", "url", "search"] = "text",
    size: Literal["sm", "md", "lg"] = "md",
    disabled: bool = False,
    readonly: bool = False,
    required: bool = False,
    error: bool = False,
    aria_label: str | None = None,
    cls: str | None = None,
    # HTMX attributes
    hx_get: str | None = None,
    hx_post: str | None = None,
    hx_put: str | None = None,
    hx_patch: str | None = None,
    hx_delete: str | None = None,
    hx_trigger: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    hx_vals: str | None = None,
    hx_vars: str | None = None,
    hx_include: str | None = None,
    hx_ext: str | None = None,
    hx_boost: bool | None = None,
    hx_indicator: str | None = None,
    hx_prompt: str | None = None,
    hx_preserve: bool | None = None,
    hx_sync: str | None = None,
    **kwargs: Any,
) -> FtInput:
    """
    Text input component with various types and states.

    Note: When used standalone, provide aria_label for accessibility.
    When wrapped in field(), the label is automatically associated.

    Args:
        name: Input name attribute
        value: Input value
        placeholder: Placeholder text
        type: Input type (text, email, password, etc.)
        size: Input size (sm, md, lg)
        disabled: Whether input is disabled
        readonly: Whether input is read-only
        required: Whether input is required
        error: Whether input has an error state
        aria_label: Accessible label for screen readers (required if used standalone)
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint
        hx_post: HTMX POST endpoint
        hx_put: HTMX PUT endpoint
        hx_patch: HTMX PATCH endpoint
        hx_delete: HTMX DELETE endpoint
        hx_trigger: HTMX trigger event
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        hx_vals: HTMX values to send
        hx_vars: HTMX variables to send
        hx_include: HTMX include selector
        hx_ext: HTMX extension
        hx_boost: HTMX boost mode
        hx_indicator: HTMX loading indicator
        hx_prompt: HTMX prompt message
        hx_preserve: HTMX preserve elements
        hx_sync: HTMX sync strategy
        **kwargs: Additional HTML attributes (including id for label association)

    Returns:
        Input element

    Example:
        >>> # With field wrapper (label automatically associated)
        >>> field(
        ...     input(name="email", type="email", id="email"),
        ...     label="Email Address",
        ...     label_for="email"
        ... )
        >>> # Standalone (requires aria-label)
        >>> input(
        ...     name="search",
        ...     type="search",
        ...     placeholder="Search...",
        ...     aria_label="Search tests"
        ... )
    """
    css_class = merge_classes(
        "input",
        f"input-{size}",
        "input-error" if error else None,
        cls,
    )

    attrs = {
        "name": name,
        "type": type,
        "cls": css_class,
        "placeholder": placeholder,
        "disabled": disabled,
        "readonly": readonly,
        "required": required,
    }

    if value is not None:
        attrs["value"] = value

    if aria_label:
        attrs["aria_label"] = aria_label

    # HTMX attributes
    if hx_get:
        attrs["hx_get"] = hx_get
    if hx_post:
        attrs["hx_post"] = hx_post
    if hx_put:
        attrs["hx_put"] = hx_put
    if hx_patch:
        attrs["hx_patch"] = hx_patch
    if hx_delete:
        attrs["hx_delete"] = hx_delete
    if hx_trigger:
        attrs["hx_trigger"] = hx_trigger
    if hx_target:
        attrs["hx_target"] = hx_target
    if hx_swap:
        attrs["hx_swap"] = hx_swap
    if hx_vals:
        attrs["hx_vals"] = hx_vals
    if hx_vars:
        attrs["hx_vars"] = hx_vars
    if hx_include:
        attrs["hx_include"] = hx_include
    if hx_ext:
        attrs["hx_ext"] = hx_ext
    if hx_boost is not None:
        attrs["hx_boost"] = hx_boost
    if hx_indicator:
        attrs["hx_indicator"] = hx_indicator
    if hx_prompt:
        attrs["hx_prompt"] = hx_prompt
    if hx_preserve is not None:
        attrs["hx_preserve"] = hx_preserve
    if hx_sync:
        attrs["hx_sync"] = hx_sync

    return FtInput(**{**attrs, **kwargs})
