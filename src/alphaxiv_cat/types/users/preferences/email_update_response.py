# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["EmailUpdateResponse", "Data"]


class Data(BaseModel):
    success: bool


class EmailUpdateResponse(BaseModel):
    data: Data
