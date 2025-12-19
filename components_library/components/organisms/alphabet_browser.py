"""Alphabet browser organism component for A-Z navigation."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ..atoms import button, hstack, text, vstack


def alphabet_browser(
    selected_letter: str | None = None,
    target_id: str = "#search-results",
    base_url: str = "/browse",
    component_id: str = "alphabet-browser",
    **kwargs: Any,
) -> Div:
    """
    Create an alphabet browser organism for A-Z navigation.

    Features:
    - Responsive grid layout with A-Z buttons
    - Visual indication of selected letter
    - HTMX integration for dynamic updates with OOB swaps
    - Server-side state management (no JavaScript)
    - Accessible design with proper labels

    Args:
        selected_letter: Currently selected letter (if any)
        target_id: HTMX target element ID for search results
        base_url: Base URL for letter navigation
        component_id: HTML ID for this component (for OOB swaps)
        **kwargs: Additional attributes for the container

    Returns:
        Alphabet browser organism component

    Example:
        >>> alphabet_browser(selected_letter="A", target_id="#results")
        >>> alphabet_browser(base_url="/search")
    """
    # Generate A-Z buttons
    az_buttons = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        is_selected = selected_letter == letter
        az_buttons.append(
            button(
                letter,
                variant="solid" if is_selected else "outline",
                color_palette="brand" if is_selected else "gray",
                size="sm",
                cls="alphabet-btn",
                hx_get=f"{base_url}?letter={letter}",
                hx_target=target_id,
                hx_swap="innerHTML",
                hx_push_url="true",
                style="min-width: 28px; min-height: 28px; font-weight: 500; font-size: 0.875rem; padding: 0.25rem 0.5rem;",
                aria_label=f"Browse tests starting with {letter}",
            )
        )

    return Div(
        vstack(
            text("Browse by Letter", variant="label", cls="alphabet-label"),
            hstack(
                *az_buttons,
                gap=1,
                cls="alphabet-browser",
                style="flex-wrap: wrap; justify-content: center; align-items: center;",
            ),
            gap=2,
        ),
        id=component_id,
        cls="alphabet-browser-organism",
        style="margin-bottom: 1.5rem;",
        **kwargs,
    )
