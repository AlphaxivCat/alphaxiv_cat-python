# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["V2ListTopResponse", "V2ListTopResponseItem"]


class V2ListTopResponseItem(BaseModel):
    id: str

    image: Optional[str] = None

    name: str

    slug: str


V2ListTopResponse: TypeAlias = List[V2ListTopResponseItem]
