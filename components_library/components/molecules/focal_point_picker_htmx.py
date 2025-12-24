"""Focal point picker molecule - HTMX-based focal point selector for avatar cropping."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Img, Script

from ..atoms import heading, text, vstack


def focal_point_picker_htmx(
    image_url: str,
    image_id: str,
    current_x: int = 50,
    current_y: int = 25,
    **kwargs: Any,
) -> Any:
    """
    Click-to-set focal point picker (HTMX-only, minimal JavaScript for coordinates).

    User clicks on the image to set the focal point.
    HTMX sends coordinates to server, which updates the preview.

    Args:
        image_url: URL of the uploaded image
        image_id: ID of the image (for API calls)
        current_x: Current focal point X (0-100)
        current_y: Current focal point Y (0-100)
        **kwargs: Additional HTML attributes

    Returns:
        Div element with focal point picker

    Example:
        >>> focal_point_picker_htmx(
        ...     image_url="/static/avatar.jpg",
        ...     image_id="123e4567-e89b-12d3-a456-426614174000",
        ...     current_x=50,
        ...     current_y=25,
        ... )
    """
    preview_id = f"avatar-preview-{image_id}"

    return Div(
        vstack(
            heading("Set Avatar Focus Point", level=4),
            text(
                "Click on the image where you want the avatar to focus (usually the face)",
                style="color: var(--color-text-muted); margin-bottom: 0.5rem; font-size: 0.875rem;",
            ),
            # Clickable image container
            Div(
                Img(
                    src=image_url,
                    style="""
                        width: 100%;
                        max-width: 400px;
                        cursor: crosshair;
                        display: block;
                        border-radius: 0.5rem;
                        border: 2px solid var(--color-border-muted);
                    """,
                    id=f"focal-image-{image_id}",
                ),
                # Focal point marker overlay
                Div(
                    style=f"""
                        position: absolute;
                        left: {current_x}%;
                        top: {current_y}%;
                        width: 30px;
                        height: 30px;
                        margin: -15px 0 0 -15px;
                        border: 3px solid var(--color-primary);
                        border-radius: 50%;
                        pointer-events: none;
                        box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.8), 0 0 10px rgba(0, 0, 0, 0.3);
                        background: rgba(59, 130, 246, 0.2);
                    """,
                    id=f"focal-marker-{image_id}",
                ),
                style="position: relative; display: inline-block; margin-bottom: 1rem;",
                id=f"focal-container-{image_id}",
            ),
            # Avatar preview
            Div(
                heading("Preview", level=5, style="margin-bottom: 0.5rem;"),
                Div(
                    style=f"""
                        width: 120px;
                        height: 120px;
                        border-radius: 50%;
                        background-image: url('{image_url}');
                        background-size: cover;
                        background-position: {current_x}% {current_y}%;
                        border: 3px solid var(--color-border);
                        margin: 0 auto;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    """,
                    id=preview_id,
                ),
                text(
                    "This is how your avatar will appear",
                    style="font-size: 0.75rem; color: var(--color-text-muted); text-align: center; margin-top: 0.5rem;",
                ),
                style="margin-top: 1rem; padding: 1rem; background: rgba(0, 0, 0, 0.05); border-radius: 0.5rem;",
            ),
            gap=2,
        ),
        # Minimal JavaScript for click coordinate calculation
        # This is necessary as HTMX doesn't have a built-in way to get click coordinates
        Script(f"""
            (function() {{
                const img = document.getElementById('focal-image-{image_id}');
                if (!img) return;

                img.addEventListener('click', function(e) {{
                    const rect = this.getBoundingClientRect();
                    const x = Math.round(((e.clientX - rect.left) / rect.width) * 100);
                    const y = Math.round(((e.clientY - rect.top) / rect.height) * 100);

                    // Update marker position
                    const marker = document.getElementById('focal-marker-{image_id}');
                    if (marker) {{
                        marker.style.left = x + '%';
                        marker.style.top = y + '%';
                    }}

                    // Update preview
                    const preview = document.getElementById('{preview_id}');
                    if (preview) {{
                        preview.style.backgroundPosition = x + '% ' + y + '%';
                    }}

                    // Update any other avatar elements on the page with this image
                    const avatars = document.querySelectorAll('[data-image-id="{image_id}"]');
                    avatars.forEach(function(avatar) {{
                        avatar.style.backgroundPosition = x + '% ' + y + '%';
                    }});

                    // Send to server via HTMX
                    htmx.ajax('POST', '/api/images/{image_id}/focal-point', {{
                        values: {{ focal_x: x, focal_y: y }},
                        target: '#{preview_id}',
                        swap: 'outerHTML'
                    }});
                }});
            }})();
        """),
        **kwargs,
    )
