"""OverflowTooltip molecule - Text with automatic overflow tooltip."""

from __future__ import annotations

from typing import Any, Literal

from ..atoms import text


def overflow_tooltip(
    label: str | None = None,
    variant: Literal["body", "caption", "label", "helper", "error"] = "body",
    no_of_lines: int = 1,
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Overflow tooltip molecule that shows a tooltip for potentially truncated text.

    Uses CSS for text truncation with line clamping. The title attribute is always
    set to show the full text on hover, providing a tooltip for truncated content.

    Note: This component uses pure CSS/HTML - no JavaScript required.

    Args:
        label: Text content to display
        variant: Text variant style
        no_of_lines: Number of lines before truncating
        cls: Additional CSS classes
        **kwargs: Additional text properties

    Returns:
        Text element with truncation styling and title tooltip

    Example:
        >>> overflow_tooltip(
        ...     label="This is a very long text that might overflow",
        ...     no_of_lines=1
        ... )
    """
    if not label:
        return text("", variant=variant, cls=cls, **kwargs)

    # CSS for text truncation using line-clamp
    truncate_style = f"""
        display: -webkit-box;
        -webkit-line-clamp: {no_of_lines};
        -webkit-box-orient: vertical;
        overflow: hidden;
        text-overflow: ellipsis;
        word-break: break-word;
    """

    # Text element with truncation - title always set to show full text on hover
    return text(
        label,
        variant=variant,
        cls=cls,
        style=truncate_style,
        title=label,  # Always show full text on hover
        **kwargs,
    )
