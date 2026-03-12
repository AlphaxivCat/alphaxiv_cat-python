# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3ImplementationResponse", "Implementation"]


class Implementation(BaseModel):
    id: str

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    type: Literal["github", "marimo"]

    url: str


class V3ImplementationResponse(BaseModel):
    implementation: Implementation
