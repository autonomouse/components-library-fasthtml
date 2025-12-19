"""Footer molecule - Application footer with version and copyright."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ..atoms import text


def footer(
    version: str = "1.2.0",
    copyright_text: str = "© 2024 Copyright Test SOP",
    align: str = "right",
    **kwargs: Any,
) -> Div:
    """
    Application footer with version and copyright information.

    Args:
        version: Version string to display
        copyright_text: Copyright text to display
        align: Text alignment (left, center, right)
        **kwargs: Additional HTML attributes

    Returns:
        Footer component

    Example:
        >>> footer()
        >>> footer(version="2.0.0", copyright_text="© 2025 My Company")
        >>> footer(align="center")
    """
    footer_text = f"v{version} {copyright_text}"

    return Div(
        text(footer_text, variant="caption"),
        cls="footer",
        style=f"text-align: {align}; margin-top: 3rem; padding: 1rem; color: #6b7280; font-size: 0.75rem;",
        **kwargs,
    )
