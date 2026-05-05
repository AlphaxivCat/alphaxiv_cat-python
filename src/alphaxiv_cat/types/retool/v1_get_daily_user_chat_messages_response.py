# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["V1GetDailyUserChatMessagesResponse", "V1GetDailyUserChatMessagesResponseItem"]


class V1GetDailyUserChatMessagesResponseItem(BaseModel):
    count: float

    date: str

    variant: Literal["homepage", "paper"]


V1GetDailyUserChatMessagesResponse: TypeAlias = List[V1GetDailyUserChatMessagesResponseItem]
