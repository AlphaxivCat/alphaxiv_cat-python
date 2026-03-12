# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaperVoteResponse", "Data", "DataPaperGroup"]


class DataPaperGroup(BaseModel):
    api_id: str = FieldInfo(alias="_id")


class Data(BaseModel):
    paper_group: DataPaperGroup = FieldInfo(alias="paperGroup")


class PaperVoteResponse(BaseModel):
    data: Data
