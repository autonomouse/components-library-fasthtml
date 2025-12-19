"""Session management utilities for Starlette-based FastHTML applications.

Provides helper functions for managing session data, particularly for
token-based search interfaces. These are pure utility functions with
no dependencies on application-specific configuration.

Usage:
    from components_library.utils import (
        SessionToken,
        get_session_tokens,
        set_session_tokens,
        add_session_token,
        remove_session_token,
        toggle_session_operator,
    )

    # In a route handler
    tokens = get_session_tokens(request)
    tokens = add_session_token(
        request,
        token=SessionToken(id="123", name="BRCA1", type="gene")
    )
"""

from __future__ import annotations

import contextlib
import json
from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel

if TYPE_CHECKING:
    from starlette.requests import Request


class SessionToken(BaseModel):
    """Token stored in user session for search queries.

    This model is compatible with SearchToken from the articles_search
    component, allowing seamless conversion between session storage
    and UI display.

    Attributes:
        id: Unique identifier for the token
        name: Display name of the token
        type: Type of token (e.g., 'disease', 'drug', 'gene', 'freetext')
        description: Optional description or additional context
        operator: Logical operator connecting to previous token
    """

    id: str
    name: str
    type: str | None = None
    description: str | None = None
    operator: Literal["AND", "OR", "NOT"] = "AND"


def get_session_tokens(
    request: Request,
    session_key: str = "search_tokens",
) -> list[SessionToken]:
    """
    Retrieve tokens from the user's session.

    Args:
        request: The Starlette request object containing the session
        session_key: Session key to use for storing tokens

    Returns:
        List of SessionToken objects, empty list if none exist or on parse error
    """
    tokens_json = request.session.get(session_key, "[]")
    with contextlib.suppress(json.JSONDecodeError, ValueError):
        raw_tokens: list[dict] = json.loads(tokens_json)
        return [SessionToken.model_validate(t) for t in raw_tokens]
    return []


def set_session_tokens(
    request: Request,
    tokens: list[SessionToken],
    session_key: str = "search_tokens",
) -> None:
    """
    Save tokens to the user's session.

    Args:
        request: The Starlette request object containing the session
        tokens: List of SessionToken objects to save
        session_key: Session key to use for storing tokens
    """
    tokens_data = [t.model_dump() for t in tokens]
    request.session[session_key] = json.dumps(tokens_data)


def add_session_token(
    request: Request,
    token: SessionToken,
    session_key: str = "search_tokens",
) -> list[SessionToken]:
    """
    Add a new token to the session if it doesn't already exist.

    Args:
        request: The Starlette request object containing the session
        token: SessionToken to add
        session_key: Session key to use for storing tokens

    Returns:
        Updated list of tokens
    """
    tokens = get_session_tokens(request, session_key)

    if not any(t.id == token.id for t in tokens):
        tokens.append(token)
        set_session_tokens(request, tokens, session_key)

    return tokens


def remove_session_token(
    request: Request,
    token_id: str,
    session_key: str = "search_tokens",
) -> list[SessionToken]:
    """
    Remove a token from the session by its ID.

    Args:
        request: The Starlette request object containing the session
        token_id: ID of the token to remove
        session_key: Session key to use for storing tokens

    Returns:
        Updated list of tokens
    """
    tokens = get_session_tokens(request, session_key)
    tokens = [t for t in tokens if t.id != token_id]
    set_session_tokens(request, tokens, session_key)
    return tokens


def toggle_session_operator(
    request: Request,
    index: int,
    session_key: str = "search_tokens",
) -> list[SessionToken]:
    """
    Toggle the operator at a given token index between AND and OR.

    Args:
        request: The Starlette request object containing the session
        index: Index of the token whose operator to toggle (must be > 0)
        session_key: Session key to use for storing tokens

    Returns:
        Updated list of tokens
    """
    tokens = get_session_tokens(request, session_key)

    if 0 < index < len(tokens):
        current_op = tokens[index].operator
        tokens[index].operator = "OR" if current_op == "AND" else "AND"
        set_session_tokens(request, tokens, session_key)

    return tokens


def clear_session_tokens(
    request: Request,
    session_key: str = "search_tokens",
) -> None:
    """
    Clear all tokens from the session.

    Args:
        request: The Starlette request object containing the session
        session_key: Session key to use for storing tokens
    """
    set_session_tokens(request, [], session_key)
