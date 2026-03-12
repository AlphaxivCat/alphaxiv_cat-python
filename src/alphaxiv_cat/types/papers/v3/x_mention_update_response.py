# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["XMentionUpdateResponse", "Mention", "MentionQuality"]


class MentionQuality(BaseModel):
    contains_profanity: bool = FieldInfo(alias="containsProfanity")

    has_unique_perspective: bool = FieldInfo(alias="hasUniquePerspective")

    is_bot: bool = FieldInfo(alias="isBot")

    is_english: bool = FieldInfo(alias="isEnglish")

    is_grok: bool = FieldInfo(alias="isGrok")

    is_meaningful: bool = FieldInfo(alias="isMeaningful")

    is_relevant: bool = FieldInfo(alias="isRelevant")

    reason: str

    should_include: bool = FieldInfo(alias="shouldInclude")


class Mention(BaseModel):
    author_avatar: str = FieldInfo(alias="authorAvatar")

    author_name: str = FieldInfo(alias="authorName")

    author_username: str = FieldInfo(alias="authorUsername")

    conversation_id: str = FieldInfo(alias="conversationId")

    created_at: str = FieldInfo(alias="createdAt")

    likes: float

    quality: MentionQuality

    replies: float

    retweets: float

    text: str

    tweet_id: str = FieldInfo(alias="tweetId")

    tweet_url: str = FieldInfo(alias="tweetUrl")


class XMentionUpdateResponse(BaseModel):
    mentions: List[Mention]

    quality_tweets_count: float = FieldInfo(alias="qualityTweetsCount")

    total_tweets_found: float = FieldInfo(alias="totalTweetsFound")
