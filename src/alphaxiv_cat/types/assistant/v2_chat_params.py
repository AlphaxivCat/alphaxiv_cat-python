# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2ChatParams", "File"]


class V2ChatParams(TypedDict, total=False):
    files: Required[Iterable[File]]

    llm_chat_id: Required[Annotated[Optional[str], PropertyInfo(alias="llmChatId")]]

    message: Required[str]

    paper_version_id: Required[Annotated[Optional[str], PropertyInfo(alias="paperVersionId")]]

    parent_message_id: Required[Annotated[Optional[str], PropertyInfo(alias="parentMessageId")]]

    selection_page_range: Required[Annotated[Optional[Iterable[int]], PropertyInfo(alias="selectionPageRange")]]

    thinking: Required[Union[bool, str, None]]

    web_search: Required[Annotated[Literal["off", "full"], PropertyInfo(alias="webSearch")]]

    assistant_variant: Annotated[
        Literal["homepage", "paper", "folder", "landing", "folder-add-papers"], PropertyInfo(alias="assistantVariant")
    ]

    folder_add_papers: Annotated[bool, PropertyInfo(alias="folderAddPapers")]

    folder_id: Annotated[str, PropertyInfo(alias="folderId")]

    model: Literal[
        "claude-opus-4.5",
        "claude-opus-4.6",
        "claude-opus-4.7",
        "claude-sonnet-4.5",
        "claude-sonnet-4.6",
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-3-flash",
        "gemini-3.1-pro",
        "glm-5-turbo",
        "glm-5.1",
        "gpt-5",
        "gpt-5.1",
        "gpt-5.2",
        "gpt-5.4",
        "gpt-5.4-mini",
        "gpt-5.4-nano",
        "kimi-k2.5",
        "kimi-k2.6",
        "mercury-2",
        "minimax-m2.5",
        "minimax-m2.7",
        "qwen-3.5",
        "fast",
        "smart",
        "pro",
    ]

    plan: Literal["free", "pro"]

    signature: str


class File(TypedDict, total=False):
    content_type: Required[Annotated[str, PropertyInfo(alias="contentType")]]

    url: Required[str]
