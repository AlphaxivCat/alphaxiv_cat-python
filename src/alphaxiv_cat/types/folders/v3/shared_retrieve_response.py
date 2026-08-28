# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "SharedRetrieveResponse",
    "ChildFolder",
    "ChildFolderPaper",
    "ChildFolderPaperAuthor",
    "ChildFolderPaperAuthorsV2",
    "ChildFolderPaperAuthorsV2Researcher",
    "ChildFolderPaperAuthorsV2ResearcherLinkedUser",
    "ChildFolderPaperAuthorsV2ResearcherLinks",
    "ChildFolderPaperAuthorsV2ResearcherReason",
    "ChildFolderPaperAuthorsV2ResearcherReasonUnionMember0",
    "ChildFolderPaperAuthorsV2ResearcherReasonKind",
    "ChildFolderPaperAuthorsV2ResearcherReasonUnionMember2",
    "ChildFolderPaperAuthorsV2ResearcherReasonUnionMember2Followed",
    "ChildFolderPaperOrganization",
    "ChildFolderPaperUserAuthor",
    "ChildFolderPaperUserAuthorAvatar",
    "Folder",
    "FolderPaper",
    "FolderPaperAuthor",
    "FolderPaperAuthorsV2",
    "FolderPaperAuthorsV2Researcher",
    "FolderPaperAuthorsV2ResearcherLinkedUser",
    "FolderPaperAuthorsV2ResearcherLinks",
    "FolderPaperAuthorsV2ResearcherReason",
    "FolderPaperAuthorsV2ResearcherReasonUnionMember0",
    "FolderPaperAuthorsV2ResearcherReasonKind",
    "FolderPaperAuthorsV2ResearcherReasonUnionMember2",
    "FolderPaperAuthorsV2ResearcherReasonUnionMember2Followed",
    "FolderPaperOrganization",
    "FolderPaperUserAuthor",
    "FolderPaperUserAuthorAvatar",
]


class ChildFolderPaperAuthor(BaseModel):
    id: str

    full_name: str

    user_id: Optional[str] = None

    username: Optional[str] = None


class ChildFolderPaperAuthorsV2ResearcherLinkedUser(BaseModel):
    name: str

    username: str


class ChildFolderPaperAuthorsV2ResearcherLinks(BaseModel):
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


class ChildFolderPaperAuthorsV2ResearcherReasonUnionMember0(BaseModel):
    kind: Literal["interest"]

    paper_title: Optional[str] = FieldInfo(alias="paperTitle", default=None)


class ChildFolderPaperAuthorsV2ResearcherReasonKind(BaseModel):
    kind: Literal["read"]


class ChildFolderPaperAuthorsV2ResearcherReasonUnionMember2Followed(BaseModel):
    name: str

    slug: str


class ChildFolderPaperAuthorsV2ResearcherReasonUnionMember2(BaseModel):
    count: float

    kind: Literal["coauthor"]

    followed: Optional[ChildFolderPaperAuthorsV2ResearcherReasonUnionMember2Followed] = None


ChildFolderPaperAuthorsV2ResearcherReason: TypeAlias = Union[
    ChildFolderPaperAuthorsV2ResearcherReasonUnionMember0,
    ChildFolderPaperAuthorsV2ResearcherReasonKind,
    ChildFolderPaperAuthorsV2ResearcherReasonUnionMember2,
]


class ChildFolderPaperAuthorsV2Researcher(BaseModel):
    affiliation: Optional[str] = None

    bio: Optional[str] = None

    citations: float

    headline: Optional[str] = None

    h_index: float = FieldInfo(alias="hIndex")

    linked_user: Optional[ChildFolderPaperAuthorsV2ResearcherLinkedUser] = FieldInfo(alias="linkedUser", default=None)

    links: ChildFolderPaperAuthorsV2ResearcherLinks

    name: str

    photo_url: str = FieldInfo(alias="photoUrl")

    research_areas: List[str] = FieldInfo(alias="researchAreas")

    slug: str

    reason: Optional[ChildFolderPaperAuthorsV2ResearcherReason] = None


class ChildFolderPaperAuthorsV2(BaseModel):
    full_name: str

    researcher: Optional[ChildFolderPaperAuthorsV2Researcher] = None


class ChildFolderPaperOrganization(BaseModel):
    image: Optional[str] = None

    name: str


class ChildFolderPaperUserAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class ChildFolderPaperUserAuthor(BaseModel):
    id: str

    avatar: Optional[List[ChildFolderPaperUserAuthorAvatar]] = None

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


class ChildFolderPaper(BaseModel):
    abstract: str

    added_at: str = FieldInfo(alias="addedAt")

    authors: List[ChildFolderPaperAuthor]

    authors_v2: List[ChildFolderPaperAuthorsV2]

    canonical_id: Optional[str] = FieldInfo(alias="canonicalId", default=None)
    """A versioned paper ID (e.g. 1706.03762v1)"""

    citation: Optional[str] = None

    cover_blob_id: Optional[str] = FieldInfo(alias="coverBlobId", default=None)

    is_external_blog: bool = FieldInfo(alias="isExternalBlog")

    organizations: List[ChildFolderPaperOrganization]

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    publication_date: str = FieldInfo(alias="publicationDate")

    title: str

    topics: List[str]

    type: Literal["private", "public"]

    universal_paper_id: str = FieldInfo(alias="universalPaperId")

    user_authors: List[ChildFolderPaperUserAuthor] = FieldInfo(alias="userAuthors")

    votes: float


class ChildFolder(BaseModel):
    id: str

    name: str

    order: float

    papers: List[ChildFolderPaper]

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)

    sharing_status: Literal["not_shared", "shared"] = FieldInfo(alias="sharingStatus")

    type: str


class FolderPaperAuthor(BaseModel):
    id: str

    full_name: str

    user_id: Optional[str] = None

    username: Optional[str] = None


class FolderPaperAuthorsV2ResearcherLinkedUser(BaseModel):
    name: str

    username: str


class FolderPaperAuthorsV2ResearcherLinks(BaseModel):
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


class FolderPaperAuthorsV2ResearcherReasonUnionMember0(BaseModel):
    kind: Literal["interest"]

    paper_title: Optional[str] = FieldInfo(alias="paperTitle", default=None)


class FolderPaperAuthorsV2ResearcherReasonKind(BaseModel):
    kind: Literal["read"]


class FolderPaperAuthorsV2ResearcherReasonUnionMember2Followed(BaseModel):
    name: str

    slug: str


class FolderPaperAuthorsV2ResearcherReasonUnionMember2(BaseModel):
    count: float

    kind: Literal["coauthor"]

    followed: Optional[FolderPaperAuthorsV2ResearcherReasonUnionMember2Followed] = None


FolderPaperAuthorsV2ResearcherReason: TypeAlias = Union[
    FolderPaperAuthorsV2ResearcherReasonUnionMember0,
    FolderPaperAuthorsV2ResearcherReasonKind,
    FolderPaperAuthorsV2ResearcherReasonUnionMember2,
]


class FolderPaperAuthorsV2Researcher(BaseModel):
    affiliation: Optional[str] = None

    bio: Optional[str] = None

    citations: float

    headline: Optional[str] = None

    h_index: float = FieldInfo(alias="hIndex")

    linked_user: Optional[FolderPaperAuthorsV2ResearcherLinkedUser] = FieldInfo(alias="linkedUser", default=None)

    links: FolderPaperAuthorsV2ResearcherLinks

    name: str

    photo_url: str = FieldInfo(alias="photoUrl")

    research_areas: List[str] = FieldInfo(alias="researchAreas")

    slug: str

    reason: Optional[FolderPaperAuthorsV2ResearcherReason] = None


class FolderPaperAuthorsV2(BaseModel):
    full_name: str

    researcher: Optional[FolderPaperAuthorsV2Researcher] = None


class FolderPaperOrganization(BaseModel):
    image: Optional[str] = None

    name: str


class FolderPaperUserAuthorAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class FolderPaperUserAuthor(BaseModel):
    id: str

    avatar: Optional[List[FolderPaperUserAuthorAvatar]] = None

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


class FolderPaper(BaseModel):
    abstract: str

    added_at: str = FieldInfo(alias="addedAt")

    authors: List[FolderPaperAuthor]

    authors_v2: List[FolderPaperAuthorsV2]

    canonical_id: Optional[str] = FieldInfo(alias="canonicalId", default=None)
    """A versioned paper ID (e.g. 1706.03762v1)"""

    citation: Optional[str] = None

    cover_blob_id: Optional[str] = FieldInfo(alias="coverBlobId", default=None)

    is_external_blog: bool = FieldInfo(alias="isExternalBlog")

    organizations: List[FolderPaperOrganization]

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    publication_date: str = FieldInfo(alias="publicationDate")

    title: str

    topics: List[str]

    type: Literal["private", "public"]

    universal_paper_id: str = FieldInfo(alias="universalPaperId")

    user_authors: List[FolderPaperUserAuthor] = FieldInfo(alias="userAuthors")

    votes: float


class Folder(BaseModel):
    id: str

    name: str

    order: float

    papers: List[FolderPaper]

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)

    sharing_status: Literal["not_shared", "shared"] = FieldInfo(alias="sharingStatus")

    type: str


class SharedRetrieveResponse(BaseModel):
    child_folders: List[ChildFolder] = FieldInfo(alias="childFolders")

    folder: Folder

    owner_name: str = FieldInfo(alias="ownerName")
