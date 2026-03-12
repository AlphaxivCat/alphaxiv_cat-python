# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PaperKickoffGitHubResponse", "Data"]


class Data(BaseModel):
    message: str


class PaperKickoffGitHubResponse(BaseModel):
    data: Data
