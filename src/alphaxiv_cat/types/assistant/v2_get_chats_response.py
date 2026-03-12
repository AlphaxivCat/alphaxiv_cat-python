# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V2GetChatsResponse", "V2GetChatsResponseItem"]


class V2GetChatsResponseItem(BaseModel):
    id: str

    newest_message: float = FieldInfo(alias="newestMessage")
    """UNIX milliseconds"""

    title: str


V2GetChatsResponse: TypeAlias = List[V2GetChatsResponseItem]
