"""Feature card for marketing page."""

from __future__ import annotations

from typing import Any

from fasthtml.common import H3, Div, Img, P, Span
from fasthtml.xtend import Style


def feature_card(
    title: str,
    description: str | None = None,
    icon: Any = None,  # Component or string URL
    progress: int | None = None,
    **kwargs: Any,
) -> Div:
    """
    Glassmorphism feature card.

    Args:
        title: Card title.
        description: Optional text description.
        icon: Icon component or URL string.
        progress: Optional integer 0-100 for a progress bar visual.
        **kwargs: Additional HTML attributes.
    """

    card_styles = Style("""
        .feature-card {
            background: var(--theme-card-bg);
            border: 1px solid var(--theme-card-border);
            border-radius: 1rem;
            padding: 2rem;
            text-align: center;
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease, border-color 0.3s ease;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem;
            height: 100%;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            border-color: var(--theme-accent-primary);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .feature-icon-wrapper {
            width: 80px;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 50%;
            margin-bottom: 0.5rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .feature-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--theme-text-primary);
            margin: 0;
        }

        .feature-progress-track {
            width: 100%;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            margin-top: auto;
            overflow: hidden;
        }

        .feature-progress-bar {
            height: 100%;
            background: linear-gradient(90deg, var(--theme-accent-primary), var(--theme-accent-secondary));
            border-radius: 3px;
            width: 0%; /* animate to width */
            transition: width 1s ease-out;
        }

        .neon-border-glow {
            position: absolute;
            inset: 0;
            border-radius: 1rem;
            padding: 1px;
            background: linear-gradient(135deg, transparent 40%, rgba(0, 240, 255, 0.3) 100%);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
        }
    """)

    # Render icon
    icon_el = None
    if isinstance(icon, str):
        # Assume it's a URL or emoji text if simple
        if icon.startswith("http") or icon.startswith("/"):
            icon_el = Img(
                src=icon, alt=title, style="width: 40px; height: 40px; object-fit: contain;"
            )
        else:
            icon_el = Span(icon, style="font-size: 3rem;")
    else:
        icon_el = icon

    # Render progress bar if present
    progress_el = None
    if progress is not None:
        progress_el = Div(
            Div(cls="feature-progress-bar", style=f"width: {progress}%;"),
            cls="feature-progress-track",
        )

    return Div(
        # Top glow border effect
        Div(cls="neon-border-glow"),
        # Icon
        Div(icon_el, cls="feature-icon-wrapper"),
        # Content
        H3(title, cls="feature-title"),
        P(description, style="color: var(--theme-text-secondary); opacity: 0.8;")
        if description
        else None,
        # Progress bar (optional visual candy)
        progress_el,
        card_styles,
        cls="feature-card",
        **kwargs,
    )
