"""Generate inline CSS from design tokens."""

from __future__ import annotations

from typing import Any, Literal

from ..design_system.tokens import Colors, Spacing, Typography

colors = Colors()
spacing = Spacing()
typography = Typography()


def color_value(color_path: str) -> str:
    """
    Get color value from design tokens.

    Args:
        color_path: Dot-notation path to color (e.g., "primary.s600")

    Returns:
        Color hex value

    Example:
        >>> color_value("primary.s600")
        "#2563eb"
    """
    parts = color_path.split(".")
    value: Any = colors

    for part in parts:
        value = getattr(value, part)

    return str(value)


def spacing_value(spacing_key: str) -> str:
    """
    Get spacing value from design tokens.

    Args:
        spacing_key: Spacing key (e.g., "_4", "_8")

    Returns:
        Spacing value in rem

    Example:
        >>> spacing_value("_4")
        "1rem"
    """
    return str(getattr(spacing, spacing_key))


def font_size_value(size_key: str) -> tuple[str, str]:
    """
    Get font size and line height from design tokens.

    Args:
        size_key: Font size key (e.g., "base", "lg", "xl")

    Returns:
        Tuple of (font-size, line-height)

    Example:
        >>> font_size_value("base")
        ("1rem", "1.5rem")
    """
    font_size = getattr(typography, size_key)
    return (font_size.size, font_size.line_height)


def responsive_gap(gap: int) -> str:
    """
    Convert numeric gap to responsive spacing value.

    Maps 1-10 to appropriate spacing scale for responsive design.

    Args:
        gap: Numeric gap value (1-10)

    Returns:
        Spacing value

    Example:
        >>> responsive_gap(4)
        "1rem"
    """
    gap_map = {
        1: spacing._2,
        2: spacing._3,
        3: spacing._4,
        4: spacing._5,
        5: spacing._6,
        6: spacing._8,
        7: spacing._10,
        8: spacing._12,
        9: spacing._14,
        10: spacing._16,
    }
    return gap_map.get(gap, spacing._4)


def generate_box_shadow(level: Literal["sm", "md", "lg", "xl"] = "md") -> str:
    """
    Generate box shadow CSS value.

    Args:
        level: Shadow depth level

    Returns:
        Box shadow CSS value
    """
    shadows = {
        "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
        "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
    }
    return shadows[level]


def generate_border_radius(size: Literal["sm", "md", "lg", "full"] = "md") -> str:
    """
    Generate border radius value.

    Args:
        size: Radius size

    Returns:
        Border radius CSS value
    """
    radii = {
        "sm": spacing._1,
        "md": spacing._2,
        "lg": spacing._3,
        "full": "9999px",
    }
    return radii[size]


def focus_ring_styles(color: str | None = None) -> str:
    """
    Generate focus ring styles for accessibility.

    Args:
        color: Focus ring color (defaults to primary)

    Returns:
        CSS style string for focus ring
    """
    focus_color = color or colors.primary.s500
    return f"outline: 2px solid {focus_color}; outline-offset: 2px;"
