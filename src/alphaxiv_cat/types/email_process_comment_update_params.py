# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailProcessCommentUpdateParams", "CustomContent", "CustomContentEvent"]


class EmailProcessCommentUpdateParams(TypedDict, total=False):
    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]

    custom_content: Annotated[CustomContent, PropertyInfo(alias="customContent")]


class CustomContentEvent(TypedDict, total=False):
    date: Required[str]

    description: Required[str]

    link: Required[str]

    title: Required[str]

    end_time_raw: Annotated[str, PropertyInfo(alias="endTimeRaw")]

    start_time_raw: Annotated[str, PropertyInfo(alias="startTimeRaw")]


class CustomContent(TypedDict, total=False):
    events: Iterable[CustomContentEvent]

    intro_text: Annotated[str, PropertyInfo(alias="introText")]

    subject: str
