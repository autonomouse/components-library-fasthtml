"""Discrete slider component for selecting between specific options."""

from typing import Any

from fasthtml.common import Div, Input, Label, Option, Select, Span, Style


def discrete_slider(
    name: str,
    value: str,
    options: list[tuple[str, int]] | None = None,
    dropdown_name: str | None = None,
    dropdown_options: list[tuple[str, str]] | None = None,
    dropdown_trigger_value: str | None = None,
    label: str = "Select Option",
) -> Any:
    """
    A slider for selecting between discrete options.
    Optionally shows a secondary dropdown when a specific value is selected.

    Args:
        name: Form input name for the slider value
        value: Current value (must match one of the option labels)
        options: List of (Label, NumericValue) tuples.
                 Default: [("Prequel", 0), ("Main", 1), ("Sequel", 2)]
        dropdown_name: Name for the secondary dropdown input
        dropdown_options: Options for the secondary dropdown
        dropdown_trigger_value: The slider value (label) that triggers the dropdown display
        label: Label for the component
    """

    if options is None:
        options = [("Prequel", 0), ("Main", 1), ("Sequel", 2)]

    # Create mapping
    label_to_val = dict(options)
    val_to_label = {val: label for label, val in options}

    current_numeric = label_to_val.get(value, 1)

    min_val = min(val_to_label.keys())
    max_val = max(val_to_label.keys())

    slider_id = f"slider-{name}"
    dropdown_container_id = f"dropdown-container-{name}"
    hidden_input_id = f"{name}-hidden"

    styles = """
    .discrete-slider-container {
        margin-top: 1rem;
        background: rgba(255, 255, 255, 0.03);
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .slider-labels {
        display: flex;
        justify-content: space-between;
        margin-top: 0.5rem;
        color: var(--pico-muted-color);
        font-size: 0.8rem;
    }
    .slider-controls {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    .slider-wrapper {
        flex: 1;
    }
    """

    # Build Map for JS
    # We need a JS object string like {0: 'Prequel', 1: 'Main', ...}
    js_map = "{" + ", ".join([f"{val}: '{label}'" for label, val in options]) + "}"

    # Trigger logic
    trigger_condition = "false"
    if dropdown_trigger_value and dropdown_trigger_value in label_to_val:
        trigger_val = label_to_val[dropdown_trigger_value]
        trigger_condition = f"val == '{trigger_val}'"

    update_script = (
        f"const val = this.value; "
        f"const map = {js_map}; "
        f"document.getElementById('{hidden_input_id}').value = map[val]; "
        f"const container = document.getElementById('{dropdown_container_id}'); "
        f"if (container) container.style.display = ({trigger_condition}) ? 'block' : 'none';"
    )

    # Initial Display
    initial_display = "none"
    if dropdown_trigger_value and value == dropdown_trigger_value:
        initial_display = "block"

    dropdown_elem = ""
    if dropdown_name:
        dropdown_elem = Div(
            Select(
                *(
                    [Option(opt[0], value=opt[1]) for opt in dropdown_options]
                    if dropdown_options
                    else [Option("Select...", value="")]
                ),
                name=dropdown_name,
            ),
            id=dropdown_container_id,
            style=f"display: {initial_display}; min-width: 150px;",
        )

    return Div(
        Label(label),
        Div(
            Div(
                Input(
                    type="range",
                    min=str(min_val),
                    max=str(max_val),
                    step="1",
                    value=str(current_numeric),
                    id=slider_id,
                    **{"hx-on:input": update_script},
                ),
                Div(
                    *[Span(opt[0]) for opt in options],
                    cls="slider-labels",
                ),
                # Hidden input to store the actual string value expected by backend
                Input(type="hidden", name=name, id=hidden_input_id, value=value),
                cls="slider-wrapper",
            ),
            dropdown_elem,
            cls="slider-controls",
        ),
        Style(styles),
        cls="discrete-slider-container",
    )
