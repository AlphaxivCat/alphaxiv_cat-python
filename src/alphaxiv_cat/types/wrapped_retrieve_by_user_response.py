# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["WrappedRetrieveByUserResponse", "WrappedRetrieveByUserResponseItem"]


class WrappedRetrieveByUserResponseItem(BaseModel):
    id: str

    order: float

    type: str

    year: float

    data: Optional[object] = None


WrappedRetrieveByUserResponse: TypeAlias = List[WrappedRetrieveByUserResponseItem]
