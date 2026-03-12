# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "V3GetFeaturedActivityResponse",
    "V3GetFeaturedActivityResponseItem",
    "V3GetFeaturedActivityResponseItemUnionMember0",
    "V3GetFeaturedActivityResponseItemUnionMember0Data",
    "V3GetFeaturedActivityResponseItemUnionMember1",
    "V3GetFeaturedActivityResponseItemUnionMember1Data",
]


class V3GetFeaturedActivityResponseItemUnionMember0Data(BaseModel):
    id: str

    date: str

    link: Optional[str] = None

    organization: Optional[str] = None

    recording: Optional[str] = None

    speaker: Optional[str] = None

    title: str


class V3GetFeaturedActivityResponseItemUnionMember0(BaseModel):
    data: V3GetFeaturedActivityResponseItemUnionMember0Data

    type: Literal["video"]


class V3GetFeaturedActivityResponseItemUnionMember1Data(BaseModel):
    abstract: Optional[str] = None

    publication_date: str

    title: str

    universal_paper_id: str


class V3GetFeaturedActivityResponseItemUnionMember1(BaseModel):
    data: V3GetFeaturedActivityResponseItemUnionMember1Data

    type: Literal["paper"]


V3GetFeaturedActivityResponseItem: TypeAlias = Union[
    V3GetFeaturedActivityResponseItemUnionMember0, V3GetFeaturedActivityResponseItemUnionMember1
]

V3GetFeaturedActivityResponse: TypeAlias = List[V3GetFeaturedActivityResponseItem]
