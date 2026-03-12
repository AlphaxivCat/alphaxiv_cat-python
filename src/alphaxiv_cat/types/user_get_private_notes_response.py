# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["UserGetPrivateNotesResponse", "Data"]


class Data(BaseModel):
    comments: List[Optional[object]]

    total: float


class UserGetPrivateNotesResponse(BaseModel):
    data: Data
