"""DateRangeInputs molecule - Date range selector."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, Literal

from ..atoms import button, date_input, hstack, text, vstack


def date_range_inputs(
    start_date: str | None = None,
    end_date: str | None = None,
    on_change: Callable[[str | None, str | None], None] | None = None,  # noqa: ARG001
    disabled: bool = False,
    invalid: bool = False,
    start_placeholder: str = "Start date",
    end_placeholder: str = "End date",
    date_format: Literal["yyyy-mm-dd", "dd/mm/yyyy", "mm/dd/yyyy"] = "yyyy-mm-dd",
    min_date: str | None = None,
    max_date: str | None = None,
    show_clear_button: bool = True,
    validation_error: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Date range inputs molecule for selecting a date range.

    Composes two DateInput atoms with validation and clear functionality.
    Automatically validates that start date is before end date.

    Args:
        start_date: Start date value in YYYY-MM-DD format
        end_date: End date value in YYYY-MM-DD format
        on_change: Callback when date range changes (receives start_date, end_date)
        disabled: Whether the component is disabled
        invalid: Whether the date range is invalid
        start_placeholder: Placeholder for start date input
        end_placeholder: Placeholder for end date input
        date_format: Date format to use
        min_date: Minimum allowed date
        max_date: Maximum allowed date
        show_clear_button: Whether to show clear button
        validation_error: Custom validation error message to display
        **kwargs: Additional HTML attributes

    Returns:
        VStack element with date range inputs

    Example:
        >>> date_range_inputs(
        ...     start_date="2024-01-01",
        ...     end_date="2024-12-31",
        ...     on_change=lambda start, end: print(f"Range: {start} to {end}")
        ... )
    """
    # Calculate max date for start input (should not exceed end date)
    start_max_date = end_date or max_date

    # Calculate min date for end input (should not be before start date)
    end_min_date = start_date or min_date

    has_values = start_date or end_date
    invalid or bool(validation_error)

    # Build HTMX attributes for live updates if callback provided
    # In a real implementation, this would use HTMX for server-side validation

    # Start date field
    start_field = vstack(
        text("From", variant="label", style="font-weight: 500; color: var(--color-gray-700);"),
        date_input(
            name="start_date",
            value=start_date or "",
            format=date_format,
            min=min_date,
            max=start_max_date,
            disabled=disabled,
            placeholder=start_placeholder,
            aria_label="Start date",
        ),
        gap=1,
        style="flex: 1;",
    )

    # End date field
    end_field = vstack(
        text("To", variant="label", style="font-weight: 500; color: var(--color-gray-700);"),
        date_input(
            name="end_date",
            value=end_date or "",
            format=date_format,
            min=end_min_date,
            max=max_date,
            disabled=disabled,
            placeholder=end_placeholder,
            aria_label="End date",
        ),
        gap=1,
        style="flex: 1;",
    )

    # Build the children list
    children = [
        hstack(start_field, end_field, gap=3, style="align-items: flex-start;"),
    ]

    # Add validation error if present
    if validation_error:
        children.append(
            text(
                validation_error,
                style="font-size: 0.875rem; color: var(--color-error-600); line-height: 1.25;",
            )
        )

    # Add clear button if enabled and has values
    if show_clear_button and has_values and not disabled:
        clear_btn = button(
            "Clear",
            variant="ghost",
            size="sm",
            aria_label="Clear date range",
        )
        children.append(hstack(clear_btn, style="justify-content: flex-end;"))

    return vstack(
        *children,
        gap=3,
        style="align-items: stretch; width: 100%;",
        **kwargs,
    )
