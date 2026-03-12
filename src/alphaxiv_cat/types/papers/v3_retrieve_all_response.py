# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3RetrieveAllResponse"]


class V3RetrieveAllResponse(BaseModel):
    limit: float

    skip: float

    universal_ids: List[str] = FieldInfo(alias="universalIds")
