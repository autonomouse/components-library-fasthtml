"""Flex component - flexbox layout container."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...utils import generate_style_string, merge_classes


def flex(
    *children: Any,
    direction: Literal["row", "column", "row-reverse", "column-reverse"] = "row",
    align: Literal["start", "center", "end", "stretch", "baseline"] = "stretch",
    justify: Literal["start", "center", "end", "between", "around", "evenly"] = "start",
    wrap: Literal["nowrap", "wrap", "wrap-reverse"] = "nowrap",
    gap: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Flexbox layout container.

    Args:
        *children: Child elements
        direction: Flex direction
        align: Align items
        justify: Justify content
        wrap: Flex wrap
        gap: Gap between items
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div with flexbox layout

    Example:
        >>> flex(
        ...     box("Item 1"),
        ...     box("Item 2"),
        ...     direction="row",
        ...     gap="1rem"
        ... )
    """
    # Map align and justify to CSS values
    align_map = {
        "start": "flex-start",
        "center": "center",
        "end": "flex-end",
        "stretch": "stretch",
        "baseline": "baseline",
    }

    justify_map = {
        "start": "flex-start",
        "center": "center",
        "end": "flex-end",
        "between": "space-between",
        "around": "space-around",
        "evenly": "space-evenly",
    }

    style = generate_style_string(
        display="flex",
        flex_direction=direction,
        align_items=align_map[align],
        justify_content=justify_map[justify],
        flex_wrap=wrap,
        gap=gap,
    )

    # Build class list
    classes = ["flex"]
    if direction in ["row", "column"]:
        classes.append(f"flex-{direction}")
    if wrap == "wrap":
        classes.append("flex-wrap")

    css_class = merge_classes(*classes, cls)

    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    return Div(*children, cls=css_class, style=style if style else None, **kwargs)
