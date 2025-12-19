"""Button component - Primary interaction element."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Button as FtButton

from ...utils import merge_classes


def button(
    text: str,
    variant: Literal["solid", "outline", "ghost"] = "solid",
    color_palette: Literal["brand", "gray", "red", "green"] = "brand",
    size: Literal["xs", "sm", "md", "lg", "xl"] = "md",
    disabled: bool = False,
    loading: bool = False,
    type: Literal["button", "submit", "reset"] = "button",
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
    hx_confirm: str | None = None,
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
) -> FtButton:
    """
    Button component for user interactions.

    Args:
        text: Button text content
        variant: Visual variant (solid, outline, ghost)
        color_palette: Color scheme (brand, gray, red, green)
        size: Button size (xs, sm, md, lg, xl)
        disabled: Whether button is disabled
        loading: Show loading state (adds spinner, disables button)
        type: HTML button type attribute
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint
        hx_post: HTMX POST endpoint
        hx_put: HTMX PUT endpoint
        hx_patch: HTMX PATCH endpoint
        hx_delete: HTMX DELETE endpoint
        hx_trigger: HTMX trigger event
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        hx_confirm: HTMX confirmation message
        hx_vals: HTMX values to send
        hx_vars: HTMX variables to send
        hx_include: HTMX include selector
        hx_ext: HTMX extension
        hx_boost: HTMX boost mode
        hx_indicator: HTMX loading indicator
        hx_prompt: HTMX prompt message
        hx_preserve: HTMX preserve elements
        hx_sync: HTMX sync strategy
        **kwargs: Additional HTML attributes

    Returns:
        Button element

    Example:
        >>> button("Save", variant="solid", color_palette="brand")
        >>> button("Delete", color_palette="red", hx_delete="/api/item/1")
        >>> button("Loading...", loading=True)
    """
    css_class = merge_classes(
        "btn",
        f"btn-{variant}",
        f"btn-{color_palette}",
        f"btn-{size}",
        "btn-loading" if loading else None,
        cls,
    )

    attrs = {
        "type": type,
        "cls": css_class,
        "disabled": disabled or loading,
    }

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
    if hx_confirm:
        attrs["hx_confirm"] = hx_confirm
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

    return FtButton(text, **{**attrs, **kwargs})
