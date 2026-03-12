# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaperAddAuthorResponse", "Data"]


class Data(BaseModel):
    warning: str


class PaperAddAuthorResponse(BaseModel):
    accept: Literal[0, 1, 2]

    data: Optional[Data] = None
