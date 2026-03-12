# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1GetStatusResponse"]


class V1GetStatusResponse(BaseModel):
    claimed_papers: float = FieldInfo(alias="claimedPapers")
    """How many papers have been claimed since the current sync started"""

    email_domain: str = FieldInfo(alias="emailDomain")

    errored_papers: float = FieldInfo(alias="erroredPapers")
    """How many papers had an error during processing"""

    google_scholar_id: str = FieldInfo(alias="googleScholarId")

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
