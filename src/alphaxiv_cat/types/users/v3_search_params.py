# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V3SearchParams"]


class V3SearchParams(TypedDict, total=False):
    q: Required[str]

    limit: str
