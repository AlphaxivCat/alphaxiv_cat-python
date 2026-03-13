# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .v4.v4 import (
    V4Resource,
    AsyncV4Resource,
    V4ResourceWithRawResponse,
    AsyncV4ResourceWithRawResponse,
    V4ResourceWithStreamingResponse,
    AsyncV4ResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.notification_send_kickoff_notification_emails_response import (
    NotificationSendKickoffNotificationEmailsResponse,
)

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    @cached_property
    def v4(self) -> V4Resource:
        return V4Resource(self._client)

    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def send_kickoff_notification_emails(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationSendKickoffNotificationEmailsResponse:
        """
        Queues notification emails for all users with unseen notifications

        Source file:
        `api-server/src/controllers/v2/notifications/kickoff-notification-emails.controller.ts`
        """
        return self._post(
            "/v2/notifications/kickoff-notification-emails",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationSendKickoffNotificationEmailsResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    @cached_property
    def v4(self) -> AsyncV4Resource:
        return AsyncV4Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    async def send_kickoff_notification_emails(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationSendKickoffNotificationEmailsResponse:
        """
        Queues notification emails for all users with unseen notifications

        Source file:
        `api-server/src/controllers/v2/notifications/kickoff-notification-emails.controller.ts`
        """
        return await self._post(
            "/v2/notifications/kickoff-notification-emails",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationSendKickoffNotificationEmailsResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.send_kickoff_notification_emails = to_raw_response_wrapper(
            notifications.send_kickoff_notification_emails,
        )

    @cached_property
    def v4(self) -> V4ResourceWithRawResponse:
        return V4ResourceWithRawResponse(self._notifications.v4)


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.send_kickoff_notification_emails = async_to_raw_response_wrapper(
            notifications.send_kickoff_notification_emails,
        )

    @cached_property
    def v4(self) -> AsyncV4ResourceWithRawResponse:
        return AsyncV4ResourceWithRawResponse(self._notifications.v4)


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.send_kickoff_notification_emails = to_streamed_response_wrapper(
            notifications.send_kickoff_notification_emails,
        )

    @cached_property
    def v4(self) -> V4ResourceWithStreamingResponse:
        return V4ResourceWithStreamingResponse(self._notifications.v4)


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.send_kickoff_notification_emails = async_to_streamed_response_wrapper(
            notifications.send_kickoff_notification_emails,
        )

    @cached_property
    def v4(self) -> AsyncV4ResourceWithStreamingResponse:
        return AsyncV4ResourceWithStreamingResponse(self._notifications.v4)
