# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
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

    thinking: Required[bool]

    web_search: Required[Annotated[Literal["off", "full"], PropertyInfo(alias="webSearch")]]

    assistant_variant: Annotated[
        Literal["homepage", "paper", "folder", "landing", "folder-add-papers"], PropertyInfo(alias="assistantVariant")
    ]

    folder_add_papers: Annotated[bool, PropertyInfo(alias="folderAddPapers")]

    folder_id: Annotated[str, PropertyInfo(alias="folderId")]

    model: Literal[
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-3-flash",
        "gemini-3-pro",
        "gemini-3.1-pro",
        "claude-4.5-sonnet",
        "claude-4.6-sonnet",
        "grok-4",
        "qwen-3",
        "qwen-3-next",
        "qwen-3.5",
        "gpt-5",
        "gpt-5.2",
        "gpt-5.4",
        "gpt-oss-120b",
        "llama-4-maverick",
        "kimi-k2",
        "kimi-k2.5",
        "glm-5",
        "glm-5-turbo",
        "minimax-m2.5",
        "minimax-m2.7",
        "aurelle-1",
    ]


class File(TypedDict, total=False):
    content_type: Required[Annotated[str, PropertyInfo(alias="contentType")]]

    url: Required[str]
