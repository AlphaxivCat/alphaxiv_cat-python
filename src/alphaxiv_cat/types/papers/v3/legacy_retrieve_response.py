# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "LegacyRetrieveResponse",
    "Comment",
    "CommentAnnotation",
    "CommentAnnotationAnchorPosition",
    "CommentAnnotationFocusPosition",
    "CommentAnnotationHighlightRect",
    "CommentAnnotationHighlightRectRect",
    "CommentAuthor",
    "CommentAuthorAvatar",
    "CommentEndorsement",
    "CommentResponse",
    "CommentResponseAnnotation",
    "CommentResponseAnnotationAnchorPosition",
    "CommentResponseAnnotationFocusPosition",
    "CommentResponseAnnotationHighlightRect",
    "CommentResponseAnnotationHighlightRectRect",
    "CommentResponseAuthor",
    "CommentResponseAuthorAvatar",
    "CommentResponseEndorsement",
]


class CommentAnnotationAnchorPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class CommentAnnotationFocusPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class CommentAnnotationHighlightRectRect(BaseModel):
    x1: float

    x2: float

    y1: float

    y2: float


class CommentAnnotationHighlightRect(BaseModel):
    page_index: float = FieldInfo(alias="pageIndex")

    rects: List[CommentAnnotationHighlightRectRect]


class CommentAnnotation(BaseModel):
    anchor_position: CommentAnnotationAnchorPosition = FieldInfo(alias="anchorPosition")

    focus_position: CommentAnnotationFocusPosition = FieldInfo(alias="focusPosition")

    highlight_rects: List[CommentAnnotationHighlightRect] = FieldInfo(alias="highlightRects")

    selected_text: str = FieldInfo(alias="selectedText")

    type: Literal["highlight"]

    color: Optional[str] = None


class CommentAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class CommentAuthor(BaseModel):
    id: str

    avatar: Optional[List[CommentAuthorAvatar]] = None

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


class CommentEndorsement(BaseModel):
    id: str

    name: str


class CommentResponseAnnotationAnchorPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class CommentResponseAnnotationFocusPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class CommentResponseAnnotationHighlightRectRect(BaseModel):
    x1: float

    x2: float

    y1: float

    y2: float


class CommentResponseAnnotationHighlightRect(BaseModel):
    page_index: float = FieldInfo(alias="pageIndex")

    rects: List[CommentResponseAnnotationHighlightRectRect]


class CommentResponseAnnotation(BaseModel):
    anchor_position: CommentResponseAnnotationAnchorPosition = FieldInfo(alias="anchorPosition")

    focus_position: CommentResponseAnnotationFocusPosition = FieldInfo(alias="focusPosition")

    highlight_rects: List[CommentResponseAnnotationHighlightRect] = FieldInfo(alias="highlightRects")

    selected_text: str = FieldInfo(alias="selectedText")

    type: Literal["highlight"]

    color: Optional[str] = None


class CommentResponseAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class CommentResponseAuthor(BaseModel):
    id: str

    avatar: Optional[List[CommentResponseAuthorAvatar]] = None

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


class CommentResponseEndorsement(BaseModel):
    id: str

    name: str


class CommentResponse(BaseModel):
    id: str

    annotation: Optional[CommentResponseAnnotation] = None

    author: CommentResponseAuthor

    author_responded: bool = FieldInfo(alias="authorResponded")

    body: Optional[str] = None

    date: str

    endorsements: List[CommentResponseEndorsement]

    has_downvoted: bool = FieldInfo(alias="hasDownvoted")

    has_flagged: bool = FieldInfo(alias="hasFlagged")

    has_upvoted: bool = FieldInfo(alias="hasUpvoted")

    is_author: bool = FieldInfo(alias="isAuthor")

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    paper_title: str = FieldInfo(alias="paperTitle")

    paper_version_id: str = FieldInfo(alias="paperVersionId")

    tag: str

    title: Optional[str] = None

    universal_id: str = FieldInfo(alias="universalId")

    upvotes: float

    was_edited: bool = FieldInfo(alias="wasEdited")


class Comment(BaseModel):
    id: str

    annotation: Optional[CommentAnnotation] = None

    author: CommentAuthor

    author_responded: bool = FieldInfo(alias="authorResponded")

    body: Optional[str] = None

    date: str

    endorsements: List[CommentEndorsement]

    has_downvoted: bool = FieldInfo(alias="hasDownvoted")

    has_flagged: bool = FieldInfo(alias="hasFlagged")

    has_upvoted: bool = FieldInfo(alias="hasUpvoted")

    is_author: bool = FieldInfo(alias="isAuthor")

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    paper_title: str = FieldInfo(alias="paperTitle")

    paper_version_id: str = FieldInfo(alias="paperVersionId")

    responses: List[CommentResponse]

    tag: str

    title: Optional[str] = None

    universal_id: str = FieldInfo(alias="universalId")

    upvotes: float

    was_edited: bool = FieldInfo(alias="wasEdited")


class LegacyRetrieveResponse(BaseModel):
    comments: List[Comment]

    paper: Optional[object] = None
