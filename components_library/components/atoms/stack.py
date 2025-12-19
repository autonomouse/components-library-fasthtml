"""Stack components - vertical and horizontal stacks."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...utils import generate_style_string, merge_classes, responsive_gap


def vstack(
    *children: Any,
    gap: int | str | None = None,
    align: Literal["start", "center", "end", "stretch"] = "stretch",
    width: str = "100%",
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Vertical stack - arranges children vertically with consistent gap.

    Args:
        *children: Child elements
        gap: Gap between items (numeric 1-10 or CSS value)
        align: Align items horizontally
        width: Stack width
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div with vertical stack layout

    Example:
        >>> vstack(
        ...     box("Item 1"),
        ...     box("Item 2"),
        ...     gap=4,
        ...     align="center"
        ... )
    """
    # Convert numeric gap to responsive spacing
    gap_value = responsive_gap(gap) if isinstance(gap, int) else gap

    align_map = {
        "start": "flex-start",
        "center": "center",
        "end": "flex-end",
        "stretch": "stretch",
    }

    style = generate_style_string(
        display="flex",
        flex_direction="column",
        gap=gap_value,
        align_items=align_map[align],
        width=width,
    )

    css_class = merge_classes("vstack", cls)

    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    return Div(*children, cls=css_class, style=style if style else None, **kwargs)


def hstack(
    *children: Any,
    gap: int | str | None = None,
    align: Literal["start", "center", "end", "stretch", "baseline"] = "center",
    justify: Literal["start", "center", "end", "between", "around"] = "start",
    wrap: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Horizontal stack - arranges children horizontally with consistent gap.

    Args:
        *children: Child elements
        gap: Gap between items (numeric 1-10 or CSS value)
        align: Align items vertically
        justify: Justify content horizontally
        wrap: Enable flex wrap
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div with horizontal stack layout

    Example:
        >>> hstack(
        ...     box("Item 1"),
        ...     box("Item 2"),
        ...     gap=2,
        ...     align="center"
        ... )
    """
    # Convert numeric gap to responsive spacing
    gap_value = responsive_gap(gap) if isinstance(gap, int) else gap

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
    }

    style = generate_style_string(
        display="flex",
        flex_direction="row",
        gap=gap_value,
        align_items=align_map[align],
        justify_content=justify_map[justify],
        flex_wrap="wrap" if wrap else None,
    )

    css_class = merge_classes("hstack", cls)

    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    return Div(*children, cls=css_class, style=style if style else None, **kwargs)
