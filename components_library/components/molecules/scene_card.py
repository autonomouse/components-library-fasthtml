"""Scene Card molecule - displays a scene with characters and location."""

from typing import Any

from fasthtml.common import A, Div

from ...components.atoms import avatar, badge, flex, heading, icon, text


def scene_card(
    title: str,
    characters: list[dict[str, Any]] | None = None,
    location_name: str | None = None,
    location_icon: str = "map-pin",
    status: str | None = None,
    href: str | None = None,
    accent_color: str = "var(--theme-accent-primary, #00f0ff)",
    scene_id: str | None = None,
    draggable: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Card component for displaying a scene in a storyboard/kanban view.

    Args:
        title: Scene title
        characters: List of character dicts with 'name' and optional 'image_url'
        location_name: Name of the location where scene takes place
        location_icon: Icon name for location (default: map-pin)
        status: Scene status (e.g., "Draft", "Outlined", "Revised")
        href: Link URL for clicking the card
        accent_color: Color for the left border accent
        scene_id: Unique ID for drag-and-drop operations
        draggable: Enable drag-and-drop for this card
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Example:
        scene_card(
            title="Discovery of the Artifact",
            characters=[
                {"name": "Elara Vance", "image_url": "/images/elara.jpg"},
                {"name": "Kai", "image_url": None},
            ],
            location_name="Titan Metropolis",
            status="Draft",
            href="/projects/123/scenes/456",
            scene_id="scene-123",
            draggable=True,
        )
    """
    from ...utils import merge_classes

    elements = []

    # Header row: Title and optional status badge
    header_items = [
        heading(
            title,
            level=4,
            style="font-size: 0.95rem; font-weight: 600; color: white; margin: 0; flex: 1;",
        )
    ]
    if status:
        status_colors = {
            "Draft": "default",
            "Outlined": "accent",
            "Revised": "success",
            "Final": "brand",
        }
        header_items.append(
            badge(
                status,
                color_palette=status_colors.get(status, "default"),
                size="sm",
            )
        )
    elements.append(
        flex(
            *header_items,
            justify="between",
            align="center",
            gap="0.5rem",
            style="width: 100%; margin-bottom: 0.75rem;",
        )
    )

    # Characters row
    if characters:
        char_avatars = []
        for char in characters[:4]:  # Limit to 4 characters displayed
            char_avatars.append(
                flex(
                    avatar(
                        name=char.get("name", "?"),
                        image_url=char.get("image_url"),
                        size=28,
                        style="border: 1px solid rgba(255,255,255,0.2);",
                    ),
                    text(
                        char.get("name", "Unknown"),
                        style="font-size: 0.8rem; color: var(--theme-text-secondary, #e0e0e0); margin-left: 0.4rem;",
                    ),
                    align="center",
                    gap="0",
                )
            )

        # Show "+N more" if there are more than 4 characters
        if len(characters) > 4:
            char_avatars.append(
                text(
                    f"+{len(characters) - 4} more",
                    style="font-size: 0.75rem; color: var(--theme-text-muted, #9ca3af);",
                )
            )

        elements.append(
            flex(
                *char_avatars,
                direction="column",
                gap="0.4rem",
                style="width: 100%; margin-bottom: 0.5rem;",
            )
        )

    # Location row
    if location_name:
        elements.append(
            flex(
                Div(
                    icon(name=location_icon, size="sm"),
                    style=f"color: {accent_color}; margin-right: 0.4rem;",
                ),
                text(
                    location_name,
                    style="font-size: 0.8rem; color: var(--theme-text-muted, #9ca3af);",
                ),
                align="center",
                gap="0",
            )
        )

    # Content container
    content = flex(
        *elements,
        direction="column",
        gap="0",
        style="width: 100%;",
    )

    # Card styles with left accent border
    card_style = f"""
        background: rgba(13, 17, 34, 0.7);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-left: 3px solid {accent_color};
        border-radius: 8px;
        padding: 0.875rem;
        transition: all 0.2s ease;
        cursor: pointer;
    """

    # Merge any additional styles
    if "style" in kwargs:
        card_style = f"{card_style} {kwargs.pop('style')}"

    css_class = merge_classes("scene-card hover-glow", cls)

    # Add draggable attributes if enabled
    card_attrs = {"style": card_style, "cls": css_class, **kwargs}
    if draggable and scene_id:
        card_attrs["data_scene_id"] = scene_id
        card_attrs["cls"] = merge_classes(css_class, "sortable-item")

    card_element = Div(
        content,
        **card_attrs,
    )

    if href and href != "#":
        link_element = A(
            card_element,
            href=href,
            style="text-decoration: none; display: block;",
        )
        # For sortable, wrap in a Div with the sortable attributes
        if draggable and scene_id:
            return Div(
                link_element,
                cls="sortable-item",
                data_scene_id=scene_id,
            )
        return link_element

    return card_element
