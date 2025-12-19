"""Link component - Styled anchor element."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import A

from ...design_system.tokens import Colors
from ...utils import merge_classes

colors = Colors()


def link(
    text: str,
    href: str,
    variant: Literal["default", "primary", "muted", "underline"] = "default",
    size: Literal["xs", "sm", "md", "lg", "xl"] = "md",
    external: bool = False,
    disabled: bool = False,
    cls: str | None = None,
    # HTMX attributes
    hx_get: str | None = None,
    hx_post: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    hx_push_url: bool | str = False,
    **kwargs: Any,
) -> A:
    """
    Link component with styling variants.

    Args:
        text: Link text content
        href: Link destination URL
        variant: Visual variant (default, primary, muted, underline)
        size: Link size (xs, sm, md, lg, xl)
        external: Whether link opens in new tab (adds target="_blank")
        disabled: Whether link is disabled (prevents navigation)
        cls: Additional CSS classes
        hx_get: HTMX GET endpoint (for SPA-style navigation)
        hx_post: HTMX POST endpoint
        hx_target: HTMX target selector
        hx_swap: HTMX swap strategy
        hx_push_url: HTMX push URL to browser history
        **kwargs: Additional HTML attributes

    Returns:
        Anchor element

    Example:
        >>> link("Home", href="/")
        >>> link("Docs", href="/docs", variant="primary")
        >>> link("External", href="https://example.com", external=True)
        >>> link("Dashboard", href="/dashboard", hx_get="/dashboard", hx_push_url=True)
    """
    css_class = merge_classes(
        "link",
        f"link-{variant}",
        f"link-{size}",
        "link-disabled" if disabled else None,
        cls,
    )

    attrs = {
        "href": href if not disabled else "#",
        "cls": css_class,
    }

    # External link attributes
    if external:
        attrs["target"] = "_blank"
        attrs["rel"] = "noopener noreferrer"

    # Disabled state
    if disabled:
        attrs["aria-disabled"] = "true"
        attrs["style"] = "pointer-events: none; opacity: 0.6;"

    # HTMX attributes (for SPA-style navigation)
    if hx_get:
        attrs["hx_get"] = hx_get
    if hx_post:
        attrs["hx_post"] = hx_post
    if hx_target:
        attrs["hx_target"] = hx_target
    if hx_swap:
        attrs["hx_swap"] = hx_swap
    if hx_push_url:
        attrs["hx_push_url"] = "true" if hx_push_url is True else hx_push_url

    return A(text, **{**attrs, **kwargs})
