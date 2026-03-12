# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1ConnectParams"]


class V1ConnectParams(TypedDict, total=False):
    google_scholar_id: Required[Annotated[str, PropertyInfo(alias="googleScholarId")]]
    """Google Scholar ID"""
