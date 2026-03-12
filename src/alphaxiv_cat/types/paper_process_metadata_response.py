# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PaperProcessMetadataResponse", "Data"]


class Data(BaseModel):
    status: str


class PaperProcessMetadataResponse(BaseModel):
    data: Optional[Data] = None

    error: Optional[str] = None
