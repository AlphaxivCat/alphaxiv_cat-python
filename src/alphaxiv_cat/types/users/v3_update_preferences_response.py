# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V3UpdatePreferencesResponse", "Banner", "Base", "BaseAssistantCustomStyle", "Email", "Folder"]


class Banner(BaseModel):
    id: str

    link: Optional[str] = None

    name: str

    type: Literal["success", "info", "warning", "error"]


class BaseAssistantCustomStyle(BaseModel):
    id: str

    instructions: str

    name: str


class Base(BaseModel):
    assistant_custom_styles: List[BaseAssistantCustomStyle] = FieldInfo(alias="assistantCustomStyles")

    assistant_style_selection: Union[Literal["default", "concise", "tutor", "thorough", "skeptical"], str] = FieldInfo(
        alias="assistantStyleSelection"
    )

    default_private_paper_sidebar_tab: Optional[Literal["assistant", "notes", "similar"]] = FieldInfo(
        alias="defaultPrivatePaperSidebarTab", default=None
    )

    default_public_paper_sidebar_tab: Optional[Literal["comments", "assistant", "similar", "notes", "social"]] = (
        FieldInfo(alias="defaultPublicPaperSidebarTab", default=None)
    )

    feed_sort: Literal["Hot", "Comments", "Views", "Likes", "GitHub", "Twitter (X)", "Recommended"] = FieldInfo(
        alias="feedSort"
    )

    is_dark_mode_enabled: bool = FieldInfo(alias="isDarkModeEnabled")

    is_debug_mode_enabled: bool = FieldInfo(alias="isDebugModeEnabled")

    is_members_sidebar_visible: bool = FieldInfo(alias="isMembersSidebarVisible")

    preferred_language: Optional[
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
    ] = FieldInfo(alias="preferredLanguage", default=None)

    preferred_llm_follow_latest_category: Optional[str] = FieldInfo(
        alias="preferredLlmFollowLatestCategory", default=None
    )

    preferred_llm_model: Optional[str] = FieldInfo(alias="preferredLlmModel", default=None)

    preferred_llm_thinking: Optional[str] = FieldInfo(alias="preferredLlmThinking", default=None)

    reading_mode_enabled: bool = FieldInfo(alias="readingModeEnabled")

    show_model_thinking: bool = FieldInfo(alias="showModelThinking")

    tooling_pane_width: Optional[float] = FieldInfo(alias="toolingPaneWidth", default=None)

    web_search: Literal["off", "full"] = FieldInfo(alias="webSearch")


class Email(BaseModel):
    bounced: bool

    direct_notifications: bool = FieldInfo(alias="directNotifications")

    relevant_activity: bool = FieldInfo(alias="relevantActivity")


class Folder(BaseModel):
    folder_id: str = FieldInfo(alias="folderId")

    opened: bool


class V3UpdatePreferencesResponse(BaseModel):
    banners: List[Banner]

    base: Base

    email: Email

    folders: List[Folder]
