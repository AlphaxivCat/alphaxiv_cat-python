# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaperViewCountKickoffJobParams"]


class PaperViewCountKickoffJobParams(TypedDict, total=False):
    type: Required[str]
    """Time period filter: 'all' or number of days"""

    like: str
    """Optional filter for likes"""
