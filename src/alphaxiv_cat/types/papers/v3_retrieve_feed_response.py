# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V3RetrieveFeedResponse",
    "Paper",
    "PaperAuthorInfo",
    "PaperAuthorInfoAvatar",
    "PaperFullAuthor",
    "PaperMetrics",
    "PaperMetricsVisitsCount",
    "PaperOrganizationInfo",
    "PaperPaperSummary",
]


class PaperAuthorInfoAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class PaperAuthorInfo(BaseModel):
    id: str

    avatar: Optional[List[PaperAuthorInfoAvatar]] = None

    bluesky_username: Optional[str] = FieldInfo(alias="blueskyUsername", default=None)

    github_username: Optional[str] = FieldInfo(alias="githubUsername", default=None)

    google_scholar_id: Optional[str] = FieldInfo(alias="googleScholarId", default=None)

    institution: Optional[str] = None

    linkedin_username: Optional[str] = FieldInfo(alias="linkedinUsername", default=None)

    orcid_id: Optional[str] = FieldInfo(alias="orcidId", default=None)

    public_email: Optional[str] = FieldInfo(alias="publicEmail", default=None)

    real_name: str = FieldInfo(alias="realName")

    reputation: float

    role: Literal["user", "reviewer", "admin", "bot"]

    username: str

    verified: bool

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)


class PaperFullAuthor(BaseModel):
    id: str

    full_name: str

    user_id: Optional[str] = None

    username: Optional[str] = None


class PaperMetricsVisitsCount(BaseModel):
    all: float

    last_7_days: float


class PaperMetrics(BaseModel):
    public_total_votes: float

    total_votes: float

    visits_count: PaperMetricsVisitsCount


class PaperOrganizationInfo(BaseModel):
    image: Optional[str] = None

    name: str


class PaperPaperSummary(BaseModel):
    key_insights: List[str] = FieldInfo(alias="keyInsights")

    original_problem: List[str] = FieldInfo(alias="originalProblem")

    results: List[str]

    solution: List[str]

    summary: str


class Paper(BaseModel):
    id: str

    abstract: str

    author_info: List[PaperAuthorInfo]

    authors: List[str]

    canonical_id: str
    """A versioned paper ID (e.g. 1706.03762v1)"""

    first_publication_date: str

    full_authors: List[PaperFullAuthor]

    github_stars: Optional[float] = None

    github_url: Optional[str] = None

    image_url: Optional[str] = None

    metrics: PaperMetrics

    organization_info: List[PaperOrganizationInfo]

    paper_group_id: str

    paper_summary: Optional[PaperPaperSummary] = None

    publication_date: str

    title: str

    topics: List[str]

    universal_paper_id: str
    """A versionless universal paper ID (e.g. 1706.03762)"""

    updated_at: str

    version_id: str


class V3RetrieveFeedResponse(BaseModel):
    page: float

    papers: List[Paper]
