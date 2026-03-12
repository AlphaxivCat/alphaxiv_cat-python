# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["V1GetDailyNewAccountsResponse", "V1GetDailyNewAccountsResponseItem"]


class V1GetDailyNewAccountsResponseItem(BaseModel):
    count: float

    date: str


V1GetDailyNewAccountsResponse: TypeAlias = List[V1GetDailyNewAccountsResponseItem]
