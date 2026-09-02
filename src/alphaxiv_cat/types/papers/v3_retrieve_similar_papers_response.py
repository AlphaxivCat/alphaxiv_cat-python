# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
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
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherLinkedUser",
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherLinks",
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReason",
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember0",
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonKind",
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember2",
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember2Followed",
    "V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember3",
    "V3RetrieveSimilarPapersResponseItemMetrics",
    "V3RetrieveSimilarPapersResponseItemMetricsVisitsCount",
    "V3RetrieveSimilarPapersResponseItemOrganizationInfo",
    "V3RetrieveSimilarPapersResponseItemPaperSummary",
    "V3RetrieveSimilarPapersResponseItemExternalLink",
    "V3RetrieveSimilarPapersResponseItemRecommendationContext",
    "V3RetrieveSimilarPapersResponseItemRecommendationContextFollowedAuthor",
    "V3RetrieveSimilarPapersResponseItemRecommendationContextFollowedLiker",
    "V3RetrieveSimilarPapersResponseItemRecommendationContextFollowedLikerAvatar",
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

    researcher_slug: Optional[str] = FieldInfo(alias="researcherSlug", default=None)

    role: Literal["user", "reviewer", "admin", "bot"]

    username: str

    verified: bool

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)


class V3RetrieveSimilarPapersResponseItemExternalBlog(BaseModel):
    body_blob_id: str

    cover_blob_id: Optional[str] = None

    source_name: str

    source_url: str


class V3RetrieveSimilarPapersResponseItemFullAuthor(BaseModel):
    id: str

    full_name: str

    user_id: Optional[str] = None

    username: Optional[str] = None

    researcher_slug: Optional[str] = None


class V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherLinkedUser(BaseModel):
    name: str

    username: str


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


class V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember0(BaseModel):
    kind: Literal["interest"]

    paper_title: Optional[str] = FieldInfo(alias="paperTitle", default=None)


class V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonKind(BaseModel):
    kind: Literal["read"]


class V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember2Followed(BaseModel):
    name: str

    slug: str


class V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember2(BaseModel):
    count: float

    kind: Literal["coauthor"]

    followed: Optional[V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember2Followed] = None


class V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember3(BaseModel):
    count: float

    kind: Literal["coauthored"]


V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReason: TypeAlias = Union[
    V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember0,
    V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonKind,
    V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember2,
    V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReasonUnionMember3,
]


class V3RetrieveSimilarPapersResponseItemFullAuthorsV2Researcher(BaseModel):
    affiliation: Optional[str] = None

    bio: Optional[str] = None

    citations: float

    headline: Optional[str] = None

    h_index: float = FieldInfo(alias="hIndex")

    linked_user: Optional[V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherLinkedUser] = FieldInfo(
        alias="linkedUser", default=None
    )

    links: V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherLinks

    name: str

    photo_url: str = FieldInfo(alias="photoUrl")

    research_areas: List[str] = FieldInfo(alias="researchAreas")

    slug: str

    reason: Optional[V3RetrieveSimilarPapersResponseItemFullAuthorsV2ResearcherReason] = None


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


class V3RetrieveSimilarPapersResponseItemExternalLink(BaseModel):
    cover_blob_id: Optional[str] = None

    source_name: str

    source_url: str


class V3RetrieveSimilarPapersResponseItemRecommendationContextFollowedAuthor(BaseModel):
    name: str

    slug: Optional[str] = None


class V3RetrieveSimilarPapersResponseItemRecommendationContextFollowedLikerAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class V3RetrieveSimilarPapersResponseItemRecommendationContextFollowedLiker(BaseModel):
    id: str

    avatar: Optional[List[V3RetrieveSimilarPapersResponseItemRecommendationContextFollowedLikerAvatar]] = None

    google_scholar_id: Optional[str] = FieldInfo(alias="googleScholarId", default=None)

    institution: Optional[str] = None

    real_name: str = FieldInfo(alias="realName")

    reputation: float

    researcher_slug: Optional[str] = FieldInfo(alias="researcherSlug", default=None)

    username: str

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")


class V3RetrieveSimilarPapersResponseItemRecommendationContext(BaseModel):
    followed_authors: Optional[List[V3RetrieveSimilarPapersResponseItemRecommendationContextFollowedAuthor]] = None

    followed_likers: Optional[List[V3RetrieveSimilarPapersResponseItemRecommendationContextFollowedLiker]] = None

    hot: Optional[bool] = None


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

    pdf_only: bool

    publication_date: str

    title: str

    topics: List[str]

    universal_paper_id: str
    """A versionless universal paper ID (e.g. 1706.03762)"""

    updated_at: str

    version_id: str

    card_preview_blob_id: Optional[str] = None

    external_link: Optional[V3RetrieveSimilarPapersResponseItemExternalLink] = None

    narration_audio_url: Optional[str] = None

    recommendation_context: Optional[V3RetrieveSimilarPapersResponseItemRecommendationContext] = None


V3RetrieveSimilarPapersResponse: TypeAlias = List[V3RetrieveSimilarPapersResponseItem]
