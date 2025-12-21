"""Entity Overview Layout Template."""

from typing import Any

from fasthtml.common import Div, Form

from ...components.atoms import box, button_link, flex, heading, icon, input, text, vstack
from ...components.molecules import BreadcrumbItem, breadcrumbs
from ...components.templates.base_page import base_page
from ...components.templates.page_container import page_container
from ..organisms.navigation import navigation


def entity_overview_layout(
    user: Any,
    page_title: str,
    title: str,
    breadcrumb_items: list[BreadcrumbItem],
    search_endpoint: str,
    search_target: str,
    cta_text: str,
    cta_href: str,
    children: Any,
    search_placeholder: str = "Search...",
    search_swap: str = "innerHTML",
    empty_state_title: str | None = None,
    empty_state_description: str | None = None,
    empty_state_cta_text: str | None = None,
    empty_state_cta_href: str | None = None,
    is_empty: bool = False,
    app_name: str = "StoryVibe",
    app_version: str = "0.1.0",
    extra_controls: Any | None = None,
) -> Any:
    """
    Standard layout for "Overview" pages (lists of entities).

    Includes:
    - Navigation
    - Breadcrumbs
    - Header with Title and "Create New" CTA
    - Search/Filter Bar
    - Content Grid (or Empty State)
    """

    # Header Section
    header_section = flex(
        flex(
            breadcrumbs(breadcrumb_items),
            heading(title, level=1, style="margin-top: 0.5rem;"),
            direction="column",
            gap="0.5rem",
        ),
        button_link(
            icon("plus"),
            f" {cta_text}",
            variant="solid",
            color_palette="brand",
            href=cta_href,
            style="display: flex; gap: 0.5rem; align-items: center;",
        ),
        justify="between",
        align="end",
        style="margin-bottom: 2rem;",
    )

    # Filter Bar (HTMX)
    filter_form = Form(
        flex(
            flex(
                input(
                    name="search",
                    placeholder=search_placeholder,
                    style="width: 300px;",
                ),
                gap="1rem",
                align="center",
            ),
            extra_controls if extra_controls else "",
            gap="1rem",
            align="center",
            justify="between",
            style="width: 100%;",
        ),
        hx_get=search_endpoint,
        hx_target=search_target,
        hx_swap=search_swap,
        hx_trigger="input delay:200ms, change",
        style="margin-bottom: 1.5rem;",
    )

    # Content or Empty State
    if is_empty and empty_state_title:
        content_area = box(
            heading(empty_state_title, level=3, style="color: var(--theme-text-secondary);"),
            text(
                empty_state_description or "",
                style="color: var(--theme-text-muted);",
            ),
            button_link(
                empty_state_cta_text or cta_text,
                variant="outline",
                href=empty_state_cta_href or cta_href,
                style="margin-top: 1rem;",
            )
            if empty_state_cta_text
            else "",
            style="text-align: center; padding: 4rem; border: 1px dashed var(--theme-border-subtle); border-radius: 1rem;",
        )
    else:
        content_area = children

    # Page Assembly
    main_content = page_container(
        Div(
            header_section,
            filter_form,
            content_area,
        )
    )

    full_page = vstack(navigation(user, brand_name=app_name), main_content, gap=0)

    return base_page(
        full_page,
        title=page_title,
        app_name=app_name,
        app_version=app_version,
    )
