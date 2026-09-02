# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchGoogleSearchParams"]


class SearchGoogleSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query"""

    link_blogs: Annotated[str, PropertyInfo(alias="linkBlogs")]
