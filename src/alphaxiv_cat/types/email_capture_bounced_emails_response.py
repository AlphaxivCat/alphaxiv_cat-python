# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EmailCaptureBouncedEmailsResponse", "Data"]


class Data(BaseModel):
    message: str


class EmailCaptureBouncedEmailsResponse(BaseModel):
    data: Data
