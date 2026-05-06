# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ByUsernameGetProfilePageResponse",
    "Activity",
    "ActivityItem",
    "ActivityItemAnnotation",
    "ActivityItemAnnotationAnchorPosition",
    "ActivityItemAnnotationFocusPosition",
    "ActivityItemAnnotationHighlightRect",
    "ActivityItemAnnotationHighlightRectRect",
    "ActivityItemAuthor",
    "ActivityItemAuthorAvatar",
    "ActivityItemEndorsement",
    "ClaimedPaper",
    "Featured",
    "FeaturedUnionMember0",
    "FeaturedUnionMember0Data",
    "FeaturedUnionMember1",
    "FeaturedUnionMember1Data",
    "User",
    "UserAvatar",
    "UserSemanticScholar",
    "UserFeatured",
]


class ActivityItemAnnotationAnchorPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class ActivityItemAnnotationFocusPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class ActivityItemAnnotationHighlightRectRect(BaseModel):
    x1: float

    x2: float

    y1: float

    y2: float


class ActivityItemAnnotationHighlightRect(BaseModel):
    page_index: float = FieldInfo(alias="pageIndex")

    rects: List[ActivityItemAnnotationHighlightRectRect]


class ActivityItemAnnotation(BaseModel):
    anchor_position: ActivityItemAnnotationAnchorPosition = FieldInfo(alias="anchorPosition")

    focus_position: ActivityItemAnnotationFocusPosition = FieldInfo(alias="focusPosition")

    highlight_rects: List[ActivityItemAnnotationHighlightRect] = FieldInfo(alias="highlightRects")

    selected_text: str = FieldInfo(alias="selectedText")

    type: Literal["highlight"]

    highlight_color: Optional[str] = FieldInfo(alias="highlightColor", default=None)


class ActivityItemAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class ActivityItemAuthor(BaseModel):
    id: str

    avatar: Optional[List[ActivityItemAuthorAvatar]] = None

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


class ActivityItemEndorsement(BaseModel):
    id: str

    name: str


class ActivityItem(BaseModel):
    id: str

    annotation: Optional[ActivityItemAnnotation] = None

    author: ActivityItemAuthor

    body: Optional[str] = None

    date: str

    endorsements: List[ActivityItemEndorsement]

    has_downvoted: bool = FieldInfo(alias="hasDownvoted")

    has_flagged: bool = FieldInfo(alias="hasFlagged")

    has_upvoted: bool = FieldInfo(alias="hasUpvoted")

    is_author: bool = FieldInfo(alias="isAuthor")

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    paper_title: str = FieldInfo(alias="paperTitle")

    paper_version_id: str = FieldInfo(alias="paperVersionId")

    parent_comment_id: Optional[str] = FieldInfo(alias="parentCommentId", default=None)

    tag: str

    title: Optional[str] = None

    universal_id: str = FieldInfo(alias="universalId")

    upvotes: float

    was_edited: bool = FieldInfo(alias="wasEdited")


class Activity(BaseModel):
    date: str

    item: ActivityItem

    liked: float

    type: Literal["comment"]

    paper_likes: Optional[float] = FieldInfo(alias="paperLikes", default=None)

    paper_publication_date: Optional[str] = FieldInfo(alias="paperPublicationDate", default=None)

    paper_topics: Optional[List[str]] = FieldInfo(alias="paperTopics", default=None)


class ClaimedPaper(BaseModel):
    id: str

    abstract: str

    authors: List[str]

    citations: float

    google_citation_id: Optional[str] = None

    image_url: Optional[str] = FieldInfo(alias="imageURL", default=None)

    paper_id: str
    """A versionless universal paper ID (e.g. 1706.03762)"""

    public_total_votes: float

    publication_date: str

    title: str

    topics: List[str]


class FeaturedUnionMember0Data(BaseModel):
    id: str

    date: str

    link: Optional[str] = None

    organization: Optional[str] = None

    recording: Optional[str] = None

    speaker: Optional[str] = None

    title: str


class FeaturedUnionMember0(BaseModel):
    data: FeaturedUnionMember0Data

    type: Literal["video"]


class FeaturedUnionMember1Data(BaseModel):
    abstract: Optional[str] = None

    publication_date: str

    title: str

    universal_paper_id: str


class FeaturedUnionMember1(BaseModel):
    data: FeaturedUnionMember1Data

    type: Literal["paper"]


Featured: TypeAlias = Union[FeaturedUnionMember0, FeaturedUnionMember1]


class UserAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class UserSemanticScholar(BaseModel):
    id: str

    citation_count: Optional[float] = FieldInfo(alias="citationCount", default=None)

    external_ids: Optional[List[Optional[object]]] = FieldInfo(alias="externalIds", default=None)

    h_index: Optional[float] = FieldInfo(alias="hIndex", default=None)

    homepage: Optional[str] = None

    paper_count: Optional[float] = FieldInfo(alias="paperCount", default=None)


class UserFeatured(BaseModel):
    event_id: Optional[str] = FieldInfo(alias="eventId", default=None)

    paper_version_id: Optional[str] = FieldInfo(alias="paperVersionId", default=None)

    type: Literal["video", "paper"]


class User(BaseModel):
    id: str

    avatar: Optional[List[UserAvatar]] = None

    biography: Optional[str] = None

    bluesky_username: Optional[str] = FieldInfo(alias="blueskyUsername", default=None)

    email: str

    first_login: bool = FieldInfo(alias="firstLogin")

    follower_count: float = FieldInfo(alias="followerCount")

    following_count: float = FieldInfo(alias="followingCount")

    following_topics_count: float = FieldInfo(alias="followingTopicsCount")

    github_username: Optional[str] = FieldInfo(alias="githubUsername", default=None)

    google_scholar_id: Optional[str] = FieldInfo(alias="googleScholarId", default=None)

    institution: Optional[str] = None

    linkedin_username: Optional[str] = FieldInfo(alias="linkedinUsername", default=None)

    location: Optional[str] = None

    orcid_id: Optional[str] = FieldInfo(alias="orcidId", default=None)

    public_email: Optional[str] = FieldInfo(alias="publicEmail", default=None)

    real_name: str = FieldInfo(alias="realName")

    reputation: float

    role: Literal["user", "reviewer", "admin", "bot"]

    semantic_scholar: Optional[UserSemanticScholar] = FieldInfo(alias="semanticScholar", default=None)

    username: str

    verified: bool

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)

    featured: Optional[List[UserFeatured]] = None

    following_organizations: Optional[List[str]] = FieldInfo(alias="followingOrganizations", default=None)


class ByUsernameGetProfilePageResponse(BaseModel):
    activity: List[Activity]

    claimed_papers: List[ClaimedPaper] = FieldInfo(alias="claimedPapers")

    featured: List[Featured]

    user: User
