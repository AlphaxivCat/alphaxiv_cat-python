# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3KickoffPaperCountriesParams"]


class V3KickoffPaperCountriesParams(TypedDict, total=False):
    batch: float
    """Number of papers to process in each batch"""

    max_papers: Annotated[float, PropertyInfo(alias="maxPapers")]
    """Maximum number of papers to process"""

    months: float
    """Only process papers at least this many months old"""
