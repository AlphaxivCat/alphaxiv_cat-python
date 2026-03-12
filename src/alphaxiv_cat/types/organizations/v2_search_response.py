# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["V2SearchResponse", "V2SearchResponseItem"]


class V2SearchResponseItem(BaseModel):
    id: str

    image: Optional[str] = None

    name: str

    slug: str


V2SearchResponse: TypeAlias = List[V2SearchResponseItem]
