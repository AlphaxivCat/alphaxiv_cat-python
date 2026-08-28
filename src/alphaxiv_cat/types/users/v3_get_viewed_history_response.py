# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3GetViewedHistoryResponse", "V3GetViewedHistoryResponseItem"]


class V3GetViewedHistoryResponseItem(BaseModel):
    id: str

    abstract: str

    authors: List[str]

    canonical_id: str = FieldInfo(alias="canonicalId")
    """A versioned paper ID (e.g. 1706.03762v1)"""

    cover_blob_id: Optional[str] = FieldInfo(alias="coverBlobId", default=None)

    is_external_blog: bool = FieldInfo(alias="isExternalBlog")

    paper_id: str = FieldInfo(alias="paperId")
    """A versionless universal paper ID (e.g. 1706.03762)"""

    publication_date: str = FieldInfo(alias="publicationDate")

    public_total_votes: float = FieldInfo(alias="publicTotalVotes")

    title: str

    topics: List[str]

    viewed_at: str = FieldInfo(alias="viewedAt")


V3GetViewedHistoryResponse: TypeAlias = List[V3GetViewedHistoryResponseItem]
