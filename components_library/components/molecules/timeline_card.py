"""Timeline Card component for displaying items in a sequence."""

from typing import Any

from fasthtml.common import A, Div, Img

from ...components.atoms.badge import badge
from ...components.atoms.heading import heading
from ...components.atoms.text import text
from ...utils import generate_style_string


def timeline_card(
    title: str,
    item_type: str,
    status: str,
    sequence_position: str,
    image_url: str | None = None,
    href: str = "#",
    **kwargs: Any,
) -> Any:
    """
    A card representing an item in a timeline or sequence.

    Generic component for displaying sequential items like stories, episodes,
    phases, milestones, chapters, or any ordered content.

    Args:
        title: Item title
        item_type: Type/format of item (e.g., "Novel", "Episode", "Phase")
        status: Current status (e.g., "Planning", "In Progress", "Complete")
        sequence_position: Position in sequence (e.g., "Prequel", "Main", "Sequel",
                          "Phase 1", "Episode 1")
        image_url: Optional URL for cover/background image
        href: Link to item detail page
        **kwargs: Additional HTML attributes
    """

    # Theme colors based on sequence position
    position_colors = {
        "Prequel": "var(--theme-space-accent-secondary, #60a5fa)",  # Blue-ish
        "Main": "var(--theme-space-accent-primary, #06b6d4)",  # Cyan
        "Sequel": "var(--theme-space-accent-tertiary, #c084fc)",  # Purple
        "Parallel": "#f472b6",  # Pink
    }

    accent_color = position_colors.get(
        sequence_position, "var(--theme-space-accent-primary, #06b6d4)"
    )

    # Base container style
    base_style = generate_style_string(
        position="relative",
        width="280px",
        height="400px",
        border_radius="16px",
        overflow="hidden",
        border=f"1px solid {accent_color}",
        box_shadow=f"0 0 15px {accent_color}40",  # 40 for transparency
        background="rgba(17, 24, 39, 0.6)",  # Dark semi-transparent
        display="flex",
        flex_direction="column",
        justify_content="space-between",
        transition="all 0.3s ease",
        text_decoration="none",
        cursor="pointer",
    )

    # Background Image
    bg_content = []
    if image_url:
        bg_content.append(
            Img(
                src=image_url,
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.6; z-index: 0;",
            )
        )

    # Gradient Overlay
    gradient_overlay = Div(
        style="""
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to bottom, rgba(0,0,0,0.2), rgba(0,0,0,0.9));
            z-index: 1;
        """
    )

    # Content Container (Z-index 2)
    content_style = generate_style_string(
        position="relative",
        z_index="2",
        padding="1.5rem",
        height="100%",
        display="flex",
        flex_direction="column",
        justify_content="space-between",
        align_items="center",
        text_align="center",
    )

    # Top Section: Sequence Position
    top_section = Div(
        text(
            sequence_position,
            style=f"color: {accent_color}; font-weight: bold; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.875rem;",
        ),
    )

    # Bottom Section: Title, Type, Status
    bottom_section = Div(
        heading(
            title,
            level=3,
            style="color: white; margin-bottom: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.8);",
        ),
        text(
            f"Type: {item_type}",
            style="color: #9ca3af; font-size: 0.875rem; margin-bottom: 1rem;",
        ),
        badge(
            status,
            variant="gray",
            style=f"background: transparent; border: 1px solid {accent_color}; color: {accent_color}; box-shadow: 0 0 8px {accent_color}40;",
        ),
        style="display: flex; flex-direction: column; align-items: center;",
    )

    return A(
        *bg_content,
        gradient_overlay,
        Div(top_section, bottom_section, style=content_style),
        href=href,
        style=base_style,
        cls="timeline-card transition-transform hover:scale-105",
        **kwargs,
    )
