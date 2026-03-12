# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1SyncResponse", "NewPaper", "NewPaperUnionMember0", "NewPaperUnionMember1"]


class NewPaperUnionMember0(BaseModel):
    status: Literal["claimed"]

    title: str

    universal_id: str = FieldInfo(alias="universalId")
    """A versionless universal paper ID (e.g. 1706.03762)"""


class NewPaperUnionMember1(BaseModel):
    google_citation_id: str = FieldInfo(alias="googleCitationId")

    status: Literal["error", "not-found"]

    title: str


NewPaper: TypeAlias = Union[NewPaperUnionMember0, NewPaperUnionMember1]


class V1SyncResponse(BaseModel):
    claimed_papers: float = FieldInfo(alias="claimedPapers")
    """How many papers have been claimed since the current sync started"""

    email_domain: str = FieldInfo(alias="emailDomain")

    errored_papers: float = FieldInfo(alias="erroredPapers")
    """How many papers had an error during processing"""

    google_scholar_id: str = FieldInfo(alias="googleScholarId")

    new_papers: List[NewPaper] = FieldInfo(alias="newPapers")

    not_found_papers: float = FieldInfo(alias="notFoundPapers")
    """How many papers were not found on arXiv"""

    pending_papers: float = FieldInfo(alias="pendingPapers")
    """
    How many papers are ready and will be claimed once the user verifies their email
    """

    remaining_papers: float = FieldInfo(alias="remainingPapers")
    """How many papers have not been processed at all"""

    sync_started_at_date: str = FieldInfo(alias="syncStartedAtDate")

    verified: bool

    email_local_part: Optional[str] = FieldInfo(alias="emailLocalPart", default=None)
