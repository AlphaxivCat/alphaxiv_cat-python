# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "LegacyRetrieveCommentsResponse",
    "LegacyRetrieveCommentsResponseItem",
    "LegacyRetrieveCommentsResponseItemAnnotation",
    "LegacyRetrieveCommentsResponseItemAnnotationAnchorPosition",
    "LegacyRetrieveCommentsResponseItemAnnotationFocusPosition",
    "LegacyRetrieveCommentsResponseItemAnnotationHighlightRect",
    "LegacyRetrieveCommentsResponseItemAnnotationHighlightRectRect",
    "LegacyRetrieveCommentsResponseItemAuthor",
    "LegacyRetrieveCommentsResponseItemAuthorAvatar",
    "LegacyRetrieveCommentsResponseItemEndorsement",
    "LegacyRetrieveCommentsResponseItemResponse",
    "LegacyRetrieveCommentsResponseItemResponseAnnotation",
    "LegacyRetrieveCommentsResponseItemResponseAnnotationAnchorPosition",
    "LegacyRetrieveCommentsResponseItemResponseAnnotationFocusPosition",
    "LegacyRetrieveCommentsResponseItemResponseAnnotationHighlightRect",
    "LegacyRetrieveCommentsResponseItemResponseAnnotationHighlightRectRect",
    "LegacyRetrieveCommentsResponseItemResponseAuthor",
    "LegacyRetrieveCommentsResponseItemResponseAuthorAvatar",
    "LegacyRetrieveCommentsResponseItemResponseEndorsement",
]


class LegacyRetrieveCommentsResponseItemAnnotationAnchorPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class LegacyRetrieveCommentsResponseItemAnnotationFocusPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class LegacyRetrieveCommentsResponseItemAnnotationHighlightRectRect(BaseModel):
    x1: float

    x2: float

    y1: float

    y2: float


class LegacyRetrieveCommentsResponseItemAnnotationHighlightRect(BaseModel):
    page_index: float = FieldInfo(alias="pageIndex")

    rects: List[LegacyRetrieveCommentsResponseItemAnnotationHighlightRectRect]


class LegacyRetrieveCommentsResponseItemAnnotation(BaseModel):
    anchor_position: LegacyRetrieveCommentsResponseItemAnnotationAnchorPosition = FieldInfo(alias="anchorPosition")

    focus_position: LegacyRetrieveCommentsResponseItemAnnotationFocusPosition = FieldInfo(alias="focusPosition")

    highlight_rects: List[LegacyRetrieveCommentsResponseItemAnnotationHighlightRect] = FieldInfo(alias="highlightRects")

    selected_text: str = FieldInfo(alias="selectedText")

    type: Literal["highlight"]

    color: Optional[str] = None


class LegacyRetrieveCommentsResponseItemAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class LegacyRetrieveCommentsResponseItemAuthor(BaseModel):
    id: str

    avatar: Optional[List[LegacyRetrieveCommentsResponseItemAuthorAvatar]] = None

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


class LegacyRetrieveCommentsResponseItemEndorsement(BaseModel):
    id: str

    name: str


class LegacyRetrieveCommentsResponseItemResponseAnnotationAnchorPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class LegacyRetrieveCommentsResponseItemResponseAnnotationFocusPosition(BaseModel):
    offset: float

    page_index: float = FieldInfo(alias="pageIndex")

    span_index: float = FieldInfo(alias="spanIndex")


class LegacyRetrieveCommentsResponseItemResponseAnnotationHighlightRectRect(BaseModel):
    x1: float

    x2: float

    y1: float

    y2: float


class LegacyRetrieveCommentsResponseItemResponseAnnotationHighlightRect(BaseModel):
    page_index: float = FieldInfo(alias="pageIndex")

    rects: List[LegacyRetrieveCommentsResponseItemResponseAnnotationHighlightRectRect]


class LegacyRetrieveCommentsResponseItemResponseAnnotation(BaseModel):
    anchor_position: LegacyRetrieveCommentsResponseItemResponseAnnotationAnchorPosition = FieldInfo(
        alias="anchorPosition"
    )

    focus_position: LegacyRetrieveCommentsResponseItemResponseAnnotationFocusPosition = FieldInfo(alias="focusPosition")

    highlight_rects: List[LegacyRetrieveCommentsResponseItemResponseAnnotationHighlightRect] = FieldInfo(
        alias="highlightRects"
    )

    selected_text: str = FieldInfo(alias="selectedText")

    type: Literal["highlight"]

    color: Optional[str] = None


class LegacyRetrieveCommentsResponseItemResponseAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class LegacyRetrieveCommentsResponseItemResponseAuthor(BaseModel):
    id: str

    avatar: Optional[List[LegacyRetrieveCommentsResponseItemResponseAuthorAvatar]] = None

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


class LegacyRetrieveCommentsResponseItemResponseEndorsement(BaseModel):
    id: str

    name: str


class LegacyRetrieveCommentsResponseItemResponse(BaseModel):
    id: str

    annotation: Optional[LegacyRetrieveCommentsResponseItemResponseAnnotation] = None

    author: LegacyRetrieveCommentsResponseItemResponseAuthor

    author_responded: bool = FieldInfo(alias="authorResponded")

    body: Optional[str] = None

    date: str

    endorsements: List[LegacyRetrieveCommentsResponseItemResponseEndorsement]

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


class LegacyRetrieveCommentsResponseItem(BaseModel):
    id: str

    annotation: Optional[LegacyRetrieveCommentsResponseItemAnnotation] = None

    author: LegacyRetrieveCommentsResponseItemAuthor

    author_responded: bool = FieldInfo(alias="authorResponded")

    body: Optional[str] = None

    date: str

    endorsements: List[LegacyRetrieveCommentsResponseItemEndorsement]

    has_downvoted: bool = FieldInfo(alias="hasDownvoted")

    has_flagged: bool = FieldInfo(alias="hasFlagged")

    has_upvoted: bool = FieldInfo(alias="hasUpvoted")

    is_author: bool = FieldInfo(alias="isAuthor")

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    paper_title: str = FieldInfo(alias="paperTitle")

    paper_version_id: str = FieldInfo(alias="paperVersionId")

    responses: List[LegacyRetrieveCommentsResponseItemResponse]

    tag: str

    title: Optional[str] = None

    universal_id: str = FieldInfo(alias="universalId")

    upvotes: float

    was_edited: bool = FieldInfo(alias="wasEdited")


LegacyRetrieveCommentsResponse: TypeAlias = List[LegacyRetrieveCommentsResponseItem]
