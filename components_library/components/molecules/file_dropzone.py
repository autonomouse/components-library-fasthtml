"""FileDropzone molecule - File upload zone with click-to-upload.

Note: For drag-and-drop functionality, use browser's native drag-drop events
which require JavaScript. This component provides a click-to-upload interface
using only HTML (via Label element) and HTMX for file uploads.

For a simpler HTMX-only version, see htmx_file_dropzone.
"""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from fasthtml.common import Div, Input, Label

from ..atoms import heading, icon_button, text, vstack


def file_dropzone(
    accept: str = ".csv",
    max_size: str = "1MB",
    max_items: int = 100,
    accepted_formats: str = "CSV",
    on_drop: str | None = None,
    disabled: bool = False,
    **kwargs: Any,
) -> Any:
    """
    File dropzone molecule for file uploads via click.

    Provides a visual dropzone area with click-to-upload functionality.
    Uses HTMX for handling file uploads. No JavaScript required.

    Note: Native drag-and-drop requires JavaScript event handlers which this
    component does not include. Use htmx_file_dropzone for a similar alternative,
    or add custom drag-drop handlers if needed.

    Args:
        accept: File type to accept (e.g., ".csv", ".pdf")
        max_size: Maximum file size (e.g., "1MB", "10MB")
        max_items: Maximum number of items/rows in file
        accepted_formats: Human-readable format description
        on_drop: HTMX endpoint for file upload (hx-post URL)
        disabled: Whether the dropzone is disabled
        **kwargs: Additional HTML attributes

    Returns:
        Div element with dropzone

    Example:
        >>> file_dropzone(
        ...     accept=".csv",
        ...     accepted_formats="CSV",
        ...     on_drop="/api/upload",
        ...     max_size="5MB"
        ... )
    """
    # Generate unique ID for the file input
    input_id = f"file-input-{uuid4().hex[:8]}"

    # File input (hidden) with HTMX attributes
    file_input = Input(
        type="file",
        accept=accept,
        id=input_id,
        name="file",
        style="display: none;",
        disabled=disabled,
        **{
            "hx-post": on_drop if on_drop else None,
            "hx-encoding": "multipart/form-data",
            "hx-target": "#upload-result",
            "hx-swap": "innerHTML",
            "hx-trigger": "change",
        }
        if on_drop
        else {},
    )

    # Upload icon button (decorative, no interaction)
    upload_icon = icon_button(
        "☁️",
        aria_label=f"Upload {accepted_formats} file",
        variant="outline",
        size="lg",
        disabled=disabled,
        style="""
            background-color: var(--color-background);
            color: var(--color-text-muted);
            pointer-events: none;
        """,
    )

    # Dropzone content
    dropzone_content = vstack(
        upload_icon,
        heading(
            f"Select a {accepted_formats} file to import",
            level=4,
            style="color: var(--color-text-primary); text-align: center;",
        ),
        text("Click to upload", style="text-align: center;"),
        text(
            f"{accepted_formats} format (max. {max_size} or {max_items} line items)",
            style="font-size: 0.875rem; color: var(--color-text-muted); text-align: center;",
        ),
        gap=2,
        style="""
            border: 2px dashed var(--color-border-muted);
            border-radius: 1rem;
            background-color: var(--color-background-muted);
            height: 189px;
            padding: 2rem;
            justify-content: center;
            width: 100%;
            transition: all 0.2s;
        """,
        cls="dropzone-area",
    )

    # Label wraps content - clicking anywhere opens file picker (no JS needed)
    dropzone_label = Label(
        dropzone_content,
        fr=input_id,
        style="cursor: pointer; display: block;"
        if not disabled
        else "cursor: not-allowed; display: block;",
    )

    return Div(
        file_input,
        dropzone_label,
        Div(id="upload-result"),  # Target for upload response
        style="width: 100%;",
        **kwargs,
    )
