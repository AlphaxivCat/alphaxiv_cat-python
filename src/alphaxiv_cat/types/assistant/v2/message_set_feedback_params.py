# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageSetFeedbackParams", "Feedback"]


class MessageSetFeedbackParams(TypedDict, total=False):
    feedback: Required[Optional[Feedback]]


class Feedback(TypedDict, total=False):
    type: Required[Literal["upvote", "downvote"]]

    category: Optional[str]

    details: Optional[str]
