# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AssistantUploadFileResponse", "Data"]


class Data(BaseModel):
    id: str

    content_type: str

    filename: str

    size: float

    url: str


class AssistantUploadFileResponse(BaseModel):
    data: Data
