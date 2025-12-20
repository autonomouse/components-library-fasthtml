"""Form card select component for visual option selection."""

from typing import Any

from fasthtml.common import Div, Input, Label, NotStr, Span, Style


def form_card_select(
    name: str,
    options: list[dict[str, str]],
    selected: str | None = None,
    label: str | None = None,
) -> Any:
    """
    A unified single-select component where options are presented as cards with icons.

    Args:
        name: Form field name.
        options: List of dicts with 'value', 'label', 'icon' (SVG string).
        selected: Currently selected value.
        label: Optional section label.
    """

    styles = """
    .card-select-container {
        display: flex;
        gap: 1rem;
        margin-top: 0.5rem;
    }
    .card-option {
        position: relative;
        flex: 1;
        cursor: pointer;
    }
    .card-option input {
        position: absolute;
        opacity: 0;
        width: 0;
        height: 0;
    }
    .card-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 0.75rem;
        transition: all 0.2s ease;
        height: 100%;
    }
    .card-option input:checked + .card-content {
        background: rgba(255, 255, 255, 0.1);
        border-color: var(--theme-accent-primary);
        box-shadow: 0 0 15px var(--theme-accent-primary);
    }
    .card-option:hover .card-content {
        background: rgba(255, 255, 255, 0.08);
        transform: translateY(-2px);
    }
    .card-icon {
        margin-bottom: 0.75rem;
        color: var(--theme-accent-primary);
    }
    .card-label {
        font-weight: 600;
        font-size: 0.9rem;
    }
    """

    cards = []
    for opt in options:
        is_checked = opt["value"] == selected

        cards.append(
            Label(
                Input(type="radio", name=name, value=opt["value"], checked=is_checked),
                Div(
                    Div(NotStr(opt["icon"]), cls="card-icon"),
                    Span(opt["label"], cls="card-label"),
                    cls="card-content",
                ),
                cls="card-option",
            )
        )

    return Div(
        Label(label) if label else None,
        Div(*cards, cls="card-select-container"),
        Style(styles),
    )
