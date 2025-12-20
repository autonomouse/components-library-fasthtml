"""Logo component - Application logo."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Img, NotStr

from ...design_system.tokens import Colors
from ...utils import generate_style_string, merge_classes

colors = Colors()

_DEFAULT_LOGO_SVG = ""


def logo(
    text: str | None = None,
    src: str | None = None,
    alt: str = "Logo",
    size: Literal["sm", "md", "lg"] = "md",
    href: str | None = None,
    use_icon: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Logo component for branding.

    Args:
        text: Logo text (if no image)
        src: Logo image URL
        alt: Image alt text
        size: Logo size
        href: Optional link URL
        use_icon: Use the default icon logo (blue network icon)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with logo

    Example:
        >>> logo(text="Company", size="lg")
        >>> logo(src="/logo.svg", alt="Company Logo")
        >>> logo(use_icon=True, size="lg")  # Default icon
    """
    size_map = {
        "sm": {"height": "1.25rem", "font_size": "0.875rem", "icon_px": 20},
        "md": {"height": "1.5rem", "font_size": "1rem", "icon_px": 24},
        "lg": {"height": "2rem", "font_size": "1.25rem", "icon_px": 28},
    }

    css_class = merge_classes("logo", f"logo-{size}", cls)

    dimensions = size_map[size]

    # Icon logo (default icon)
    if use_icon:
        svg = _DEFAULT_LOGO_SVG.format(size=dimensions["icon_px"])
        logo_element = Div(
            NotStr(svg),
            style=generate_style_string(
                display="inline-flex",
                align_items="center",
                justify_content="center",
            ),
        )
    # Image logo
    elif src:
        logo_element = Img(
            src=src,
            alt=alt,
            style=generate_style_string(height=dimensions["height"], width="auto", display="block"),
        )
    # Text logo
    elif text:
        logo_element = Div(
            text,
            style=generate_style_string(
                font_size=dimensions["font_size"],
                font_weight="bold",
                color=colors.primary.s600,
                line_height="1",
            ),
        )
    else:
        # Default placeholder
        logo_element = Div(
            "Logo",
            style=generate_style_string(
                font_size=dimensions["font_size"],
                font_weight="bold",
                color=colors.neutral.s400,
                line_height="1",
            ),
        )

    # Wrap in link if href provided
    if href:
        from fasthtml.common import A

        return A(
            logo_element,
            href=href,
            cls=css_class,
            style="text-decoration: none; display: flex; align-items: center;",
            **kwargs,
        )

    return Div(logo_element, cls=css_class, **kwargs)
