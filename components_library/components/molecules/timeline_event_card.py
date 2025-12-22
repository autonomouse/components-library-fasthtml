"""Timeline Event Card component for individual events."""

from typing import Any

from fasthtml.common import A, Div

from ...components.atoms import badge, flex, heading, icon, text, vstack


def timeline_event_card(
    title: str,
    date: str | None = None,
    description: str | None = None,
    href: str = "#",
    icon_name: str = "calendar",
    icon_color: str = "var(--theme-accent-primary)",
    type_name: str = "Event",
    is_shared: bool = False,
    story_count: int = 0,
    **kwargs: Any,
) -> Any:
    """
    Render a timeline event card for the story or global timeline.

    Args:
        title: Title of the event
        date: Date or Era string
        description: Short description of the event
        href: Link structure for the card
        icon_name: Name of the icon to display
        icon_color: Color of the icon and glow
        type_name: Name of the event type (e.g. "Battle", "Discovery")
        is_shared: Whether this event is shared across multiple stories
        story_count: Number of stories this event appears in (0 for global)
        **kwargs: Additional arguments for the container
    """
    # Determine badge text
    if story_count == 0:
        badge_text = "Global"
    elif is_shared:
        badge_text = f"Shared ({story_count})"
    else:
        badge_text = None

    # Icon with glow
    icon_component = Div(
        icon(name=icon_name, size="md", stroke_width=1.5),
        style=f"""
            color: {icon_color};
            filter: drop-shadow(0 0 6px {icon_color});
        """,
    )

    # Header with icon, type badge, and shared badge
    header = flex(
        icon_component,
        badge(type_name, color_palette="default", size="sm"),
        badge(badge_text, color_palette="accent", size="sm") if badge_text else "",
        gap="0.5rem",
        align="center",
    )

    # Content
    content = vstack(
        header,
        heading(
            title,
            level=4,
            style="font-size: 1rem; font-weight: 600; color: white; margin: 0.75rem 0 0.25rem 0;",
        ),
        text(
            date or "",
            style="color: var(--theme-accent-primary); font-size: 0.85rem; margin-bottom: 0.5rem;",
        )
        if date
        else "",
        text(
            (description[:100] + "..." if len(description or "") > 100 else description or ""),
            style="color: var(--theme-text-muted); font-size: 0.85rem; line-height: 1.4;",
        )
        if description
        else "",
        gap="0",
        align="start",
        style="width: 100%;",
    )

    card_style = """
        background: rgba(13, 17, 34, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.25rem;
        transition: all 0.3s ease;
        height: 100%;
    """

    return A(
        Div(content, style=card_style, cls="hover-glow"),
        href=href,
        style="text-decoration: none; display: block; height: 100%;",
        **kwargs,
    )
