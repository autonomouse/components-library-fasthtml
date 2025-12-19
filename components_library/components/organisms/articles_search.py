"""ArticlesSearch organism - Token-based search interface for articles."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from fasthtml.common import Div, Input, Label, NotStr
from pydantic import BaseModel, Field

from ...design_system.tokens import Colors, Spacing
from ...utils import generate_style_string, merge_classes
from ..atoms import hstack, icon, text, vstack
from ..molecules.token_pill import Token, token_pill

# SVG icons for search interface
_SEARCH_ICON_SVG = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>"""

_STAR_ICON_SVG = """<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>"""


class SearchToken(BaseModel):
    """Represents a selected search token."""

    id: str
    name: str
    type: str | None = None
    description: str | None = None
    operator: Literal["AND", "OR"] = "AND"


class ArticlesSearchState(BaseModel):
    """State for the articles search component."""

    tokens: list[SearchToken] = Field(default_factory=list)
    input_value: str = ""
    is_loading: bool = False


def articles_search(
    tokens: Sequence[SearchToken | dict[str, Any]] | None = None,
    input_value: str = "",
    placeholder: str = "Add token",
    is_loading: bool = False,  # noqa: ARG001 - reserved for future loading state display
    suggestions: Sequence[dict[str, Any]] | None = None,
    show_suggestions: bool = False,
    # Endpoints for HTMX
    suggestions_url: str = "/api/concepts/search",
    add_token_url: str = "/api/search/tokens/add",
    remove_token_url: str = "/api/search/tokens/remove",
    toggle_operator_url: str = "/api/search/tokens/operator",
    search_url: str = "/api/search",
    # Targets
    container_id: str = "articles-search",
    suggestions_target: str = "#concept-suggestions",
    tokens_target: str = "#selected-tokens",
    results_target: str = "#search-results",
    # Options
    debounce_ms: int = 300,
    min_query_length: int = 2,  # noqa: ARG001 - reserved for client-side validation
    cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """
    Token-based search interface for articles.

    Provides a search experience where users can:
    - Type to get autocomplete suggestions from a concepts API
    - Select concepts to add as tokens
    - Toggle logical operators (AND/OR) between tokens
    - Remove tokens
    - Execute search against documents API

    Args:
        tokens: List of selected search tokens
        input_value: Current input field value
        placeholder: Placeholder text for the input
        is_loading: Whether suggestions are loading
        suggestions: List of concept suggestions to display
        show_suggestions: Whether to show the suggestions dropdown
        suggestions_url: HTMX endpoint for fetching suggestions
        add_token_url: HTMX endpoint for adding a token
        remove_token_url: HTMX endpoint for removing a token
        toggle_operator_url: HTMX endpoint for toggling operator
        search_url: HTMX endpoint for executing search
        container_id: ID for the main container
        suggestions_target: Target selector for suggestions
        tokens_target: Target selector for tokens area
        results_target: Target selector for search results
        debounce_ms: Debounce delay for autocomplete
        min_query_length: Minimum characters before fetching suggestions
        cls: Additional CSS classes
        **kwargs: Additional HTML attributes

    Returns:
        Articles search component

    Example:
        >>> articles_search(
        ...     tokens=[
        ...         SearchToken(id="DOID:123", name="Cancer", type="disease"),
        ...     ],
        ...     suggestions_url="/api/concepts/search",
        ...     search_url="/api/documents/search",
        ... )
    """
    colors = Colors()
    spacing = Spacing()

    # Normalize tokens
    normalized_tokens: list[SearchToken] = []
    if tokens:
        for t in tokens:
            if isinstance(t, dict):
                normalized_tokens.append(
                    SearchToken(
                        id=t.get("id", ""),
                        name=t.get("name", ""),
                        type=t.get("type"),
                        description=t.get("description"),
                        operator=t.get("operator", "AND"),
                    )
                )
            else:
                normalized_tokens.append(t)

    css_class = merge_classes("articles-search", cls)

    # Container styles - no border, just the input row
    container_style = generate_style_string(
        background_color=colors.background,
    )

    # Build the component
    return Div(
        # Hidden input to store token data as JSON
        Input(
            type="hidden",
            name="tokens_json",
            id="tokens-json-input",
            value=_serialize_tokens(normalized_tokens),
        ),
        vstack(
            # Tokens area + input + star button
            _build_tokens_input_row(
                tokens=normalized_tokens,
                input_value=input_value,
                placeholder=placeholder,
                suggestions_url=suggestions_url,
                remove_token_url=remove_token_url,
                toggle_operator_url=toggle_operator_url,
                suggestions_target=suggestions_target,
                tokens_target=tokens_target,
                search_url=search_url,
                results_target=results_target,
                debounce_ms=debounce_ms,
                colors=colors,
                spacing=spacing,
            ),
            # Suggestions dropdown
            _build_suggestions_dropdown(
                suggestions=suggestions or [],
                show=show_suggestions,
                add_token_url=add_token_url,
                tokens_target=tokens_target,
                colors=colors,
                spacing=spacing,
            ),
            gap="3",
            align="stretch",
        ),
        id=container_id,
        cls=css_class,
        style=container_style,
        **kwargs,
    )


def _serialize_tokens(tokens: list[SearchToken]) -> str:
    """Serialize tokens to JSON string for form submission."""
    import json

    return json.dumps(
        [
            {
                "id": t.id,
                "name": t.name,
                "type": t.type,
                "description": t.description,
                "operator": t.operator,
            }
            for t in tokens
        ]
    )


def _build_tokens_input_row(
    tokens: list[SearchToken],
    input_value: str,
    placeholder: str,
    suggestions_url: str,
    remove_token_url: str,
    toggle_operator_url: str,
    suggestions_target: str,
    tokens_target: str,
    search_url: str,
    results_target: str,
    debounce_ms: int,
    colors: Colors,
    spacing: Spacing,
) -> Div:
    """Build the tokens display, input row, and search trigger."""
    # Outer container with border - explicit min-height so star button can stretch
    container_style = generate_style_string(
        display="flex",
        align_items="stretch",
        background_color="white",
        border=f"1px solid {colors.border}",
        border_radius="8px",
        overflow="hidden",
        min_height="48px",
    )

    # Inner input area style (flexible, wrapping tokens)
    input_area_style = generate_style_string(
        display="flex",
        flex_wrap="wrap",
        align_items="center",
        gap=spacing._2,
        padding=spacing._3,
        flex="1",
        cursor="text",
    )

    # Search icon style - center vertically within stretched container
    search_icon_style = generate_style_string(
        color=colors.neutral.s400,
        display="flex",
        align_items="center",
        padding_left=spacing._3,
        align_self="center",
    )

    # Build token pills with operators
    token_elements: list[Any] = []
    for idx, token in enumerate(tokens):
        # Add operator toggle before token (except first)
        if idx > 0:
            token_elements.append(
                _build_operator_toggle(
                    token_index=idx,
                    operator=token.operator,
                    toggle_url=toggle_operator_url,
                    tokens_target=tokens_target,
                    colors=colors,
                )
            )

        # Add token pill
        token_elements.append(
            _build_token_pill(
                token=token,
                remove_url=remove_token_url,
                tokens_target=tokens_target,
            )
        )

    # "Add token" placeholder text - plain gray text as visual cue
    add_token_text_style = generate_style_string(
        font_size="0.875rem",
        color=colors.neutral.s400,
        white_space="nowrap",
        padding=f"{spacing._1} {spacing._2}",
    )

    add_token_text = Div(
        placeholder,
        style=add_token_text_style,
        id="add-token-placeholder",
    )

    # Input field - minimal styling, expands to fill remaining space
    input_style = generate_style_string(
        flex="1",
        min_width="60px",
        border="none",
        outline="none",
        font_size="0.875rem",
        background="transparent",
        padding=f"{spacing._1} 0",
    )

    input_element = Input(
        type="text",
        name="q",
        id="concept-search-input",
        value=input_value,
        style=input_style,
        autocomplete="off",
        hx_get=suggestions_url,
        hx_trigger=f"keyup changed delay:{debounce_ms}ms",
        hx_target=suggestions_target,
        hx_swap="innerHTML",
        hx_indicator="#search-loading-indicator",
    )

    # Loading indicator (hidden by default)
    loading_indicator = Div(
        icon("spinner", size="sm"),
        id="search-loading-indicator",
        cls="htmx-indicator",
        style="display: none;",
    )

    # Star button (search trigger) - no height/align-self needed, parent handles stretch
    star_button_style = generate_style_string(
        background_color=colors.primary.s600,
        border="none",
        cursor="pointer",
        padding=f"0 {spacing._4}",
        display="flex",
        align_items="center",
        justify_content="center",
        color="white",
        min_width="48px",
    )

    star_button = Div(
        NotStr(_STAR_ICON_SVG),
        style=star_button_style,
        hx_post=search_url,
        hx_target=results_target,
        hx_swap="innerHTML",
        hx_include="#tokens-json-input",
        hx_indicator="#search-loading-indicator",
        title="Search articles",
        role="button",
        tabindex="0",
    )

    # Search icon
    search_icon = Div(
        NotStr(_SEARCH_ICON_SVG),
        style=search_icon_style,
    )

    # Input area with tokens and "Add token" text
    # Using Label element - clicking anywhere in the area focuses the input
    input_area = Label(
        Div(
            *token_elements,
            id="selected-tokens",
            style="display: inline-flex; flex-wrap: wrap; align-items: center; gap: 0.5rem;",
        ),
        add_token_text,
        input_element,
        loading_indicator,
        style=input_area_style,
        fr="concept-search-input",
    )

    return Div(
        search_icon,
        input_area,
        star_button,
        id="tokens-input-container",
        style=container_style,
    )


def _build_token_pill(
    token: SearchToken,
    remove_url: str,
    tokens_target: str,
) -> Div:
    """Build a single token pill with remove functionality."""
    # All tokens use gray styling for consistency
    pill = token_pill(
        token=Token(
            id=token.id,
            name=token.name,
            type=token.type,
            description=token.description,
        ),
        size="md",
        variant="subtle",
        color_palette="gray",
        closable=True,
        hx_delete=f"{remove_url}?token_id={token.id}",
        hx_target=tokens_target,
        hx_swap="innerHTML",
    )

    return Div(
        pill,
        style="display: inline-flex; align-items: center;",
        data_token_id=token.id,
    )


def _build_operator_toggle(
    token_index: int,
    operator: str,
    toggle_url: str,
    tokens_target: str,
    colors: Colors,
) -> Div:
    """Build an operator toggle button with dropdown arrow."""
    # Different styling for NOT (red) vs AND/OR (gray)
    is_not_operator = operator == "NOT"

    style = generate_style_string(
        padding="0.25rem 0.5rem",
        font_size="0.75rem",
        font_weight="600",
        color="white" if is_not_operator else colors.neutral.s700,
        background_color=colors.error.s600 if is_not_operator else colors.neutral.s100,
        border=f"1px solid {colors.error.s600 if is_not_operator else colors.neutral.s300}",
        border_radius="4px",
        cursor="pointer",
        transition="background-color 0.15s",
        display="inline-flex",
        align_items="center",
        gap="0.25rem",
    )

    # Chevron down SVG for dropdown indicator
    chevron_svg = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>'

    return Div(
        Div(
            operator,
            NotStr(chevron_svg),
            style=style,
            hx_post=f"{toggle_url}?index={token_index}",
            hx_target=tokens_target,
            hx_swap="innerHTML",
            title=f"Toggle operator (currently {operator})",
            role="button",
            tabindex="0",
        ),
        style="display: inline-flex; align-items: center; margin: 0 4px;",
    )


def _build_suggestions_dropdown(
    suggestions: Sequence[dict[str, Any]],
    show: bool,
    add_token_url: str,
    tokens_target: str,
    colors: Colors,
    spacing: Spacing,
) -> Div:
    """Build the suggestions dropdown."""
    dropdown_style = generate_style_string(
        position="absolute",
        top="100%",
        left="0",
        right="0",
        background_color="white",
        border=f"1px solid {colors.border}",
        border_radius="8px",
        box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
        max_height="300px",
        overflow_y="auto",
        z_index="1000",
        display="block" if show and suggestions else "none",
    )

    suggestion_items = []
    for suggestion in suggestions:
        suggestion_items.append(
            _build_suggestion_item(
                suggestion=suggestion,
                add_url=add_token_url,
                tokens_target=tokens_target,
                colors=colors,
                spacing=spacing,
            )
        )

    return Div(
        *suggestion_items,
        id="concept-suggestions",
        style=dropdown_style,
    )


def _build_suggestion_item(
    suggestion: dict[str, Any],
    add_url: str,
    tokens_target: str,
    colors: Colors,
    spacing: Spacing,
) -> Div:
    """Build a single suggestion item."""
    item_style = generate_style_string(
        padding=spacing._3,
        cursor="pointer",
        border_bottom=f"1px solid {colors.neutral.s100}",
        transition="background-color 0.15s",
    )

    concept_id = suggestion.get("id", "")
    concept_name = suggestion.get("name", "")
    concept_type = suggestion.get("type", "")
    description = suggestion.get("description", "")

    # Type badge color
    type_colors = {
        "disease": colors.primary.s100,
        "drug": colors.success.s100,
        "gene": colors.warning.s100,
    }
    type_bg = type_colors.get(concept_type, colors.neutral.s100)

    return Div(
        hstack(
            vstack(
                text(concept_name, weight="semibold", size="sm"),
                text(
                    description[:100] + "..." if len(description) > 100 else description,
                    size="xs",
                    variant="caption",
                )
                if description
                else None,
                gap="1",
                align="start",
            ),
            Div(
                text(concept_type, size="xs"),
                style=generate_style_string(
                    padding="2px 8px",
                    background_color=type_bg,
                    border_radius="9999px",
                    text_transform="capitalize",
                ),
            )
            if concept_type
            else None,
            justify="between",
            align="center",
            style="width: 100%;",
        ),
        style=item_style,
        cls="suggestion-item",
        hx_post=add_url,
        hx_vals=f'{{"id": "{concept_id}", "name": "{concept_name}", "type": "{concept_type}"}}',
        hx_target=tokens_target,
        hx_swap="innerHTML",
    )


def concept_suggestions_partial(
    suggestions: Sequence[dict[str, Any]],
    add_token_url: str = "/api/search/tokens/add",
    tokens_target: str = "#selected-tokens",
) -> Div:
    """
    Partial view for HTMX concept suggestions update.

    Args:
        suggestions: List of concept suggestions
        add_token_url: HTMX endpoint for adding a token
        tokens_target: Target selector for tokens area

    Returns:
        Suggestions dropdown HTML
    """
    colors = Colors()
    spacing = Spacing()

    if not suggestions:
        return Div(
            text("No concepts found", size="sm", variant="caption"),
            style=generate_style_string(
                padding=spacing._3,
                text_align="center",
                color=colors.neutral.s500,
            ),
        )

    suggestion_items = []
    for suggestion in suggestions:
        suggestion_items.append(
            _build_suggestion_item(
                suggestion=suggestion,
                add_url=add_token_url,
                tokens_target=tokens_target,
                colors=colors,
                spacing=spacing,
            )
        )

    dropdown_style = generate_style_string(
        position="absolute",
        top="100%",
        left="0",
        right="0",
        background_color="white",
        border=f"1px solid {colors.border}",
        border_radius="8px",
        box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
        max_height="300px",
        overflow_y="auto",
        z_index="1000",
    )

    return Div(
        *suggestion_items,
        style=dropdown_style,
    )


def selected_tokens_partial(
    tokens: Sequence[SearchToken | dict[str, Any]],
    remove_token_url: str = "/api/search/tokens/remove",
    toggle_operator_url: str = "/api/search/tokens/operator",
    tokens_target: str = "#selected-tokens",
) -> Div:
    """
    Partial view for HTMX selected tokens update.

    Args:
        tokens: List of selected tokens
        remove_token_url: HTMX endpoint for removing a token
        toggle_operator_url: HTMX endpoint for toggling operator
        tokens_target: Target selector for tokens area

    Returns:
        Selected tokens HTML
    """
    colors = Colors()

    # Normalize tokens
    normalized_tokens: list[SearchToken] = []
    for t in tokens:
        if isinstance(t, dict):
            normalized_tokens.append(
                SearchToken(
                    id=t.get("id", ""),
                    name=t.get("name", ""),
                    type=t.get("type"),
                    description=t.get("description"),
                    operator=t.get("operator", "AND"),
                )
            )
        else:
            normalized_tokens.append(t)

    if not normalized_tokens:
        return Div()

    token_elements: list[Any] = []
    for idx, token in enumerate(normalized_tokens):
        # Add operator toggle before token (except first)
        if idx > 0:
            token_elements.append(
                _build_operator_toggle(
                    token_index=idx,
                    operator=token.operator,
                    toggle_url=toggle_operator_url,
                    tokens_target=tokens_target,
                    colors=colors,
                )
            )

        # Add token pill
        token_elements.append(
            _build_token_pill(
                token=token,
                remove_url=remove_token_url,
                tokens_target=tokens_target,
            )
        )

    return Div(*token_elements)
