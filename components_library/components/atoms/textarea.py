"""Textarea component - Multi-line text input."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Textarea as FtTextarea

from ...utils import merge_classes


def textarea(
    name: str,
    value: str | None = None,
    placeholder: str | None = None,
    rows: int = 4,
    size: Literal["sm", "md", "lg"] = "md",
    disabled: bool = False,
    readonly: bool = False,
    required: bool = False,
    error: bool = False,
    resize: Literal["none", "vertical", "horizontal", "both"] = "vertical",
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
) -> FtTextarea:
    """
    Multi-line text input component.

    Note: When used standalone, provide aria_label for accessibility.
    When wrapped in field(), the label is automatically associated.

    Args:
        name: Textarea name attribute
        value: Textarea value/content
        placeholder: Placeholder text
        rows: Number of visible text rows
        size: Textarea size (sm, md, lg)
        disabled: Whether textarea is disabled
        readonly: Whether textarea is read-only
        required: Whether textarea is required
        error: Whether textarea has an error state
        resize: CSS resize behavior
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
        Textarea element

    Example:
        >>> # With field wrapper
        >>> field(
        ...     textarea(name="description", id="description"),
        ...     label="Description",
        ...     label_for="description"
        ... )
        >>> # Standalone (requires aria-label)
        >>> textarea(
        ...     name="notes",
        ...     placeholder="Enter notes...",
        ...     aria_label="Notes"
        ... )
    """
    css_class = merge_classes(
        "input",
        "textarea",
        f"input-{size}",
        "input-error" if error else None,
        cls,
    )

    inline_style = f"resize: {resize};"
    if "style" in kwargs:
        inline_style = f"{inline_style} {kwargs.pop('style')}"

    attrs = {
        "name": name,
        "cls": css_class,
        "rows": rows,
        "placeholder": placeholder,
        "disabled": disabled,
        "readonly": readonly,
        "required": required,
        "style": inline_style,
    }

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

    content = value or ""

    return FtTextarea(content, **{**attrs, **kwargs})
