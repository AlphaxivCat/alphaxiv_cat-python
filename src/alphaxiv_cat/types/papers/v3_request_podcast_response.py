# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["V3RequestPodcastResponse"]


class V3RequestPodcastResponse(BaseModel):
    message: str

    state: Literal["queued", "generating", "done", "errored"]
