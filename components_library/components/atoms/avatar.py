"""Avatar atom component with Gravatar support."""

from __future__ import annotations

import hashlib
from typing import Any

from fasthtml.common import Div
from fasthtml.xtend import A

from ...utils import merge_classes


def _get_initials(name: str | None = None, email: str | None = None) -> str:
    """Generate initials from name or email."""
    if name:
        name_parts = name.split()
        if len(name_parts) >= 2:
            return (name_parts[0][0] + name_parts[-1][0]).upper()
        elif len(name_parts) == 1:
            return name_parts[0][0].upper()
    if email:
        return email[0].upper()
    return "?"


def avatar(
    email: str | None = None,
    name: str | None = None,
    size: int = 40,
    href: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Create an avatar component with Gravatar support.

    Features:
    - Gravatar integration for profile images
    - Fallback to initials if no Gravatar
    - Configurable size and styling
    - Optional link wrapper

    Args:
        email: User email for Gravatar lookup
        name: User name for initials fallback
        size: Avatar size in pixels (default: 40)
        href: Optional link URL for the avatar
        **kwargs: Additional attributes for the avatar container

    Returns:
        Avatar component

    Example:
        >>> avatar(email="user@example.com", name="John Doe", size=50)
        >>> avatar(name="Jane Smith", href="/profile")
    """
    # Generate Gravatar URL if email provided
    gravatar_url = None
    if email:
        # Create MD5 hash of email for Gravatar (MD5 is required by Gravatar API)
        # Not a security concern - MD5 is Gravatar's specified hash algorithm
        email_hash = hashlib.md5(  # nosec B324
            email.lower().strip().encode(), usedforsecurity=False
        ).hexdigest()
        gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=404"

    # Generate initials from name
    initials = ""
    if name:
        name_parts = name.strip().split()
        if len(name_parts) >= 2:
            initials = name_parts[0][0].upper() + name_parts[-1][0].upper()
        elif len(name_parts) == 1:
            initials = name_parts[0][0].upper()
        else:
            initials = "?"

    # Avatar container styles
    avatar_styles = f"""
        width: {size}px;
        height: {size}px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #f1f5f9;
        color: #64748b;
        font-weight: 500;
        font-size: {size * 0.4}px;
        border: 3px solid #3b82f6;
        transition: all 0.2s ease;
        cursor: pointer;
        overflow: hidden;
    """

    # Avatar content - show initials by default, Gravatar as overlay
    avatar_content = Div(
        initials,
        style=f"""
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: {size * 0.4}px;
            color: #64748b;
            font-weight: 500;
            position: relative;
            z-index: 1;
        """,
    )

    # Add Gravatar as background if available
    if gravatar_url:
        avatar_content = Div(
            avatar_content,
            style=f"""
                width: 100%;
                height: 100%;
                background-image: url('{gravatar_url}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                position: relative;
            """,
        )

    # Create avatar container
    css_class = merge_classes("user-avatar", kwargs.pop("cls", None))

    avatar_container = Div(
        avatar_content,
        style=avatar_styles,
        cls=css_class,
        **kwargs,
    )

    # Wrap in link if href provided
    if href:
        return A(
            avatar_container,
            href=href,
            cls="avatar-link",
            style="text-decoration: none;",
        )

    return avatar_container
