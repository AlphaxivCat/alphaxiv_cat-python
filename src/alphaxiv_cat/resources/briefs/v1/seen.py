# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
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
from ....types.briefs.v1 import seen_mark_seen_params
from ....types.briefs.v1.seen_get_seen_response import SeenGetSeenResponse

__all__ = ["SeenResource", "AsyncSeenResource"]


class SeenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SeenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return SeenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return SeenResourceWithStreamingResponse(self)

    def get_seen(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SeenGetSeenResponse:
        """
        Returns the list of paper group IDs the current user has already viewed as
        briefs

        Source file: `api-server/src/controllers/briefs/v1/get-seen.controller.ts`
        """
        return self._get(
            "/briefs/v1/seen",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SeenGetSeenResponse,
        )

    def mark_seen(
        self,
        *,
        paper_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Records that the current user has viewed a brief for the given paper group

        Source file: `api-server/src/controllers/briefs/v1/mark-seen.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/briefs/v1/seen",
            body=maybe_transform({"paper_group_id": paper_group_id}, seen_mark_seen_params.SeenMarkSeenParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSeenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSeenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSeenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncSeenResourceWithStreamingResponse(self)

    async def get_seen(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SeenGetSeenResponse:
        """
        Returns the list of paper group IDs the current user has already viewed as
        briefs

        Source file: `api-server/src/controllers/briefs/v1/get-seen.controller.ts`
        """
        return await self._get(
            "/briefs/v1/seen",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SeenGetSeenResponse,
        )

    async def mark_seen(
        self,
        *,
        paper_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Records that the current user has viewed a brief for the given paper group

        Source file: `api-server/src/controllers/briefs/v1/mark-seen.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/briefs/v1/seen",
            body=await async_maybe_transform(
                {"paper_group_id": paper_group_id}, seen_mark_seen_params.SeenMarkSeenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SeenResourceWithRawResponse:
    def __init__(self, seen: SeenResource) -> None:
        self._seen = seen

        self.get_seen = to_raw_response_wrapper(
            seen.get_seen,
        )
        self.mark_seen = to_raw_response_wrapper(
            seen.mark_seen,
        )


class AsyncSeenResourceWithRawResponse:
    def __init__(self, seen: AsyncSeenResource) -> None:
        self._seen = seen

        self.get_seen = async_to_raw_response_wrapper(
            seen.get_seen,
        )
        self.mark_seen = async_to_raw_response_wrapper(
            seen.mark_seen,
        )


class SeenResourceWithStreamingResponse:
    def __init__(self, seen: SeenResource) -> None:
        self._seen = seen

        self.get_seen = to_streamed_response_wrapper(
            seen.get_seen,
        )
        self.mark_seen = to_streamed_response_wrapper(
            seen.mark_seen,
        )


class AsyncSeenResourceWithStreamingResponse:
    def __init__(self, seen: AsyncSeenResource) -> None:
        self._seen = seen

        self.get_seen = async_to_streamed_response_wrapper(
            seen.get_seen,
        )
        self.mark_seen = async_to_streamed_response_wrapper(
            seen.mark_seen,
        )
