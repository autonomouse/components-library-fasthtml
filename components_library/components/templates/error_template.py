"""ErrorTemplate - Error page template with consistent layout."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A

from ..atoms import heading, hstack, text, vstack
from .page_container import page_container

# Button link styles (anchor styled as button)
_PRIMARY_LINK_STYLE = """
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 0.375rem;
    padding: 0.75rem 2rem;
    min-width: 160px;
    font-weight: 500;
    text-decoration: none;
    background-color: var(--color-primary-600, #4f46e5);
    color: white;
    transition: background-color 0.15s;
"""

_SECONDARY_LINK_STYLE = """
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 0.375rem;
    padding: 0.75rem 2rem;
    min-width: 160px;
    font-weight: 500;
    text-decoration: none;
    background-color: transparent;
    color: var(--color-text-secondary, #6b7280);
    border: 1px solid var(--color-border, #e5e7eb);
    transition: background-color 0.15s;
"""


def error_template(
    error_code: str,
    title: str,
    description: str,
    primary_action_text: str = "Go Home",
    primary_action_href: str | None = None,
    secondary_action_text: str | None = None,
    secondary_action_href: str | None = None,
    illustration: Any | None = None,
    **kwargs: Any,
) -> Any:
    """
    Template for error pages (404, 500, etc.) with consistent layout and styling.

    Provides a centered layout with error information and action buttons.

    Args:
        error_code: Error code (e.g., "404", "500")
        title: Main error title
        description: Error description
        primary_action_text: Primary action button text
        primary_action_href: Primary action button URL
        secondary_action_text: Optional secondary action button text
        secondary_action_href: Optional secondary action button URL
        illustration: Optional illustration or icon to display above error
        **kwargs: Additional HTML attributes

    Returns:
        PageContainer with error content

    Example:
        >>> error_template(
        ...     error_code="404",
        ...     title="Page Not Found",
        ...     description="The page you're looking for doesn't exist.",
        ...     primary_action_href="/"
        ... )
    """
    # Build children for vstack
    children = []

    # Add illustration if provided
    if illustration:
        children.append(illustration)

    # Error code
    if error_code:
        children.append(
            heading(
                error_code,
                level=1,
                size="xl6",
                style="color: var(--color-text-muted); font-weight: 700; letter-spacing: -0.05em;",
            )
        )

    # Title
    children.append(
        heading(
            title,
            level=2,
            size="xl2",
            style="color: var(--color-text-primary); font-weight: 600; line-height: 1.2;",
        )
    )

    # Description
    children.append(
        text(
            description,
            style="color: var(--color-text-muted); font-size: 1.125rem; line-height: 1.6; padding: 0.5rem 1rem;",
        )
    )

    # Action buttons
    button_children = []

    # Primary action - use anchor link for navigation
    if primary_action_href:
        button_children.append(
            A(
                primary_action_text,
                href=primary_action_href,
                style=_PRIMARY_LINK_STYLE,
                cls="btn btn-solid btn-brand btn-lg",
            )
        )

    # Secondary action - use anchor link for navigation
    if secondary_action_text and secondary_action_href:
        button_children.append(
            A(
                secondary_action_text,
                href=secondary_action_href,
                style=_SECONDARY_LINK_STYLE,
                cls="btn btn-outline btn-gray btn-lg",
            )
        )

    if button_children:
        children.append(
            hstack(
                *button_children,
                gap=4,
                style="width: 100%; max-width: 28rem; justify-content: center; margin-top: 1.5rem;",
            )
        )

    # Build the error content
    error_content = vstack(
        *children,
        gap=8,
        style="""
            text-align: center;
            width: 100%;
            max-width: none;
            margin: 0 auto;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        """,
    )

    return page_container(
        error_content,
        padding="2rem",
        **kwargs,
    )
