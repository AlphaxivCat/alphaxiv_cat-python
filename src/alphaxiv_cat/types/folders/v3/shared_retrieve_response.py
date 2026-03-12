# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "SharedRetrieveResponse",
    "ChildFolder",
    "ChildFolderPaper",
    "ChildFolderPaperAuthor",
    "ChildFolderPaperOrganization",
    "ChildFolderPaperUserAuthor",
    "ChildFolderPaperUserAuthorAvatar",
    "Folder",
    "FolderPaper",
    "FolderPaperAuthor",
    "FolderPaperOrganization",
    "FolderPaperUserAuthor",
    "FolderPaperUserAuthorAvatar",
]


class ChildFolderPaperAuthor(BaseModel):
    id: str

    full_name: str

    user_id: Optional[str] = None

    username: Optional[str] = None


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

    role: Literal["user", "reviewer", "admin", "bot"]

    username: str

    verified: bool

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)


class ChildFolderPaper(BaseModel):
    abstract: str

    added_at: str = FieldInfo(alias="addedAt")

    authors: List[ChildFolderPaperAuthor]

    citation: Optional[str] = None

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    organizations: List[ChildFolderPaperOrganization]

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    publication_date: str = FieldInfo(alias="publicationDate")

    title: str

    topics: List[str]

    type: Literal["private", "community", "public"]

    universal_paper_id: str = FieldInfo(alias="universalPaperId")

    user_authors: List[ChildFolderPaperUserAuthor] = FieldInfo(alias="userAuthors")


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

    role: Literal["user", "reviewer", "admin", "bot"]

    username: str

    verified: bool

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)


class FolderPaper(BaseModel):
    abstract: str

    added_at: str = FieldInfo(alias="addedAt")

    authors: List[FolderPaperAuthor]

    citation: Optional[str] = None

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    organizations: List[FolderPaperOrganization]

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    publication_date: str = FieldInfo(alias="publicationDate")

    title: str

    topics: List[str]

    type: Literal["private", "community", "public"]

    universal_paper_id: str = FieldInfo(alias="universalPaperId")

    user_authors: List[FolderPaperUserAuthor] = FieldInfo(alias="userAuthors")


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
