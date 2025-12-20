"""Timeline slider component for story placement."""

from typing import Any

from fasthtml.common import Div, Input, Label, Option, Script, Select, Span, Style


def timeline_slider(
    name: str,
    value: str = "Main",
    relation_name: str = "related_story_id",
    relation_options: list[tuple[str, str]] | None = None,
) -> Any:
    """
    Timeline slider selecting between Prequel, Current (Main), and Sequel.
    Shows a dropdown context when Sequel is selected.
    """

    # Map model values to slider values
    # Main/Current -> 1. Prequel -> 0. Sequel -> 2.
    if relation_options is None:
        relation_options = []
    mapping = {"Prequel": 0, "Main": 1, "Sequel": 2}
    current_val = mapping.get(value, 1)

    slider_id = f"timeline-slider-{name}"
    dropdown_container_id = f"timeline-dropdown-container-{name}"

    styles = """
    .timeline-container {
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
    .timeline-controls {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    .slider-wrapper {
        flex: 1;
    }
    """

    # JS to handle interaction: update hidden input for text value, toggle dropdown
    # We will submit the numeric value as 'timeline_numeric' and handle logic in backend,
    # OR simpler: update a hidden input with the real string value.

    js_logic = f"""
    const slider = document.getElementById('{slider_id}');
    const container = document.getElementById('{dropdown_container_id}');
    const hidden = document.getElementById('{name}-hidden');

    const map = {{0: 'Prequel', 1: 'Main', 2: 'Sequel'}};

    function update() {{
        const val = parseInt(slider.value);
        hidden.value = map[val];

        if (val === 2) {{
            container.style.display = 'block';
        }} else {{
            container.style.display = 'none';
        }}
    }}

    slider.addEventListener('input', update);
    update(); // Init
    """

    return Div(
        Label("Timeline Placement"),
        Div(
            Div(
                Input(
                    type="range",
                    min="0",
                    max="2",
                    step="1",
                    value=str(current_val),
                    id=slider_id,
                ),
                Div(
                    Span("Prequel"),
                    Span("Current"),
                    Span("Sequel"),
                    cls="slider-labels",
                ),
                # Hidden input to store the actual string value expected by backend
                Input(type="hidden", name=name, id=f"{name}-hidden", value=value),
                cls="slider-wrapper",
            ),
            Div(
                Select(
                    *(
                        [Option(opt[0], value=opt[1]) for opt in relation_options]
                        if relation_options
                        else [Option("Select Story...", value="")]
                    ),
                    name=relation_name,
                ),
                id=dropdown_container_id,
                style="display: none; min-width: 150px;",
            ),
            cls="timeline-controls",
        ),
        Style(styles),
        Script(js_logic),
        cls="timeline-container",
    )
