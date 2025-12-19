"""Header organism - page header with navigation and user actions."""

from __future__ import annotations

from typing import Any, Literal, TypedDict

from fasthtml.common import A, Div, NotStr
from fasthtml.common import Header as HtmlHeader

from ...design_system.tokens import Colors, Spacing
from ...utils import generate_style_string, merge_classes
from ..atoms import flex, hstack, logo
from ..atoms.menu import menu, menu_divider, menu_item
from ..molecules import breadcrumbs, user_actions
from ..molecules.breadcrumbs import BreadcrumbItem
from ..molecules.user_actions import UserAction

# SVG icons for header utility buttons
# Vertical 3-dots icon
_MORE_OPTIONS_SVG = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="12" cy="19" r="1"/></svg>"""

_NOTIFICATIONS_SVG = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>"""

_USER_PROFILE_SVG = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M20 21a8 8 0 1 0-16 0"/></svg>"""


class _HeaderSizeConfig(TypedDict):
    height: str
    logo_size: Literal["sm", "md", "lg"]
    px: str


colors = Colors()
spacing = Spacing()


def header(
    logo_text: str = "App",
    logo_href: str = "/",
    logo_icon: bool = False,
    breadcrumb_items: list[dict[str, str]] | None = None,
    user_avatar: str | None = None,
    user_name: str = "User",
    user_email: str | None = None,
    menu_items: list[UserAction] | list[dict[str, Any]] | None = None,
    user_menu_items: list[UserAction] | list[dict[str, Any]] | None = None,
    notification_count: int = 0,
    has_new_notifications: bool = False,
    sticky: bool = False,
    size: Literal["sm", "md", "lg"] = "md",
    use_utility_icons: bool = False,
    cls: str | None = None,
    # HTMX endpoints
    hx_logout: str | None = None,
    hx_notifications: str | None = None,
    hx_target: str | None = None,
    # Utility icon menu URLs
    projects_href: str = "/projects",
    whats_new_href: str = "/changelog",
    attributions_href: str = "/attributions",
    account_settings_href: str = "/account-settings",
    logout_href: str | None = None,
    **kwargs: Any,
) -> HtmlHeader:
    """
    Header organism providing navigation, breadcrumbs, and user actions.

    Combines branding, main navigation, breadcrumbs, and user-specific
    actions into a cohesive page header.

    Args:
        logo_text: Text for the logo
        logo_href: URL for logo link
        logo_icon: Use the default icon logo instead of text
        breadcrumb_items: List of breadcrumb items [{label, href}]
        user_avatar: URL to user's avatar image
        user_name: User's display name
        user_email: User's email address
        menu_items: Main navigation menu items
        user_menu_items: User dropdown menu items
        notification_count: Number of unread notifications
        has_new_notifications: Whether there are new notifications
        sticky: Whether header should be sticky
        size: Size variant (sm, md, lg)
        use_utility_icons: Use simple utility icons (more, notifications, profile)
        cls: Additional CSS classes
        hx_logout: HTMX endpoint for logout
        hx_notifications: HTMX endpoint for notifications
        hx_target: HTMX target selector
        projects_href: URL for Projects link in more menu
        whats_new_href: URL for What's New link in more menu
        attributions_href: URL for Attributions link in more menu
        account_settings_href: URL for Account Settings link in user menu
        logout_href: URL for logout action (if None, logout option is hidden)
        **kwargs: Additional HTML attributes

    Returns:
        Header element

    Example:
        >>> header(
        ...     logo_text="Labs App",
        ...     user_name="John Doe",
        ...     breadcrumb_items=[{"label": "Home", "href": "/"}, {"label": "Settings"}],
        ...     hx_logout="/logout"
        ... )
        >>> header(logo_icon=True, use_utility_icons=True)  # Minimal icon-based header
    """
    # Size configurations
    size_map: dict[str, _HeaderSizeConfig] = {
        "sm": {
            "height": "3rem",
            "logo_size": "sm",
            "px": spacing._4,
        },
        "md": {
            "height": "3.5rem",
            "logo_size": "md",
            "px": spacing._6,
        },
        "lg": {
            "height": "4rem",
            "logo_size": "lg",
            "px": spacing._8,
        },
    }
    config: _HeaderSizeConfig = size_map[size]

    # Container styles
    container_style = generate_style_string(
        position="sticky" if sticky else "static",
        top="0" if sticky else None,
        z_index="1100" if sticky else None,
        background_color=colors.background,
        border_bottom=f"1px solid {colors.border}",
    )

    css_class = merge_classes("header", f"header-{size}", cls)

    # Left section: Logo + Breadcrumbs
    logo_element = logo(use_icon=logo_icon, text=logo_text, size=config["logo_size"])
    left_items = [
        A(
            logo_element,
            href=logo_href,
            style="text-decoration: none; display: inline-flex; align-items: center;",
        )
    ]

    if breadcrumb_items:
        # Convert dicts to BreadcrumbItem objects
        breadcrumb_objects = [
            BreadcrumbItem(name=item.get("label", ""), href=item.get("href") or item.get("url"))
            for item in breadcrumb_items
        ]
        left_items.append(
            Div(
                breadcrumbs(items=breadcrumb_objects),
                style=f"margin-left: {spacing._4}; display: flex; align-items: center;",
            )
        )

    left_section = flex(
        *left_items,
        align="center",
        gap="1rem",
    )

    # Right section: User actions or utility icons
    if use_utility_icons:
        right_section = _build_utility_icons(
            notification_count=notification_count,
            hx_notifications=hx_notifications,
            hx_target=hx_target,
            projects_href=projects_href,
            whats_new_href=whats_new_href,
            attributions_href=attributions_href,
            account_settings_href=account_settings_href,
            logout_href=logout_href,
        )
    else:
        right_section = user_actions(
            user_avatar=user_avatar,
            user_name=user_name,
            user_email=user_email,
            menu_items=menu_items,
            user_menu_items=user_menu_items,
            notification_count=notification_count,
            has_new_notifications=has_new_notifications,
            size=size,
            hx_logout=hx_logout,
            hx_notifications=hx_notifications,
            hx_target=hx_target,
        )

    return HtmlHeader(
        hstack(
            left_section,
            right_section,
            justify="between",
            align="center",
            style=f"height: {config['height']}; padding: 0 {config['px']};",
        ),
        cls=css_class,
        style=container_style,
        **kwargs,
    )


def _build_utility_icons(
    notification_count: int = 0,
    hx_notifications: str | None = None,
    hx_target: str | None = None,
    projects_href: str = "/projects",
    whats_new_href: str = "/changelog",
    attributions_href: str = "/attributions",
    account_settings_href: str = "/account-settings",
    logout_href: str | None = None,
) -> Div:
    """Build the utility icons section (more options, notifications, profile)."""
    icon_btn_style = generate_style_string(
        background="transparent",
        border="none",
        cursor="pointer",
        padding=spacing._2,
        border_radius="50%",
        display="inline-flex",
        align_items="center",
        justify_content="center",
        color=colors.neutral.s600,
        transition="background-color 0.15s",
    )

    # More options icon (trigger for menu)
    more_icon = Div(
        NotStr(_MORE_OPTIONS_SVG),
        style=icon_btn_style,
        title="More options",
        role="button",
        tabindex="0",
    )

    # More options menu with Projects, What's New, Attributions
    more_menu = menu(
        more_icon,
        menu_item("Projects", href=projects_href),
        menu_item("What's New", href=whats_new_href),
        menu_divider(),
        menu_item("Attributions", href=attributions_href),
        position="bottom-right",
    )

    # User profile icon (trigger for menu)
    profile_icon = Div(
        NotStr(_USER_PROFILE_SVG),
        style=icon_btn_style,
        title="User profile",
        role="button",
        tabindex="0",
    )

    # User profile menu items
    user_menu_items = [menu_item("Account Settings", href=account_settings_href)]
    if logout_href:
        user_menu_items.append(menu_divider())
        user_menu_items.append(menu_item("Log Out", href=logout_href))

    # User profile menu
    profile_menu = menu(
        profile_icon,
        *user_menu_items,
        position="bottom-right",
    )

    # Build the icons list
    icons: list[Any] = [more_menu]

    # Only show notification bell if there are notifications
    if notification_count > 0:
        notif_btn = Div(
            NotStr(_NOTIFICATIONS_SVG),
            style=icon_btn_style,
            hx_get=hx_notifications if hx_notifications else None,
            hx_target=hx_target if hx_notifications else None,
            title="Notifications",
            role="button",
            tabindex="0",
        )
        icons.append(notif_btn)

    icons.append(profile_menu)

    return hstack(
        *icons,
        gap="4",
        align="center",
    )
