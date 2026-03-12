# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3MovePapersResponse"]


class V3MovePapersResponse(BaseModel):
    duplicate_count: float = FieldInfo(alias="duplicateCount")

    moved_count: float = FieldInfo(alias="movedCount")
