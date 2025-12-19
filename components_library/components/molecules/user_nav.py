"""User navigation component - Shows user info and logout."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Form, Span

from ..atoms import button, flex, text


def user_nav(user: dict[str, Any] | None = None) -> Div:
    """
    User navigation component.

    Shows user email and logout button when authenticated.
    Shows login link when not authenticated.

    Args:
        user: Authenticated user data (from get_current_user)

    Returns:
        User navigation component

    Example:
        >>> user_nav(user={"email": "user@example.com"})
        >>> user_nav()  # Not authenticated
    """
    if not user:
        # Not authenticated - show login link
        return Div(
            button(
                "Sign In",
                variant="outline",
                size="sm",
                hx_get="/login",
                hx_push_url="true",
            ),
            cls="user-nav",
        )

    # Authenticated - show user email and logout button
    return Div(
        flex(
            Span(
                text(user.get("email", "User"), cls="text-sm font-medium"),
                cls="user-email",
            ),
            Form(
                button(
                    "Sign Out",
                    type="submit",
                    variant="outline",
                    size="sm",
                    color_palette="gray",
                ),
                method="POST",
                action="/logout",
            ),
            gap="0.75rem",
            align="center",
        ),
        cls="user-nav",
    )
