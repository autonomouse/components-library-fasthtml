"""Stats Chart component - Visual representation of character stats."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...utils import merge_classes


def stats_chart(
    label_top: str = "Agility",
    label_left: str = "Strength",
    label_right: str = "Charisma",
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Render a stats chart visualization (Placeholder Radar Chart).

    Args:
        label_top: Label for top axis
        label_left: Label for left axis
        label_right: Label for right axis
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes
    """
    css_class = merge_classes("stats-chart", cls)

    return Div(
        # The circle
        Div(
            style="width: 150px; height: 150px; margin: 0 auto; border: 2px solid var(--theme-border); border-radius: 50%; opacity: 0.3; position: relative;"
        ),
        # Labels
        Div(
            label_top,
            style="position: absolute; top: 10%; left: 50%; transform: translateX(-50%); font-size: 0.7rem;",
        ),
        Div(
            label_left,
            style="position: absolute; bottom: 10%; left: 30%; font-size: 0.7rem;",
        ),
        Div(
            label_right,
            style="position: absolute; bottom: 10%; right: 30%; font-size: 0.7rem;",
        ),
        cls=merge_classes("relative flex items-center justify-center p-4 mb-4", css_class),
        **kwargs,
    )
