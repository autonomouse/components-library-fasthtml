"""Templates - page-level layout components."""

from .auth_page_layout import auth_page_layout
from .base_page import base_page
from .centered_content import centered_content
from .error_template import error_template
from .labs_intro_page import BadgeConfig, labs_intro_page
from .page_container import page_container
from .sidebar_layout import sidebar_layout
from .ui_showcase_page import ui_showcase_page

__all__ = [
    # Data classes
    "BadgeConfig",
    # Templates
    "auth_page_layout",
    "base_page",
    "centered_content",
    "error_template",
    "labs_intro_page",
    "page_container",
    "sidebar_layout",
    "ui_showcase_page",
]
