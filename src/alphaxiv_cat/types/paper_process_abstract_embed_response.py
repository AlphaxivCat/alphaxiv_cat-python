# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PaperProcessAbstractEmbedResponse", "Data"]


class Data(BaseModel):
    status: str


class PaperProcessAbstractEmbedResponse(BaseModel):
    data: Data
