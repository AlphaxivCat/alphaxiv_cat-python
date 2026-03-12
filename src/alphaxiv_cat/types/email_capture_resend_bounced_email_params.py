# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmailCaptureResendBouncedEmailParams", "Data"]


class EmailCaptureResendBouncedEmailParams(TypedDict, total=False):
    data: Required[Data]
    """Event data containing bounced emails"""

    type: Required[str]
    """Event type from Resend"""


class Data(TypedDict, total=False):
    """Event data containing bounced emails"""

    to: SequenceNotStr[str]
    """Bounced email addresses"""
