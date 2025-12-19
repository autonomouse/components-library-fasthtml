"""SearchBar molecule - Search input with button."""

from __future__ import annotations

from typing import Any, Literal

from ..atoms import box, hstack, icon_button, input


def search_bar(
    value: str = "",
    placeholder: str = "Search...",
    disabled: bool = False,
    size: Literal["sm", "md", "lg"] = "md",
    search_button_aria_label: str = "Search",
    width: str = "100%",
    is_loading: bool = False,
    **kwargs: Any,
) -> Any:
    """
    Search bar molecule combining Input and IconButton atoms.

    Creates a simple search interface with an input field and search button.
    For Enter key submission, wrap in a form element or use HTMX attributes
    like hx-trigger="keyup[key=='Enter']" on the input.

    Args:
        value: Current search value
        placeholder: Placeholder text for the input
        disabled: Whether the search bar is disabled
        size: Size of the search bar (sm, md, lg)
        search_button_aria_label: ARIA label for the search button
        width: Width of the search bar
        is_loading: Whether the search bar is in a loading state
        **kwargs: Additional HTML attributes

    Returns:
        HStack element with input and search button

    Example:
        >>> search_bar(
        ...     placeholder="Search articles...",
        ... )
    """
    input_el = input(
        name="search",
        value=value,
        placeholder=placeholder,
        aria_label="Search",
        size=size,
        disabled=disabled,
    )

    # Search button
    search_btn = icon_button(
        "🔍",
        aria_label=search_button_aria_label,
        color_palette="brand",
        size=size,
        disabled=disabled or is_loading,
        loading=is_loading,
    )

    return hstack(
        box(input_el, style="flex: 1;"),
        search_btn,
        gap=2,
        style=f"align-items: stretch; width: {width};",
        **kwargs,
    )
