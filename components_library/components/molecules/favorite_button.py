"""Favorite button molecule - Toggle favorite status with HTMX."""

from __future__ import annotations

from typing import Any

from ..atoms import icon_button


def favorite_button(
    item_id: int,
    is_favorite: bool = False,
    add_url: str = "/favorites",
    remove_url: str = "/favorites/remove",
    hx_swap: str = "outerHTML",
    **kwargs: Any,
) -> Any:
    """
    Favorite button molecule for toggling item favorite status.

    Provides a star icon that toggles between filled (⭐) and empty (☆) states.
    Uses HTMX for seamless updates without page refresh.

    Args:
        item_id: ID of the item to favorite/unfavorite
        is_favorite: Current favorite status
        add_url: URL to add to favorites (POST)
        remove_url: URL to remove from favorites (POST)
        hx_swap: HTMX swap strategy for the button itself
        **kwargs: Additional HTML attributes

    Returns:
        Icon button element with favorite functionality

    Example:
        >>> favorite_button(item_id=123, is_favorite=True)
        >>> favorite_button(item_id=456, is_favorite=False, add_url="/api/favorites")
    """
    return icon_button(
        icon="⭐" if is_favorite else "☆",
        aria_label="Remove from favorites" if is_favorite else "Add to favorites",
        variant="ghost",
        size="lg",
        cls="favorite-button touch-target",
        hx_post=remove_url if is_favorite else add_url,
        hx_vals=f'{{"item_id": {item_id}}}',
        hx_swap=hx_swap,
        style="min-width: 44px; min-height: 44px;",
        **kwargs,
    )
