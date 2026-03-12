# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3ProcessFullTextParams"]


class V3ProcessFullTextParams(TypedDict, total=False):
    paper_version_id: Required[Annotated[str, PropertyInfo(alias="paperVersionId")]]
    """Paper version ID to process for full text extraction"""
