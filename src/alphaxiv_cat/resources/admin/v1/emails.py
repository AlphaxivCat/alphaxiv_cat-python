# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.admin.v1 import email_send_weekly_digest_params

__all__ = ["EmailsResource", "AsyncEmailsResource"]


class EmailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return EmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return EmailsResourceWithStreamingResponse(self)

    def send_weekly_digest(
        self,
        *,
        a: email_send_weekly_digest_params.A | Omit = omit,
        b: email_send_weekly_digest_params.B | Omit = omit,
        events: Iterable[email_send_weekly_digest_params.Event] | Omit = omit,
        role: Literal["admin", "user"] | Omit = omit,
        test_batch_size: int | Omit = omit,
        test_emails: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Queue weekly digest emails to users

        Source file:
        `api-server/file:/app/api-server/src/controllers/admin/v1/emails/send-weekly-digest.controller.ts`

        Args:
          a: Text overrides for copy variant A

          b: Text overrides for copy variant B

          events: Custom events to include, both variants

          role: Filter by user role

          test_batch_size: Test mode: page size override, to exercise batching

          test_emails: Test mode: only these addresses can receive the digest

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/admin/v1/emails/send-weekly-digest",
            body=maybe_transform(
                {
                    "a": a,
                    "b": b,
                    "events": events,
                    "role": role,
                    "test_batch_size": test_batch_size,
                    "test_emails": test_emails,
                },
                email_send_weekly_digest_params.EmailSendWeeklyDigestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEmailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncEmailsResourceWithStreamingResponse(self)

    async def send_weekly_digest(
        self,
        *,
        a: email_send_weekly_digest_params.A | Omit = omit,
        b: email_send_weekly_digest_params.B | Omit = omit,
        events: Iterable[email_send_weekly_digest_params.Event] | Omit = omit,
        role: Literal["admin", "user"] | Omit = omit,
        test_batch_size: int | Omit = omit,
        test_emails: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Queue weekly digest emails to users

        Source file:
        `api-server/file:/app/api-server/src/controllers/admin/v1/emails/send-weekly-digest.controller.ts`

        Args:
          a: Text overrides for copy variant A

          b: Text overrides for copy variant B

          events: Custom events to include, both variants

          role: Filter by user role

          test_batch_size: Test mode: page size override, to exercise batching

          test_emails: Test mode: only these addresses can receive the digest

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/admin/v1/emails/send-weekly-digest",
            body=await async_maybe_transform(
                {
                    "a": a,
                    "b": b,
                    "events": events,
                    "role": role,
                    "test_batch_size": test_batch_size,
                    "test_emails": test_emails,
                },
                email_send_weekly_digest_params.EmailSendWeeklyDigestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.send_weekly_digest = to_raw_response_wrapper(
            emails.send_weekly_digest,
        )


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.send_weekly_digest = async_to_raw_response_wrapper(
            emails.send_weekly_digest,
        )


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.send_weekly_digest = to_streamed_response_wrapper(
            emails.send_weekly_digest,
        )


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.send_weekly_digest = async_to_streamed_response_wrapper(
            emails.send_weekly_digest,
        )
