# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ImplementationListResponse", "AlphaXivImplementation", "PaperResource"]


class AlphaXivImplementation(BaseModel):
    id: str

    type: Literal["github", "marimo"]

    url: str


class PaperResource(BaseModel):
    id: str

    description: Optional[str] = None

    language: Optional[str] = None

    source: Literal["author", "other"]

    stars: float

    type: Literal["github", "marimo"]

    url: str


class ImplementationListResponse(BaseModel):
    alpha_xiv_implementations: List[AlphaXivImplementation] = FieldInfo(alias="alphaXivImplementations")

    paper_resources: List[PaperResource] = FieldInfo(alias="paperResources")
