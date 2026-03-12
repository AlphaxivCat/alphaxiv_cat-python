# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailCaptureBouncedEmailsParams"]


class EmailCaptureBouncedEmailsParams(TypedDict, total=False):
    message: Required[Annotated[str, PropertyInfo(alias="Message")]]
    """Stringified JSON message containing bounce/complaint data"""

    type: Required[Annotated[str, PropertyInfo(alias="Type")]]
    """SNS notification type"""
