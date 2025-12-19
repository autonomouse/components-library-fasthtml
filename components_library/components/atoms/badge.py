"""Badge component - Small status indicator."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Span

from ...utils import merge_classes


def badge(
    text: str,
    variant: Literal["brand", "gray", "success", "error"] = "gray",
    size: Literal["sm", "md"] = "md",
    cls: str | None = None,
    **kwargs: Any,
) -> Span:
    """
    Badge component for status indicators and labels.

    Args:
        text: Badge text content
        variant: Color variant (brand, gray, success, error)
        size: Badge size (sm, md)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Span element with badge styling

    Example:
        >>> badge("New")
        >>> badge("Active", variant="success")
        >>> badge("3", variant="brand", size="sm")
    """
    css_class = merge_classes("badge", f"badge-{variant}", f"badge-{size}", cls)

    return Span(text, cls=css_class, **kwargs)
