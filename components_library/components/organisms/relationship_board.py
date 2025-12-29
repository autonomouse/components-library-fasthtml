"""Relationship Board organism - Kanban-style board for managing entity relationships."""

from collections.abc import Sequence
from itertools import groupby
from typing import Any, cast

from fasthtml.common import Div, Option, Select

from ..atoms.avatar import avatar
from ..atoms.button import button
from ..atoms.button_link import button_link
from ..atoms.card import card
from ..atoms.flex import flex
from ..atoms.heading import heading
from ..atoms.icon import icon
from ..atoms.input import input
from ..atoms.stack import vstack
from ..atoms.text import text


def relationship_board(
    items: Sequence[tuple[str, str, str | None, str | None, str | None, str | None]],
    add_url: str | None,
    options: list[tuple[str, str]],
    is_editing: bool = False,
    empty_label: str = "No relationships defined.",
    item_icon: str = "user",
    select_placeholder: str = "Select item...",
    dom_id: str | None = None,
    hidden_inputs: dict[str, str] | None = None,
    verb_field: str = "relationship_verb",
    detail_field: str = "relationship_detail",
    update_url_suffix: str = "/relationship",
) -> Any:
    """
    A Kanban-style board for managing entity relationships grouped by verb.

    This component displays relationships organized into columns by their verb/type,
    with inline add forms that use HTMX for dynamic updates without nested forms.

    Args:
        items: List of tuples (id, name, verb, detail, delete_url, view_url) for each relationship.
               - id: Unique identifier for the related entity
               - name: Display name of the related entity
               - verb: The relationship type (e.g., "Born in", "Knows secret")
               - detail: Optional additional context about the relationship
               - delete_url: HTMX DELETE endpoint to remove this relationship
               - view_url: Optional URL to view the entity details
        add_url: HTMX POST endpoint for adding new relationships.
        options: List of (id, name) tuples for the add dropdown.
        is_editing: Whether to show add/delete controls.
        empty_label: Message shown when no relationships exist and not editing.
        item_icon: Icon name for items (default "user" shows avatar).
        select_placeholder: Placeholder text for the add dropdown.
        dom_id: Unique DOM ID for HTMX targeting (required for add/delete to work).
        hidden_inputs: Optional dictionary of hidden fields to include in the add form.
        verb_field: Name of the form field for the relationship verb (default: "relationship_verb").
        detail_field: Name of the form field for the relationship detail (default: "relationship_detail").
        update_url_suffix: Suffix to append to the delete URL to create the update URL (default: "/relationship").

    Returns:
        A flex container with Kanban-style columns grouped by relationship verb.
    """
    wrapper_kwargs: dict[str, Any] = {"id": dom_id} if dom_id else {}

    if not items and not is_editing:
        return Div(text(empty_label, style="color: var(--theme-text-muted);"), **wrapper_kwargs)

    # Sort and Group - using "Unspecified" for None verbs
    # Note: we are unpacking only the verb (index 2) for sorting/grouping
    sorted_items = sorted(items, key=lambda x: (x[2] if x[2] else "Unspecified"))
    grouped_items = {
        k: list(v)
        for k, v in groupby(sorted_items, key=lambda x: (x[2] if x[2] else "Unspecified"))
    }

    # Helper for a single column
    def board_column(verb_key: str, col_items: list) -> Any:
        is_unspecified = verb_key == "Unspecified"
        display_verb = "General / Unspecified" if is_unspecified else verb_key

        return Div(
            vstack(
                # Header
                flex(
                    heading(
                        display_verb,
                        level=4,
                        style="margin: 0; white-space: nowrap; font-size: 0.95rem; font-weight: 600; color: var(--theme-text-primary);",
                    ),
                    justify="between",
                    align="center",
                    style="padding-bottom: 0.75rem; border-bottom: 1px solid var(--theme-border-subtle); margin-bottom: 0.75rem;",
                    cls="w-full",
                ),
                # Cards
                vstack(
                    *[
                        card(
                            flex(
                                flex(
                                    # Avatar or Icon
                                    avatar(name=item_name, size=32)
                                    if item_icon == "user"
                                    else Div(
                                        icon(
                                            item_icon,
                                            size="sm",
                                            style="color: var(--theme-text-secondary);",
                                        ),
                                        style="width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.05); border-radius: 50%;",
                                    ),
                                    vstack(
                                        text(
                                            item_name,
                                            weight="medium",
                                            size="sm",
                                            style="color: var(--theme-text-primary);",
                                        ),
                                        text(
                                            detail if detail else "No details",
                                            size="xs",
                                            style="color: var(--theme-text-muted); font-size: 0.75rem;",
                                        ),
                                        gap="0.1rem",
                                    ),
                                    gap="0.75rem",
                                    align="center",
                                ),
                                # Actions
                                flex(
                                    # View Link
                                    button_link(
                                        icon("external-link", size="xs"),
                                        href=view_url,
                                        size="xs",
                                        variant="ghost",
                                        style="opacity: 0.5; padding: 0.25rem;",
                                        cls="hover:opacity-100 hover:text-primary",
                                    )
                                    if view_url
                                    else "",
                                    # Delete Button
                                    button(
                                        icon("x", size="xs"),
                                        size="xs",
                                        variant="ghost",
                                        hx_delete=delete_url,
                                        hx_target=f"#{dom_id}" if dom_id else None,
                                        hx_swap="outerHTML" if dom_id else None,
                                        style="opacity: 0.5; padding: 0.25rem;",
                                        cls="hover:opacity-100 hover:bg-red-500/20 hover:text-red-500",
                                    )
                                    if is_editing and delete_url
                                    else "",
                                    gap="0.25rem",
                                    align="center",
                                ),
                                justify="between",
                                align="center",
                                cls="w-full",
                            ),
                            style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 0.75rem;",
                            cls="hover-glow w-full",
                            **{
                                "data-delete-url": delete_url,
                                "data-detail": detail if detail else "",
                            }
                            if is_editing
                            else {},
                        )
                        for _, item_name, _, detail, delete_url, view_url in col_items
                    ],
                    gap="0.5rem",
                    cls="w-full relationship-column",
                    **cast(
                        dict[str, Any],
                        {"data-verb": "" if is_unspecified else verb_key} if is_editing else {},
                    ),
                ),
                # Add Form for this column
                Div(
                    vstack(
                        # Inject Hidden Fields
                        *[
                            input(type="hidden", name=k, value=v)
                            for k, v in (hidden_inputs or {}).items()
                        ],
                        Select(
                            Option(select_placeholder, value="", disabled=True, selected=True),
                            *[Option(opt_name, value=opt_id) for opt_id, opt_name in options],
                            name="target_id",
                            style="width: 100%; background: rgba(0,0,0,0.2); border: 1px solid var(--theme-border-subtle); font-size: 0.8rem; padding: 0.25rem; color: var(--theme-text-primary);",
                        ),
                        input(
                            type="hidden",
                            name=verb_field,
                            value="" if is_unspecified else verb_key,
                        ),
                        input(
                            name=detail_field,
                            placeholder="Details...",
                            style="width: 100%; background: rgba(0,0,0,0.2); border: 1px solid var(--theme-border-subtle); font-size: 0.8rem; padding: 0.25rem; color: var(--theme-text-primary);",
                        ),
                        button(
                            "Add",
                            size="xs",
                            variant="outline",
                            cls="w-full",
                            type="button",
                            hx_post=add_url if add_url else "",
                            hx_target=f"#{dom_id}" if dom_id else None,
                            hx_swap="outerHTML" if dom_id else None,
                            hx_include="closest .rel-form",
                        ),
                        gap="0.5rem",
                    ),
                    style="margin-top: auto; padding-top: 1rem;",
                    cls="rel-form",
                )
                if is_editing and add_url
                else "",
                gap="0rem",
                cls="h-full",
            ),
            style="min-width: 280px; max-width: 320px; background: rgba(0,0,0,0.2); border-radius: 0.75rem; padding: 1rem; backdrop-filter: blur(10px); height: fit-content; max-height: 500px; overflow-y: auto; border: 1px solid rgba(255,255,255,0.05);",
        )

    # New Group Column
    new_group_column = (
        Div(
            vstack(
                flex(
                    Div(
                        icon("plus", size="lg", style="color: var(--theme-accent-primary);"),
                        style="""
                            width: 48px;
                            height: 48px;
                            border-radius: 50%;
                            background: rgba(255, 255, 255, 0.05);
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            border: 1px solid rgba(255, 255, 255, 0.1);
                        """,
                    ),
                    heading(
                        "New Group",
                        level=4,
                        style="color: var(--theme-accent-primary); font-size: 1rem;",
                    ),
                    gap="0.5rem",
                    align="center",
                    justify="center",
                    cls="h-full",
                ),
                Div(
                    vstack(
                        # Inject Hidden Fields
                        *[
                            input(type="hidden", name=k, value=v)
                            for k, v in (hidden_inputs or {}).items()
                        ],
                        input(
                            name=verb_field,
                            placeholder="New Verb (e.g. Exploits)",
                            style="background: rgba(0,0,0,0.2); border: 1px solid var(--theme-border-subtle); color: var(--theme-text-primary);",
                        ),
                        Select(
                            Option(select_placeholder, value="", disabled=True, selected=True),
                            *[Option(opt_name, value=opt_id) for opt_id, opt_name in options],
                            name="target_id",
                            style="background: rgba(0,0,0,0.2); border: 1px solid var(--theme-border-subtle); color: var(--theme-text-primary);",
                        ),
                        button(
                            "Create Group",
                            variant="solid",
                            color="primary",
                            cls="w-full",
                            type="button",
                            hx_post=add_url if add_url else "",
                            hx_target=f"#{dom_id}" if dom_id else None,
                            hx_swap="outerHTML" if dom_id else None,
                            hx_include="closest .rel-form",
                        ),
                        gap="0.75rem",
                    ),
                    style="margin-top: 1rem;",
                    cls="rel-form",
                ),
                justify="center",
                cls="h-full",
            ),
            style="min-width: 280px; background: rgba(0,0,0,0.1); border: 1px dashed var(--theme-border-subtle); border-radius: 0.75rem; padding: 1rem; opacity: 0.7;",
        )
        if is_editing and add_url
        else ""
    )

    columns = [board_column(verb, col_items) for verb, col_items in grouped_items.items()]

    board = flex(
        *columns,
        new_group_column,
        gap="1.5rem",
        style="overflow-x: auto; padding-bottom: 1rem; width: 100%; align-items: flex-start;",
        cls="relationship-board scrollbar-hide",
        **wrapper_kwargs,
    )

    if not is_editing:
        return board

    # SortableJS Script for drag-and-drop support
    # JS Exception: Necessary for drag-and-drop functionality (no pure CSS/HTMX alternative available)
    sortable_script = f"""
    (function() {{
        var CONFIG = {{
            verbField: "{verb_field}",
            detailField: "{detail_field}",
            updateSuffix: "{update_url_suffix}"
        }};

        if (typeof Sortable === 'undefined') {{
            var script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/sortablejs@1.15.0/Sortable.min.js';
            script.onload = initAllBoards;
            document.head.appendChild(script);
        }} else {{
            initAllBoards();
        }}

        function initAllBoards() {{
            // Init on load
            initSortables(document.body);
            // Init on HTMX swap
            document.body.addEventListener('htmx:afterSwap', function(evt) {{
                initSortables(evt.detail.elt);
            }});
        }}

        function initSortables(root) {{
            var columns = root.querySelectorAll('.relationship-column');
            columns.forEach(function(column) {{
                if (column._sortable) return;

                column._sortable = new Sortable(column, {{
                    group: 'relationships', // Allow dragging between columns
                    animation: 150,
                    ghostClass: 'opacity-50',

                    onEnd: function(evt) {{
                        var item = evt.item;
                        var newVerb = evt.to.dataset.verb;

                        // Check if moved to valid column and actually changed
                        if (newVerb === undefined || evt.from === evt.to) return;

                        var deleteUrl = item.dataset.deleteUrl;
                        var detail = item.dataset.detail || "";

                        if (deleteUrl) {{
                            // Construct update URL from delete URL
                            var splitUrl = deleteUrl.split('?');
                            var baseUrl = splitUrl[0];
                            var queryParams = splitUrl[1] || '';

                            var updateUrl = baseUrl + CONFIG.updateSuffix;
                            if (queryParams) updateUrl += '?' + queryParams;

                            // Prepared values
                            var vals = {{}};
                            vals[CONFIG.verbField] = newVerb;
                            vals[CONFIG.detailField] = detail;

                            // Send HTMX request
                            htmx.ajax('POST', updateUrl, {{
                                values: vals,
                                swap: 'none'
                            }});
                        }}
                    }}
                }});
            }});
        }}
    }})();
    """

    from fasthtml.common import Script

    return Div(board, Script(sortable_script))
