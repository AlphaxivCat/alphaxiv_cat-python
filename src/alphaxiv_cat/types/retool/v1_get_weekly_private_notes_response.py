# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["V1GetWeeklyPrivateNotesResponse", "V1GetWeeklyPrivateNotesResponseItem"]


class V1GetWeeklyPrivateNotesResponseItem(BaseModel):
    count: float

    week: str


V1GetWeeklyPrivateNotesResponse: TypeAlias = List[V1GetWeeklyPrivateNotesResponseItem]
