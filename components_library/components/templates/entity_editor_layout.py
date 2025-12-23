"""Entity Editor Layout - Two-column layout for inline editing pages.

This template provides a consistent layout for pages that use HTMX-driven
inline editing rather than traditional form submission. It features:
- Navigation bar
- Breadcrumbs
- Configurable header section
- Two-column grid (main editor + sidebar metadata)
- No form wrapper (each section manages its own HTMX updates)

Use this for entities like scenes, chapters, or any page where individual
fields auto-save independently via HTMX.
"""

from typing import Any

from fasthtml.common import Div

from ..atoms.grid import grid
from ..atoms.stack import vstack
from ..molecules.breadcrumbs import BreadcrumbItem, breadcrumbs
from ..organisms.navigation import navigation
from .base_page import base_page


def entity_editor_layout(
    user: Any,
    title: str,
    breadcrumb_items: list[BreadcrumbItem],
    header_content: Any,
    editor_panel: Any,
    sidebar_panels: list[Any],
    context_selector: Any | None = None,
    editor_width: str = "3fr",
    sidebar_width: str = "2fr",
    app_name: str | None = None,
) -> Any:
    """
    Two-column layout for inline editing pages.

    Unlike entity_detail_layout, this template does NOT wrap content in a form.
    Each section should manage its own HTMX updates independently.

    Args:
        user: Current user info for navigation.
        title: Page title for browser tab.
        breadcrumb_items: List of breadcrumb items for navigation path.
        header_content: Header section content (title, status, actions).
        editor_panel: Main content/editor panel (left column).
        sidebar_panels: List of sidebar card panels (right column).
        context_selector: Optional context selector (e.g., chapter dropdown).
        editor_width: CSS grid width for editor panel (default "3fr").
        sidebar_width: CSS grid width for sidebar (default "2fr").
        app_name: Application name for navigation branding.
        app_version: Application version for navigation.

    Returns:
        Complete page with two-column editor layout.

    Example:
        >>> entity_editor_layout(
        ...     user=current_user,
        ...     title="Edit Scene - My Story",
        ...     breadcrumb_items=[...],
        ...     header_content=flex(title_input, status_badge, save_button),
        ...     editor_panel=card(textarea(...)),
        ...     sidebar_panels=[
        ...         card(heading("Metadata"), ...),
        ...         card(heading("Characters"), ...),
        ...     ],
        ...     context_selector=chapter_dropdown,
        ... )
    """
    # Breadcrumb navigation
    breadcrumb_nav = breadcrumbs(breadcrumb_items, style="margin-bottom: 1.5rem;")

    # Sidebar from panels
    sidebar = vstack(*sidebar_panels, gap="1rem")

    # Two-column grid layout
    main_content = grid(
        editor_panel,
        sidebar,
        cols=f"{editor_width} {sidebar_width}",
        gap="1.5rem",
        style="align-items: start;",
    )

    # Page content assembly
    page_elements = [breadcrumb_nav, header_content]
    if context_selector:
        page_elements.append(context_selector)
    page_elements.append(main_content)

    page_content = Div(
        *page_elements,
        style="max-width: 1400px; margin: 0 auto; padding: 2rem;",
    )

    # Full page with navigation
    full_page = vstack(
        navigation(user, brand_name=app_name or "StoryVibe"),
        page_content,
        gap=0,
    )

    return base_page(full_page, title=title)
