"""Image Montage component - Grid of images for backgrounds."""

from typing import Any

from fasthtml.common import Div

from ...utils import generate_style_string


def image_montage(
    images: list[str],
    limit: int = 12,
    opacity: float = 0.6,
    filter_effect: str = "grayscale(30%)",
    **kwargs: Any,
) -> Div:
    """
    Create a responsive grid montage of images, suitable for backgrounds.

    Args:
        images: List of image URLs
        limit: Maximum number of images to display
        opacity: Opacity of individual images
        filter_effect: CSS filter to apply (e.g., 'grayscale(100%)')
        **kwargs: Additional HTML attributes for the container

    Returns:
        Div containing the image grid
    """
    if not images:
        return Div(**kwargs)

    display_images = images[:limit]

    image_divs = [
        Div(
            style=generate_style_string(
                background_image=f"url('{img}')",
                background_size="cover",
                background_position="center",
                width="100%",
                aspect_ratio="16/9",
                opacity=str(opacity),
                filter=filter_effect,
            )
        )
        for img in display_images
    ]

    base_style = generate_style_string(
        display="grid",
        grid_template_columns="repeat(auto-fill, minmax(150px, 1fr))",
        width="100%",
        height="100%",
        overflow="hidden",
    )

    custom_style = kwargs.pop("style", "")
    style = f"{base_style} {custom_style}"

    return Div(
        *image_divs,
        style=style,
        **kwargs,
    )
