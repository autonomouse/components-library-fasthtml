from collections.abc import Sequence
from typing import Any

from ..atoms.flex import flex


def carousel(
    items: Sequence[Any], gap: str = "1rem", cls: str = "", style: str = "", **kwargs: Any
) -> Any:
    """
    A generic horizontal scrolling carousel component.

    Args:
        items: List of components to display in the carousel
        gap: Space between items
        cls: Additional CSS classes
        style: Additional inline styles
    """
    return flex(
        *items,
        gap=gap,
        wrap="nowrap",
        cls=f"w-full overflow-x-auto pb-4 snap-x {cls}",
        style=f"scrollbar-width: thin; -webkit-overflow-scrolling: touch; {style}",
        **kwargs,
    )
