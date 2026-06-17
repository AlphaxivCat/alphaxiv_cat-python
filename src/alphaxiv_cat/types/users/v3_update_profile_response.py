# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3UpdateProfileResponse", "Avatar", "SemanticScholar", "Featured"]


class Avatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class SemanticScholar(BaseModel):
    id: str

    citation_count: Optional[float] = FieldInfo(alias="citationCount", default=None)

    external_ids: Optional[List[Optional[object]]] = FieldInfo(alias="externalIds", default=None)

    h_index: Optional[float] = FieldInfo(alias="hIndex", default=None)

    homepage: Optional[str] = None

    paper_count: Optional[float] = FieldInfo(alias="paperCount", default=None)


class Featured(BaseModel):
    event_id: Optional[str] = FieldInfo(alias="eventId", default=None)

    paper_version_id: Optional[str] = FieldInfo(alias="paperVersionId", default=None)

    type: Literal["video", "paper"]


class V3UpdateProfileResponse(BaseModel):
    id: str

    avatar: Optional[List[Avatar]] = None

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

    semantic_scholar: Optional[SemanticScholar] = FieldInfo(alias="semanticScholar", default=None)

    username: str

    verified: bool

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)

    featured: Optional[List[Featured]] = None

    following_organizations: Optional[List[str]] = FieldInfo(alias="followingOrganizations", default=None)
