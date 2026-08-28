# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["EmailSendWeeklyDigestParams", "A", "B", "Event"]


class EmailSendWeeklyDigestParams(TypedDict, total=False):
    a: A
    """Text overrides for copy variant A"""

    b: B
    """Text overrides for copy variant B"""

    events: Iterable[Event]
    """Custom events to include, both variants"""

    role: Literal["admin", "user"]
    """Filter by user role"""

    test_batch_size: Annotated[int, PropertyInfo(alias="testBatchSize")]
    """Test mode: page size override, to exercise batching"""

    test_emails: Annotated[SequenceNotStr[str], PropertyInfo(alias="testEmails")]
    """Test mode: only these addresses can receive the digest"""


class A(TypedDict, total=False):
    """Text overrides for copy variant A"""

    intro_text: Annotated[str, PropertyInfo(alias="introText")]
    """Custom intro message"""

    subject: str
    """Custom email subject"""


class B(TypedDict, total=False):
    """Text overrides for copy variant B"""

    intro_text: Annotated[str, PropertyInfo(alias="introText")]
    """Custom intro message"""

    subject: str
    """Custom email subject"""


class Event(TypedDict, total=False):
    date: Required[str]

    description: Required[str]

    link: Required[str]

    title: Required[str]

    cta_text: Annotated[str, PropertyInfo(alias="ctaText")]

    end_time_raw: Annotated[str, PropertyInfo(alias="endTimeRaw")]

    start_time_raw: Annotated[str, PropertyInfo(alias="startTimeRaw")]
