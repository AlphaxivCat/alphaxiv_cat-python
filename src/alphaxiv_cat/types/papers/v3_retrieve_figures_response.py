# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["V3RetrieveFiguresResponse"]


class V3RetrieveFiguresResponse(BaseModel):
    figures: List[str]
