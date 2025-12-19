"""Authentication form molecule - Login/signup form with validation."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Form, P

from ..atoms import alert, button, field, heading, input, link, vstack


def auth_form(
    form_type: str = "login",
    error_message: str | None = None,
    action: str = "/login",
    method: str = "POST",
    **kwargs: Any,
) -> Form:
    """
    Authentication form molecule for login/signup.

    Args:
        form_type: Type of form ("login" or "signup")
        error_message: Optional error message to display
        action: Form action URL
        method: HTTP method
        **kwargs: Additional HTML attributes

    Returns:
        Authentication form component

    Example:
        >>> auth_form("login", error_message="Invalid credentials")
        >>> auth_form("signup", action="/register")
    """
    is_login = form_type == "login"

    # Form content
    content = [
        # Header
        heading(
            "Sign In" if is_login else "Create Account",
            level=2,
            cls="text-center",
        ),
        P(
            "Welcome! Please sign in to continue."
            if is_login
            else "Create your account to get started.",
            cls="text-muted text-center",
        ),
    ]

    # Error alert
    if error_message:
        content.append(
            alert(
                error_message,
                variant="error",
                closeable=True,
            )
        )

    # Form fields
    fields = [
        field(
            input(
                name="email",
                type="email",
                placeholder="your@email.com",
                required=True,
                id="email",
            ),
            label="Email Address",
            label_for="email",
            required=True,
        ),
    ]

    if not is_login:
        # Additional fields for signup
        fields.extend(
            [
                field(
                    input(
                        name="name",
                        type="text",
                        placeholder="Your full name",
                        required=True,
                        id="name",
                    ),
                    label="Full Name",
                    label_for="name",
                    required=True,
                ),
            ]
        )

    fields.append(
        field(
            input(
                name="password",
                type="password",
                placeholder="Enter your password",
                required=True,
                id="password",
            ),
            label="Password",
            label_for="password",
            required=True,
        ),
    )

    if not is_login:
        # Confirm password for signup
        fields.append(
            field(
                input(
                    name="confirm_password",
                    type="password",
                    placeholder="Confirm your password",
                    required=True,
                    id="confirm_password",
                ),
                label="Confirm Password",
                label_for="confirm_password",
                required=True,
            ),
        )

    # Submit button
    fields.append(
        button(
            "Sign In" if is_login else "Create Account",
            type="submit",
            variant="solid",
            color_palette="brand",
            size="lg",
            cls="w-full",
        ),
    )

    content.append(
        vstack(
            *fields,
            gap=4,
        )
    )

    # Footer links
    footer_links = []
    if is_login:
        footer_links.append(
            link(
                "Forgot your password?",
                href="/forgot-password",
                cls="text-sm",
            )
        )
    else:
        footer_links.append(
            link(
                "Already have an account? Sign in",
                href="/login",
                cls="text-sm",
            )
        )

    if footer_links:
        content.append(
            P(
                *footer_links,
                cls="text-center text-muted mt-4",
            )
        )

    return Form(
        vstack(*content, gap=4),
        method=method,
        action=action,
        cls="auth-form",
        **kwargs,
    )
