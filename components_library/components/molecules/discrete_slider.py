"""Discrete slider component for selecting between specific options.

Uses radio buttons styled as a segmented control - no JavaScript needed.
"""

from typing import Any

from fasthtml.common import Div, Input, Label, Style


def discrete_slider(
    name: str,
    value: str,
    options: list[tuple[str, int]] | None = None,
    dropdown_name: str | None = None,  # noqa: ARG001 - Deprecated, kept for API compat
    dropdown_options: list[tuple[str, str]] | None = None,  # noqa: ARG001
    dropdown_trigger_value: str | None = None,  # noqa: ARG001
    label: str = "Select Option",
) -> Any:
    """
    A segmented control for selecting between discrete options.

    Uses native radio buttons styled as a button group - no JavaScript required.

    Args:
        name: Form input name for the selected value
        value: Current value (must match one of the option labels)
        options: List of (Label, NumericValue) tuples.
                 Default: [("Prequel", 0), ("Main", 1), ("Sequel", 2)]
                 Note: NumericValue is used for ordering only; the label is submitted.
        dropdown_name: DEPRECATED - Not supported in radio button implementation
        dropdown_options: DEPRECATED - Not supported in radio button implementation
        dropdown_trigger_value: DEPRECATED - Not supported in radio button implementation
        label: Label for the component
    """

    if options is None:
        options = [("Prequel", 0), ("Main", 1), ("Sequel", 2)]

    # Sort options by numeric value for consistent ordering
    sorted_options = sorted(options, key=lambda x: x[1])

    # Generate unique ID for this instance
    slider_id = f"segmented-{name}"

    styles = """
    .segmented-control-container {
        margin-top: 1rem;
        background: rgba(255, 255, 255, 0.03);
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .segmented-control-label {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    .segmented-control {
        display: flex;
        border-radius: 0.5rem;
        overflow: hidden;
        border: 1px solid var(--theme-border-subtle, rgba(255,255,255,0.1));
    }
    .segmented-control input[type="radio"] {
        position: absolute;
        opacity: 0;
        pointer-events: none;
    }
    .segmented-control label {
        flex: 1;
        padding: 0.5rem 1rem;
        text-align: center;
        cursor: pointer;
        background: var(--theme-surface-1, rgba(0,0,0,0.2));
        color: var(--theme-text-secondary, #888);
        border-right: 1px solid var(--theme-border-subtle, rgba(255,255,255,0.1));
        transition: background 0.15s, color 0.15s;
        margin: 0;
        font-size: 0.9rem;
    }
    .segmented-control label:last-of-type {
        border-right: none;
    }
    .segmented-control label:hover {
        background: var(--theme-surface-2, rgba(255,255,255,0.05));
    }
    .segmented-control input[type="radio"]:checked + label {
        background: var(--theme-accent-primary, #6366f1);
        color: white;
    }
    .segmented-control input[type="radio"]:focus + label {
        outline: 2px solid var(--theme-accent-primary, #6366f1);
        outline-offset: -2px;
    }
    """

    # Build radio buttons with labels
    radio_elements = []
    for opt_label, opt_value in sorted_options:
        radio_id = f"{slider_id}-{opt_value}"
        is_checked = opt_label == value

        # Radio input (hidden but functional)
        radio_elements.append(
            Input(
                type="radio",
                name=name,
                value=opt_label,  # Submit the label, not the numeric value
                id=radio_id,
                checked=is_checked if is_checked else None,
            )
        )
        # Visible label styled as button segment
        radio_elements.append(Label(opt_label, fr=radio_id))

    return Div(
        Label(label, cls="segmented-control-label"),
        Div(*radio_elements, cls="segmented-control"),
        Style(styles),
        cls="segmented-control-container",
    )
