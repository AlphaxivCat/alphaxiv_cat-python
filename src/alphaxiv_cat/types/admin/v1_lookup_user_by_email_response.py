# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1LookupUserByEmailResponse"]


class V1LookupUserByEmailResponse(BaseModel):
    id: str

    email: str

    institution: Optional[str] = None

    real_name: str = FieldInfo(alias="realName")

    role: Literal["user", "reviewer", "admin", "bot"]

    updated_at: str = FieldInfo(alias="updatedAt")

    username: str

    verified: bool
