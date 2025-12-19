"""Button Link component - Anchor element styled as a button."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import A

from ...utils import merge_classes


def button_link(
    text: str,
    href: str,
    variant: Literal["solid", "outline", "ghost"] = "solid",
    color_palette: Literal["brand", "gray", "red", "green", "blue"] = "brand",
    size: Literal["xs", "sm", "md", "lg", "xl"] = "md",
    disabled: bool = False,
    loading: bool = False,
    full_width: bool = False,
    cls: str | None = None,
    # HTMX attributes
    hx_get: str | None = None,
    hx_post: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    **kwargs: Any,
) -> A:
    """
    Button Link - An anchor element styled as a button.

    This component allows proper link behavior (middle-click, right-click, etc.)
    while maintaining button appearance.

    Args:
        text: Button text content
        href: Link destination URL
        variant: Button style variant (solid, outline, ghost)
        color_palette: Color scheme (brand, gray, red, green, blue)
        size: Button size (xs, sm, md, lg, xl)
        disabled: Whether button is disabled
        loading: Whether button is in loading state
        full_width: Whether button should take full width
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint
        hx_post: HTMX POST endpoint
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        **kwargs: Additional HTML attributes

    Returns:
        Anchor element styled as a button

    Example:
        >>> button_link("Go Home", href="/", variant="solid", color_palette="brand")
        >>> button_link("Learn More", href="/docs", variant="outline", size="lg")
    """
    css_class = merge_classes(
        "btn",
        f"btn-{variant}",
        f"btn-{color_palette}",
        f"btn-{size}",
        "btn-loading" if loading else None,
        "btn-disabled" if disabled else None,
        cls,
    )

    # Build styles
    styles = []
    if full_width:
        styles.append("width: 100%")

    # Remove text-decoration from link
    styles.append("text-decoration: none")
    styles.append("display: inline-flex")

    style = "; ".join(styles) if styles else None

    attrs = {
        "href": href if not disabled else "#",
        "cls": css_class,
    }

    if style:
        attrs["style"] = style

    # Disabled state
    if disabled:
        attrs["aria-disabled"] = "true"
        if "style" in attrs:
            attrs["style"] += "; pointer-events: none; opacity: 0.6;"
        else:
            attrs["style"] = "pointer-events: none; opacity: 0.6;"

    # HTMX attributes
    if hx_get:
        attrs["hx_get"] = hx_get
    if hx_post:
        attrs["hx_post"] = hx_post
    if hx_target:
        attrs["hx_target"] = hx_target
    if hx_swap:
        attrs["hx_swap"] = hx_swap

    return A(text, **{**attrs, **kwargs})
