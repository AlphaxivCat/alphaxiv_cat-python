# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V3RetrieveSimilarPapersResponse",
    "V3RetrieveSimilarPapersResponseItem",
    "V3RetrieveSimilarPapersResponseItemAuthorInfo",
    "V3RetrieveSimilarPapersResponseItemAuthorInfoAvatar",
    "V3RetrieveSimilarPapersResponseItemExternalBlog",
    "V3RetrieveSimilarPapersResponseItemFullAuthor",
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2",
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2Researcher",
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherLinks",
    "V3RetrieveSimilarPapersResponseItemMetrics",
    "V3RetrieveSimilarPapersResponseItemMetricsVisitsCount",
    "V3RetrieveSimilarPapersResponseItemOrganizationInfo",
    "V3RetrieveSimilarPapersResponseItemPaperSummary",
]


class V3RetrieveSimilarPapersResponseItemAuthorInfoAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class V3RetrieveSimilarPapersResponseItemAuthorInfo(BaseModel):
    id: str

    avatar: Optional[List[V3RetrieveSimilarPapersResponseItemAuthorInfoAvatar]] = None

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


class V3RetrieveSimilarPapersResponseItemExternalBlog(BaseModel):
    body_blob_id: str

    cover_blob_id: Optional[str] = None


class V3RetrieveSimilarPapersResponseItemFullAuthor(BaseModel):
    id: str

    full_name: str

    user_id: Optional[str] = None

    username: Optional[str] = None

    researcher_slug: Optional[str] = None


class V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherLinks(BaseModel):
    bluesky: Optional[str] = None

    cv: Optional[str] = None

    dblp: Optional[str] = None

    email: Optional[str] = None

    github: Optional[str] = None

    huggingface: Optional[str] = None

    linkedin: Optional[str] = None

    openreview: Optional[str] = None

    orcid: Optional[str] = None

    personal_site: Optional[str] = FieldInfo(alias="personalSite", default=None)

    scholar: Optional[str] = None

    twitter: Optional[str] = None

    wikipedia: Optional[str] = None


class V3RetrieveSimilarPapersResponseItemFullAuthorsV2Researcher(BaseModel):
    affiliation: Optional[str] = None

    bio: Optional[str] = None

    citations: float

    headline: Optional[str] = None

    h_index: float = FieldInfo(alias="hIndex")

    links: V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherLinks

    name: str

    photo_url: str = FieldInfo(alias="photoUrl")

    research_areas: List[str] = FieldInfo(alias="researchAreas")

    slug: str


class V3RetrieveSimilarPapersResponseItemFullAuthorsV2(BaseModel):
    full_name: str

    researcher: Optional[V3RetrieveSimilarPapersResponseItemFullAuthorsV2Researcher] = None


class V3RetrieveSimilarPapersResponseItemMetricsVisitsCount(BaseModel):
    all: float

    last_7_days: float


class V3RetrieveSimilarPapersResponseItemMetrics(BaseModel):
    public_total_votes: float

    total_votes: float

    visits_count: V3RetrieveSimilarPapersResponseItemMetricsVisitsCount


class V3RetrieveSimilarPapersResponseItemOrganizationInfo(BaseModel):
    image: Optional[str] = None

    name: str


class V3RetrieveSimilarPapersResponseItemPaperSummary(BaseModel):
    key_insights: List[str] = FieldInfo(alias="keyInsights")

    original_problem: List[str] = FieldInfo(alias="originalProblem")

    results: List[str]

    solution: List[str]

    summary: str


class V3RetrieveSimilarPapersResponseItem(BaseModel):
    id: str

    abstract: str

    author_info: List[V3RetrieveSimilarPapersResponseItemAuthorInfo]

    authors: List[str]

    canonical_id: str
    """A versioned paper ID (e.g. 1706.03762v1)"""

    external_blog: Optional[V3RetrieveSimilarPapersResponseItemExternalBlog] = None

    first_publication_date: str

    full_authors: List[V3RetrieveSimilarPapersResponseItemFullAuthor]

    full_authors_v2: List[V3RetrieveSimilarPapersResponseItemFullAuthorsV2]

    github_stars: Optional[float] = None

    github_url: Optional[str] = None

    has_run_report: bool

    image_url: Optional[str] = None

    metrics: V3RetrieveSimilarPapersResponseItemMetrics

    organization_info: List[V3RetrieveSimilarPapersResponseItemOrganizationInfo]

    paper_group_id: str

    paper_summary: Optional[V3RetrieveSimilarPapersResponseItemPaperSummary] = None

    publication_date: str

    title: str

    topics: List[str]

    universal_paper_id: str
    """A versionless universal paper ID (e.g. 1706.03762)"""

    updated_at: str

    version_id: str


V3RetrieveSimilarPapersResponse: TypeAlias = List[V3RetrieveSimilarPapersResponseItem]
