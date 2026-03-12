# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SitemapListPapersResponse", "Data", "DataPagination", "DataPaper"]


class DataPagination(BaseModel):
    limit: float

    page: float

    total: float


class DataPaper(BaseModel):
    id: str

    universal_id: str = FieldInfo(alias="universalId")

    updated_at: str = FieldInfo(alias="updatedAt")


class Data(BaseModel):
    pagination: DataPagination

    papers: List[DataPaper]


class SitemapListPapersResponse(BaseModel):
    data: Data
