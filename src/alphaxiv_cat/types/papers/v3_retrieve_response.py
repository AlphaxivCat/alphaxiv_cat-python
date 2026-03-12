# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3RetrieveResponse", "Resource", "Version"]


class Resource(BaseModel):
    id: str

    description: str

    language: str

    stars: float

    type: Literal["github"]

    url: str


class Version(BaseModel):
    id: str

    label: str

    order: float


class V3RetrieveResponse(BaseModel):
    abstract: str

    citation_bibtex: Optional[str] = FieldInfo(alias="citationBibtex", default=None)

    citations_count: float = FieldInfo(alias="citationsCount")

    first_publication_date: float = FieldInfo(alias="firstPublicationDate")

    google_citation_id: Optional[str] = FieldInfo(alias="googleCitationId", default=None)

    group_id: str = FieldInfo(alias="groupId")

    license: Optional[str] = None

    publication_date: float = FieldInfo(alias="publicationDate")

    resources: List[Resource]

    source_name: str = FieldInfo(alias="sourceName")

    source_url: str = FieldInfo(alias="sourceUrl")

    title: str

    type: Literal["public", "private", "community"]

    universal_id: str = FieldInfo(alias="universalId")

    uploader: Optional[str] = None

    version_id: str = FieldInfo(alias="versionId")

    version_label: str = FieldInfo(alias="versionLabel")

    version_order: float = FieldInfo(alias="versionOrder")

    versions: List[Version]
