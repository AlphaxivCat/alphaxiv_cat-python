# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaperToggleFollowResponse", "Data"]


class Data(BaseModel):
    paper_group_id: str = FieldInfo(alias="paperGroupId")


class PaperToggleFollowResponse(BaseModel):
    data: Data
