# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3RetrieveSimilarPapersParams"]


class V3RetrieveSimilarPapersParams(TypedDict, total=False):
    exclude: str

    exclude_likes: Annotated[Literal["false", "true"], PropertyInfo(alias="excludeLikes")]

    interval: Literal["3 Days", "7 Days", "30 Days", "90 Days", "All time"]

    limit: str
