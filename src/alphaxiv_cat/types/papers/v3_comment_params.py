# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["V3CommentParams"]


class V3CommentParams(TypedDict, total=False):
    tag: Required[Literal["anonymous", "general", "personal", "research", "resources"]]

    body: Optional[str]

    parent: Optional[str]

    title: Optional[str]
