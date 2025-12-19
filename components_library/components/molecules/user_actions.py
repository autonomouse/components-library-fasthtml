"""UserActions component - user navigation and action buttons."""

from __future__ import annotations

from typing import Any, Literal, TypedDict

from fasthtml.common import Div
from pydantic import BaseModel

from ...design_system.tokens import Colors, Spacing
from ...utils import generate_style_string, merge_classes
from ..atoms import avatar, badge, button, hstack, icon_button, menu, menu_divider, menu_item


class _SizeConfig(TypedDict):
    avatar_size: int
    icon_size: str
    gap: str


colors = Colors()
spacing = Spacing()


class UserAction(BaseModel):
    """Represents a user action/menu item."""

    id: str
    label: str
    href: str | None = None
    icon: str | None = None
    variant: str = "default"


def user_actions(
    user_avatar: str | None = None,
    user_name: str = "User",
    user_email: str | None = None,
    menu_items: list[UserAction] | list[dict[str, Any]] | None = None,
    user_menu_items: list[UserAction] | list[dict[str, Any]] | None = None,
    notification_count: int = 0,
    has_new_notifications: bool = False,
    size: Literal["sm", "md", "lg"] = "md",
    cls: str | None = None,
    # HTMX endpoints
    hx_logout: str | None = None,
    hx_notifications: str | None = None,
    hx_target: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    UserActions component providing user menu and notifications.

    Combines avatar, notification badge, and dropdown menu for user-specific
    actions like profile, settings, and logout.

    Args:
        user_avatar: URL to user's avatar image
        user_name: User's display name
        user_email: User's email address
        menu_items: Main navigation menu items
        user_menu_items: User dropdown menu items
        notification_count: Number of unread notifications
        has_new_notifications: Whether there are new notifications
        size: Component size (sm, md, lg)
        cls: Additional CSS classes
        hx_logout: HTMX endpoint for logout
        hx_notifications: HTMX endpoint for notifications
        hx_target: HTMX target selector
        **kwargs: Additional HTML attributes

    Returns:
        User actions element

    Example:
        >>> user_actions(
        ...     user_name="John Doe",
        ...     user_email="john@example.com",
        ...     notification_count=3,
        ...     hx_logout="/logout"
        ... )
    """

    # Convert dicts to UserAction if needed
    def to_action(item: UserAction | dict[str, Any]) -> UserAction:
        if isinstance(item, dict):
            return UserAction(
                id=item.get("id", ""),
                label=item.get("label", ""),
                href=item.get("href"),
                icon=item.get("icon"),
                variant=item.get("variant", "default"),
            )
        return item

    menu_list = [to_action(item) for item in (menu_items or [])]
    user_menu_list = [to_action(item) for item in (user_menu_items or [])]

    # Size configurations
    size_map: dict[str, _SizeConfig] = {
        "sm": {"avatar_size": 28, "icon_size": "sm", "gap": spacing._2},
        "md": {"avatar_size": 36, "icon_size": "md", "gap": spacing._3},
        "lg": {"avatar_size": 44, "icon_size": "lg", "gap": spacing._4},
    }
    config: _SizeConfig = size_map[size]

    css_class = merge_classes("user-actions", cls)

    children = []

    # Main menu items as buttons
    for item in menu_list:
        children.append(
            button(
                item.label,
                variant="ghost",
                size=size,
                hx_get=item.href if item.href else None,
                hx_push_url="true" if item.href else None,
                hx_target=hx_target,
            )
        )

    # Notifications button
    if hx_notifications or notification_count > 0:
        notif_btn_style = generate_style_string(position="relative")
        notif_content = [
            icon_button(
                icon="🔔",
                variant="ghost",
                size=size,
                aria_label="Notifications",
                hx_get=hx_notifications,
                hx_target=hx_target,
            )
        ]

        if notification_count > 0:
            badge_style = generate_style_string(
                position="absolute",
                top="-4px",
                right="-4px",
            )
            notif_content.append(
                Div(
                    badge(
                        str(notification_count),
                        color_palette="red" if has_new_notifications else "gray",
                        size="sm",
                    ),
                    style=badge_style,
                )
            )

        children.append(Div(*notif_content, style=notif_btn_style))

    # User menu dropdown
    user_menu_children = []

    # User info header
    if user_email:
        user_info_style = generate_style_string(
            padding=spacing._3,
            border_bottom=f"1px solid {colors.border}",
        )
        user_menu_children.append(
            Div(
                Div(user_name, style="font-weight: 500;"),
                Div(user_email, style=f"font-size: 0.75rem; color: {colors.text_secondary};"),
                style=user_info_style,
            )
        )

    # User menu items
    for item in user_menu_list:
        user_menu_children.append(
            menu_item(
                item.label,
                href=item.href,
                hx_get=item.href if item.href else None,
                hx_target=hx_target,
            )
        )

    # Logout
    if hx_logout:
        if user_menu_list:
            user_menu_children.append(menu_divider())
        user_menu_children.append(
            menu_item(
                "Logout",
                hx_post=hx_logout,
                hx_target=hx_target,
                cls="menu-item-danger",
            )
        )

    # User avatar with dropdown
    if user_menu_children:
        children.append(
            menu(
                avatar(
                    name=user_name,
                    src=user_avatar,
                    size=config["avatar_size"],
                    style="cursor: pointer;",
                ),
                *user_menu_children,
            )
        )
    else:
        children.append(
            avatar(
                name=user_name,
                src=user_avatar,
                size=config["avatar_size"],
            )
        )

    return Div(
        hstack(*children, gap=config["gap"], align="center"),
        cls=css_class,
        **kwargs,
    )
