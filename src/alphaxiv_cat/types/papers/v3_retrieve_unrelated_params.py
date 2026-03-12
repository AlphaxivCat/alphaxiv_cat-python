# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V3RetrieveUnrelatedParams"]


class V3RetrieveUnrelatedParams(TypedDict, total=False):
    limit: Required[str]

    papers: Required[str]

    topics: Required[str]
