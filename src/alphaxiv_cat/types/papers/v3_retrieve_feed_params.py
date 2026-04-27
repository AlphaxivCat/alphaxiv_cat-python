# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3RetrieveFeedParams"]


class V3RetrieveFeedParams(TypedDict, total=False):
    interval: Required[Literal["3 Days", "7 Days", "30 Days", "90 Days", "All time"]]

    page_num: Required[Annotated[str, PropertyInfo(alias="pageNum")]]

    page_size: Required[Annotated[str, PropertyInfo(alias="pageSize")]]

    sort: Required[Literal["Hot", "Comments", "Views", "Likes", "GitHub", "Twitter (X)", "Recommended"]]

    organizations: str

    source: Literal["GitHub", "Twitter (X)"]

    topics: str

    universal_id: Annotated[str, PropertyInfo(alias="universalId")]
    """A versionless universal paper ID (e.g. 1706.03762)"""
