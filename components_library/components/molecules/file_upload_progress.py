"""FileUploadProgress molecule - File upload progress indicator."""

from __future__ import annotations

from typing import Any, Literal

from ..atoms import box, flex, icon_button, progress, text


def file_upload_progress(
    file_name: str,
    file_size: int,
    cancel_url: str | None = None,
    cancel_target: str | None = None,
    progress_value: int | None = None,
    status: Literal["uploading", "processing", "complete", "error"] = "uploading",
    **kwargs: Any,
) -> Any:
    """
    File upload progress molecule for displaying file upload progress.

    Shows file information, upload progress, and provides cancellation option.
    Uses HTMX for interactions - no JavaScript required.

    Args:
        file_name: Name of the file being uploaded
        file_size: Size of the file in bytes
        cancel_url: HTMX endpoint URL for cancel button (hx-delete)
        cancel_target: HTMX target selector for cancel response
        progress_value: Upload progress percentage (0-100), None for indeterminate
        status: Current upload status
        **kwargs: Additional HTML attributes

    Returns:
        Div element with upload progress display

    Example:
        >>> file_upload_progress(
        ...     file_name="data.csv",
        ...     file_size=1024000,
        ...     progress_value=45,
        ...     status="uploading",
        ...     cancel_url="/uploads/123/cancel",
        ...     cancel_target="closest .upload-item"
        ... )
    """

    def format_bytes(bytes_val: int, decimals: int = 2) -> str:
        """Format bytes to human readable format."""
        if bytes_val == 0:
            return "0 Bytes"

        k = 1024
        sizes = ["Bytes", "KB", "MB", "GB", "TB"]
        i = 0
        size = float(bytes_val)

        while size >= k and i < len(sizes) - 1:
            size /= k
            i += 1

        return f"{size:.{decimals}f} {sizes[i]}"

    def get_progress_color() -> str:
        """Get progress bar color based on status."""
        color_map = {
            "complete": "green",
            "error": "red",
            "processing": "blue",
            "uploading": "blue",
        }
        return color_map.get(status, "blue")

    def get_status_text() -> str:
        """Get status text based on upload status."""
        if status == "complete":
            return "Upload complete"
        elif status == "error":
            return "Upload failed"
        elif status == "processing":
            return "Processing..."
        else:
            return format_bytes(file_size)

    # CSV file icon
    csv_icon = box(
        text("CSV", style="font-size: 0.75rem; font-weight: 700; color: var(--color-green-700);"),
        style="""
            width: 40px;
            height: 40px;
            background-color: var(--color-green-50);
            border: 2px solid var(--color-green-200);
            border-radius: 0.375rem;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        """,
    )

    # File info
    file_info = flex(
        text(file_name, style="font-weight: 500; font-size: 0.875rem; line-height: 1.25;"),
        text(get_status_text(), style="font-size: 0.75rem; color: var(--color-text-muted);"),
        style="flex-direction: column; gap: 0.25rem; flex: 1;",
    )

    # Cancel button with HTMX
    cancel_attrs: dict[str, Any] = {}
    if cancel_url:
        cancel_attrs["hx-delete"] = cancel_url
        cancel_attrs["hx-swap"] = "outerHTML"
        if cancel_target:
            cancel_attrs["hx-target"] = cancel_target

    cancel_btn = icon_button(
        "🗑️",
        aria_label="Cancel upload",
        variant="ghost",
        color_palette="gray",
        size="sm",
        **cancel_attrs,
    )

    # Progress bar
    progress_bar = progress(
        progress_value if progress_value is not None else 0,
        color_palette=get_progress_color(),
        size="sm",
        show_label=False,
    )

    # Build layout
    return box(
        flex(
            csv_icon,
            flex(
                flex(
                    file_info,
                    cancel_btn,
                    style="justify-content: space-between; align-items: flex-start;",
                ),
                progress_bar,
                style="flex-direction: column; flex: 1; gap: 0.5rem;",
            ),
            gap="0.75rem",
            style="align-items: flex-start;",
        ),
        style="""
            border: 1px solid var(--color-border);
            border-radius: 0.5rem;
            padding: 1rem;
            background-color: var(--color-background);
        """,
        **kwargs,
    )
