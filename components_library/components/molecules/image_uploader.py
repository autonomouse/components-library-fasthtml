"""Image uploader molecule - HTMX-based image upload with preview."""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from fasthtml.common import Div, Img, Input, Label

from ..atoms import text, vstack


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

    # Preview image
    preview_img = Img(
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

    # Upload button (styled as label)
    upload_button = Label(
        text(
            "Click to upload",
            style="""
                color: var(--color-primary);
                cursor: pointer;
                text-decoration: underline;
                font-size: 0.875rem;
            """,
        ),
        fr=upload_id,
        style="cursor: pointer;" if not disabled else "cursor: not-allowed; opacity: 0.5;",
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
                preview_img,
                current_value_input,
                id=container_id,
                style="margin-bottom: 0.5rem;",
            ),
            upload_button,
            info_text,
            loading_indicator,
            gap=1,
        ),
        file_input,
        **kwargs,
    )
