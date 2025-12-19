"""JobStatusBanner component - displays background job status."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from fasthtml.common import Div
from pydantic import BaseModel

from ...design_system.tokens import Colors, Spacing
from ...utils import generate_style_string, merge_classes
from ..atoms import badge, button, collapsible, hstack, spinner, text, vstack

colors = Colors()
spacing = Spacing()


class BackgroundJob(BaseModel):
    """Represents a background job."""

    request_id: str
    job_name: str
    status: str
    is_running: bool
    created_at: str
    error_message: str | None = None


def _get_status_color(
    status: str,
) -> Literal["brand", "gray", "red", "green"]:
    """Get badge color for job status."""
    status_upper = status.upper()
    if status_upper in ("COMPLETED", "SUCCESS"):
        return "green"
    if status_upper in ("FAILED", "ERROR"):
        return "red"
    if status_upper in ("RUNNING", "PICKED_UP", "PROCESSING"):
        return "brand"
    return "gray"


def _format_timestamp(timestamp: str) -> str:
    """Format timestamp to human-readable relative time."""
    try:
        dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        now = datetime.now(dt.tzinfo) if dt.tzinfo else datetime.now()
        diff = now - dt
        diff_mins = int(diff.total_seconds() / 60)

        if diff_mins < 1:
            return "just now"
        if diff_mins < 60:
            return f"{diff_mins}m ago"
        diff_hours = diff_mins // 60
        if diff_hours < 24:
            return f"{diff_hours}h ago"
        diff_days = diff_hours // 24
        return f"{diff_days}d ago"
    except (ValueError, TypeError):
        return timestamp


def _get_display_name(job_name: str) -> str:
    """Get display-friendly job name."""
    return job_name.replace("labs__", "").replace("_", " ").title()


def job_status_banner(
    jobs: list[BackgroundJob] | list[dict[str, Any]],
    is_loading: bool = False,
    error: str | None = None,
    default_open: bool = True,
    cls: str | None = None,
    # HTMX for job actions
    hx_cancel_url: str | None = None,
    _hx_close_url: str | None = None,  # Reserved for future use
    hx_target: str | None = None,
    **kwargs: Any,
) -> Div | None:
    """
    JobStatusBanner component for displaying background job status.

    Shows a collapsible banner with active and recent background jobs,
    including status, timestamps, and cancel functionality.

    Args:
        jobs: List of background jobs
        is_loading: Whether jobs are loading
        error: Error message if loading failed
        default_open: Whether banner is expanded by default
        cls: Additional CSS classes
        hx_cancel_url: HTMX URL template for canceling jobs (use {request_id} placeholder)
        hx_close_url: HTMX URL for closing the banner
        hx_target: HTMX target selector
        **kwargs: Additional HTML attributes

    Returns:
        Job status banner element, or None if no jobs

    Example:
        >>> jobs = [BackgroundJob(request_id="1", job_name="process_data", status="RUNNING", is_running=True, created_at="2024-01-01T12:00:00Z")]
        >>> job_status_banner(jobs, hx_cancel_url="/jobs/{request_id}/cancel")
    """
    # Convert dicts to BackgroundJob if needed
    job_list = []
    for job in jobs:
        if isinstance(job, dict):
            job_list.append(
                BackgroundJob(
                    request_id=job.get("request_id", ""),
                    job_name=job.get("job_name", ""),
                    status=job.get("status", ""),
                    is_running=job.get("is_running", False),
                    created_at=job.get("created_at", ""),
                    error_message=job.get("error_message"),
                )
            )
        else:
            job_list.append(job)

    # Don't show if no jobs and no error/loading
    if len(job_list) == 0 and not error and not is_loading:
        return None

    active_jobs = [j for j in job_list if j.is_running]
    has_active = len(active_jobs) > 0

    # Container styles
    border_color = colors.error.s200 if error else colors.primary.s200
    bg_color = colors.error.s50 if error else colors.primary.s50

    container_style = generate_style_string(
        width="100%",
        border_radius="0.375rem",
        border=f"1px solid {border_color}",
        background_color=bg_color,
    )

    css_class = merge_classes("job-status-banner", cls)

    # Header content
    header_items = []

    # Icon/spinner
    if is_loading or has_active:
        header_items.append(spinner(size="sm"))
    else:
        header_items.append(text("📋", size="lg"))

    # Status text
    if error:
        title_text = "Error Loading Jobs"
        subtitle_text = error
    elif has_active:
        title_text = (
            f"{len(active_jobs)} Background Job{'s' if len(active_jobs) != 1 else ''} Running"
        )
        subtitle_text = "Processing your requests..."
    else:
        title_text = f"{len(job_list)} Background Job{'s' if len(job_list) != 1 else ''}"
        subtitle_text = "View recent jobs"

    header_items.append(
        vstack(
            text(title_text, weight="semibold", size="sm"),
            text(subtitle_text, variant="caption", size="xs"),
            gap=0,
            align="start",
        )
    )

    header = hstack(*header_items, gap=3, align="center", style=f"padding: {spacing._4};")

    # Job items
    job_items = []
    for job in job_list:
        job_style = generate_style_string(
            padding=spacing._3,
            background_color=colors.background,
            border_radius="0.375rem",
            border=f"1px solid {colors.border}",
        )

        job_content = [
            hstack(
                text(_get_display_name(job.job_name), weight="medium", size="sm"),
                badge(job.status, color_palette=_get_status_color(job.status), size="sm"),
                gap=4,
                justify="between",
            ),
            text(f"Started {_format_timestamp(job.created_at)}", variant="caption", size="xs"),
        ]

        if job.error_message:
            job_content.append(text(f"Error: {job.error_message}", variant="error", size="xs"))

        job_row = hstack(
            vstack(*job_content, gap=1, align="start"),
            button(
                "Cancel",
                size="sm",
                variant="outline",
                color_palette="red",
                hx_post=hx_cancel_url.format(request_id=job.request_id) if hx_cancel_url else None,
                hx_target=hx_target,
            )
            if job.is_running and hx_cancel_url
            else None,
            justify="between",
            align="start",
            style=job_style,
        )
        job_items.append(job_row)

    content = vstack(
        *job_items,
        gap=3,
        align="stretch",
        style=f"padding: 0 {spacing._4} {spacing._4}; border-top: 1px solid {border_color};",
    )

    return Div(
        collapsible(
            header,
            content,
            default_open=default_open,
        ),
        cls=css_class,
        style=container_style,
        **kwargs,
    )
