# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EmailSendWeeklyDigestParams", "Event"]


class EmailSendWeeklyDigestParams(TypedDict, total=False):
    events: Iterable[Event]
    """Custom events to include"""

    intro_text: Annotated[str, PropertyInfo(alias="introText")]
    """Custom intro message"""

    role: Literal["admin", "user"]
    """Filter by user role"""

    subject: str
    """Custom email subject"""


class Event(TypedDict, total=False):
    date: Required[str]

    description: Required[str]

    link: Required[str]

    title: Required[str]

    end_time_raw: Annotated[str, PropertyInfo(alias="endTimeRaw")]

    start_time_raw: Annotated[str, PropertyInfo(alias="startTimeRaw")]
