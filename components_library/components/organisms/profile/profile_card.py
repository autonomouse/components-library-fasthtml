"""Profile card component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Hr
from fasthtml.xtend import Style

from ....utils import merge_classes
from ...atoms import avatar, button_link, heading, text, vstack


def profile_card(
    user: dict[str, Any],
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
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

    # Component-scoped styles
    styles = Style("""
        .profile-card {
            background: var(--theme-card-bg);
            border: 1px solid var(--theme-card-border);
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
            color: var(--theme-text-primary);
            max-width: 500px;
            width: 100%;
            padding: 3rem 2rem;
            margin: 0 auto;
            border-radius: 1rem;
        }

        .profile-avatar-wrapper {
            position: relative;
            display: inline-block;
            margin-bottom: 1.5rem;
            border-radius: 50%;
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.3);
        }

        .profile-avatar-wrapper::after {
            content: "";
            position: absolute;
            inset: -4px;
            border-radius: 50%;
            padding: 4px;
            background: linear-gradient(135deg, var(--theme-accent-primary), transparent 60%);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
        }

        .profile-separator {
            width: 100%;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            border: none;
            margin: 2rem 0;
        }
    """)

    card_content = vstack(
        # Avatar with glowing ring
        Div(
            avatar(
                name=name,
                email=email,
                size=120,
                cls="profile-avatar",
            ),
            cls="profile-avatar-wrapper",
        ),
        # User Info
        vstack(
            heading(
                name,
                level=2,
                cls="text-center",
                style="margin-bottom: 0.5rem; color: var(--theme-text-primary);",
            ),
            text(
                email,
                size="base",
                cls="text-center",
                style="color: var(--theme-text-secondary); opacity: 0.8;",
            ),
            gap=1,
            align="center",
        ),
        # Separator
        Hr(cls="profile-separator"),
        # Actions
        vstack(
            button_link(
                "Sign Out",
                href="/logout",
                variant="outline",
                color_palette="red",
                size="lg",
                cls="w-full",
                style="border-color: rgba(255, 23, 68, 0.5); color: #ff1744;",
            ),
            gap=4,
            width="100%",
        ),
        align="center",
        style="width: 100%;",
    )

    css_class = merge_classes("profile-card", cls)

    return Div(
        styles,
        card_content,
        cls=css_class,
        **kwargs,
    )
