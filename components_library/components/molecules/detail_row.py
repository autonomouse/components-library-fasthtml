"""Detail row molecule - Label-value pair display."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ..atoms import hstack, text


def detail_row(
    label: str,
    value: str,
    label_width: str | None = None,
    vertical: bool = False,
    **kwargs: Any,
) -> Div:
    """
    Detail row - displays a label-value pair.

    Creates a horizontal or vertical layout showing a label and its
    corresponding value. Commonly used for displaying structured information
    like test details, user profiles, settings, etc.

    Args:
        label: The label text (e.g., "Test ID", "Email", "Status")
        value: The value text to display
        label_width: Fixed width for label (e.g., "200px"). If None, labels flex naturally
        vertical: If True, stack label above value instead of side-by-side
        **kwargs: Additional HTML attributes

    Returns:
        Detail row component

    Example:
        >>> detail_row("Test ID", "12345")
        >>> detail_row("Email", "user@example.com", label_width="150px")
        >>> detail_row("Description", "Long text...", vertical=True)
    """
    label_style = f"flex-shrink: 0; width: {label_width};" if label_width else None

    label_element = text(
        label,
        variant="label",
        weight="medium",
        cls="detail-label",
        style=label_style,
    )

    value_element = text(
        value,
        variant="body",
        cls="detail-value",
        style="flex: 1; word-wrap: break-word; overflow-wrap: break-word;",
    )

    if vertical:
        from ..atoms import vstack

        return vstack(
            label_element,
            value_element,
            gap=1,
            cls="detail-row detail-row-vertical",
            **kwargs,
        )

    return hstack(
        label_element,
        value_element,
        align="start",
        gap=4,
        cls="detail-row",
        **kwargs,
    )
