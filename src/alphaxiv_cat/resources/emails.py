# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing_extensions import Literal

import httpx

from ..types import (
    email_process_bounced_email_params,
    email_capture_bounced_emails_params,
    email_process_comment_update_params,
    email_process_general_update_params,
    email_capture_resend_bounced_email_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.email_process_bounced_email_response import EmailProcessBouncedEmailResponse
from ..types.email_capture_bounced_emails_response import EmailCaptureBouncedEmailsResponse
from ..types.email_kickoff_comment_update_response import EmailKickoffCommentUpdateResponse
from ..types.email_kickoff_general_update_response import EmailKickoffGeneralUpdateResponse
from ..types.email_process_comment_update_response import EmailProcessCommentUpdateResponse
from ..types.email_process_general_update_response import EmailProcessGeneralUpdateResponse
from ..types.email_capture_resend_bounced_email_response import EmailCaptureResendBouncedEmailResponse

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

    def capture_bounced_emails(
        self,
        *,
        message: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailCaptureBouncedEmailsResponse:
        """
        Receives bounce notifications from AWS SES via SNS

        Source file:
        `api-server/src/controllers/v1/emails/capture-bounced-emails.controller.ts`

        Args:
          message: Stringified JSON message containing bounce/complaint data

          type: SNS notification type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/emails/capture-bounced-emails",
            body=maybe_transform(
                {
                    "message": message,
                    "type": type,
                },
                email_capture_bounced_emails_params.EmailCaptureBouncedEmailsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailCaptureBouncedEmailsResponse,
        )

    def capture_resend_bounced_email(
        self,
        *,
        data: email_capture_resend_bounced_email_params.Data,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailCaptureResendBouncedEmailResponse:
        """
        Receives bounce notifications from Resend

        Source file:
        `api-server/src/controllers/v1/emails/capture-resend-bounced-emails.controller.ts`

        Args:
          data: Event data containing bounced emails

          type: Event type from Resend

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/emails/capture-resend-bounced-email",
            body=maybe_transform(
                {
                    "data": data,
                    "type": type,
                },
                email_capture_resend_bounced_email_params.EmailCaptureResendBouncedEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailCaptureResendBouncedEmailResponse,
        )

    def kickoff_comment_update(
        self,
        custom: Literal["true", "false"],
        *,
        role: str,
        window: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailKickoffCommentUpdateResponse:
        """
        Kicks off a background job to send comment digest emails to users

        Source file:
        `api-server/src/controllers/v1/emails/kickoff-comment-updates.controller.ts`

        Args:
          role: User role to filter by

          window: Time window in hours

          custom: Whether to use custom digest

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role:
            raise ValueError(f"Expected a non-empty value for `role` but received {role!r}")
        if not window:
            raise ValueError(f"Expected a non-empty value for `window` but received {window!r}")
        if not custom:
            raise ValueError(f"Expected a non-empty value for `custom` but received {custom!r}")
        return self._post(
            f"/v1/emails/kickoff-comment-update/{role}/{window}/{custom}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailKickoffCommentUpdateResponse,
        )

    def kickoff_general_update(
        self,
        role: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailKickoffGeneralUpdateResponse:
        """
        Kicks off a background job to send general digest emails to users

        Source file:
        `api-server/src/controllers/v1/emails/kickoff-general-updates.controller.ts`

        Args:
          role: User role to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role:
            raise ValueError(f"Expected a non-empty value for `role` but received {role!r}")
        return self._post(
            f"/v1/emails/kickoff-general-update/{role}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailKickoffGeneralUpdateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def process_bounced_email(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailProcessBouncedEmailResponse:
        """
        Process a bounced email and update user preferences

        Source file:
        `api-server/src/controllers/v1/emails/process-bounced-email.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/emails/process-bounced-email",
            body=maybe_transform({"email": email}, email_process_bounced_email_params.EmailProcessBouncedEmailParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailProcessBouncedEmailResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def process_comment_update(
        self,
        *,
        user_id: str,
        custom_content: email_process_comment_update_params.CustomContent | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailProcessCommentUpdateResponse:
        """
        Process comment digest email for a user

        Source file:
        `api-server/src/controllers/v1/emails/process-user-comment-update.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/emails/process-comment-update",
            body=maybe_transform(
                {
                    "user_id": user_id,
                    "custom_content": custom_content,
                },
                email_process_comment_update_params.EmailProcessCommentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailProcessCommentUpdateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def process_general_update(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailProcessGeneralUpdateResponse:
        """
        Process general digest email for a user

        Source file:
        `api-server/src/controllers/v1/emails/process-user-general-update.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/emails/process-general-update",
            body=maybe_transform(
                {"user_id": user_id}, email_process_general_update_params.EmailProcessGeneralUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailProcessGeneralUpdateResponse,
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

    async def capture_bounced_emails(
        self,
        *,
        message: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailCaptureBouncedEmailsResponse:
        """
        Receives bounce notifications from AWS SES via SNS

        Source file:
        `api-server/src/controllers/v1/emails/capture-bounced-emails.controller.ts`

        Args:
          message: Stringified JSON message containing bounce/complaint data

          type: SNS notification type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/emails/capture-bounced-emails",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "type": type,
                },
                email_capture_bounced_emails_params.EmailCaptureBouncedEmailsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailCaptureBouncedEmailsResponse,
        )

    async def capture_resend_bounced_email(
        self,
        *,
        data: email_capture_resend_bounced_email_params.Data,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailCaptureResendBouncedEmailResponse:
        """
        Receives bounce notifications from Resend

        Source file:
        `api-server/src/controllers/v1/emails/capture-resend-bounced-emails.controller.ts`

        Args:
          data: Event data containing bounced emails

          type: Event type from Resend

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/emails/capture-resend-bounced-email",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "type": type,
                },
                email_capture_resend_bounced_email_params.EmailCaptureResendBouncedEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailCaptureResendBouncedEmailResponse,
        )

    async def kickoff_comment_update(
        self,
        custom: Literal["true", "false"],
        *,
        role: str,
        window: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailKickoffCommentUpdateResponse:
        """
        Kicks off a background job to send comment digest emails to users

        Source file:
        `api-server/src/controllers/v1/emails/kickoff-comment-updates.controller.ts`

        Args:
          role: User role to filter by

          window: Time window in hours

          custom: Whether to use custom digest

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role:
            raise ValueError(f"Expected a non-empty value for `role` but received {role!r}")
        if not window:
            raise ValueError(f"Expected a non-empty value for `window` but received {window!r}")
        if not custom:
            raise ValueError(f"Expected a non-empty value for `custom` but received {custom!r}")
        return await self._post(
            f"/v1/emails/kickoff-comment-update/{role}/{window}/{custom}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailKickoffCommentUpdateResponse,
        )

    async def kickoff_general_update(
        self,
        role: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailKickoffGeneralUpdateResponse:
        """
        Kicks off a background job to send general digest emails to users

        Source file:
        `api-server/src/controllers/v1/emails/kickoff-general-updates.controller.ts`

        Args:
          role: User role to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role:
            raise ValueError(f"Expected a non-empty value for `role` but received {role!r}")
        return await self._post(
            f"/v1/emails/kickoff-general-update/{role}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailKickoffGeneralUpdateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def process_bounced_email(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailProcessBouncedEmailResponse:
        """
        Process a bounced email and update user preferences

        Source file:
        `api-server/src/controllers/v1/emails/process-bounced-email.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/emails/process-bounced-email",
            body=await async_maybe_transform(
                {"email": email}, email_process_bounced_email_params.EmailProcessBouncedEmailParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailProcessBouncedEmailResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def process_comment_update(
        self,
        *,
        user_id: str,
        custom_content: email_process_comment_update_params.CustomContent | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailProcessCommentUpdateResponse:
        """
        Process comment digest email for a user

        Source file:
        `api-server/src/controllers/v1/emails/process-user-comment-update.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/emails/process-comment-update",
            body=await async_maybe_transform(
                {
                    "user_id": user_id,
                    "custom_content": custom_content,
                },
                email_process_comment_update_params.EmailProcessCommentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailProcessCommentUpdateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def process_general_update(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailProcessGeneralUpdateResponse:
        """
        Process general digest email for a user

        Source file:
        `api-server/src/controllers/v1/emails/process-user-general-update.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/emails/process-general-update",
            body=await async_maybe_transform(
                {"user_id": user_id}, email_process_general_update_params.EmailProcessGeneralUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailProcessGeneralUpdateResponse,
        )


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.capture_bounced_emails = to_raw_response_wrapper(
            emails.capture_bounced_emails,
        )
        self.capture_resend_bounced_email = to_raw_response_wrapper(
            emails.capture_resend_bounced_email,
        )
        self.kickoff_comment_update = to_raw_response_wrapper(
            emails.kickoff_comment_update,
        )
        self.kickoff_general_update = to_raw_response_wrapper(
            emails.kickoff_general_update,
        )
        self.process_bounced_email = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                emails.process_bounced_email,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_comment_update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                emails.process_comment_update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_general_update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                emails.process_general_update,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.capture_bounced_emails = async_to_raw_response_wrapper(
            emails.capture_bounced_emails,
        )
        self.capture_resend_bounced_email = async_to_raw_response_wrapper(
            emails.capture_resend_bounced_email,
        )
        self.kickoff_comment_update = async_to_raw_response_wrapper(
            emails.kickoff_comment_update,
        )
        self.kickoff_general_update = async_to_raw_response_wrapper(
            emails.kickoff_general_update,
        )
        self.process_bounced_email = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                emails.process_bounced_email,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_comment_update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                emails.process_comment_update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_general_update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                emails.process_general_update,  # pyright: ignore[reportDeprecated],
            )
        )


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.capture_bounced_emails = to_streamed_response_wrapper(
            emails.capture_bounced_emails,
        )
        self.capture_resend_bounced_email = to_streamed_response_wrapper(
            emails.capture_resend_bounced_email,
        )
        self.kickoff_comment_update = to_streamed_response_wrapper(
            emails.kickoff_comment_update,
        )
        self.kickoff_general_update = to_streamed_response_wrapper(
            emails.kickoff_general_update,
        )
        self.process_bounced_email = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                emails.process_bounced_email,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_comment_update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                emails.process_comment_update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_general_update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                emails.process_general_update,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.capture_bounced_emails = async_to_streamed_response_wrapper(
            emails.capture_bounced_emails,
        )
        self.capture_resend_bounced_email = async_to_streamed_response_wrapper(
            emails.capture_resend_bounced_email,
        )
        self.kickoff_comment_update = async_to_streamed_response_wrapper(
            emails.kickoff_comment_update,
        )
        self.kickoff_general_update = async_to_streamed_response_wrapper(
            emails.kickoff_general_update,
        )
        self.process_bounced_email = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                emails.process_bounced_email,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_comment_update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                emails.process_comment_update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_general_update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                emails.process_general_update,  # pyright: ignore[reportDeprecated],
            )
        )
