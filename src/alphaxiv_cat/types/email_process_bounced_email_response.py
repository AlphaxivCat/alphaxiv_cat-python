# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EmailProcessBouncedEmailResponse", "Data"]


class Data(BaseModel):
    message: str


class EmailProcessBouncedEmailResponse(BaseModel):
    data: Data
