# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V2CommentResponse",
    "Annotation",
    "AnnotationAnchorPosition",
    "AnnotationFocusPosition",
    "AnnotationHighlightRect",
    "AnnotationHighlightRectRect",
    "Author",
    "AuthorAvatar",
    "Endorsement",
    "Response",
    "ResponseAnnotation",
    "ResponseAnnotationAnchorPosition",
    "ResponseAnnotationFocusPosition",
    "ResponseAnnotationHighlightRect",
    "ResponseAnnotationHighlightRectRect",
    "ResponseAuthor",
    "ResponseAuthorAvatar",
    "ResponseEndorsement",
]


class AnnotationAnchorPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class AnnotationFocusPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class AnnotationHighlightRectRect(BaseModel):
    x1: float

    x2: float

    y1: float

    y2: float


class AnnotationHighlightRect(BaseModel):
    page_index: float = FieldInfo(alias="pageIndex")

    rects: List[AnnotationHighlightRectRect]


class Annotation(BaseModel):
    anchor_position: AnnotationAnchorPosition = FieldInfo(alias="anchorPosition")

    focus_position: AnnotationFocusPosition = FieldInfo(alias="focusPosition")

    highlight_rects: List[AnnotationHighlightRect] = FieldInfo(alias="highlightRects")

    selected_text: str = FieldInfo(alias="selectedText")

    type: Literal["highlight"]

    highlight_color: Optional[str] = FieldInfo(alias="highlightColor", default=None)


class AuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class Author(BaseModel):
    id: str

    avatar: Optional[List[AuthorAvatar]] = None

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


class Endorsement(BaseModel):
    id: str

    name: str


class ResponseAnnotationAnchorPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class ResponseAnnotationFocusPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class ResponseAnnotationHighlightRectRect(BaseModel):
    x1: float

    x2: float

    y1: float

    y2: float


class ResponseAnnotationHighlightRect(BaseModel):
    page_index: float = FieldInfo(alias="pageIndex")

    rects: List[ResponseAnnotationHighlightRectRect]


class ResponseAnnotation(BaseModel):
    anchor_position: ResponseAnnotationAnchorPosition = FieldInfo(alias="anchorPosition")

    focus_position: ResponseAnnotationFocusPosition = FieldInfo(alias="focusPosition")

    highlight_rects: List[ResponseAnnotationHighlightRect] = FieldInfo(alias="highlightRects")

    selected_text: str = FieldInfo(alias="selectedText")

    type: Literal["highlight"]

    highlight_color: Optional[str] = FieldInfo(alias="highlightColor", default=None)


class ResponseAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class ResponseAuthor(BaseModel):
    id: str

    avatar: Optional[List[ResponseAuthorAvatar]] = None

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


class ResponseEndorsement(BaseModel):
    id: str

    name: str


class Response(BaseModel):
    id: str

    annotation: Optional[ResponseAnnotation] = None

    author: ResponseAuthor

    author_responded: bool = FieldInfo(alias="authorResponded")

    body: Optional[str] = None

    date: str

    endorsements: List[ResponseEndorsement]

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


class V2CommentResponse(BaseModel):
    id: str

    annotation: Optional[Annotation] = None

    author: Author

    author_responded: bool = FieldInfo(alias="authorResponded")

    body: Optional[str] = None

    date: str

    endorsements: List[Endorsement]

    has_downvoted: bool = FieldInfo(alias="hasDownvoted")

    has_flagged: bool = FieldInfo(alias="hasFlagged")

    has_upvoted: bool = FieldInfo(alias="hasUpvoted")

    is_author: bool = FieldInfo(alias="isAuthor")

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    paper_title: str = FieldInfo(alias="paperTitle")

    paper_version_id: str = FieldInfo(alias="paperVersionId")

    responses: List[Response]

    tag: str

    title: Optional[str] = None

    universal_id: str = FieldInfo(alias="universalId")

    upvotes: float

    was_edited: bool = FieldInfo(alias="wasEdited")
