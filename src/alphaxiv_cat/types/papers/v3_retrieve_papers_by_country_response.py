# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3RetrievePapersByCountryResponse", "V3RetrievePapersByCountryResponseItem"]


class V3RetrievePapersByCountryResponseItem(BaseModel):
    abstract: str

    citations_count: float = FieldInfo(alias="citationsCount")

    comments_count: float = FieldInfo(alias="commentsCount")

    countries: List[str]

    first_publication_date: str = FieldInfo(alias="firstPublicationDate")

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    publication_date: str = FieldInfo(alias="publicationDate")

    public_total_votes: float = FieldInfo(alias="publicTotalVotes")

    title: str

    total_votes: float = FieldInfo(alias="totalVotes")

    universal_id: str = FieldInfo(alias="universalId")

    visits_all: float = FieldInfo(alias="visitsAll")


V3RetrievePapersByCountryResponse: TypeAlias = List[V3RetrievePapersByCountryResponseItem]
