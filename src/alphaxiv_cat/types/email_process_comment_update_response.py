# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailProcessCommentUpdateResponse", "Data"]


class Data(BaseModel):
    processed_user: str = FieldInfo(alias="processedUser")


class EmailProcessCommentUpdateResponse(BaseModel):
    data: Data
