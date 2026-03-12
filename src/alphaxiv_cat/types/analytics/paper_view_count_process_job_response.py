# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PaperViewCountProcessJobResponse", "Data"]


class Data(BaseModel):
    processed_paper: str = FieldInfo(alias="processedPaper")


class PaperViewCountProcessJobResponse(BaseModel):
    data: Data
