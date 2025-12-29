"""Specific Icon Atoms.

These atoms wrap the generic `icon` component to provide specific, typed access to common icons.
"""

from typing import Any

from fasthtml.common import Span

from .icon import icon


def plus_icon(**kwargs: Any) -> Span:
    """Plus / Add icon."""
    return icon("plus", **kwargs)


def edit_icon(**kwargs: Any) -> Span:
    """Edit / Pencil icon."""
    return icon("edit", **kwargs)


def trash_icon(**kwargs: Any) -> Span:
    """Trash / Delete icon."""
    return icon("trash-2", **kwargs)


def check_icon(**kwargs: Any) -> Span:
    """Check / Confirm icon."""
    return icon("check", **kwargs)


def close_icon(**kwargs: Any) -> Span:
    """Close / X icon."""
    return icon("x", **kwargs)


def search_icon(**kwargs: Any) -> Span:
    """Search icon."""
    return icon("search", **kwargs)


def filter_icon(**kwargs: Any) -> Span:
    """Filter icon."""
    return icon("filter", **kwargs)


def settings_icon(**kwargs: Any) -> Span:
    """Settings icon."""
    return icon("settings", **kwargs)


def more_vertical_icon(**kwargs: Any) -> Span:
    """More Vertical / Menu icon."""
    return icon("more-vertical", **kwargs)


def file_text_icon(**kwargs: Any) -> Span:
    """File Text / Document icon."""
    return icon("file-text", **kwargs)


def map_pin_icon(**kwargs: Any) -> Span:
    """Map Pin / Location icon."""
    return icon("map-pin", **kwargs)


def book_open_icon(**kwargs: Any) -> Span:
    """Book Open / Story icon."""
    return icon("book-open", **kwargs)


def user_icon(**kwargs: Any) -> Span:
    """User / Character icon."""
    return icon("user", **kwargs)


def layout_dashboard_icon(**kwargs: Any) -> Span:
    """Layout Dashboard icon."""
    return icon("layout-dashboard", **kwargs)


def image_icon(**kwargs: Any) -> Span:
    """Image icon."""
    return icon("image", **kwargs)


def clapperboard_icon(**kwargs: Any) -> Span:
    """Clapperboard / Scene icon."""
    return icon("clapperboard", **kwargs)


def star_icon(filled: bool = False, **kwargs: Any) -> Span:
    """Star / Favorite icon."""
    # Note: Using color/fill style for filled state if SVG supports it, or different icon name?
    # ICON_STAR is outline path. Lucide uses 'fill' attr for filled.
    # Our svg_icon supports 'fill' param.
    if filled:
        # Default yellow/gold for star if filled, or use passed color.
        # But 'fill' in svg_icon defaults to brand blue if not specified.
        # Check kwargs for 'fill', else default to something visible?
        # Ideally, we pass fill="currentColor" or specific color.
        if "fill" not in kwargs:
            kwargs["fill"] = "currentColor"
    else:
        kwargs["fill"] = "none"

    return icon("star", **kwargs)


def eye_icon(off: bool = False, **kwargs: Any) -> Span:
    """Eye / Visibility icon."""
    return icon("eye-off" if off else "eye", **kwargs)


def checkbox_icon(checked: bool = False, **kwargs: Any) -> Span:
    """Checkbox icon state."""
    return icon("check-square" if checked else "square", **kwargs)
