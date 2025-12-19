"""Navigation organism with responsive design and hamburger menu for mobile using HTMX."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Nav
from fasthtml.xtend import Style

from ..atoms import avatar, button_link, flex, hstack, logo


def navigation(
    user: dict[str, Any] | None = None,
    show_cta: bool = False,
    nav_items: list[Any] | None = None,
    brand_name: str = "Company",
) -> Nav:
    """
    Navigation organism with responsive design and hamburger menu for mobile using HTMX.

    Features:
    - Full navigation on desktop/tablet
    - Hamburger menu on mobile with HTMX-powered modal
    - No JavaScript required - uses HTMX patterns
    - Maintains all existing functionality
    - Accessible design with proper ARIA labels

    Args:
        user: Authenticated user data (from get_current_user)
        show_cta: Whether to show "Launch App" CTA button (for landing page)
        nav_items: Optional list of navigation link components. If None, no nav links shown.
        brand_name: The brand/company name to display in the logo. Defaults to "Company".

    Returns:
        Navigation organism component

    Example:
        >>> navigation(user={"email": "user@example.com"})
        >>> navigation()  # Not authenticated
        >>> navigation(show_cta=True)  # Landing page with CTA
        >>> navigation(user=user, nav_items=[button("Custom", hx_get="/custom")])
    """
    # Navigation links - use provided items or empty list
    nav_links = nav_items if nav_items and user else None

    # Right side content: CTA button or user avatar
    if show_cta and not user:
        right_content = button_link(
            "Launch App",
            href="/app",
            variant="solid",
            color_palette="brand",
            size="md",
        )
    elif user:
        # Use avatar instead of full user nav for cleaner header
        right_content = avatar(
            email=user.get("email"),
            name=user.get("name"),
            size=40,
            href="/profile",
        )
    else:
        right_content = None

    # Mobile navigation styles using CSS-only approach
    mobile_nav_styles = Style("""
        /* Mobile navigation styles - CSS only approach */
        .mobile-nav-toggle {
            display: none;
            background: none;
            border: none;
            cursor: pointer;
            padding: 0.5rem;
            border-radius: 0.375rem;
            transition: background-color 0.2s ease;
        }

        .mobile-nav-toggle:hover {
            background-color: var(--color-background-subtle);
        }

        /* Mobile menu container - hidden by default */
        .mobile-nav-container {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: white;
            z-index: 1000;
            padding: 1rem;
            overflow-y: auto;
        }

        /* Show mobile menu when target is present */
        .mobile-nav-container:target {
            display: flex;
            flex-direction: column;
        }

        .mobile-nav-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--color-border-default);
            margin-bottom: 2rem;
        }

        .mobile-nav-links {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        .mobile-nav-links .nav-link {
            width: 100%;
            justify-content: flex-start;
            padding: 1rem;
            font-size: 1.125rem;
            border-radius: 0.5rem;
        }

        .mobile-nav-close {
            background: none;
            border: none;
            cursor: pointer;
            padding: 0.5rem;
            border-radius: 0.375rem;
            color: var(--color-text-default);
            text-decoration: none;
        }

        .mobile-nav-close:hover {
            background-color: var(--color-background-subtle);
        }

        /* Desktop navigation - hide hamburger, show nav links */
        @media (min-width: 769px) {
            .mobile-nav-toggle {
                display: none !important;
            }

            .desktop-nav-links {
                display: flex !important;
            }
        }

        /* Mobile navigation - show hamburger, hide nav links */
        @media (max-width: 768px) {
            .mobile-nav-toggle {
                display: flex !important;
            }

            .desktop-nav-links {
                display: none !important;
            }
        }
    """)

    return Nav(
        hstack(
            # Brand/Logo section
            flex(
                logo(
                    text=brand_name,
                    size="lg",
                    href="/" if not user else "/app",
                ),
                cls="nav-brand",
            ),
            # Desktop navigation links (hidden on mobile)
            flex(
                *nav_links if nav_links else [],
                gap="1",
                cls="nav-links desktop-nav-links",
            ),
            # Mobile hamburger menu toggle - uses CSS :target selector
            button_link(
                "☰",  # Hamburger menu emoji (3 horizontal lines)
                href="#mobile-nav",  # Link to the modal target
                cls="mobile-nav-toggle",
                aria_label="Open navigation menu",
                style="font-size: 1.5rem; font-weight: bold;",
            )
            if nav_links
            else None,
            # Right side: CTA or user controls
            right_content,
            justify="between",
            align="center",
            gap=4,
        ),
        # Mobile navigation modal - uses CSS :target selector
        Div(
            # Mobile nav header
            Div(
                logo(
                    text=brand_name,
                    size="lg",
                    href="/" if not user else "/app",
                ),
                button_link(
                    "✕",  # Close button
                    href="#",  # Close the modal
                    cls="mobile-nav-close",
                    aria_label="Close navigation menu",
                ),
                cls="mobile-nav-header",
            ),
            # Mobile nav links
            Div(
                *nav_links if nav_links else [],
                cls="mobile-nav-links",
            ),
            cls="mobile-nav-container",
            id="mobile-nav",
        ),
        mobile_nav_styles,
        cls="navigation",
        style="padding: 1rem 2rem; border-bottom: 1px solid var(--color-border-default); background: var(--color-background);",
    )
