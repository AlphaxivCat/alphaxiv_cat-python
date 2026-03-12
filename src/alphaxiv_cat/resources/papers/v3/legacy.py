# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.papers.v3.legacy_retrieve_response import LegacyRetrieveResponse
from ....types.papers.v3.legacy_retrieve_comments_response import LegacyRetrieveCommentsResponse

__all__ = ["LegacyResource", "AsyncLegacyResource"]


class LegacyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LegacyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return LegacyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LegacyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return LegacyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        unresolved: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LegacyRetrieveResponse:
        """Retrieve paper version metadata and comments.

        Fetches from ArXiv if needed. This
        runs the old id resolution implementation, old fetching service, and old JSON
        format. Do not write new code with this please.

        Source file:
        `api-server/src/controllers/papers/v3/legacy/get-v2-paper-for-display.controller.ts`

        Args:
          unresolved: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unresolved:
            raise ValueError(f"Expected a non-empty value for `unresolved` but received {unresolved!r}")
        return self._get(
            f"/papers/v3/legacy/{unresolved}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LegacyRetrieveResponse,
        )

    def retrieve_comments(
        self,
        group: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LegacyRetrieveCommentsResponse:
        """Retrieve paper group comments.

        Does not distinguish "paper group does not exist"
        from "there are no comments"

        Source file:
        `api-server/src/controllers/papers/v3/legacy/get-v2-comments.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group:
            raise ValueError(f"Expected a non-empty value for `group` but received {group!r}")
        return self._get(
            f"/papers/v3/legacy/{group}/comments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LegacyRetrieveCommentsResponse,
        )


class AsyncLegacyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLegacyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLegacyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLegacyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncLegacyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        unresolved: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LegacyRetrieveResponse:
        """Retrieve paper version metadata and comments.

        Fetches from ArXiv if needed. This
        runs the old id resolution implementation, old fetching service, and old JSON
        format. Do not write new code with this please.

        Source file:
        `api-server/src/controllers/papers/v3/legacy/get-v2-paper-for-display.controller.ts`

        Args:
          unresolved: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unresolved:
            raise ValueError(f"Expected a non-empty value for `unresolved` but received {unresolved!r}")
        return await self._get(
            f"/papers/v3/legacy/{unresolved}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LegacyRetrieveResponse,
        )

    async def retrieve_comments(
        self,
        group: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LegacyRetrieveCommentsResponse:
        """Retrieve paper group comments.

        Does not distinguish "paper group does not exist"
        from "there are no comments"

        Source file:
        `api-server/src/controllers/papers/v3/legacy/get-v2-comments.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group:
            raise ValueError(f"Expected a non-empty value for `group` but received {group!r}")
        return await self._get(
            f"/papers/v3/legacy/{group}/comments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LegacyRetrieveCommentsResponse,
        )


class LegacyResourceWithRawResponse:
    def __init__(self, legacy: LegacyResource) -> None:
        self._legacy = legacy

        self.retrieve = to_raw_response_wrapper(
            legacy.retrieve,
        )
        self.retrieve_comments = to_raw_response_wrapper(
            legacy.retrieve_comments,
        )


class AsyncLegacyResourceWithRawResponse:
    def __init__(self, legacy: AsyncLegacyResource) -> None:
        self._legacy = legacy

        self.retrieve = async_to_raw_response_wrapper(
            legacy.retrieve,
        )
        self.retrieve_comments = async_to_raw_response_wrapper(
            legacy.retrieve_comments,
        )


class LegacyResourceWithStreamingResponse:
    def __init__(self, legacy: LegacyResource) -> None:
        self._legacy = legacy

        self.retrieve = to_streamed_response_wrapper(
            legacy.retrieve,
        )
        self.retrieve_comments = to_streamed_response_wrapper(
            legacy.retrieve_comments,
        )


class AsyncLegacyResourceWithStreamingResponse:
    def __init__(self, legacy: AsyncLegacyResource) -> None:
        self._legacy = legacy

        self.retrieve = async_to_streamed_response_wrapper(
            legacy.retrieve,
        )
        self.retrieve_comments = async_to_streamed_response_wrapper(
            legacy.retrieve_comments,
        )
