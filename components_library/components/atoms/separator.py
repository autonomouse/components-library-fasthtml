"""Separator component - visual divider."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Hr

from ...utils import merge_classes


def separator(
    orientation: Literal["horizontal", "vertical"] = "horizontal",
    cls: str | None = None,
    **kwargs: Any,
) -> Hr:
    """
    Visual divider to separate content.

    Args:
        orientation: Separator orientation
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Hr element styled as separator

    Example:
        >>> separator()
        >>> separator(orientation="vertical")
    """
    css_class = merge_classes("separator", f"separator-{orientation}", cls)

    return Hr(cls=css_class, **kwargs)
