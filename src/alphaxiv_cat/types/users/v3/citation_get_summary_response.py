# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CitationGetSummaryResponse", "Citations", "HIndex", "I10Index"]


class Citations(BaseModel):
    all: float

    since_2020: float


class HIndex(BaseModel):
    all: float

    since_2020: float


class I10Index(BaseModel):
    all: float

    since_2020: float


class CitationGetSummaryResponse(BaseModel):
    citations: Citations

    h_index: HIndex

    i10_index: I10Index

    updated_at: str = FieldInfo(alias="updatedAt")
