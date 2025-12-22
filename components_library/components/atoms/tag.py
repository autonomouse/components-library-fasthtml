"""Tag component - Removable label."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Span

from ...utils import merge_classes


def tag(
    text: str,
    removable: bool = False,
    on_remove: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Span:
    """
    Tag component for removable labels.

    Args:
        text: Tag text content
        removable: Whether tag can be removed
        on_remove: HTMX delete URL for server-side removal (if None, removes client-side)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Span element with tag styling

    Example:
        >>> tag("Python")
        >>> tag("React", removable=True)  # Client-side removal
        >>> tag("Tag", removable=True, on_remove="/api/tags/1")  # Server-side removal
    """
    css_class = merge_classes("tag", cls)

    elements = [text]

    # Close button - prefers HTMX server-side removal when URL is provided
    if removable:
        close_attrs: dict[str, str] = {"class": "tag-close"}

        if on_remove:
            # HTMX server-side removal (preferred - no JS needed)
            close_attrs["hx-delete"] = on_remove
            close_attrs["hx-swap"] = "outerHTML"
            close_attrs["hx-target"] = "closest .tag"
        else:
            # JS Exception: Client-side removal when no server endpoint provided.
            # No pure CSS alternative exists for removing DOM elements.
            close_attrs["hx-on:click"] = "this.closest('.tag').remove()"

        elements.append(Span("×", **close_attrs))

    return Span(*elements, cls=css_class, **kwargs)
