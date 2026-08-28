# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V3RetrieveFeedResponse",
    "Paper",
    "PaperAuthorInfo",
    "PaperAuthorInfoAvatar",
    "PaperExternalBlog",
    "PaperFullAuthor",
    "PaperFullAuthorsV2",
    "PaperFullAuthorsV2Researcher",
    "PaperFullAuthorsV2ResearcherLinkedUser",
    "PaperFullAuthorsV2ResearcherLinks",
    "PaperFullAuthorsV2ResearcherReason",
    "PaperFullAuthorsV2ResearcherReasonUnionMember0",
    "PaperFullAuthorsV2ResearcherReasonKind",
    "PaperFullAuthorsV2ResearcherReasonUnionMember2",
    "PaperFullAuthorsV2ResearcherReasonUnionMember2Followed",
    "PaperMetrics",
    "PaperMetricsVisitsCount",
    "PaperOrganizationInfo",
    "PaperPaperSummary",
    "PaperRecommendationContext",
    "PaperRecommendationContextFollowedAuthor",
    "PaperRecommendationContextFollowedLiker",
    "PaperRecommendationContextFollowedLikerAvatar",
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

    researcher_slug: Optional[str] = FieldInfo(alias="researcherSlug", default=None)

    role: Literal["user", "reviewer", "admin", "bot"]

    username: str

    verified: bool

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)


class PaperExternalBlog(BaseModel):
    body_blob_id: str

    cover_blob_id: Optional[str] = None

    source_name: str

    source_url: str


class PaperFullAuthor(BaseModel):
    id: str

    full_name: str

    user_id: Optional[str] = None

    username: Optional[str] = None

    researcher_slug: Optional[str] = None


class PaperFullAuthorsV2ResearcherLinkedUser(BaseModel):
    name: str

    username: str


class PaperFullAuthorsV2ResearcherLinks(BaseModel):
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


class PaperFullAuthorsV2ResearcherReasonUnionMember0(BaseModel):
    kind: Literal["interest"]

    paper_title: Optional[str] = FieldInfo(alias="paperTitle", default=None)


class PaperFullAuthorsV2ResearcherReasonKind(BaseModel):
    kind: Literal["read"]


class PaperFullAuthorsV2ResearcherReasonUnionMember2Followed(BaseModel):
    name: str

    slug: str


class PaperFullAuthorsV2ResearcherReasonUnionMember2(BaseModel):
    count: float

    kind: Literal["coauthor"]

    followed: Optional[PaperFullAuthorsV2ResearcherReasonUnionMember2Followed] = None


PaperFullAuthorsV2ResearcherReason: TypeAlias = Union[
    PaperFullAuthorsV2ResearcherReasonUnionMember0,
    PaperFullAuthorsV2ResearcherReasonKind,
    PaperFullAuthorsV2ResearcherReasonUnionMember2,
]


class PaperFullAuthorsV2Researcher(BaseModel):
    affiliation: Optional[str] = None

    bio: Optional[str] = None

    citations: float

    headline: Optional[str] = None

    h_index: float = FieldInfo(alias="hIndex")

    linked_user: Optional[PaperFullAuthorsV2ResearcherLinkedUser] = FieldInfo(alias="linkedUser", default=None)

    links: PaperFullAuthorsV2ResearcherLinks

    name: str

    photo_url: str = FieldInfo(alias="photoUrl")

    research_areas: List[str] = FieldInfo(alias="researchAreas")

    slug: str

    reason: Optional[PaperFullAuthorsV2ResearcherReason] = None


class PaperFullAuthorsV2(BaseModel):
    full_name: str

    researcher: Optional[PaperFullAuthorsV2Researcher] = None


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


class PaperRecommendationContextFollowedAuthor(BaseModel):
    name: str

    slug: Optional[str] = None


class PaperRecommendationContextFollowedLikerAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class PaperRecommendationContextFollowedLiker(BaseModel):
    id: str

    avatar: Optional[List[PaperRecommendationContextFollowedLikerAvatar]] = None

    google_scholar_id: Optional[str] = FieldInfo(alias="googleScholarId", default=None)

    institution: Optional[str] = None

    real_name: str = FieldInfo(alias="realName")

    reputation: float

    researcher_slug: Optional[str] = FieldInfo(alias="researcherSlug", default=None)

    username: str

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")


class PaperRecommendationContext(BaseModel):
    followed_authors: Optional[List[PaperRecommendationContextFollowedAuthor]] = None

    followed_likers: Optional[List[PaperRecommendationContextFollowedLiker]] = None

    hot: Optional[bool] = None


class Paper(BaseModel):
    id: str

    abstract: str

    author_info: List[PaperAuthorInfo]

    authors: List[str]

    canonical_id: str
    """A versioned paper ID (e.g. 1706.03762v1)"""

    external_blog: Optional[PaperExternalBlog] = None

    first_publication_date: str

    full_authors: List[PaperFullAuthor]

    full_authors_v2: List[PaperFullAuthorsV2]

    github_stars: Optional[float] = None

    github_url: Optional[str] = None

    has_run_report: bool

    image_url: Optional[str] = None

    metrics: PaperMetrics

    organization_info: List[PaperOrganizationInfo]

    paper_group_id: str

    paper_summary: Optional[PaperPaperSummary] = None

    pdf_only: bool

    publication_date: str

    title: str

    topics: List[str]

    universal_paper_id: str
    """A versionless universal paper ID (e.g. 1706.03762)"""

    updated_at: str

    version_id: str

    card_preview_blob_id: Optional[str] = None

    narration_audio_url: Optional[str] = None

    recommendation_context: Optional[PaperRecommendationContext] = None


class V3RetrieveFeedResponse(BaseModel):
    page: float

    papers: List[Paper]

    feed_cursor: Optional[str] = FieldInfo(alias="feedCursor", default=None)

    feed_refreshed: Optional[bool] = FieldInfo(alias="feedRefreshed", default=None)
