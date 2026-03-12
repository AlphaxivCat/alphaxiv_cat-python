# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["V1GetCumulativeUsersResponse", "V1GetCumulativeUsersResponseItem"]


class V1GetCumulativeUsersResponseItem(BaseModel):
    count: float

    date: str


V1GetCumulativeUsersResponse: TypeAlias = List[V1GetCumulativeUsersResponseItem]
