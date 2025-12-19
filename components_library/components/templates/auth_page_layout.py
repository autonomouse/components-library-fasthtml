"""Auth page layout template - Centered layout for authentication pages."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div


def auth_page_layout(*content: Any, max_width: str = "450px", **kwargs: Any) -> Div:
    """
    Authentication page layout with centered content.

    Provides a consistent centered layout for login, signup, and other
    authentication-related pages.

    Args:
        *content: Content to display in the auth layout
        max_width: Maximum width of the auth container (default: 450px)
        **kwargs: Additional HTML attributes

    Returns:
        Div element with auth layout styling

    Example:
        >>> auth_page_layout(
        ...     card(auth_form("login")),
        ...     max_width="500px"
        ... )
    """
    return Div(
        *content,
        style=f"max-width: {max_width}; margin: 0 auto; padding-top: 5rem;",
        **kwargs,
    )
