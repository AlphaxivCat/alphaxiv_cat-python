# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PaperKickoffRecentPapersResponse", "Data"]


class Data(BaseModel):
    message: str


class PaperKickoffRecentPapersResponse(BaseModel):
    data: Data
