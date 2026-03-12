# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1GetModeratorFeedParams"]


class V1GetModeratorFeedParams(TypedDict, total=False):
    feed_type: Annotated[Literal["all", "flagged", "recent"], PropertyInfo(alias="feedType")]

    page: str

    page_size: Annotated[str, PropertyInfo(alias="pageSize")]
