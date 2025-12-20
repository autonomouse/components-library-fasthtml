"""Profile card component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Hr

from ...atoms import button_link, vstack
from ...molecules import entity_card


def profile_card(
    user: dict[str, Any],
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Glassmorphism profile card for user details.

    Args:
        user: User data dictionary (name, email)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Profile card component
    """
    name = user.get("name") or "User"
    email = user.get("email") or "No email provided"

    # Profile card specific styles to override or augment generic entity card
    # We maintain the specific width and padding from the previous design
    profile_style = """
        max-width: 500px;
        margin: 0 auto;
        padding: 3rem 2rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
    """

    # Extra content: Separator and Sign Out Button
    extra_content = vstack(
        Hr(
            cls="profile-separator",
            style="width: 100%; height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); border: none; margin: 2rem 0;",
        ),
        button_link(
            "Sign Out",
            href="/logout",
            variant="outline",
            color_palette="red",
            size="lg",
            cls="w-full",
            style="border-color: rgba(255, 23, 68, 0.5); color: #ff1744; width: 100%;",
        ),
        align="center",
        width="100%",
        style="width: 100%;",
    )

    return entity_card(
        name,
        extra_content,
        subtitle=email,  # Show email as subtitle
        email=email,  # Pass email for Gravatar generation
        avatar_size=120,  # Larger avatar for profile
        centered=True,  # Centered layout
        style=profile_style,
        cls=f"profile-card {cls or ''}",
        **kwargs,
    )
