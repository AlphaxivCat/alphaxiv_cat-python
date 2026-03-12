# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["V1GetDailyConversationsResponse", "V1GetDailyConversationsResponseItem"]


class V1GetDailyConversationsResponseItem(BaseModel):
    count: float

    date: str

    variant: Literal["homepage", "paper", "folder"]


V1GetDailyConversationsResponse: TypeAlias = List[V1GetDailyConversationsResponseItem]
