# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ArchiveListParams"]


class ArchiveListParams(TypedDict, total=False):
    before: str
    """Decimal UNIX time in milliseconds"""
