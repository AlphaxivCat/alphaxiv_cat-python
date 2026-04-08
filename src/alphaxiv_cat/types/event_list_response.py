# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EventListResponse", "EventListResponseItem"]


class EventListResponseItem(BaseModel):
    id: str

    date: str

    link: str

    organization: str

    recording: Optional[str] = None

    speaker: Optional[str] = None

    title: str


EventListResponse: TypeAlias = List[EventListResponseItem]
