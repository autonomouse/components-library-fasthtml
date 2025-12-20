"""Theme configuration."""

from .components import component_styles
from .foundations import base_styles
from .htmx_script import htmx_config, htmx_script, menu_click_outside_script
from .themes import (
    DEFAULT_THEME,
    THEMES,
    Theme,
    ThemeColors,
    get_available_themes,
    get_theme,
    get_theme_css,
)

__all__ = [
    "DEFAULT_THEME",
    "THEMES",
    "Theme",
    "ThemeColors",
    "base_styles",
    "component_styles",
    "get_available_themes",
    "get_theme",
    "get_theme_css",
    "htmx_config",
    "htmx_script",
    "menu_click_outside_script",
]
