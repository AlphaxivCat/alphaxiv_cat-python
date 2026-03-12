# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["V2GetURLMetadataResponse"]


class V2GetURLMetadataResponse(BaseModel):
    favicon: Optional[str] = None

    title: Optional[str] = None
