"""Heading component - h1-h6 with consistent sizing."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import H1, H2, H3, H4, H5, H6

from ...design_system.tokens import Typography
from ...utils import generate_style_string, merge_classes

typography = Typography()


def heading(
    text: str,
    level: Literal[1, 2, 3, 4, 5, 6] = 1,
    size: Literal["xs", "sm", "base", "lg", "xl", "xl2", "xl3", "xl4", "xl5", "xl6"] | None = None,
    weight: Literal[
        "thin", "extralight", "light", "normal", "medium", "semibold", "bold", "extrabold", "black"
    ]
    | None = None,
    color: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> H1 | H2 | H3 | H4 | H5 | H6:
    """
    Heading component for semantic heading levels.

    Args:
        text: Heading text content
        level: Semantic heading level (1-6)
        size: Override default size for the level
        weight: Font weight override
        color: Text color
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Heading element (H1-H6)

    Example:
        >>> heading("Main Title", level=1)
        >>> heading("Section", level=2, size="xl3")
        >>> heading("Subsection", level=3, weight="semibold")
    """
    # Default sizes per level
    default_sizes = {
        1: typography.xl4,  # 36px
        2: typography.xl3,  # 30px
        3: typography.xl2,  # 24px
        4: typography.xl,  # 20px
        5: typography.lg,  # 18px
        6: typography.base,  # 16px
    }

    # Use custom size or default for level
    if size:  # noqa: SIM108
        font_size = getattr(typography, size)
    else:
        font_size = default_sizes[level]

    # Weight mapping
    weight_map = {
        "thin": typography.font_thin,
        "extralight": typography.font_extralight,
        "light": typography.font_light,
        "normal": typography.font_normal,
        "medium": typography.font_medium,
        "semibold": typography.font_semibold,
        "bold": typography.font_bold,
        "extrabold": typography.font_extrabold,
        "black": typography.font_black,
    }

    # Default weights per level
    default_weight = typography.font_bold if level <= 2 else typography.font_semibold
    font_weight = weight_map[weight] if weight else default_weight

    style = generate_style_string(
        font_size=font_size.size,
        line_height=font_size.line_height,
        font_weight=font_weight,
        color=color,
        margin="0",
    )

    css_class = merge_classes(f"heading heading-{level}", cls)

    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    # Map level to appropriate HTML element
    heading_elements = {1: H1, 2: H2, 3: H3, 4: H4, 5: H5, 6: H6}
    heading_element = heading_elements[level]

    return heading_element(text, cls=css_class, style=style if style else None, **kwargs)
