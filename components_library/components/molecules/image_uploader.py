"""Image uploader molecule - HTMX-based image upload with preview."""

from __future__ import annotations

from typing import Any, cast
from uuid import uuid4

from fasthtml.common import Div, Img, Input

from ..atoms import button, flex, text, vstack


def image_uploader(
    entity_type: str,
    entity_id: str,
    project_id: str,
    current_image_url: str | None = None,
    image_type: str = "image",
    label: str = "Upload Image",
    accept: str = "image/jpeg,image/png,image/webp,image/gif",
    max_size: str = "10MB",
    disabled: bool = False,
    field_name: str = "image_url",
    form_id: str | None = None,
    focal_point_x: int = 50,
    focal_point_y: int = 25,
    image_id: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Reusable image upload component with preview.

    Features:
    - Preview current image
    - Click to upload
    - Client-side validation
    - HTMX-powered upload
    - Automatic preview update
    - Focal point support for avatars

    Args:
        entity_type: Type of entity (character, location, etc.)
        entity_id: UUID of the entity
        project_id: UUID of the project
        current_image_url: URL of current image (if any)
        image_type: Type of image (avatar, portrait, banner, etc.)
        label: Label text for the uploader
        accept: Accepted MIME types
        max_size: Maximum file size (human-readable)
        disabled: Whether the uploader is disabled
        field_name: Name of the input field to update (for form submission)
        form_id: ID of the form the input belongs to
        focal_point_x: Focal point X coordinate (0-100, for avatars)
        focal_point_y: Focal point Y coordinate (0-100, for avatars)
        image_id: ID of the image record (for focal point updates)
        **kwargs: Additional HTML attributes

    Returns:
        Div element with image uploader

    Example:
        >>> image_uploader(
        ...     entity_type="character",
        ...     entity_id="123e4567-e89b-12d3-a456-426614174000",
        ...     project_id="123e4567-e89b-12d3-a456-426614174001",
        ...     current_image_url="/static/avatar.jpg",
        ...     form_id="character-form"
        ... )
    """
    # Generate unique IDs
    upload_id = f"upload-{entity_type}-{entity_id}-{image_type}-{uuid4().hex[:8]}"
    preview_id = f"preview-{upload_id}"
    container_id = f"container-{upload_id}"

    # Placeholder image if none provided
    placeholder_url = (
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'"
        "%3E%3Crect width='200' height='200' fill='%23f3f4f6'/%3E%3Ctext x='50%25' y='50%25' "
        "dominant-baseline='middle' text-anchor='middle' font-family='sans-serif' font-size='14' "
        "fill='%239ca3af'%3ENo Image%3C/text%3E%3C/svg%3E"
    )

    # For avatars, use background-image with focal point support
    if image_type == "avatar" and current_image_url:
        preview_element = Div(
            id=preview_id,
            style=f"""
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background-image: url('{current_image_url}');
                background-size: cover;
                background-position: {focal_point_x}% {focal_point_y}%;
                border: 2px solid var(--color-border-muted);
            """,
            **{"data-image-id": image_id} if image_id else {},
        )
    else:
        # For other image types or no image, use regular img tag
        preview_element = Img(
            src=current_image_url or placeholder_url,
            alt="Preview",
            id=preview_id,
            style="""
                max-width: 200px;
                max-height: 200px;
                object-fit: cover;
                border-radius: 0.5rem;
                border: 2px solid var(--color-border-muted);
            """,
        )

    # Hidden input for current value (preserved on initial load)
    current_value_input = Input(
        type="hidden",
        name=field_name,
        value=current_image_url or "",
        form=form_id,
    )

    # Build upload URL with params
    upload_url = (
        f"/api/uploads/image"
        f"?project_id={project_id}"
        f"&entity_type={entity_type}"
        f"&entity_id={entity_id}"
        f"&image_type={image_type}"
        f"&field_name={field_name}"
    )
    if form_id:
        upload_url += f"&form_id={form_id}"

    # File input with HTMX upload
    file_input = Input(
        type="file",
        id=upload_id,
        name="file",
        accept=accept,
        disabled=disabled,
        style="display: none;",
        **{
            "hx-post": upload_url,
            "hx-encoding": "multipart/form-data",
            "hx-target": f"#{container_id}",
            "hx-swap": "innerHTML",  # Replace content inside container (Img + Input)
            "hx-trigger": "change",
            "hx-indicator": f"#loading-{upload_id}",
        },
    )

    # Action Buttons Row
    # 1. Upload Button
    upload_btn = button(
        "Upload Image",
        variant="outline",
        size="sm",
        **cast(Any, {"onclick": f"document.getElementById('{upload_id}').click()"}),
        disabled=disabled,
    )

    # 2. Adjust Focus Point (Avatar only)
    adjust_btn = None
    if image_type == "avatar":
        adjust_btn = button(
            "Adjust Focus Point",
            variant="ghost",
            size="sm",
            disabled=not (current_image_url and image_id),
            style="opacity: 0.5; cursor: not-allowed;"
            if not (current_image_url and image_id)
            else "",
            **cast(
                Any,
                {
                    "hx-get": f"/api/images/{image_id}/focal-point-modal",
                    "hx-target": "#modal-container",
                    "hx-swap": "innerHTML",
                }
                if current_image_url and image_id
                else {},
            ),
        )

    # 3. View Full Image
    view_btn = button(
        "View Full Image",
        variant="ghost",
        size="sm",
        disabled=not (current_image_url and image_id),
        style="opacity: 0.5; cursor: not-allowed;" if not (current_image_url and image_id) else "",
        **cast(
            Any,
            {
                "hx-get": f"/api/images/{image_id}/view-modal",
                "hx-target": "#modal-container",
                "hx-swap": "innerHTML",
            }
            if current_image_url and image_id
            else {},
        ),
    )

    # Combine into row
    button_row = flex(
        upload_btn,
        adjust_btn,
        view_btn,
        gap="0.5rem",
        align="center",
        justify="start",
        style="margin-top: 0.5rem; flex-wrap: wrap;",
    )

    # Info text
    info_text = text(
        f"Accepted formats: JPEG, PNG, WebP, GIF (max. {max_size})",
        style="font-size: 0.75rem; color: var(--color-text-muted);",
    )

    # Loading indicator
    loading_indicator = Div(
        text("Uploading...", style="color: var(--color-primary);"),
        id=f"loading-{upload_id}",
        style="display: none;",
        cls="htmx-indicator",
    )

    return Div(
        vstack(
            text(label, style="font-weight: 600; margin-bottom: 0.5rem;"),
            Div(
                preview_element,
                current_value_input,
                id=container_id,
                style="margin-bottom: 0.5rem;",
            ),
            button_row,
            info_text,
            loading_indicator,
            gap=1,
        ),
        file_input,
        **kwargs,
    )
