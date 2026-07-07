# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V3RetrieveDiversePapersResponse",
    "V3RetrieveDiversePapersResponseItem",
    "V3RetrieveDiversePapersResponseItemAuthorInfo",
    "V3RetrieveDiversePapersResponseItemAuthorInfoAvatar",
    "V3RetrieveDiversePapersResponseItemExternalBlog",
    "V3RetrieveDiversePapersResponseItemFullAuthor",
    "V3RetrieveDiversePapersResponseItemFullAuthorsV2",
    "V3RetrieveDiversePapersResponseItemFullAuthorsV2Researcher",
    "V3RetrieveDiversePapersResponseItemFullAuthorsV2ResearcherLinks",
    "V3RetrieveDiversePapersResponseItemMetrics",
    "V3RetrieveDiversePapersResponseItemMetricsVisitsCount",
    "V3RetrieveDiversePapersResponseItemOrganizationInfo",
    "V3RetrieveDiversePapersResponseItemPaperSummary",
]


class V3RetrieveDiversePapersResponseItemAuthorInfoAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class V3RetrieveDiversePapersResponseItemAuthorInfo(BaseModel):
    id: str

    avatar: Optional[List[V3RetrieveDiversePapersResponseItemAuthorInfoAvatar]] = None

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


class V3RetrieveDiversePapersResponseItemExternalBlog(BaseModel):
    body_blob_id: str

    cover_blob_id: Optional[str] = None


class V3RetrieveDiversePapersResponseItemFullAuthor(BaseModel):
    id: str

    full_name: str

    user_id: Optional[str] = None

    username: Optional[str] = None

    researcher_slug: Optional[str] = None


class V3RetrieveDiversePapersResponseItemFullAuthorsV2ResearcherLinks(BaseModel):
    email: Optional[str] = None

    github: Optional[str] = None

    linkedin: Optional[str] = None

    personal_site: Optional[str] = FieldInfo(alias="personalSite", default=None)

    scholar: Optional[str] = None

    twitter: Optional[str] = None


class V3RetrieveDiversePapersResponseItemFullAuthorsV2Researcher(BaseModel):
    affiliation: Optional[str] = None

    bio: Optional[str] = None

    citations: float

    headline: Optional[str] = None

    h_index: float = FieldInfo(alias="hIndex")

    links: V3RetrieveDiversePapersResponseItemFullAuthorsV2ResearcherLinks

    name: str

    photo_url: str = FieldInfo(alias="photoUrl")

    research_areas: List[str] = FieldInfo(alias="researchAreas")

    slug: str


class V3RetrieveDiversePapersResponseItemFullAuthorsV2(BaseModel):
    full_name: str

    researcher: Optional[V3RetrieveDiversePapersResponseItemFullAuthorsV2Researcher] = None


class V3RetrieveDiversePapersResponseItemMetricsVisitsCount(BaseModel):
    all: float

    last_7_days: float


class V3RetrieveDiversePapersResponseItemMetrics(BaseModel):
    public_total_votes: float

    total_votes: float

    visits_count: V3RetrieveDiversePapersResponseItemMetricsVisitsCount


class V3RetrieveDiversePapersResponseItemOrganizationInfo(BaseModel):
    image: Optional[str] = None

    name: str


class V3RetrieveDiversePapersResponseItemPaperSummary(BaseModel):
    key_insights: List[str] = FieldInfo(alias="keyInsights")

    original_problem: List[str] = FieldInfo(alias="originalProblem")

    results: List[str]

    solution: List[str]

    summary: str


class V3RetrieveDiversePapersResponseItem(BaseModel):
    id: str

    abstract: str

    author_info: List[V3RetrieveDiversePapersResponseItemAuthorInfo]

    authors: List[str]

    canonical_id: str
    """A versioned paper ID (e.g. 1706.03762v1)"""

    external_blog: Optional[V3RetrieveDiversePapersResponseItemExternalBlog] = None

    first_publication_date: str

    full_authors: List[V3RetrieveDiversePapersResponseItemFullAuthor]

    full_authors_v2: List[V3RetrieveDiversePapersResponseItemFullAuthorsV2]

    github_stars: Optional[float] = None

    github_url: Optional[str] = None

    has_run_report: bool

    image_url: Optional[str] = None

    metrics: V3RetrieveDiversePapersResponseItemMetrics

    organization_info: List[V3RetrieveDiversePapersResponseItemOrganizationInfo]

    paper_group_id: str

    paper_summary: Optional[V3RetrieveDiversePapersResponseItemPaperSummary] = None

    publication_date: str

    title: str

    topics: List[str]

    universal_paper_id: str
    """A versionless universal paper ID (e.g. 1706.03762)"""

    updated_at: str

    version_id: str


V3RetrieveDiversePapersResponse: TypeAlias = List[V3RetrieveDiversePapersResponseItem]
