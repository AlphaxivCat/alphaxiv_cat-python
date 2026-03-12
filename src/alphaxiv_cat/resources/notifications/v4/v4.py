# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .archive import (
    ArchiveResource,
    AsyncArchiveResource,
    ArchiveResourceWithRawResponse,
    AsyncArchiveResourceWithRawResponse,
    ArchiveResourceWithStreamingResponse,
    AsyncArchiveResourceWithStreamingResponse,
)
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
from ....types.notifications import v4_subscribe_params, v4_unsubscribe_params
from ....types.notifications.v4_list_notifications_response import V4ListNotificationsResponse

__all__ = ["V4Resource", "AsyncV4Resource"]


class V4Resource(SyncAPIResource):
    @cached_property
    def archive(self) -> ArchiveResource:
        return ArchiveResource(self._client)

    @cached_property
    def with_raw_response(self) -> V4ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V4ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return V4ResourceWithStreamingResponse(self)

    def list_notifications(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V4ListNotificationsResponse:
        """
        Returns all active notifications.

        Source file:
        `api-server/src/controllers/notifications/v4/get-notifications.controller.ts`
        """
        return self._get(
            "/notifications/v4",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V4ListNotificationsResponse,
        )

    def subscribe(
        self,
        *,
        subscription: v4_subscribe_params.Subscription,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Subscribes the current user to push notifications

        Source file:
        `api-server/src/controllers/notifications/v4/subscribe.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/notifications/v4/subscribe",
            body=maybe_transform({"subscription": subscription}, v4_subscribe_params.V4SubscribeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def unsubscribe(
        self,
        *,
        endpoint: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unsubscribes the current user to push notifications

        Source file:
        `api-server/src/controllers/notifications/v4/unsubscribe.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/notifications/v4/unsubscribe",
            body=maybe_transform({"endpoint": endpoint}, v4_unsubscribe_params.V4UnsubscribeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncV4Resource(AsyncAPIResource):
    @cached_property
    def archive(self) -> AsyncArchiveResource:
        return AsyncArchiveResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV4ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV4ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV4ResourceWithStreamingResponse(self)

    async def list_notifications(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V4ListNotificationsResponse:
        """
        Returns all active notifications.

        Source file:
        `api-server/src/controllers/notifications/v4/get-notifications.controller.ts`
        """
        return await self._get(
            "/notifications/v4",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V4ListNotificationsResponse,
        )

    async def subscribe(
        self,
        *,
        subscription: v4_subscribe_params.Subscription,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Subscribes the current user to push notifications

        Source file:
        `api-server/src/controllers/notifications/v4/subscribe.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/notifications/v4/subscribe",
            body=await async_maybe_transform({"subscription": subscription}, v4_subscribe_params.V4SubscribeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def unsubscribe(
        self,
        *,
        endpoint: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unsubscribes the current user to push notifications

        Source file:
        `api-server/src/controllers/notifications/v4/unsubscribe.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/notifications/v4/unsubscribe",
            body=await async_maybe_transform({"endpoint": endpoint}, v4_unsubscribe_params.V4UnsubscribeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class V4ResourceWithRawResponse:
    def __init__(self, v4: V4Resource) -> None:
        self._v4 = v4

        self.list_notifications = to_raw_response_wrapper(
            v4.list_notifications,
        )
        self.subscribe = to_raw_response_wrapper(
            v4.subscribe,
        )
        self.unsubscribe = to_raw_response_wrapper(
            v4.unsubscribe,
        )

    @cached_property
    def archive(self) -> ArchiveResourceWithRawResponse:
        return ArchiveResourceWithRawResponse(self._v4.archive)


class AsyncV4ResourceWithRawResponse:
    def __init__(self, v4: AsyncV4Resource) -> None:
        self._v4 = v4

        self.list_notifications = async_to_raw_response_wrapper(
            v4.list_notifications,
        )
        self.subscribe = async_to_raw_response_wrapper(
            v4.subscribe,
        )
        self.unsubscribe = async_to_raw_response_wrapper(
            v4.unsubscribe,
        )

    @cached_property
    def archive(self) -> AsyncArchiveResourceWithRawResponse:
        return AsyncArchiveResourceWithRawResponse(self._v4.archive)


class V4ResourceWithStreamingResponse:
    def __init__(self, v4: V4Resource) -> None:
        self._v4 = v4

        self.list_notifications = to_streamed_response_wrapper(
            v4.list_notifications,
        )
        self.subscribe = to_streamed_response_wrapper(
            v4.subscribe,
        )
        self.unsubscribe = to_streamed_response_wrapper(
            v4.unsubscribe,
        )

    @cached_property
    def archive(self) -> ArchiveResourceWithStreamingResponse:
        return ArchiveResourceWithStreamingResponse(self._v4.archive)


class AsyncV4ResourceWithStreamingResponse:
    def __init__(self, v4: AsyncV4Resource) -> None:
        self._v4 = v4

        self.list_notifications = async_to_streamed_response_wrapper(
            v4.list_notifications,
        )
        self.subscribe = async_to_streamed_response_wrapper(
            v4.subscribe,
        )
        self.unsubscribe = async_to_streamed_response_wrapper(
            v4.unsubscribe,
        )

    @cached_property
    def archive(self) -> AsyncArchiveResourceWithStreamingResponse:
        return AsyncArchiveResourceWithStreamingResponse(self._v4.archive)
