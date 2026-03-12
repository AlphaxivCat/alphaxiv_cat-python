# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["V3MovePapersParams"]


class V3MovePapersParams(TypedDict, total=False):
    paper_group_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="paperGroupIds")]]

    from_folder_id: Annotated[str, PropertyInfo(alias="fromFolderId")]
