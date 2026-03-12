# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.papers.v3 import x_mention_update_params
from ....types.papers.v3.x_mention_update_response import XMentionUpdateResponse

__all__ = ["XMentionsResource", "AsyncXMentionsResource"]


class XMentionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> XMentionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return XMentionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> XMentionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return XMentionsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def update(
        self,
        paper_group_id: str,
        *,
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XMentionUpdateResponse:
        """
        Search for X (Twitter) mentions of a paper, filter for quality, and save to
        database

        Source file:
        `api-server/src/controllers/papers/v3/get-paper-x-mentions.controller.ts`

        Args:
          paper_group_id: Paper group ID (UUID)

          dry_run: If true, only logs results without saving to database

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return self._post(
            f"/papers/v3/x-mentions/{paper_group_id}",
            body=maybe_transform({"dry_run": dry_run}, x_mention_update_params.XMentionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=XMentionUpdateResponse,
        )

    def delete(
        self,
        paper_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete all X (Twitter) mentions for a paper

        Source file:
        `api-server/src/controllers/papers/v3/delete-paper-x-mentions.controller.ts`

        Args:
          paper_group_id: Paper group ID (UUID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/papers/v3/x-mentions/{paper_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncXMentionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncXMentionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncXMentionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncXMentionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncXMentionsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def update(
        self,
        paper_group_id: str,
        *,
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XMentionUpdateResponse:
        """
        Search for X (Twitter) mentions of a paper, filter for quality, and save to
        database

        Source file:
        `api-server/src/controllers/papers/v3/get-paper-x-mentions.controller.ts`

        Args:
          paper_group_id: Paper group ID (UUID)

          dry_run: If true, only logs results without saving to database

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return await self._post(
            f"/papers/v3/x-mentions/{paper_group_id}",
            body=await async_maybe_transform({"dry_run": dry_run}, x_mention_update_params.XMentionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=XMentionUpdateResponse,
        )

    async def delete(
        self,
        paper_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete all X (Twitter) mentions for a paper

        Source file:
        `api-server/src/controllers/papers/v3/delete-paper-x-mentions.controller.ts`

        Args:
          paper_group_id: Paper group ID (UUID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/papers/v3/x-mentions/{paper_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class XMentionsResourceWithRawResponse:
    def __init__(self, x_mentions: XMentionsResource) -> None:
        self._x_mentions = x_mentions

        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                x_mentions.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = to_raw_response_wrapper(
            x_mentions.delete,
        )


class AsyncXMentionsResourceWithRawResponse:
    def __init__(self, x_mentions: AsyncXMentionsResource) -> None:
        self._x_mentions = x_mentions

        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                x_mentions.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = async_to_raw_response_wrapper(
            x_mentions.delete,
        )


class XMentionsResourceWithStreamingResponse:
    def __init__(self, x_mentions: XMentionsResource) -> None:
        self._x_mentions = x_mentions

        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                x_mentions.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = to_streamed_response_wrapper(
            x_mentions.delete,
        )


class AsyncXMentionsResourceWithStreamingResponse:
    def __init__(self, x_mentions: AsyncXMentionsResource) -> None:
        self._x_mentions = x_mentions

        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                x_mentions.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = async_to_streamed_response_wrapper(
            x_mentions.delete,
        )
