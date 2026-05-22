# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["V3LikeResponse", "Metrics"]


class Metrics(BaseModel):
    public_total_votes: float

    total_votes: float


class V3LikeResponse(BaseModel):
    liked: bool

    metrics: Metrics
