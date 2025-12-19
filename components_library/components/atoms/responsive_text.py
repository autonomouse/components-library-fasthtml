"""Responsive text component - adapts to viewport size."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Span

from ...design_system.tokens import Breakpoints, Colors, Typography
from ...utils import generate_style_string, merge_classes

colors = Colors()
typography = Typography()
breakpoints = Breakpoints()


def responsive_text(
    content: str,
    size_mobile: Literal["xs", "sm", "base", "lg", "xl", "xl2", "xl3"] = "base",
    size_tablet: Literal["xs", "sm", "base", "lg", "xl", "xl2", "xl3", "xl4"] | None = None,
    size_desktop: Literal["xs", "sm", "base", "lg", "xl", "xl2", "xl3", "xl4", "xl5"] | None = None,
    weight: Literal["normal", "medium", "semibold", "bold"] | None = "normal",
    color: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Span:
    """
    Text that adapts its size based on viewport width.

    Designed for responsive typography that scales appropriately on mobile,
    tablet (primary use case), and desktop devices.

    Args:
        content: Text content
        size_mobile: Font size for mobile (default)
        size_tablet: Font size for tablet (≥768px)
        size_desktop: Font size for desktop (≥1024px)
        weight: Font weight
        color: Text color
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Span element with responsive text sizing

    Example:
        >>> responsive_text(
        ...     "Responsive Title",
        ...     size_mobile="lg",
        ...     size_tablet="xl2",
        ...     size_desktop="xl3"
        ... )
    """
    # Get mobile size
    mobile_size = getattr(typography, size_mobile)

    # Weight mapping
    weight_map = {
        "normal": typography.font_normal,
        "medium": typography.font_medium,
        "semibold": typography.font_semibold,
        "bold": typography.font_bold,
    }

    font_weight = weight_map[weight] if weight else typography.font_normal
    text_color = color or colors.text_primary

    # Base mobile styles
    style = generate_style_string(
        font_size=mobile_size.size,
        line_height=mobile_size.line_height,
        font_weight=font_weight,
        color=text_color,
    )

    # Add responsive overrides via inline media queries
    # Note: For better support, these could be class-based in the theme
    responsive_styles = []

    if size_tablet:
        tablet_size = getattr(typography, size_tablet)
        responsive_styles.append(
            f"@media (min-width: {breakpoints.tablet}) {{ "
            f"font-size: {tablet_size.size}; "
            f"line-height: {tablet_size.line_height}; "
            f"}}"
        )

    if size_desktop:
        desktop_size = getattr(typography, size_desktop)
        responsive_styles.append(
            f"@media (min-width: {breakpoints.desktop}) {{ "
            f"font-size: {desktop_size.size}; "
            f"line-height: {desktop_size.line_height}; "
            f"}}"
        )

    css_class = merge_classes("text-responsive", cls)

    if "style" in kwargs:
        style = f"{style} {kwargs.pop('style')}"

    # For inline media queries to work, we need to wrap in a unique class
    # and generate a style tag. For now, use data attributes that theme can target
    attrs = {
        "data-mobile-size": size_mobile,
    }
    if size_tablet:
        attrs["data-tablet-size"] = size_tablet  # type: ignore[assignment]
    if size_desktop:
        attrs["data-desktop-size"] = size_desktop  # type: ignore[assignment]

    return Span(
        content,
        cls=css_class,
        style=style if style else None,
        **attrs,
        **kwargs,
    )
