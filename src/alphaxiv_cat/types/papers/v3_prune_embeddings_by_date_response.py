# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3PruneEmbeddingsByDateResponse"]


class V3PruneEmbeddingsByDateResponse(BaseModel):
    rows_updated: List[float] = FieldInfo(alias="rowsUpdated")
