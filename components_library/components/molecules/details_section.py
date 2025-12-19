"""Details section molecule - Display multiple detail rows with separators."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ..atoms import separator, vstack
from .detail_row import detail_row


def details_section(
    details: list[tuple[str, str]],
    show_separators: bool = True,
    label_width: str | None = None,
    vertical_layout: bool = False,
    **kwargs: Any,
) -> Div:
    """
    Details section - displays multiple label-value pairs with separators.

    Creates a formatted section displaying multiple pieces of information
    as label-value pairs, with optional separators between each row.
    Commonly used for displaying structured data like test details,
    user profiles, order information, etc.

    Args:
        details: List of (label, value) tuples to display
        show_separators: Whether to show separators between rows (default: True)
        label_width: Fixed width for all labels (e.g., "200px")
        vertical_layout: If True, stack labels above values
        **kwargs: Additional HTML attributes

    Returns:
        Details section component

    Example:
        >>> details_section([
        ...     ("Item ID", "12345"),
        ...     ("Name", "Example Item"),
        ...     ("Location", "Warehouse A"),
        ... ])
        >>> details_section(
        ...     [("Name", "John"), ("Email", "john@example.com")],
        ...     label_width="150px",
        ...     show_separators=False
        ... )
    """
    if not details:
        return vstack(gap=3, **kwargs)

    # Build detail rows
    rows = []
    for i, (label, value) in enumerate(details):
        rows.append(
            detail_row(
                label=label,
                value=value,
                label_width=label_width,
                vertical=vertical_layout,
            )
        )

        # Add separator between rows (but not after the last row)
        if show_separators and i < len(details) - 1:
            rows.append(separator())

    return vstack(
        *rows,
        gap=3,
        cls="details-section",
        **kwargs,
    )
