# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2ChatParams", "File", "CustomFilter"]


class V2ChatParams(TypedDict, total=False):
    files: Required[Iterable[File]]

    llm_chat_id: Required[Annotated[Optional[str], PropertyInfo(alias="llmChatId")]]

    message: Required[str]

    paper_version_id: Required[Annotated[Optional[str], PropertyInfo(alias="paperVersionId")]]

    parent_message_id: Required[Annotated[Optional[str], PropertyInfo(alias="parentMessageId")]]

    selection_page_range: Required[Annotated[Optional[Iterable[int]], PropertyInfo(alias="selectionPageRange")]]

    thinking: Required[Union[bool, str, None]]

    web_search: Required[Annotated[Literal["off", "full"], PropertyInfo(alias="webSearch")]]

    assistant_variant: Annotated[Literal["homepage", "paper", "landing"], PropertyInfo(alias="assistantVariant")]

    custom_filter: Annotated[CustomFilter, PropertyInfo(alias="customFilter")]

    filter_model: Annotated[Literal["cohere"], PropertyInfo(alias="filterModel")]

    model: str

    plan: Literal["free", "pro"]

    protocol: int

    signature: str


class File(TypedDict, total=False):
    content_type: Required[Annotated[str, PropertyInfo(alias="contentType")]]

    url: Required[str]


class CustomFilter(TypedDict, total=False):
    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]

    url: Required[str]
