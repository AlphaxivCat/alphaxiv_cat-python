# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1GetWeeklyMessageCountsByUserResponse", "V1GetWeeklyMessageCountsByUserResponseItem"]


class V1GetWeeklyMessageCountsByUserResponseItem(BaseModel):
    count: float

    email: str

    user_id: str = FieldInfo(alias="userId")

    username: str


V1GetWeeklyMessageCountsByUserResponse: TypeAlias = List[V1GetWeeklyMessageCountsByUserResponseItem]
