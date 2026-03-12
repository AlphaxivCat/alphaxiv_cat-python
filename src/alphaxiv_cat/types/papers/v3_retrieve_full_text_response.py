# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3RetrieveFullTextResponse", "Page"]


class Page(BaseModel):
    page_number: float = FieldInfo(alias="pageNumber")

    text: str


class V3RetrieveFullTextResponse(BaseModel):
    pages: List[Page]
