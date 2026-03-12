# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PaperViewCountIngestEventResponse", "Data"]


class Data(BaseModel):
    ingested_paper: str = FieldInfo(alias="ingestedPaper")


class PaperViewCountIngestEventResponse(BaseModel):
    data: Data
