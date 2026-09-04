# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V3RetrievePreviewResponse",
    "AuthorInfo",
    "AuthorInfoAvatar",
    "ExternalBlog",
    "FullAuthorsV2",
    "FullAuthorsV2Researcher",
    "FullAuthorsV2ResearcherLinkedUser",
    "FullAuthorsV2ResearcherLinks",
    "FullAuthorsV2ResearcherReason",
    "FullAuthorsV2ResearcherReasonUnionMember0",
    "FullAuthorsV2ResearcherReasonKind",
    "FullAuthorsV2ResearcherReasonUnionMember2",
    "FullAuthorsV2ResearcherReasonUnionMember2Followed",
    "FullAuthorsV2ResearcherReasonUnionMember3",
    "Metrics",
    "MetricsVisitsCount",
    "OrganizationInfo",
    "PaperSummary",
    "ExternalLink",
    "RecommendationContext",
    "RecommendationContextFollowedAuthor",
    "RecommendationContextFollowedLiker",
    "RecommendationContextFollowedLikerAvatar",
]


class AuthorInfoAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class AuthorInfo(BaseModel):
    id: str

    avatar: Optional[List[AuthorInfoAvatar]] = None

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


class ExternalBlog(BaseModel):
    body_blob_id: str

    cover_blob_id: Optional[str] = None

    source_name: str

    source_url: str


class FullAuthorsV2ResearcherLinkedUser(BaseModel):
    name: str

    username: str


class FullAuthorsV2ResearcherLinks(BaseModel):
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


class FullAuthorsV2ResearcherReasonUnionMember0(BaseModel):
    kind: Literal["interest"]

    paper_title: Optional[str] = FieldInfo(alias="paperTitle", default=None)


class FullAuthorsV2ResearcherReasonKind(BaseModel):
    kind: Literal["read"]


class FullAuthorsV2ResearcherReasonUnionMember2Followed(BaseModel):
    name: str

    slug: str


class FullAuthorsV2ResearcherReasonUnionMember2(BaseModel):
    count: float

    kind: Literal["coauthor"]

    followed: Optional[FullAuthorsV2ResearcherReasonUnionMember2Followed] = None


class FullAuthorsV2ResearcherReasonUnionMember3(BaseModel):
    count: float

    kind: Literal["coauthored"]


FullAuthorsV2ResearcherReason: TypeAlias = Union[
    FullAuthorsV2ResearcherReasonUnionMember0,
    FullAuthorsV2ResearcherReasonKind,
    FullAuthorsV2ResearcherReasonUnionMember2,
    FullAuthorsV2ResearcherReasonUnionMember3,
]


class FullAuthorsV2Researcher(BaseModel):
    affiliation: Optional[str] = None

    bio: Optional[str] = None

    citations: float

    headline: Optional[str] = None

    h_index: float = FieldInfo(alias="hIndex")

    linked_user: Optional[FullAuthorsV2ResearcherLinkedUser] = FieldInfo(alias="linkedUser", default=None)

    links: FullAuthorsV2ResearcherLinks

    name: str

    photo_url: str = FieldInfo(alias="photoUrl")

    research_areas: List[str] = FieldInfo(alias="researchAreas")

    slug: str

    reason: Optional[FullAuthorsV2ResearcherReason] = None


class FullAuthorsV2(BaseModel):
    full_name: str

    researcher: Optional[FullAuthorsV2Researcher] = None


class MetricsVisitsCount(BaseModel):
    all: float

    last_7_days: float


class Metrics(BaseModel):
    public_total_votes: float

    total_votes: float

    visits_count: MetricsVisitsCount


class OrganizationInfo(BaseModel):
    image: Optional[str] = None

    name: str


class PaperSummary(BaseModel):
    key_insights: List[str] = FieldInfo(alias="keyInsights")

    original_problem: List[str] = FieldInfo(alias="originalProblem")

    results: List[str]

    solution: List[str]

    summary: str


class ExternalLink(BaseModel):
    cover_blob_id: Optional[str] = None

    source_name: str

    source_url: str


class RecommendationContextFollowedAuthor(BaseModel):
    name: str

    slug: Optional[str] = None


class RecommendationContextFollowedLikerAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class RecommendationContextFollowedLiker(BaseModel):
    id: str

    avatar: Optional[List[RecommendationContextFollowedLikerAvatar]] = None

    google_scholar_id: Optional[str] = FieldInfo(alias="googleScholarId", default=None)

    institution: Optional[str] = None

    real_name: str = FieldInfo(alias="realName")

    reputation: float

    researcher_slug: Optional[str] = FieldInfo(alias="researcherSlug", default=None)

    username: str

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")


class RecommendationContext(BaseModel):
    followed_authors: Optional[List[RecommendationContextFollowedAuthor]] = None

    followed_likers: Optional[List[RecommendationContextFollowedLiker]] = None

    hot: Optional[bool] = None


class V3RetrievePreviewResponse(BaseModel):
    id: str

    abstract: str

    author_info: List[AuthorInfo]

    authors: List[str]

    canonical_id: str
    """A versioned paper ID (e.g. 1706.03762v1)"""

    external_blog: Optional[ExternalBlog] = None

    first_publication_date: str

    full_authors: List[Optional[object]]

    full_authors_v2: List[FullAuthorsV2]

    github_stars: Optional[float] = None

    github_url: Optional[str] = None

    has_run_report: bool

    image_url: Optional[str] = None

    metrics: Metrics

    organization_info: List[OrganizationInfo]

    paper_group_id: str

    paper_summary: Optional[PaperSummary] = None

    pdf_only: bool

    publication_date: str

    title: str

    topics: List[str]

    universal_paper_id: str
    """A versionless universal paper ID (e.g. 1706.03762)"""

    updated_at: str

    version_id: str

    card_preview_blob_id: Optional[str] = None

    external_link: Optional[ExternalLink] = None

    narration_audio_url: Optional[str] = None

    recommendation_context: Optional[RecommendationContext] = None
