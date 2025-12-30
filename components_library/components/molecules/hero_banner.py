"""Hero Banner molecule - Full-width banner with background image."""

from __future__ import annotations

from typing import Any

from fasthtml.common import H1, Div, P

from ...utils import merge_classes
from ..atoms import vstack


def hero_banner(
    title: str,
    subtitle: str | None = None,
    *children: Any,
    background_image: str | None = None,
    background_color: str | None = None,
    overlay_opacity: float = 0.5,
    min_height: str = "400px",
    text_align: str = "center",
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Full-width hero banner with background image and text overlay.

    A flexible banner component for page headers, featuring sections, or
    promotional content. Supports background images with configurable overlay.

    Args:
        title: Main heading text
        subtitle: Optional subtitle/description text
        *children: Additional content (buttons, badges, etc.)
        background_image: URL for background image
        background_color: Fallback/overlay color (CSS color value)
        overlay_opacity: Opacity of the dark overlay (0-1, default 0.5)
        min_height: Minimum height of the banner (default "400px")
        text_align: Text alignment - "left", "center", "right"
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Hero banner component

    Example:
        >>> hero_banner(
        ...     "Welcome to Japan",
        ...     subtitle="Explore ancient traditions and modern wonders",
        ...     background_image="https://example.com/japan.jpg",
        ...     button("Start Exploring", variant="solid"),
        ... )
    """
    # Build background style
    bg_parts = []

    if background_image:
        # Dark overlay + image
        bg_parts.append(
            f"linear-gradient(rgba(0, 0, 0, {overlay_opacity}), rgba(0, 0, 0, {overlay_opacity}))"
        )
        bg_parts.append(f"url('{background_image}')")

    if background_color:
        bg_parts.append(background_color)
    elif not background_image:
        # Default gradient background
        bg_parts.append(
            "linear-gradient(135deg, var(--theme-bg-start, #1a1a2e) 0%, var(--theme-bg-end, #16213e) 100%)"
        )

    background_style = ", ".join(bg_parts) if bg_parts else "var(--theme-bg-start, #1a1a2e)"

    # Container style
    container_style = f"""
        background: {background_style};
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: {min_height};
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 3rem 1.5rem;
        text-align: {text_align};
        color: white;
        position: relative;
    """

    # Title style
    title_style = """
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-weight: 700;
        margin: 0 0 1rem 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        line-height: 1.2;
        color: white;
    """

    # Subtitle style
    subtitle_style = """
        font-size: clamp(1rem, 2vw, 1.25rem);
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.6;
        color: rgba(255, 255, 255, 0.9);
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
    """

    # Content items
    content_items = [H1(title, style=title_style)]

    if subtitle:
        content_items.append(P(subtitle, style=subtitle_style))

    # Additional children
    if children:
        content_items.extend(children)

    # Content wrapper
    content_wrapper = vstack(
        *content_items,
        gap=4,
        style=f"""
            max-width: 1000px;
            width: 100%;
            align-items: {"center" if text_align == "center" else "flex-start" if text_align == "left" else "flex-end"};
        """,
    )

    css_class = merge_classes("hero-banner", cls)

    # Merge any incoming style
    extra_style = kwargs.pop("style", "")
    combined_style = f"{container_style} {extra_style}".strip()

    return Div(
        content_wrapper,
        cls=css_class,
        style=combined_style,
        **kwargs,
    )
