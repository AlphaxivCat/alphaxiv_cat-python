# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.papers import v2_comment_params
from ...types.papers.v2_comment_response import V2CommentResponse

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)

    def comment(
        self,
        version: str,
        *,
        anchor_position: Optional[v2_comment_params.AnchorPosition],
        body: str,
        focus_position: Optional[v2_comment_params.FocusPosition],
        highlight_rects: Optional[Iterable[v2_comment_params.HighlightRect]],
        parent_comment_id: Optional[str],
        selected_text: Optional[str],
        tag: Optional[Literal["anonymous", "general", "personal", "research", "resources"]],
        title: Optional[str],
        highlight_color: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2CommentResponse:
        """
        Add comment to paper version

        Source file: `api-server/src/controllers/papers/v2/add-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._post(
            f"/papers/v2/{version}/comment",
            body=maybe_transform(
                {
                    "anchor_position": anchor_position,
                    "body": body,
                    "focus_position": focus_position,
                    "highlight_rects": highlight_rects,
                    "parent_comment_id": parent_comment_id,
                    "selected_text": selected_text,
                    "tag": tag,
                    "title": title,
                    "highlight_color": highlight_color,
                },
                v2_comment_params.V2CommentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2CommentResponse,
        )


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)

    async def comment(
        self,
        version: str,
        *,
        anchor_position: Optional[v2_comment_params.AnchorPosition],
        body: str,
        focus_position: Optional[v2_comment_params.FocusPosition],
        highlight_rects: Optional[Iterable[v2_comment_params.HighlightRect]],
        parent_comment_id: Optional[str],
        selected_text: Optional[str],
        tag: Optional[Literal["anonymous", "general", "personal", "research", "resources"]],
        title: Optional[str],
        highlight_color: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2CommentResponse:
        """
        Add comment to paper version

        Source file: `api-server/src/controllers/papers/v2/add-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return await self._post(
            f"/papers/v2/{version}/comment",
            body=await async_maybe_transform(
                {
                    "anchor_position": anchor_position,
                    "body": body,
                    "focus_position": focus_position,
                    "highlight_rects": highlight_rects,
                    "parent_comment_id": parent_comment_id,
                    "selected_text": selected_text,
                    "tag": tag,
                    "title": title,
                    "highlight_color": highlight_color,
                },
                v2_comment_params.V2CommentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2CommentResponse,
        )


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.comment = to_raw_response_wrapper(
            v2.comment,
        )


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.comment = async_to_raw_response_wrapper(
            v2.comment,
        )


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.comment = to_streamed_response_wrapper(
            v2.comment,
        )


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.comment = async_to_streamed_response_wrapper(
            v2.comment,
        )
