"""Timeline Lane component for grouping events horizontally."""

from typing import Any

from fasthtml.common import A, Div

from ...components.atoms.flex import flex
from ...components.atoms.heading import heading
from ...components.atoms.text import text


def timeline_lane(
    title: str,
    items: list[dict[str, Any]],
    lane_color: str = "var(--theme-accent-primary)",
    **kwargs: Any,
) -> Div:
    """
    Render a horizontal timeline lane with events.

    Args:
        title: Lane title (e.g., "Global Events", "Story 1")
        items: List of event dictionaries. Each dict should contain:
               - title: str
               - date: str | None
               - icon_color: str (e.g. hex code or var)
               - href: str
        lane_color: Color for the lane accent (left border)
        **kwargs: Additional arguments for the container
    """
    if not items:
        return Div(
            flex(
                heading(title, level=4, style=f"color: {lane_color}; margin: 0;"),
                text(
                    "No events yet",
                    style="color: var(--theme-text-muted); font-size: 0.9rem;",
                ),
                direction="column",
                gap="0.5rem",
            ),
            style=f"""
                background: rgba(0,0,0,0.2);
                border-left: 3px solid {lane_color};
                padding: 1rem;
                border-radius: 0.5rem;
            """,
            **kwargs,
        )

    event_nodes = []
    for item in items:
        color = item.get("icon_color", "var(--theme-accent-primary)")

        event_nodes.append(
            A(
                Div(
                    # Diamond marker
                    Div(
                        style=f"""
                            width: 12px;
                            height: 12px;
                            background: {color};
                            transform: rotate(45deg);
                            margin: 0 auto 0.5rem auto;
                        """,
                    ),
                    text(
                        item.get("title", "Untitled"),
                        style="color: white; font-size: 0.85rem; text-align: center; max-width: 120px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;",
                    ),
                    text(
                        item.get("date") or "",
                        style="color: var(--theme-text-muted); font-size: 0.7rem; text-align: center;",
                    ),
                    style="display: flex; flex-direction: column; align-items: center; padding: 0.5rem;",
                ),
                href=item.get("href", "#"),
                style="text-decoration: none;",
                cls="hover-glow",
            )
        )

    return Div(
        flex(
            heading(title, level=4, style=f"color: {lane_color}; margin: 0; min-width: 120px;"),
            flex(
                *event_nodes,
                gap="1rem",
                align="center",
                style="overflow-x: auto; flex: 1;",
            ),
            gap="1rem",
            align="center",
        ),
        style=f"""
            background: rgba(0,0,0,0.2);
            border-left: 3px solid {lane_color};
            padding: 1rem;
            border-radius: 0.5rem;
            min-height: 100px;
        """,
        **kwargs,
    )
