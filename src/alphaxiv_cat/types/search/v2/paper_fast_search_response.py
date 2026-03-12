# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PaperFastSearchResponse", "PaperFastSearchResponseItem"]


class PaperFastSearchResponseItem(BaseModel):
    link: str

    paper_id: str = FieldInfo(alias="paperId")
    """An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)"""

    snippet: str

    title: str

    is_private: Optional[bool] = FieldInfo(alias="isPrivate", default=None)


PaperFastSearchResponse: TypeAlias = List[PaperFastSearchResponseItem]
