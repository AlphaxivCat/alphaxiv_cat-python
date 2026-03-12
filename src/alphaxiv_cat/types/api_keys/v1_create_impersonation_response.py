# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1CreateImpersonationResponse", "APIKey"]


class APIKey(BaseModel):
    id: str

    label: str

    last_used_at: Optional[str] = FieldInfo(alias="lastUsedAt", default=None)

    prefix: str

    revoked_at: Optional[str] = FieldInfo(alias="revokedAt", default=None)


class V1CreateImpersonationResponse(BaseModel):
    api_key: APIKey = FieldInfo(alias="apiKey")

    secret: str
