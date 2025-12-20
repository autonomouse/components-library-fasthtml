"""Form Modal component - Modal dialog with embedded form.

A molecule that composes modal and form elements into a reusable pattern
for creating entities, editing data, or collecting user input.
"""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Form

from ..atoms import button, hstack, modal, text


def form_modal(
    *form_fields: Any,
    modal_id: str,
    title: str,
    form_action: str,
    form_method: str = "POST",
    form_target: str | None = None,
    form_swap: str = "innerHTML",
    submit_label: str = "Submit",
    cancel_label: str = "Cancel",
    submit_color: Literal["brand", "gray", "red", "green"] = "brand",
    error_message: str | None = None,
    modal_size: str = "500px",
    form_id: str | None = None,
    cls: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Modal dialog with embedded form for data entry.

    This molecule composes modal and form components into a reusable pattern.
    It follows dependency injection principles - all configuration is passed
    as parameters rather than hardcoded.

    Args:
        *form_fields: Form field components (field, input, select, etc.)
        modal_id: Unique ID for the modal dialog
        title: Modal header title
        form_action: URL for form submission
        form_method: HTTP method (POST, PUT, PATCH)
        form_target: HTMX target selector for response
        form_swap: HTMX swap strategy
        submit_label: Text for submit button
        cancel_label: Text for cancel button
        submit_color: Color palette for submit button
        error_message: Optional error message to display
        modal_size: Modal max-width (CSS value)
        form_id: Custom form ID (defaults to {modal_id}-form)
        cls: Additional CSS classes
        **kwargs: Additional attributes passed to modal

    Returns:
        Modal component containing form with fields and action buttons

    Example:
        >>> # Basic usage
        >>> form_modal(
        ...     field(input(name="name", required=True), label="Name"),
        ...     field(textarea(name="desc"), label="Description"),
        ...     modal_id="create-item",
        ...     title="Create Item",
        ...     form_action="/items",
        ... )

        >>> # With custom configuration
        >>> form_modal(
        ...     field(input(name="title"), label="Title"),
        ...     field(select(name="type", options=types), label="Type"),
        ...     modal_id="edit-project",
        ...     title="Edit Project",
        ...     form_action="/projects/123",
        ...     form_method="PUT",
        ...     submit_label="Save Changes",
        ...     submit_color="green",
        ... )
    """
    actual_form_id = form_id or f"{modal_id}-form"

    # Build form content with fields and error placeholder
    form_content_items = list(form_fields)

    # Always include error div (empty or with message) so HX-Retarget can find it
    error_content = text(error_message, style="color: var(--color-error);") if error_message else ""
    form_content_items.append(
        Div(
            error_content,
            id=f"{modal_id}-error",
            style="margin-top: 0.5rem;" if error_message else "",
        )
    )

    # Form element with HTMX attributes
    form_attrs: dict[str, Any] = {
        "id": actual_form_id,
        "method": form_method,
        "action": form_action,  # Fallback if HTMX doesn't intercept
    }

    # Use HTMX for form submission
    if form_method.upper() == "POST":
        form_attrs["hx_post"] = form_action
    elif form_method.upper() == "PUT":
        form_attrs["hx_put"] = form_action
    elif form_method.upper() == "PATCH":
        form_attrs["hx_patch"] = form_action

    if form_target:
        form_attrs["hx_target"] = form_target
    if form_swap:
        form_attrs["hx_swap"] = form_swap

    # Close modal on successful submission
    form_attrs["hx-on:htmx:after-request"] = (
        "if(event.detail.successful) this.closest('dialog').close()"
    )

    form_element = Form(
        Div(
            *form_content_items,
            style="display: flex; flex-direction: column; gap: 1rem;",
        ),
        **form_attrs,
    )

    # Footer with action buttons
    footer = hstack(
        button(
            submit_label,
            type="submit",
            form=actual_form_id,
            variant="solid",
            color_palette=submit_color,
        ),
        button(
            cancel_label,
            variant="outline",
            **{"hx-on:click": "this.closest('dialog').close()"},  # type: ignore[arg-type]
        ),
        gap=3,
    )

    return modal(
        form_element,
        modal_id=modal_id,
        title=title,
        footer=footer,
        size=modal_size,
        cls=cls,
        **kwargs,
    )
