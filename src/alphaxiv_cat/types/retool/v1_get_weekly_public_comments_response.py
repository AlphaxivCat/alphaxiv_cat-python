# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["V1GetWeeklyPublicCommentsResponse", "V1GetWeeklyPublicCommentsResponseItem"]


class V1GetWeeklyPublicCommentsResponseItem(BaseModel):
    count: float

    week: str


V1GetWeeklyPublicCommentsResponse: TypeAlias = List[V1GetWeeklyPublicCommentsResponseItem]
