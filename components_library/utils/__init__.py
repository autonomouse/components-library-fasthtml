"""Utility functions and helpers."""

from .component_helpers import (
    generate_style_string,
    get_size_class,
    get_variant_class,
    merge_classes,
)
from .htmx_helpers import (
    confirm_delete,
    debounced_search,
    htmx_attrs,
    modal_trigger,
)
from .session import (
    SessionToken,
    add_session_token,
    clear_session_tokens,
    get_session_tokens,
    remove_session_token,
    set_session_tokens,
    toggle_session_operator,
)
from .style_generator import (
    color_value,
    focus_ring_styles,
    font_size_value,
    generate_border_radius,
    generate_box_shadow,
    responsive_gap,
    spacing_value,
)

__all__ = [
    # Session utilities
    "SessionToken",
    "add_session_token",
    "clear_session_tokens",
    # Style generators
    "color_value",
    # HTMX helpers
    "confirm_delete",
    "debounced_search",
    "focus_ring_styles",
    "font_size_value",
    "generate_border_radius",
    "generate_box_shadow",
    # Component helpers
    "generate_style_string",
    "get_session_tokens",
    "get_size_class",
    "get_variant_class",
    "htmx_attrs",
    "merge_classes",
    "modal_trigger",
    "remove_session_token",
    "responsive_gap",
    "set_session_tokens",
    "spacing_value",
    "toggle_session_operator",
]
