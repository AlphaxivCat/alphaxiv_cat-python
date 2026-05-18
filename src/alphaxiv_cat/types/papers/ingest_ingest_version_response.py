# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["IngestIngestVersionResponse", "Data"]


class Data(BaseModel):
    authors: List[Optional[object]]

    max_version_order: float

    verified_authors: List[Optional[object]]

    paper_group: Optional[object] = None

    paper_version: Optional[object] = None


class IngestIngestVersionResponse(BaseModel):
    data: Data
