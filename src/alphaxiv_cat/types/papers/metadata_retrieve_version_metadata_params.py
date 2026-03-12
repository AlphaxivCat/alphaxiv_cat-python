# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MetadataRetrieveVersionMetadataParams"]


class MetadataRetrieveVersionMetadataParams(TypedDict, total=False):
    upid: Required[str]

    prevent_tracking: Annotated[str, PropertyInfo(alias="preventTracking")]
