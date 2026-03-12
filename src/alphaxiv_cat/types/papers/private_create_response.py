# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PrivateCreateResponse", "Data"]


class Data(BaseModel):
    id: str

    content_type: str

    filename: str

    size: float

    url: str

    paper_data: Optional[object] = None


class PrivateCreateResponse(BaseModel):
    data: Data
