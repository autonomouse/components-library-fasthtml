"""IconButton component - Button with icon only."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Button as FtButton

from ...utils import merge_classes


def icon_button(
    icon: str,
    aria_label: str,
    variant: Literal["solid", "outline", "ghost"] = "ghost",
    color_palette: Literal["brand", "gray", "red", "green"] = "gray",
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
    **kwargs: Any,
) -> FtButton:
    """
    Icon-only button component.

    Requires aria-label for accessibility.

    Args:
        icon: Icon content (text, emoji, or SVG)
        aria_label: Accessibility label (required)
        variant: Visual variant (solid, outline, ghost)
        color_palette: Color scheme (brand, gray, red, green)
        size: Button size (xs, sm, md, lg, xl)
        disabled: Whether button is disabled
        loading: Show loading state
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
        **kwargs: Additional HTML attributes

    Returns:
        Button element with icon only

    Example:
        >>> icon_button("×", aria_label="Close", size="sm")
        >>> icon_button("🗑️", aria_label="Delete", color_palette="red")
        >>> icon_button("⚙️", aria_label="Settings", hx_get="/settings")
    """
    css_class = merge_classes(
        "btn",
        "icon-btn",
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
        "aria-label": aria_label,
        "title": aria_label,  # Also add title for hover tooltip
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

    return FtButton(icon, **{**attrs, **kwargs})
