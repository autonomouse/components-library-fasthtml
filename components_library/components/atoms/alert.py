"""Alert component - Notification and feedback messages."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Span

from ...utils import merge_classes


def alert(
    message: str,
    variant: Literal["info", "success", "warning", "error"] = "info",
    title: str | None = None,
    icon: str | None = None,
    closeable: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Alert component for displaying important messages.

    Args:
        message: Alert message content
        variant: Alert type (info, success, warning, error)
        title: Optional title/heading
        icon: Optional icon (emoji or text)
        closeable: Whether alert can be dismissed (adds close button)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with alert styling

    Example:
        >>> alert("Your changes have been saved", variant="success")
        >>> alert("Please verify your email", variant="info", title="Action Required")
        >>> alert("Error processing request", variant="error", closeable=True)
    """
    css_class = merge_classes("alert", f"alert-{variant}", cls)

    # Default icons for each variant
    default_icons = {
        "info": "ℹ️",
        "success": "✅",
        "warning": "⚠️",
        "error": "❌",
    }

    icon_text = icon if icon is not None else default_icons[variant]

    elements = []

    # Icon
    if icon_text:
        elements.append(Span(icon_text, cls="alert-icon"))

    # Content
    content_elements = []
    if title:
        content_elements.append(Div(title, cls="alert-title"))
    content_elements.append(Div(message, cls="alert-description"))

    elements.append(Div(*content_elements, cls="alert-content"))

    # Close button (if closeable)
    # Uses HTMX hx-on:click for event handling (part of HTMX, not raw JS)
    if closeable:
        elements.append(
            Span(
                "×",
                cls="alert-close",
                style="margin-left: auto; cursor: pointer; font-size: 1.25rem; font-weight: bold;",
                **{"hx-on:click": "this.closest('.alert').remove()"},
            )
        )

    return Div(*elements, cls=css_class, **kwargs)
