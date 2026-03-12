# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["TopicListResponse", "Topic"]


class Topic(BaseModel):
    id: str

    topic: str


class TopicListResponse(BaseModel):
    topics: List[Topic]
