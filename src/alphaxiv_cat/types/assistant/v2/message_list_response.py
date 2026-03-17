# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["MessageListResponse", "MessageListResponseItem"]


class MessageListResponseItem(BaseModel):
    id: str

    content: Optional[str] = None

    feedback_category: Optional[str] = FieldInfo(alias="feedbackCategory", default=None)

    feedback_details: Optional[str] = FieldInfo(alias="feedbackDetails", default=None)

    feedback_type: Optional[Literal["upvote", "downvote"]] = FieldInfo(alias="feedbackType", default=None)

    kind: Optional[str] = None

    model: Optional[str] = None

    parent_message_id: Optional[str] = FieldInfo(alias="parentMessageId", default=None)

    selected_at: str = FieldInfo(alias="selectedAt")

    tool_use_id: Optional[str] = FieldInfo(alias="toolUseId", default=None)

    type: Literal[
        "tool_use",
        "tool_result_text",
        "tool_result_file",
        "input_file",
        "input_text",
        "output_reasoning",
        "output_text",
    ]

    trace: Optional[str] = None


MessageListResponse: TypeAlias = List[MessageListResponseItem]
