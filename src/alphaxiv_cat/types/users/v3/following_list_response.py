# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FollowingListResponse", "User", "UserAvatar"]


class UserAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class User(BaseModel):
    id: str

    avatar: Optional[List[UserAvatar]] = None

    google_scholar_id: Optional[str] = FieldInfo(alias="googleScholarId", default=None)

    institution: Optional[str] = None

    real_name: str = FieldInfo(alias="realName")

    reputation: float

    username: str

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")


class FollowingListResponse(BaseModel):
    users: List[User]
