"""Notifications organism - notification dropdown with management."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from fasthtml.common import Div
from pydantic import BaseModel

from ...design_system.tokens import Colors, Spacing
from ...utils import generate_style_string, merge_classes
from ..atoms import badge, button, hstack, menu, text

colors = Colors()
spacing = Spacing()


class NotificationTag(BaseModel):
    """Tag for categorizing notifications."""

    label: str
    color: str = "gray"


class NotificationItem(BaseModel):
    """Represents a notification."""

    id: str
    type: str
    message: str
    is_read: bool
    created_at: str
    tags: list[NotificationTag] | None = None
    reference_id: str | None = None
    reference_type: str | None = None


def _format_date(date_str: str) -> str:
    """Format date string to human-readable format."""
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%b %d, %Y")
    except (ValueError, TypeError):
        return date_str


def _notification_item(
    notification: NotificationItem,
    hx_click_url: str | None = None,
    hx_target: str | None = None,
) -> Div:
    """Render a single notification item."""
    # Get tags
    tags = notification.tags or [NotificationTag(label=notification.type)]

    item_style = generate_style_string(
        padding=spacing._4,
        border_bottom=f"1px solid {colors.border}",
        border_left="2px solid",
        border_left_color=colors.primary.s500 if not notification.is_read else "transparent",
        cursor="pointer",
        transition="background-color 0.2s",
    )

    tag_elements = []
    for tag in tags:
        tag_style = generate_style_string(
            font_size="0.75rem",
            padding=f"{spacing._0_5} {spacing._2}",
            border_radius="0.375rem",
            background_color=colors.neutral.s100,
            color=colors.neutral.s700,
        )
        tag_elements.append(Div(tag.label, style=tag_style))

    attrs: dict[str, Any] = {
        "cls": "notification-item",
        "style": item_style,
        "tabindex": "0",
        "role": "button",
    }

    if hx_click_url:
        attrs["hx_post"] = hx_click_url.format(id=notification.id)
        attrs["hx_target"] = hx_target

    return Div(
        hstack(
            hstack(*tag_elements, gap=spacing._2),
            text(_format_date(notification.created_at), variant="caption", size="xs"),
            justify="between",
            align="center",
        ),
        text(
            notification.message,
            size="sm",
            weight="medium" if not notification.is_read else "normal",
            color=colors.text_primary if not notification.is_read else colors.text_secondary,
        ),
        **attrs,
    )


def notifications(
    items: list[NotificationItem] | list[dict[str, Any]] | None = None,
    is_loading: bool = False,
    max_height: str = "450px",
    width: str = "350px",
    cls: str | None = None,
    # HTMX endpoints
    hx_mark_all_read: str | None = None,
    hx_click_url: str | None = None,
    hx_target: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Notifications organism providing a dropdown with notification management.

    Features unread count badge, notification list, and mark as read functionality.

    Args:
        items: List of notification items
        is_loading: Whether notifications are loading
        max_height: Maximum height of dropdown
        width: Width of dropdown
        cls: Additional CSS classes
        hx_mark_all_read: HTMX endpoint for marking all as read
        hx_click_url: HTMX URL template for clicking notification (use {id} placeholder)
        hx_target: HTMX target selector
        **kwargs: Additional HTML attributes

    Returns:
        Notifications dropdown element

    Example:
        >>> notifications(
        ...     items=[
        ...         NotificationItem(id="1", type="info", message="New update", is_read=False, created_at="2024-01-01")
        ...     ],
        ...     hx_mark_all_read="/notifications/mark-all-read"
        ... )
    """
    # Convert dicts to NotificationItem if needed
    notification_list = []
    if items:
        for item in items:
            if isinstance(item, dict):
                tags = None
                if item.get("tags"):
                    tags = [
                        NotificationTag(
                            label=t.get("label", ""),
                            color=t.get("color", "gray"),
                        )
                        for t in item["tags"]
                    ]
                notification_list.append(
                    NotificationItem(
                        id=item.get("id", ""),
                        type=item.get("type", ""),
                        message=item.get("message", ""),
                        is_read=item.get("is_read", False),
                        created_at=item.get("created_at", ""),
                        tags=tags,
                        reference_id=item.get("reference_id"),
                        reference_type=item.get("reference_type"),
                    )
                )
            else:
                notification_list.append(item)

    unread_count = sum(1 for n in notification_list if not n.is_read)
    total_count = len(notification_list)

    css_class = merge_classes("notifications", cls)

    # Trigger button with badge
    trigger_style = generate_style_string(position="relative")
    trigger = Div(
        button(
            "🔔",
            variant="ghost",
            size="sm",
            aria_label="Notifications",
        ),
        Div(
            badge(str(unread_count), color_palette="red", size="sm"),
            style="position: absolute; top: -4px; right: -4px;",
        )
        if unread_count > 0
        else None,
        style=trigger_style,
    )

    # Header
    header_style = generate_style_string(
        padding=spacing._4,
        border_bottom=f"1px solid {colors.border}",
    )
    header_content = hstack(
        hstack(
            text("Notifications", weight="bold", size="base"),
            badge(str(unread_count), color_palette="brand", size="sm")
            if unread_count > 0
            else None,
            gap=spacing._2,
        ),
        button(
            "Mark all as read",
            variant="ghost",
            size="sm",
            color_palette="brand",
            hx_post=hx_mark_all_read,
            hx_target=hx_target,
        )
        if unread_count > 0 and hx_mark_all_read
        else None,
        justify="between",
        align="center",
    )
    header = Div(header_content, style=header_style)

    # Content
    content_style = generate_style_string(
        max_height=max_height,
        overflow_y="auto",
    )

    if is_loading:
        content = Div(
            text("Loading notifications...", variant="caption"),
            style=f"padding: {spacing._4}; text-align: center;",
        )
    elif total_count == 0:
        content = Div(
            text("No notifications", variant="caption"),
            style=f"padding: {spacing._4}; text-align: center;",
        )
    else:
        content = Div(
            *[
                _notification_item(n, hx_click_url=hx_click_url, hx_target=hx_target)
                for n in notification_list
            ],
            style=content_style,
        )

    dropdown_style = generate_style_string(
        width=width,
        padding="0",
    )

    return Div(
        menu(
            trigger,
            Div(header, content, style=dropdown_style),
            placement="bottom-end",
        ),
        cls=css_class,
        **kwargs,
    )
