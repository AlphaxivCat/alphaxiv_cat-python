# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3GetClaimedPapersResponse", "V3GetClaimedPapersResponseItem"]


class V3GetClaimedPapersResponseItem(BaseModel):
    id: str

    abstract: str

    authors: List[str]

    canonical_id: str = FieldInfo(alias="canonicalId")
    """A versioned paper ID (e.g. 1706.03762v1)"""

    citations: float

    google_citation_id: Optional[str] = None

    is_external_blog: bool = FieldInfo(alias="isExternalBlog")

    paper_id: str
    """A versionless universal paper ID (e.g. 1706.03762)"""

    public_total_votes: float

    publication_date: str

    title: str

    topics: List[str]


V3GetClaimedPapersResponse: TypeAlias = List[V3GetClaimedPapersResponseItem]
