# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserGetPrivateNotesParams"]


class UserGetPrivateNotesParams(TypedDict, total=False):
    limit: str
    """Items per page (default: 10)"""

    page: str
    """Page number (default: 0)"""
