# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3ToggleSharingResponse"]


class V3ToggleSharingResponse(BaseModel):
    sharing_status: Literal["not_shared", "shared"] = FieldInfo(alias="sharingStatus")
