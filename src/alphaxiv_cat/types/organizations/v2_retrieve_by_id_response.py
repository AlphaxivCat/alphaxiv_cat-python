# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["V2RetrieveByIDResponse"]


class V2RetrieveByIDResponse(BaseModel):
    id: str

    image: Optional[str] = None

    name: str

    slug: str
