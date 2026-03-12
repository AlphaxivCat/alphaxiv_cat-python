# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["V2RetrieveByNameResponse"]


class V2RetrieveByNameResponse(BaseModel):
    id: str

    image: Optional[str] = None

    name: str

    slug: str
