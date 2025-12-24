"""Voice Waveform component - Visual representation of voice data."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...utils import merge_classes


def voice_waveform(
    height: str = "30px",
    width: str = "100%",
    primary_color: str = "var(--theme-primary)",
    secondary_color: str = "var(--theme-secondary)",
    opacity: float = 0.8,
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Render a voice waveform visualization.

    Args:
        height: Height of the visualization
        width: Width of the visualization
        primary_color: Start/End color of gradient
        secondary_color: Middle color of gradient
        opacity: Opacity of the waveform
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Div element containing the waveform
    """
    css_class = merge_classes("voice-waveform", cls)

    style = f"""
        height: {height};
        width: {width};
        background: linear-gradient(90deg, {primary_color} 0%, {secondary_color} 50%, {primary_color} 100%);
        mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20" preserveAspectRatio="none"><path d="M0 10 Q 5 0 10 10 T 20 10 T 30 10 T 40 10 T 50 10 T 60 10 T 70 10 T 80 10 T 90 10 T 100 10" stroke="white" stroke-width="2" fill="none" /></svg>');
        -webkit-mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20" preserveAspectRatio="none"><path d="M0 10 Q 5 20 10 10 T 20 10 T 30 10 T 40 10 T 50 10 T 60 10 T 70 10 T 80 10 T 90 10 T 100 10" stroke="black" stroke-width="20" fill="none" /></svg>');
        opacity: {opacity};
        border-radius: 4px;
    """

    if "style" in kwargs:
        style += kwargs.pop("style")

    return Div(
        style=style,
        cls=css_class,
        **kwargs,
    )
