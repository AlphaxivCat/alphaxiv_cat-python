# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2CommentParams", "AnchorPosition", "FocusPosition", "HighlightRect", "HighlightRectRect"]


class V2CommentParams(TypedDict, total=False):
    anchor_position: Required[Annotated[Optional[AnchorPosition], PropertyInfo(alias="anchorPosition")]]

    body: Required[str]

    focus_position: Required[Annotated[Optional[FocusPosition], PropertyInfo(alias="focusPosition")]]

    highlight_rects: Required[Annotated[Optional[Iterable[HighlightRect]], PropertyInfo(alias="highlightRects")]]

    parent_comment_id: Required[Annotated[Optional[str], PropertyInfo(alias="parentCommentId")]]

    selected_text: Required[Annotated[Optional[str], PropertyInfo(alias="selectedText")]]

    tag: Required[Optional[Literal["anonymous", "general", "personal", "research", "resources"]]]

    title: Required[Optional[str]]

    highlight_color: Annotated[Optional[str], PropertyInfo(alias="highlightColor")]


class AnchorPosition(TypedDict, total=False):
    offset: Required[float]

    page_index: Required[Annotated[float, PropertyInfo(alias="pageIndex")]]

    span_index: Required[Annotated[float, PropertyInfo(alias="spanIndex")]]


class FocusPosition(TypedDict, total=False):
    offset: Required[float]

    page_index: Required[Annotated[float, PropertyInfo(alias="pageIndex")]]

    span_index: Required[Annotated[float, PropertyInfo(alias="spanIndex")]]


class HighlightRectRect(TypedDict, total=False):
    x1: Required[float]

    x2: Required[float]

    y1: Required[float]

    y2: Required[float]


class HighlightRect(TypedDict, total=False):
    page_index: Required[Annotated[float, PropertyInfo(alias="pageIndex")]]

    rects: Required[Iterable[HighlightRectRect]]
