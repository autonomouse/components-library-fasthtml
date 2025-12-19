"""HTMX-based file dropzone molecule - Pure HTMX implementation."""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from fasthtml.common import Div, Input, Label

from ..atoms import heading, icon_button, text, vstack


def htmx_file_dropzone(
    accept: str = ".csv",
    max_size: str = "1MB",
    max_items: int = 100,
    accepted_formats: str = "CSV",
    upload_url: str | None = None,
    disabled: bool = False,
    **kwargs: Any,
) -> Any:
    """
    HTMX-based file dropzone molecule for file uploads.

    Uses pure HTMX with CSS-only drag-and-drop styling.
    No JavaScript required - relies on HTMX for all interactions.

    Args:
        accept: File type to accept (e.g., ".csv", ".pdf")
        max_size: Maximum file size (e.g., "1MB", "10MB")
        max_items: Maximum number of items/rows in file
        accepted_formats: Human-readable format description
        upload_url: HTMX endpoint for file upload (hx-post URL)
        disabled: Whether the dropzone is disabled
        **kwargs: Additional HTML attributes

    Returns:
        Div element with HTMX-powered dropzone

    Example:
        >>> htmx_file_dropzone(
        ...     accept=".csv",
        ...     accepted_formats="CSV",
        ...     upload_url="/api/upload",
        ...     max_size="5MB"
        ... )
    """
    # Generate unique ID for file input
    input_id = f"file-input-{uuid4().hex[:8]}"

    # File input with HTMX attributes
    file_input = Input(
        type="file",
        accept=accept,
        name="file",
        id=input_id,
        disabled=disabled,
        style="display: none;",
        **{
            "hx-post": upload_url if upload_url else None,
            "hx-encoding": "multipart/form-data",
            "hx-target": "#upload-result",
            "hx-swap": "innerHTML",
            "hx-trigger": "change",
        }
        if upload_url
        else {},
    )

    # Upload icon button that triggers file input
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

    # Dropzone content with CSS-only drag-and-drop styling
    dropzone_content = vstack(
        upload_icon,
        heading(
            f"Select a {accepted_formats} file to import",
            level=4,
            style="color: var(--color-text-primary); text-align: center;",
        ),
        text("Click to upload or drag and drop", style="text-align: center;"),
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
            cursor: pointer;
        """,
        cls="htmx-dropzone-area",
    )

    # Label that triggers file input on click (native HTML behavior)
    dropzone_trigger = Label(
        dropzone_content,
        fr=input_id,
        style="cursor: pointer; display: block;"
        if not disabled
        else "cursor: not-allowed; display: block;",
    )

    return Div(
        file_input,
        dropzone_trigger,
        Div(id="upload-result"),  # Target for upload response
        style="cursor: pointer; width: 100%;",
        **kwargs,
    )
