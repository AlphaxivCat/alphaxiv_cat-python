# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3KickoffPaperFullTextParams"]


class V3KickoffPaperFullTextParams(TypedDict, total=False):
    max_papers: Annotated[float, PropertyInfo(alias="maxPapers")]
    """Maximum number of paper versions to process"""
