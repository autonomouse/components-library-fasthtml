"""Entity Detail Layout Template."""

from typing import Any

from fasthtml.common import Form

from ...components.atoms import text, vstack
from ...components.molecules import BreadcrumbItem, breadcrumbs
from ...components.templates.base_page import base_page
from ...components.templates.page_container import page_container
from ..organisms.navigation import navigation


def entity_detail_layout(
    user: Any,
    title: str,
    breadcrumb_items: list[BreadcrumbItem],
    form_action: str | None,
    children: Any,
    form_method: str = "post",
    error_message: str | None = None,
    is_multipart: bool = False,
    app_name: str | None = None,
    app_version: str | None = None,
) -> Any:
    """
    Standard layout for "Detail" pages (View/Create/Edit entity).

    Includes:
    - Navigation
    - Breadcrumbs
    - Error Message display
    - Form wrapper (only if form_action is provided)

    If form_action is None, children should contain its own form element.
    """

    # Error Message
    error_area = (
        text(
            error_message,
            style="color: var(--theme-text-error); padding: 0.5rem; background: rgba(220, 38, 38, 0.1); border-radius: 4px; border: 1px solid var(--theme-text-error);",
            cls="w-full",
        )
        if error_message
        else ""
    )

    # Main Form - only wrap in Form if form_action is provided
    # If form_action is None, assume children contains its own form
    if form_action:
        main_content = Form(
            children,
            method=form_method,
            action=form_action,
            style="width: 100%;",
            enctype="multipart/form-data" if is_multipart else None,
        )
    else:
        main_content = children

    # Page Assembly
    content = page_container(
        vstack(
            breadcrumbs(breadcrumb_items),
            error_area,
            main_content,
            gap="1.5rem",
        ),
        style="max-width: 1400px; margin: 0 auto; width: 100%;",
    )

    full_page = vstack(navigation(user, brand_name=app_name or "App"), content, gap=0)

    return base_page(
        full_page,
        title=title,
        app_name=app_name,
        app_version=app_version,
    )
