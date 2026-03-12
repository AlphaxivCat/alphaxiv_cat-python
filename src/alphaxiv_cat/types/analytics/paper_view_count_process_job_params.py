# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PaperViewCountProcessJobParams"]


class PaperViewCountProcessJobParams(TypedDict, total=False):
    paper_id: Required[Annotated[str, PropertyInfo(alias="paperId")]]
    """Paper ID to process view counts for"""

    publication_date: Required[Annotated[str, PropertyInfo(alias="publicationDate")]]
    """Publication date for age decay calculation"""

    like: bool
    """Whether to add noise to votes"""
