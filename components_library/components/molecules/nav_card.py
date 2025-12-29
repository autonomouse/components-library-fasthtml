"""Navigation Card component."""

from typing import Any

from fasthtml.common import A, Div

from ...components.atoms.heading import heading
from ...components.atoms.icon import icon
from ...components.atoms.text import text
from ...utils import generate_style_string


def _stats_row(stats: list[dict]) -> Div:
    """Render a row of statistic icons with counts."""
    items = []

    for stat in stats:
        # Create stat item: Icon with Count below it
        item = Div(
            icon(
                stat.get("icon", "circle"),
                size="sm",
                style=f"color: {stat.get('color', 'var(--theme-accent-primary, #3b82f6)')}; margin-bottom: 4px;",
            ),
            text(
                str(stat.get("count", 0)),
                style="color: white; font-weight: 600; font-size: 1rem; line-height: 1;",
            ),
            title=f"{stat.get('label', '')}: {stat.get('count', 0)}",
            style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-width: 40px;",
        )
        items.append(item)

    return Div(*items, style="display: flex; gap: 0.75rem; margin-top: 1rem; flex-wrap: wrap;")


def nav_card(
    title: str,
    description: str,
    href: str,
    preview_images: list[str | None] | None = None,
    preview_names: list[str] | None = None,
    preview_focal_points: list[tuple[int, int]] | None = None,
    stats_breakdown: list[dict] | None = None,
    **kwargs: Any,
) -> Any:
    """
    A navigation card component with optional stacked preview images.

    Args:
        title: Card title
        description: Card description (fallback)
        href: Link URL
        preview_images: Optional list of image URLs to show as stacked avatars
        preview_names: Optional list of names for initials fallback
        preview_focal_points: Optional list of (x, y) tuples for background position
        stats_breakdown: Optional list of stats {label, count, icon, color}
        **kwargs: Additional HTML attributes

    Returns:
        Anchor component
    """
    base_style = generate_style_string(
        background="rgba(17, 24, 39, 0.4)",
        backdrop_filter="blur(12px)",
        border="1px solid rgba(55, 65, 81, 0.5)",
        border_radius="12px",
        padding="1.5rem",
        transition="all 0.3s ease",
        display="block",
        text_decoration="none",
        height="100%",
        cursor="pointer",
    )

    # Merge custom style if provided
    custom_style = kwargs.pop("style", "")
    style = f"{base_style} {custom_style}"

    content = []

    # Add fanned card stack if preview data provided
    if preview_images or preview_names:
        images = preview_images or []
        names = preview_names or []
        focal_points = preview_focal_points or []
        # Ensure we have at least placeholder data
        if not images and names:
            images = [None] * len(names)
        content.append(_card_stack(images, names, focal_points))
    else:
        # Reserve space for layout consistency
        content.append(Div(style="height: 90px; margin-bottom: 0.75rem;"))

    content.append(
        heading(
            title,
            level=3,
            style="font-size: 1.25rem; font-weight: bold; color: var(--theme-text-primary, white); margin-bottom: 0.5rem;",
        )
    )

    if stats_breakdown:
        # Render dynamic stats row
        content.append(_stats_row(stats_breakdown))
    else:
        # Fallback to simple text description
        content.append(
            text(
                description,
                style="color: var(--theme-text-secondary, #9ca3af); font-size: 0.875rem;",
            )
        )

    return A(
        *content,
        href=href,
        style=style,
        cls="nav-card hover:bg-white/5",
        **kwargs,
    )


def _card_stack(
    images: list[str | None],
    names: list[str] | None = None,
    focal_points: list[tuple[int, int]] | None = None,
) -> Div:
    """
    Create a featured card with smaller stacked cards beside it.

    Args:
        images: List of image URLs
        names: Optional list of names for initials fallback
        focal_points: Optional list of (x, y) tuples for background position
    """
    if names is None:
        names = []
    if focal_points is None:
        focal_points = []

    # Pad lists to match images length or at least 4 for safe indexing if images exist
    padded_names = (names[:4] if names else []) + [None] * 4
    padded_focal = (focal_points[:4] if focal_points else []) + [(50, 50)] * 4

    items = list(zip(images[:4], padded_names[:4], padded_focal[:4], strict=False))

    if not items:
        return Div()

    def get_initials(name: str | None) -> str:
        if not name:
            return "?"
        parts = name.strip().split()
        return (parts[0][0] + (parts[-1][0] if len(parts) > 1 else "")).upper()

    def make_card(
        img_url: str | None,
        name: str | None,
        w: int,
        h: int,
        extra_style: str = "",
        focal: tuple[int, int] = (50, 50),
    ) -> Div:
        initials = get_initials(name)
        base = f"width: {w}px; height: {h}px; border-radius: 8px; border: 2px solid rgba(59, 130, 246, 0.5); box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4); {extra_style}"
        if img_url:
            fx, fy = focal
            return Div(
                style=f"{base} background-image: url('{img_url}'); background-size: cover; background-position: {fx}% {fy}%;"
            )
        return Div(
            initials,
            style=f"{base} background: linear-gradient(135deg, #1e3a5f, #3b82f6); display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: {w * 0.3}px;",
        )

    # Featured card (first item) - larger
    featured_w, featured_h = 70, 90
    featured = make_card(
        items[0][0], items[0][1], featured_w, featured_h, "flex-shrink: 0;", items[0][2]
    )

    # Smaller stacked cards on the right
    small_w, small_h = 45, 60
    stack_cards = []
    remaining = items[1:4]  # Up to 3 more cards

    for i, (img_url, name, focal) in enumerate(remaining):
        rotation = (i - 1) * 6  # -6, 0, 6 degrees
        offset_y = 8 + i * 2
        stack_cards.append(
            make_card(
                img_url,
                name,
                small_w,
                small_h,
                f"position: absolute; left: {i * 18}px; top: {offset_y}px; transform: rotate({rotation}deg); z-index: {i + 1};",
                focal,
            )
        )

    # Stack container
    stack_width = small_w + (len(remaining) - 1) * 18 + 10 if remaining else 0
    stack_container = (
        Div(
            *stack_cards,
            style=f"position: relative; width: {stack_width}px; height: {featured_h}px; margin-left: 8px;",
        )
        if stack_cards
        else None
    )

    children = [featured]
    if stack_container:
        children.append(stack_container)

    return Div(
        *children,
        style="display: flex; align-items: flex-end; margin-bottom: 0.75rem;",
    )
