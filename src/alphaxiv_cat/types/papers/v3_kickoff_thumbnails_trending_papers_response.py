# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["V3KickoffThumbnailsTrendingPapersResponse", "Data"]


class Data(BaseModel):
    message: str


class V3KickoffThumbnailsTrendingPapersResponse(BaseModel):
    data: Data
