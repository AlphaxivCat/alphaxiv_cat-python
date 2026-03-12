# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SitemapListOverviewsResponse", "Data", "DataPagination", "DataPaper"]


class DataPagination(BaseModel):
    total: float

    limit: Optional[float] = None

    page: Optional[float] = None


class DataPaper(BaseModel):
    id: str

    language: str

    universal_paper_id: str

    updated_at: str

    version_order: float


class Data(BaseModel):
    pagination: DataPagination

    papers: List[DataPaper]


class SitemapListOverviewsResponse(BaseModel):
    data: Data
