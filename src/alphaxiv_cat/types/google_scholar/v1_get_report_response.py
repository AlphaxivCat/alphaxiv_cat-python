# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V1GetReportResponse",
    "V1GetReportResponseItem",
    "V1GetReportResponseItemUnionMember0",
    "V1GetReportResponseItemUnionMember1",
]


class V1GetReportResponseItemUnionMember0(BaseModel):
    status: Literal["claimed"]

    title: str

    universal_id: str = FieldInfo(alias="universalId")
    """A versionless universal paper ID (e.g. 1706.03762)"""


class V1GetReportResponseItemUnionMember1(BaseModel):
    google_citation_id: str = FieldInfo(alias="googleCitationId")

    status: Literal["error", "not-found"]

    title: str


V1GetReportResponseItem: TypeAlias = Union[V1GetReportResponseItemUnionMember0, V1GetReportResponseItemUnionMember1]

V1GetReportResponse: TypeAlias = List[V1GetReportResponseItem]
