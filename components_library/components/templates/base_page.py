"""Base page template - provides consistent layout and structure."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Body, Head, Html, Main, NotStr, Title

from ...design_system.theme import (
    base_styles,
    component_styles,
    htmx_script,
)


def base_page(
    content: Any,
    title: str = "Labs App",
    description: str | None = None,
    include_htmx: bool = True,
    extra_head: str | None = None,
    app_name: str | None = None,
    app_version: str | None = None,
    **kwargs: Any,
) -> Html:
    """
    Base page template with consistent head and body structure.

    Args:
        content: Page content to render in the body
        title: Page title
        description: Meta description for SEO (recommended for all pages)
        include_htmx: Whether to include HTMX script
        extra_head: Additional HTML to include in the head (e.g., scripts, styles)
        app_name: Application name for console logging (e.g., "Labs")
        app_version: Application version for console logging (e.g., "1.0.0")
        **kwargs: Additional attributes for the Html element

    Returns:
        Complete HTML page

    Note:
        When both app_name and app_version are provided, a console.log statement
        is automatically added to the page head for consistency with JS apps
        in the Labs suite.

    Example:
        >>> base_page(
        ...     Div("Hello World"),
        ...     title="My Page",
        ...     description="This is a sample page"
        ... )
        >>> base_page(
        ...     content,
        ...     app_name="Labs App",
        ...     app_version="1.0.0"
        ... )
    """
    head_elements = [
        Title(title),
        NotStr('<meta name="viewport" content="width=device-width, initial-scale=1.0">'),
        NotStr('<meta charset="UTF-8">'),
    ]

    # Add meta description - use provided description or default
    meta_description = description or "A FastHTML application built with components-library"
    head_elements.append(NotStr(f'<meta name="description" content="{meta_description}">'))

    head_elements.extend(
        [
            NotStr(f"<style>{base_styles()}</style>"),
            NotStr(f"<style>{component_styles()}</style>"),
        ]
    )

    if include_htmx:
        head_elements.append(NotStr(htmx_script()))

    # Add app version console.log for consistency with JS apps
    if app_name and app_version:
        head_elements.append(NotStr(f"<script>console.log('{app_name} v{app_version}');</script>"))

    # Add extra head elements if provided
    if extra_head:
        head_elements.append(NotStr(extra_head))

    return Html(
        Head(*head_elements),
        Body(
            Main(content),
            # Modal container for HTMX modals
            NotStr('<div id="modal-container"></div>'),
        ),
        lang="en",
        **kwargs,
    )
