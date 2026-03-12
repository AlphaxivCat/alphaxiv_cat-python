# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SeenGetSeenResponse"]


class SeenGetSeenResponse(BaseModel):
    seen_paper_group_ids: List[str] = FieldInfo(alias="seenPaperGroupIds")
