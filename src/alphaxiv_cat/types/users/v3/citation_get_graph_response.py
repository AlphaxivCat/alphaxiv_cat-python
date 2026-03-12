# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["CitationGetGraphResponse", "Graph"]


class Graph(BaseModel):
    citations: float

    year: float


class CitationGetGraphResponse(BaseModel):
    graph: List[Graph]
