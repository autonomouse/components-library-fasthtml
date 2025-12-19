"""Field component - Form field wrapper with label, helper text, and error."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Label, Span

from ...design_system.tokens import Colors, Spacing, Typography
from ...utils import generate_style_string, merge_classes

colors = Colors()
spacing = Spacing()
typography = Typography()


def field(
    *children: Any,
    label: str | None = None,
    label_for: str | None = None,
    helper_text: str | None = None,
    error_text: str | None = None,
    required: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Form field wrapper component.

    Wraps form inputs with label, helper text, and error messages.

    Args:
        *children: Form input elements to wrap
        label: Label text for the field
        label_for: ID of the input element (for attribute)
        helper_text: Helper text displayed below input
        error_text: Error message displayed below input
        required: Whether field is required (adds asterisk)
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element with wrapped form field

    Example:
        >>> field(
        ...     Input(name="email", type="email", id="email"),
        ...     label="Email Address",
        ...     label_for="email",
        ...     helper_text="We'll never share your email",
        ...     required=True
        ... )
    """
    css_class = merge_classes("field", "field-error" if error_text else None, cls)

    elements = []

    # Label
    if label:
        label_content = [label]
        if required:
            label_content.append(
                Span(
                    " *",
                    style=generate_style_string(color=colors.error.s600),
                )
            )

        elements.append(
            Label(
                *label_content,
                **{"for": label_for} if label_for else {},
                cls="field-label",
            )
        )

    # Children (the actual input elements)
    elements.extend(children)

    # Helper text
    if helper_text and not error_text:
        elements.append(Span(helper_text, cls="field-help-text"))

    # Error text
    if error_text:
        elements.append(Span(error_text, cls="field-error-text"))

    return Div(*elements, cls=css_class, **kwargs)
