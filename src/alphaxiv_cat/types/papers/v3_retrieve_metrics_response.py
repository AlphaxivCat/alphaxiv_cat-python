# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3RetrieveMetricsResponse"]


class V3RetrieveMetricsResponse(BaseModel):
    comments_count: float = FieldInfo(alias="commentsCount")

    public_total_votes: float = FieldInfo(alias="publicTotalVotes")

    visits_all: float = FieldInfo(alias="visitsAll")
