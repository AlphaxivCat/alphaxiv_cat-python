# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ModeratorToggleFlagsResponse"]


class ModeratorToggleFlagsResponse(BaseModel):
    addressed: bool

    closed: bool

    flag_addressed: bool = FieldInfo(alias="flagAddressed")
