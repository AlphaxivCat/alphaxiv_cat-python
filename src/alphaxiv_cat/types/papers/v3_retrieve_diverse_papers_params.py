# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3RetrieveDiversePapersParams"]


class V3RetrieveDiversePapersParams(TypedDict, total=False):
    topics: Required[str]

    link_blogs: Annotated[str, PropertyInfo(alias="linkBlogs")]
