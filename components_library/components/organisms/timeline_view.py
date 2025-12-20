"""Timeline View organism for displaying sequential items in a flow."""

from typing import Any

from fasthtml.common import Div, Path, Svg

from ...components.molecules.timeline_card import timeline_card
from ...utils import generate_style_string


def _timeline_arrow() -> Any:
    """Render a directional arrow for the timeline."""
    return Div(
        Svg(
            Path(
                d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3",
                stroke="currentColor",
                stroke_width="2",
                stroke_linecap="round",
                stroke_linejoin="round",
            ),
            viewBox="0 0 24 24",
            fill="none",
            width="48",
            height="48",
            style="color: var(--theme-space-accent-primary, #06b6d4); filter: drop-shadow(0 0 5px currentColor);",
        ),
        style="display: flex; align-items: center; justify-content: center; margin: 0 2rem; opacity: 0.8;",
    )


def timeline_view(
    items_data: list[dict[str, Any]],
    href_template: str = "/items/{id}",
    **kwargs: Any,
) -> Any:
    """
    Renders items in a horizontal timeline flow with arrows between them.

    Generic component for displaying sequential items like stories, episodes,
    phases, milestones, or any ordered content.

    Args:
        items_data: List of dicts containing item data. Expected keys:
                   - id: Item identifier
                   - title: Display title
                   - item_type: Type/format (e.g., "Novel", "Episode")
                   - status: Current status (e.g., "Planning", "Complete")
                   - sequence_position: Position label (e.g., "Prequel", "Phase 1")
                   - image_url: Optional background image URL
        href_template: URL template for item links. Use {id} as placeholder.
                      Default: "/items/{id}"
        **kwargs: Additional attributes for the container.

    Example:
        timeline_view(
            items_data=[
                {"id": "1", "title": "Phase 1", "item_type": "Planning",
                 "status": "Complete", "sequence_position": "Start"},
                {"id": "2", "title": "Phase 2", "item_type": "Development",
                 "status": "In Progress", "sequence_position": "Current"},
            ],
            href_template="/projects/{project_id}/phases/{id}",
        )
    """

    container_style = generate_style_string(
        display="flex",
        flex_direction="row",
        align_items="center",
        justify_content="center",
        flex_wrap="wrap",
        gap="1rem",
        padding="2rem",
        width="100%",
        overflow_x="auto",
    )

    items = []
    for idx, item in enumerate(items_data):
        # Build href from template
        href = href_template.format(**item) if "{" in href_template else href_template

        # Create card
        card = timeline_card(
            title=item.get("title", "Untitled"),
            item_type=item.get("item_type", item.get("format", "Unknown")),
            status=item.get("status", "Planning"),
            sequence_position=item.get("sequence_position", item.get("timeline_relation", "Main")),
            image_url=item.get("image_url"),
            href=href,
        )
        items.append(card)

        # Add arrow if not last item
        if idx < len(items_data) - 1:
            items.append(_timeline_arrow())

    return Div(
        *items, style=container_style, cls="timeline-view-container custom-scrollbar", **kwargs
    )
