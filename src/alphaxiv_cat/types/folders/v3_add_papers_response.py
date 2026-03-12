# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3AddPapersResponse"]


class V3AddPapersResponse(BaseModel):
    added_count: float = FieldInfo(alias="addedCount")

    duplicate_count: float = FieldInfo(alias="duplicateCount")
