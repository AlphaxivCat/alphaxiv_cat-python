# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.notifications.v4 import archive_list_params, archive_create_params
from ....types.notifications.v4.archive_list_response import ArchiveListResponse
from ....types.notifications.v4.archive_create_response import ArchiveCreateResponse

__all__ = ["ArchiveResource", "AsyncArchiveResource"]


class ArchiveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArchiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return ArchiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArchiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return ArchiveResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArchiveCreateResponse:
        """
        Given an array of IDs to mark as read, move them into the notification archive.
        Invalid notifications are ignored. By checking the returned count, invalid
        client-side state can be detected and corrected.

        Source file:
        `api-server/src/controllers/notifications/v4/archive-notifications.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/notifications/v4/archive",
            body=maybe_transform({"ids": ids}, archive_create_params.ArchiveCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArchiveCreateResponse,
        )

    def list(
        self,
        *,
        before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArchiveListResponse:
        """
        The notification archive is paginated, requiring multiple calls to query long
        history.

        Source file:
        `api-server/src/controllers/notifications/v4/get-archived-notifications.controller.ts`

        Args:
          before: Decimal UNIX time in milliseconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/notifications/v4/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"before": before}, archive_list_params.ArchiveListParams),
            ),
            cast_to=ArchiveListResponse,
        )


class AsyncArchiveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArchiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArchiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArchiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncArchiveResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArchiveCreateResponse:
        """
        Given an array of IDs to mark as read, move them into the notification archive.
        Invalid notifications are ignored. By checking the returned count, invalid
        client-side state can be detected and corrected.

        Source file:
        `api-server/src/controllers/notifications/v4/archive-notifications.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/notifications/v4/archive",
            body=await async_maybe_transform({"ids": ids}, archive_create_params.ArchiveCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArchiveCreateResponse,
        )

    async def list(
        self,
        *,
        before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArchiveListResponse:
        """
        The notification archive is paginated, requiring multiple calls to query long
        history.

        Source file:
        `api-server/src/controllers/notifications/v4/get-archived-notifications.controller.ts`

        Args:
          before: Decimal UNIX time in milliseconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/notifications/v4/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"before": before}, archive_list_params.ArchiveListParams),
            ),
            cast_to=ArchiveListResponse,
        )


class ArchiveResourceWithRawResponse:
    def __init__(self, archive: ArchiveResource) -> None:
        self._archive = archive

        self.create = to_raw_response_wrapper(
            archive.create,
        )
        self.list = to_raw_response_wrapper(
            archive.list,
        )


class AsyncArchiveResourceWithRawResponse:
    def __init__(self, archive: AsyncArchiveResource) -> None:
        self._archive = archive

        self.create = async_to_raw_response_wrapper(
            archive.create,
        )
        self.list = async_to_raw_response_wrapper(
            archive.list,
        )


class ArchiveResourceWithStreamingResponse:
    def __init__(self, archive: ArchiveResource) -> None:
        self._archive = archive

        self.create = to_streamed_response_wrapper(
            archive.create,
        )
        self.list = to_streamed_response_wrapper(
            archive.list,
        )


class AsyncArchiveResourceWithStreamingResponse:
    def __init__(self, archive: AsyncArchiveResource) -> None:
        self._archive = archive

        self.create = async_to_streamed_response_wrapper(
            archive.create,
        )
        self.list = async_to_streamed_response_wrapper(
            archive.list,
        )
