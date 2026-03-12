# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V1GetModeratorFeedResponse",
    "V1GetModeratorFeedResponseItem",
    "V1GetModeratorFeedResponseItemAuthor",
    "V1GetModeratorFeedResponseItemAuthorAvatar",
]


class V1GetModeratorFeedResponseItemAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class V1GetModeratorFeedResponseItemAuthor(BaseModel):
    id: str

    avatar: Optional[List[V1GetModeratorFeedResponseItemAuthorAvatar]] = None

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


class V1GetModeratorFeedResponseItem(BaseModel):
    id: str

    author: V1GetModeratorFeedResponseItemAuthor

    body: str

    date: str

    flag_count: float = FieldInfo(alias="flagCount")

    is_addressed: bool = FieldInfo(alias="isAddressed")

    is_closed: bool = FieldInfo(alias="isClosed")

    is_flag_addressed: bool = FieldInfo(alias="isFlagAddressed")

    paper_title: str = FieldInfo(alias="paperTitle")

    selected_text: Optional[str] = FieldInfo(alias="selectedText", default=None)

    title: Optional[str] = None

    universal_id: str = FieldInfo(alias="universalId")


V1GetModeratorFeedResponse: TypeAlias = List[V1GetModeratorFeedResponseItem]
