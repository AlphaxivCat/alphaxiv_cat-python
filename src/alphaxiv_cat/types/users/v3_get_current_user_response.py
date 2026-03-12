# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V3GetCurrentUserResponse",
    "Badges",
    "Preferences",
    "PreferencesBanner",
    "PreferencesBase",
    "PreferencesBaseAssistantCustomStyle",
    "PreferencesEmail",
    "PreferencesFolder",
    "User",
    "UserAvatar",
    "UserPreferences",
    "UserPreferencesBanner",
    "UserPreferencesBase",
    "UserPreferencesBaseAssistantCustomStyle",
    "UserPreferencesEmail",
    "UserPreferencesFolder",
    "UserPushSubscription",
    "UserSemanticScholar",
    "UserFeatured",
]


class Badges(BaseModel):
    site: int


class PreferencesBanner(BaseModel):
    id: str

    link: Optional[str] = None

    name: str

    type: Literal["success", "info", "warning", "error"]


class PreferencesBaseAssistantCustomStyle(BaseModel):
    id: str

    instructions: str

    name: str


class PreferencesBase(BaseModel):
    assistant_custom_styles: List[PreferencesBaseAssistantCustomStyle] = FieldInfo(alias="assistantCustomStyles")

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

    preferred_llm_model: Optional[str] = FieldInfo(alias="preferredLlmModel", default=None)

    reading_mode_enabled: bool = FieldInfo(alias="readingModeEnabled")

    show_model_thinking: bool = FieldInfo(alias="showModelThinking")

    tooling_pane_width: Optional[float] = FieldInfo(alias="toolingPaneWidth", default=None)

    web_search: Literal["off", "full"] = FieldInfo(alias="webSearch")


class PreferencesEmail(BaseModel):
    bounced: bool

    direct_notifications: bool = FieldInfo(alias="directNotifications")

    relevant_activity: bool = FieldInfo(alias="relevantActivity")


class PreferencesFolder(BaseModel):
    folder_id: str = FieldInfo(alias="folderId")

    opened: bool


class Preferences(BaseModel):
    banners: List[PreferencesBanner]

    base: PreferencesBase

    email: PreferencesEmail

    folders: List[PreferencesFolder]


class UserAvatar(BaseModel):
    type: Literal["full_size", "thumbnail"]

    url: str


class UserPreferencesBanner(BaseModel):
    id: str

    link: Optional[str] = None

    name: str

    type: Literal["success", "info", "warning", "error"]


class UserPreferencesBaseAssistantCustomStyle(BaseModel):
    id: str

    instructions: str

    name: str


class UserPreferencesBase(BaseModel):
    assistant_custom_styles: List[UserPreferencesBaseAssistantCustomStyle] = FieldInfo(alias="assistantCustomStyles")

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

    preferred_llm_model: Optional[str] = FieldInfo(alias="preferredLlmModel", default=None)

    reading_mode_enabled: bool = FieldInfo(alias="readingModeEnabled")

    show_model_thinking: bool = FieldInfo(alias="showModelThinking")

    tooling_pane_width: Optional[float] = FieldInfo(alias="toolingPaneWidth", default=None)

    web_search: Literal["off", "full"] = FieldInfo(alias="webSearch")


class UserPreferencesEmail(BaseModel):
    bounced: bool

    direct_notifications: bool = FieldInfo(alias="directNotifications")

    relevant_activity: bool = FieldInfo(alias="relevantActivity")


class UserPreferencesFolder(BaseModel):
    folder_id: str = FieldInfo(alias="folderId")

    opened: bool


class UserPreferences(BaseModel):
    banners: List[UserPreferencesBanner]

    base: UserPreferencesBase

    email: UserPreferencesEmail

    folders: List[UserPreferencesFolder]


class UserPushSubscription(BaseModel):
    auth_key: str = FieldInfo(alias="authKey")

    endpoint: str

    p256dh_key: str = FieldInfo(alias="p256dhKey")


class UserSemanticScholar(BaseModel):
    id: str

    citation_count: Optional[float] = FieldInfo(alias="citationCount", default=None)

    external_ids: Optional[List[Optional[object]]] = FieldInfo(alias="externalIds", default=None)

    h_index: Optional[float] = FieldInfo(alias="hIndex", default=None)

    homepage: Optional[str] = None

    paper_count: Optional[float] = FieldInfo(alias="paperCount", default=None)


class UserFeatured(BaseModel):
    event_id: Optional[str] = FieldInfo(alias="eventId", default=None)

    paper_version_id: Optional[str] = FieldInfo(alias="paperVersionId", default=None)

    type: Literal["video", "paper"]


class User(BaseModel):
    id: str

    avatar: Optional[List[UserAvatar]] = None

    biography: Optional[str] = None

    bluesky_username: Optional[str] = FieldInfo(alias="blueskyUsername", default=None)

    email: str

    first_login: bool = FieldInfo(alias="firstLogin")

    follower_count: float = FieldInfo(alias="followerCount")

    following_count: float = FieldInfo(alias="followingCount")

    following_topics: List[str] = FieldInfo(alias="followingTopics")

    following_topics_count: float = FieldInfo(alias="followingTopicsCount")

    github_username: Optional[str] = FieldInfo(alias="githubUsername", default=None)

    google_scholar_id: Optional[str] = FieldInfo(alias="googleScholarId", default=None)

    institution: Optional[str] = None

    linkedin_username: Optional[str] = FieldInfo(alias="linkedinUsername", default=None)

    location: Optional[str] = None

    orcid_id: Optional[str] = FieldInfo(alias="orcidId", default=None)

    preferences: UserPreferences

    public_email: Optional[str] = FieldInfo(alias="publicEmail", default=None)

    push_subscriptions: List[UserPushSubscription] = FieldInfo(alias="pushSubscriptions")

    real_name: str = FieldInfo(alias="realName")

    reputation: float

    requested_implementations: List[str] = FieldInfo(alias="requestedImplementations")

    role: Literal["user", "reviewer", "admin", "bot"]

    semantic_scholar: Optional[UserSemanticScholar] = FieldInfo(alias="semanticScholar", default=None)

    username: str

    verified: bool

    voted_paper_groups: List[str] = FieldInfo(alias="votedPaperGroups")

    weekly_reputation: float = FieldInfo(alias="weeklyReputation")

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)

    featured: Optional[List[UserFeatured]] = None

    following_organizations: Optional[List[str]] = FieldInfo(alias="followingOrganizations", default=None)


class V3GetCurrentUserResponse(BaseModel):
    badges: Badges

    preferences: Preferences

    user: User
