"""LoadingScreen molecule - Full-page loading state."""

from __future__ import annotations

from typing import Any, Literal

from ..atoms import spinner, text, vstack


def loading_screen(
    message: str = "Loading...",
    spinner_size: Literal["sm", "md", "lg"] = "lg",
    spinner_color: str | None = None,  # noqa: ARG001
    **kwargs: Any,
) -> Any:
    """
    Loading screen molecule for full-page loading states.

    Combines Spinner and Text atoms for authentication and app initialization.

    Args:
        message: Message to display with the spinner
        spinner_size: Size of the spinner (sm, md, lg)
        spinner_color: Optional color for the spinner
        **kwargs: Additional HTML attributes

    Returns:
        Div element with centered loading screen

    Example:
        >>> loading_screen("Authenticating...", spinner_size="lg")
    """
    spinner_el = spinner(size=spinner_size)
    message_el = text(message, variant="body", style="color: var(--color-gray-600);")

    return vstack(
        spinner_el,
        message_el,
        gap=4,
        style="align-items: center; justify-content: center; min-height: 100vh;",
        **kwargs,
    )
