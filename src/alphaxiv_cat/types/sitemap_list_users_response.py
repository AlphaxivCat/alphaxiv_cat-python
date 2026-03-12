# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SitemapListUsersResponse", "Data", "DataPagination", "DataUser"]


class DataPagination(BaseModel):
    total: float

    limit: Optional[float] = None

    page: Optional[float] = None


class DataUser(BaseModel):
    id: str

    username: str


class Data(BaseModel):
    pagination: DataPagination

    users: List[DataUser]


class SitemapListUsersResponse(BaseModel):
    data: Data
