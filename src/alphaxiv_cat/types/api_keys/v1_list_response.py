# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1ListResponse", "V1ListResponseItem"]


class V1ListResponseItem(BaseModel):
    id: str

    label: str

    last_used_at: Optional[str] = FieldInfo(alias="lastUsedAt", default=None)

    prefix: str

    revoked_at: Optional[str] = FieldInfo(alias="revokedAt", default=None)


V1ListResponse: TypeAlias = List[V1ListResponseItem]
