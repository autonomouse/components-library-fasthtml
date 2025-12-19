"""Grid component - CSS grid layout container."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...utils import generate_style_string, merge_classes


def grid(
    *children: Any,
    columns: Literal[1, 2, 3, 4, 5, 6, 12] | None = None,
    gap: str | None = None,
    rows: str | None = None,
    areas: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    CSS Grid layout container.

    Args:
        *children: Child elements
        columns: Number of columns (uses predefined grid template)
        gap: Gap between grid items
        rows: Custom row template (e.g., "repeat(3, 1fr)")
        areas: Grid template areas
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div with grid layout

    Example:
        >>> grid(
        ...     box("Item 1"),
        ...     box("Item 2"),
        ...     box("Item 3"),
        ...     columns=3,
        ...     gap="1rem"
        ... )
    """
    style_props = {
        "display": "grid",
        "gap": gap,
    }

    if rows:
        style_props["grid_template_rows"] = rows
    if areas:
        style_props["grid_template_areas"] = areas

    style = generate_style_string(**style_props)

    # Build class list
    classes = ["grid"]
    if columns:
        classes.append(f"grid-cols-{columns}")

    css_class = merge_classes(*classes, cls)

    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    return Div(*children, cls=css_class, style=style if style else None, **kwargs)
