"""Enhanced search bar molecule - Search input with decorative icons and HTMX support."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ..atoms import hstack, icon, icon_button


def enhanced_search_bar(
    value: str = "",
    placeholder: str = "Search...",
    search_url: str = "/search",
    target_id: str = "#search-results",
    trigger_delay: int = 300,
    show_right_icon: bool = False,
    right_icon: Literal["search", "filter"] = "search",
    right_icon_action: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Enhanced search bar with real-time search and optional icons.

    Provides a visually enhanced search experience with:
    - Left magnifying glass icon (decorative)
    - Styled search input with HTMX live updates (real-time search)
    - Optional right icon button (search or filter with optional action)

    Args:
        value: Current search value
        placeholder: Placeholder text for the input
        search_url: HTMX endpoint for search requests
        target_id: HTMX target element ID
        trigger_delay: Delay in ms before triggering search (default: 300)
        show_right_icon: Whether to show the right icon button (default: False)
        right_icon: Type of right icon - "search" (🔍) or "filter" (🔧)
        right_icon_action: Optional HTMX action for right icon button
        **kwargs: Additional HTML attributes

    Returns:
        Enhanced search bar component

    Example:
        >>> enhanced_search_bar(
        ...     placeholder="Search laboratory tests...",
        ...     trigger_delay=500
        ... )
        >>> enhanced_search_bar(
        ...     value="glucose",
        ...     show_right_icon=True,
        ...     right_icon="filter"
        ... )
    """
    # Right icon configuration (only if enabled)
    right_icon_emoji = "🔍" if right_icon == "search" else "🔧"
    right_icon_label = "Search" if right_icon == "search" else "Filter options"

    # Build right icon button (only if show_right_icon is True)
    right_btn_attrs: dict[str, Any] = {}
    if show_right_icon:
        right_btn_attrs = {
            "aria_label": right_icon_label,
            "variant": "ghost",
            "size": "md",
            "style": "position: absolute; right: 12px; top: 50%; transform: translateY(-50%); z-index: 10;",
        }

        if right_icon_action:
            right_btn_attrs.update(
                {
                    "hx_get": right_icon_action,
                    "hx_target": target_id,
                    "hx_swap": "innerHTML",
                }
            )

        if right_icon == "filter":
            right_btn_attrs["title"] = "Filter options"

    from ..atoms import input as input_atom

    # Create custom styled input with HTMX (no JavaScript)
    custom_input = input_atom(
        id="main-search-input",
        name="query",
        value=value,
        placeholder=placeholder,
        aria_label="Search for laboratory tests",
        size="md",
        hx_get=search_url,
        hx_target=target_id,
        hx_swap="innerHTML",
        hx_trigger=f"keyup changed delay:{trigger_delay}ms",
        hx_push_url="true",
        style=(
            "flex: 1; width: 100%; "
            "padding-left: 2.5rem; padding-right: 2.5rem; "
            "border-radius: 8px; border: 2px solid #e5e7eb; "
            "font-size: 1rem; transition: border-color 0.2s, box-shadow 0.2s;"
        ),
    )

    # Build components list
    components = [
        # Left magnifying glass icon (decorative)
        icon(
            "🔍",
            size="md",
            style="position: absolute; left: 12px; top: 50%; transform: translateY(-50%); z-index: 10; color: #6b7280;",
        ),
        # Search input with custom styling
        custom_input,
    ]

    # Add right icon button only if enabled
    if show_right_icon:
        components.append(icon_button(right_icon_emoji, **right_btn_attrs))

    return hstack(
        *components,
        gap=2,
        style="position: relative; width: 100%; margin-bottom: 1rem; align-items: center;",
        **kwargs,
    )
