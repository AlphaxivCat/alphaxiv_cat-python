# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1GenerateSpeechParams"]


class V1GenerateSpeechParams(TypedDict, total=False):
    paper_group_id: Required[Annotated[str, PropertyInfo(alias="paperGroupId")]]
    """Paper group ID for caching"""

    text: Required[str]
    """Text to convert to speech"""
