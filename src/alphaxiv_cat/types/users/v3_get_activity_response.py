# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V3GetActivityResponse",
    "V3GetActivityResponseItem",
    "V3GetActivityResponseItemItem",
    "V3GetActivityResponseItemItemAnnotation",
    "V3GetActivityResponseItemItemAnnotationAnchorPosition",
    "V3GetActivityResponseItemItemAnnotationFocusPosition",
    "V3GetActivityResponseItemItemAnnotationHighlightRect",
    "V3GetActivityResponseItemItemAnnotationHighlightRectRect",
    "V3GetActivityResponseItemItemAuthor",
    "V3GetActivityResponseItemItemAuthorAvatar",
    "V3GetActivityResponseItemItemEndorsement",
]


class V3GetActivityResponseItemItemAnnotationAnchorPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class V3GetActivityResponseItemItemAnnotationFocusPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class V3GetActivityResponseItemItemAnnotationHighlightRectRect(BaseModel):
    x1: float

    x2: float

    y1: float

    y2: float


class V3GetActivityResponseItemItemAnnotationHighlightRect(BaseModel):
    page_index: float = FieldInfo(alias="pageIndex")

    rects: List[V3GetActivityResponseItemItemAnnotationHighlightRectRect]


class V3GetActivityResponseItemItemAnnotation(BaseModel):
    anchor_position: V3GetActivityResponseItemItemAnnotationAnchorPosition = FieldInfo(alias="anchorPosition")

    focus_position: V3GetActivityResponseItemItemAnnotationFocusPosition = FieldInfo(alias="focusPosition")

    highlight_rects: List[V3GetActivityResponseItemItemAnnotationHighlightRect] = FieldInfo(alias="highlightRects")

    selected_text: str = FieldInfo(alias="selectedText")

    type: Literal["highlight"]

    color: Optional[str] = None


class V3GetActivityResponseItemItemAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class V3GetActivityResponseItemItemAuthor(BaseModel):
    id: str

    avatar: Optional[List[V3GetActivityResponseItemItemAuthorAvatar]] = None

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


class V3GetActivityResponseItemItemEndorsement(BaseModel):
    id: str

    name: str


class V3GetActivityResponseItemItem(BaseModel):
    id: str

    annotation: Optional[V3GetActivityResponseItemItemAnnotation] = None

    author: V3GetActivityResponseItemItemAuthor

    body: Optional[str] = None

    date: str

    endorsements: List[V3GetActivityResponseItemItemEndorsement]

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


class V3GetActivityResponseItem(BaseModel):
    date: str

    item: V3GetActivityResponseItemItem

    liked: float

    type: Literal["comment"]

    paper_likes: Optional[float] = FieldInfo(alias="paperLikes", default=None)

    paper_publication_date: Optional[str] = FieldInfo(alias="paperPublicationDate", default=None)

    paper_topics: Optional[List[str]] = FieldInfo(alias="paperTopics", default=None)


V3GetActivityResponse: TypeAlias = List[V3GetActivityResponseItem]
