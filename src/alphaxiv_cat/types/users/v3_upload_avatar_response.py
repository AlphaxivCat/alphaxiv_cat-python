# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["V3UploadAvatarResponse", "Data"]


class Data(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class V3UploadAvatarResponse(BaseModel):
    data: List[Data]
