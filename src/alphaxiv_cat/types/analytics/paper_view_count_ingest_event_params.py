# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PaperViewCountIngestEventParams"]


class PaperViewCountIngestEventParams(TypedDict, total=False):
    paper_id: Required[Annotated[str, PropertyInfo(alias="paperId")]]
    """Paper ID to track view for"""

    created_at: Annotated[str, PropertyInfo(alias="createdAt")]
    """Optional timestamp for the view event"""

    user_id: Annotated[Optional[str], PropertyInfo(alias="userId")]
    """Optional user ID who viewed the paper"""
