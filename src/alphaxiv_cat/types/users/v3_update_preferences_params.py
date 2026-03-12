# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3UpdatePreferencesParams", "Banner", "Base", "BaseAssistantCustomStyle"]


class V3UpdatePreferencesParams(TypedDict, total=False):
    banners: Iterable[Banner]

    base: Base


class Banner(TypedDict, total=False):
    link: Required[Optional[str]]

    name: Required[str]

    type: Required[Literal["success", "info", "warning", "error"]]


class BaseAssistantCustomStyle(TypedDict, total=False):
    id: Required[str]

    instructions: Required[str]

    name: Required[str]


class Base(TypedDict, total=False):
    assistant_custom_styles: Annotated[Iterable[BaseAssistantCustomStyle], PropertyInfo(alias="assistantCustomStyles")]

    assistant_style_selection: Annotated[
        Union[Literal["default", "concise", "tutor", "thorough", "skeptical"], str],
        PropertyInfo(alias="assistantStyleSelection"),
    ]

    default_private_paper_sidebar_tab: Annotated[
        Optional[Literal["assistant", "notes", "similar"]], PropertyInfo(alias="defaultPrivatePaperSidebarTab")
    ]

    default_public_paper_sidebar_tab: Annotated[
        Optional[Literal["comments", "assistant", "similar", "notes", "social"]],
        PropertyInfo(alias="defaultPublicPaperSidebarTab"),
    ]

    feed_sort: Annotated[
        Literal["Hot", "Comments", "Views", "Likes", "GitHub", "Twitter (X)", "Recommended"],
        PropertyInfo(alias="feedSort"),
    ]

    is_dark_mode_enabled: Annotated[bool, PropertyInfo(alias="isDarkModeEnabled")]

    is_debug_mode_enabled: Annotated[bool, PropertyInfo(alias="isDebugModeEnabled")]

    is_members_sidebar_visible: Annotated[bool, PropertyInfo(alias="isMembersSidebarVisible")]

    preferred_language: Annotated[
        Optional[
            Literal[
                "am",
                "ar",
                "az",
                "bg",
                "bn",
                "ca",
                "cs",
                "da",
                "de",
                "el",
                "en",
                "es",
                "et",
                "fa",
                "fi",
                "fr",
                "gu",
                "ha",
                "he",
                "hi",
                "hr",
                "hu",
                "id",
                "it",
                "ja",
                "ka",
                "kn",
                "ko",
                "lt",
                "lv",
                "ml",
                "mr",
                "ms",
                "my",
                "ne",
                "nl",
                "no",
                "pa",
                "pl",
                "pt",
                "ro",
                "ru",
                "si",
                "sk",
                "sl",
                "sr",
                "sv",
                "sw",
                "ta",
                "te",
                "th",
                "tl",
                "tr",
                "uk",
                "ur",
                "uz",
                "vi",
                "yo",
                "zh",
            ]
        ],
        PropertyInfo(alias="preferredLanguage"),
    ]

    preferred_llm_model: Annotated[Optional[str], PropertyInfo(alias="preferredLlmModel")]

    reading_mode_enabled: Annotated[bool, PropertyInfo(alias="readingModeEnabled")]

    show_model_thinking: Annotated[bool, PropertyInfo(alias="showModelThinking")]

    tooling_pane_width: Annotated[Optional[float], PropertyInfo(alias="toolingPaneWidth")]

    web_search: Annotated[Literal["off", "full"], PropertyInfo(alias="webSearch")]
