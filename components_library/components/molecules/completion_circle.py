"""Completion Circle component."""

from typing import Any

from fasthtml.common import Div, Img

from ...components.atoms.heading import heading
from ...utils import generate_style_string


def completion_circle(
    title: str,
    percentage: int,
    subtitle: str | None = None,
    image_url: str | None = None,
    color: str = "#3b82f6",
    **kwargs: Any,
) -> Any:
    """
    A circular progress component.
    """
    # Extract style from kwargs to merge with component styles
    extra_style = kwargs.pop("style", "")

    container_style = generate_style_string(
        display="flex",
        flex_direction="column",
        align_items="center",
        justify_content="center",
        position="relative",
        width="100%",
        height="100%",
        min_height="300px",  # Ensure it takes space
    )

    # Conic gradient for the circle
    circle_size = "220px"
    circle_style = generate_style_string(
        width=circle_size,
        height=circle_size,
        border_radius="50%",
        background=f"conic-gradient({color} {percentage}%, #1e293b 0)",
        display="flex",
        align_items="center",
        justify_content="center",
        position="relative",
        box_shadow=f"0 0 20px {color}60",
        margin_top="1rem",
    )

    # Inner circle (mask)
    inner_circle_style = generate_style_string(
        width="180px",
        height="180px",
        background="#0f172a",
        border_radius="50%",
        display="flex",
        flex_direction="column",
        align_items="center",
        justify_content="center",
        position="absolute",
        overflow="hidden",
    )

    content = Div(
        heading(
            f"{percentage}%",
            level=1,
            style="font-size: 3rem; font-weight: 800; color: #fff; margin: 0; text-shadow: 0 0 10px rgba(255,255,255,0.5);",
        ),
    )

    if image_url:
        content = Div(
            heading(
                f"{percentage}%",
                level=1,
                style="font-size: 2.5rem; font-weight: 800; color: #fff; margin: 0;",
            ),
            Img(
                src=image_url,
                style="width: 50px; height: auto; margin-top: 0.5rem; border-radius: 4px; box-shadow: 0 0 5px #fff;",
            ),
        )

    return Div(
        heading(
            title,
            level=3,
            style=f"font-size: 1.25rem; color: {color}; margin-bottom: 0.5rem; text-align: center;",
        ),
        heading(
            subtitle,
            level=4,
            style="font-size: 1rem; color: #94a3b8; margin-bottom: 1rem; text-align: center; font-weight: 400;",
        )
        if subtitle
        else "",
        Div(Div(content, style=inner_circle_style), style=circle_style),
        style=f"{container_style} {extra_style}".strip(),
        **kwargs,
    )
