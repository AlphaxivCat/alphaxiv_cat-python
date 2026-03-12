# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IngestIngestLatestParams"]


class IngestIngestLatestParams(TypedDict, total=False):
    prevent_tracking: Annotated[str, PropertyInfo(alias="preventTracking")]
