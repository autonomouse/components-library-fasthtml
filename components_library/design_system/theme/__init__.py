"""Theme configuration."""

from .components import component_styles
from .foundations import base_styles
from .htmx_script import htmx_config, htmx_script, menu_click_outside_script

__all__ = [
    "base_styles",
    "component_styles",
    "htmx_config",
    "htmx_script",
    "menu_click_outside_script",
]
