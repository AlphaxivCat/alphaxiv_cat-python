# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V3ListResponse",
    "V3ListResponseItem",
    "V3ListResponseItemPaper",
    "V3ListResponseItemPaperAuthor",
    "V3ListResponseItemPaperAuthorsV2",
    "V3ListResponseItemPaperAuthorsV2Researcher",
    "V3ListResponseItemPaperAuthorsV2ResearcherLinks",
    "V3ListResponseItemPaperOrganization",
    "V3ListResponseItemPaperUserAuthor",
    "V3ListResponseItemPaperUserAuthorAvatar",
]


class V3ListResponseItemPaperAuthor(BaseModel):
    id: str

    full_name: str

    user_id: Optional[str] = None

    username: Optional[str] = None


class V3ListResponseItemPaperAuthorsV2ResearcherLinks(BaseModel):
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


class V3ListResponseItemPaperAuthorsV2Researcher(BaseModel):
    affiliation: Optional[str] = None

    bio: Optional[str] = None

    citations: float

    headline: Optional[str] = None

    h_index: float = FieldInfo(alias="hIndex")

    links: V3ListResponseItemPaperAuthorsV2ResearcherLinks

    name: str

    photo_url: str = FieldInfo(alias="photoUrl")

    research_areas: List[str] = FieldInfo(alias="researchAreas")

    slug: str


class V3ListResponseItemPaperAuthorsV2(BaseModel):
    full_name: str

    researcher: Optional[V3ListResponseItemPaperAuthorsV2Researcher] = None


class V3ListResponseItemPaperOrganization(BaseModel):
    image: Optional[str] = None

    name: str


class V3ListResponseItemPaperUserAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class V3ListResponseItemPaperUserAuthor(BaseModel):
    id: str

    avatar: Optional[List[V3ListResponseItemPaperUserAuthorAvatar]] = None

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


class V3ListResponseItemPaper(BaseModel):
    abstract: str

    added_at: str = FieldInfo(alias="addedAt")

    authors: List[V3ListResponseItemPaperAuthor]

    authors_v2: List[V3ListResponseItemPaperAuthorsV2]

    canonical_id: Optional[str] = FieldInfo(alias="canonicalId", default=None)
    """A versioned paper ID (e.g. 1706.03762v1)"""

    citation: Optional[str] = None

    cover_blob_id: Optional[str] = FieldInfo(alias="coverBlobId", default=None)

    is_external_blog: bool = FieldInfo(alias="isExternalBlog")

    organizations: List[V3ListResponseItemPaperOrganization]

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    publication_date: str = FieldInfo(alias="publicationDate")

    title: str

    topics: List[str]

    type: Literal["private", "community", "public"]

    universal_paper_id: str = FieldInfo(alias="universalPaperId")

    user_authors: List[V3ListResponseItemPaperUserAuthor] = FieldInfo(alias="userAuthors")


class V3ListResponseItem(BaseModel):
    id: str

    name: str

    order: float

    papers: List[V3ListResponseItemPaper]

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)

    sharing_status: Literal["not_shared", "shared"] = FieldInfo(alias="sharingStatus")

    type: str


V3ListResponse: TypeAlias = List[V3ListResponseItem]
