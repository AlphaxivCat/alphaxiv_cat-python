# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.google_scholar import v1_connect_params, v1_set_email_params, v1_verify_email_params
from ...types.google_scholar.v1_sync_response import V1SyncResponse
from ...types.google_scholar.v1_resync_response import V1ResyncResponse
from ...types.google_scholar.v1_connect_response import V1ConnectResponse
from ...types.google_scholar.v1_get_report_response import V1GetReportResponse
from ...types.google_scholar.v1_get_status_response import V1GetStatusResponse
from ...types.google_scholar.v1_verify_email_response import V1VerifyEmailResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def connect(
        self,
        *,
        google_scholar_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ConnectResponse:
        """
        Start connecting Google Scholar profile to user account, or replace a pending
        connection with a different profile

        Source file:
        `api-server/src/controllers/google-scholar/v1/connect.controller.ts`

        Args:
          google_scholar_id: Google Scholar ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/google-scholar/v1",
            body=maybe_transform({"google_scholar_id": google_scholar_id}, v1_connect_params.V1ConnectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ConnectResponse,
        )

    def delete_connection(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove Google Scholar ID and queued papers from a user

        Source file: `api-server/src/controllers/google-scholar/v1/delete.controller.ts`
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/google-scholar/v1",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_report(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetReportResponse:
        """
        Get a full report of a user's Google Scholar sync (including lists of papers)

        Source file: `api-server/src/controllers/google-scholar/v1/report.controller.ts`
        """
        return self._get(
            "/google-scholar/v1/report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetReportResponse,
        )

    def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetStatusResponse:
        """
        Get status of user's Google Scholar sync

        Source file: `api-server/src/controllers/google-scholar/v1/status.controller.ts`
        """
        return self._get(
            "/google-scholar/v1/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetStatusResponse,
        )

    def resync(
        self,
        mode: Literal["all", "new"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ResyncResponse:
        """
        Start a new Google Scholar sync for this user

        Source file: `api-server/src/controllers/google-scholar/v1/resync.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mode:
            raise ValueError(f"Expected a non-empty value for `mode` but received {mode!r}")
        return self._post(
            path_template("/google-scholar/v1/resync/{mode}", mode=mode),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ResyncResponse,
        )

    def set_email(
        self,
        *,
        local_part: str,
        verify_account_email: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set the local-part of a user's Google Scholar institutional email and send a
        verification email to that address

        Source file:
        `api-server/src/controllers/google-scholar/v1/set-email.controller.ts`

        Args:
          local_part: Institutional email local-part

          verify_account_email: Send verification code to the user's primary email instead of the institutional
              email. Admin only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/google-scholar/v1/email",
            body=maybe_transform(
                {
                    "local_part": local_part,
                    "verify_account_email": verify_account_email,
                },
                v1_set_email_params.V1SetEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def sync(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1SyncResponse:
        """
        Make some progress syncing a user's Google Scholar papers

        Source file: `api-server/src/controllers/google-scholar/v1/sync.controller.ts`
        """
        return self._post(
            "/google-scholar/v1/sync",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1SyncResponse,
        )

    def verify_email(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1VerifyEmailResponse:
        """
        Verify a user's Google Scholar email by entering the code sent to that email

        Source file: `api-server/src/controllers/google-scholar/v1/verify.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/google-scholar/v1/verify",
            body=maybe_transform({"code": code}, v1_verify_email_params.V1VerifyEmailParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1VerifyEmailResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def connect(
        self,
        *,
        google_scholar_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ConnectResponse:
        """
        Start connecting Google Scholar profile to user account, or replace a pending
        connection with a different profile

        Source file:
        `api-server/src/controllers/google-scholar/v1/connect.controller.ts`

        Args:
          google_scholar_id: Google Scholar ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/google-scholar/v1",
            body=await async_maybe_transform(
                {"google_scholar_id": google_scholar_id}, v1_connect_params.V1ConnectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ConnectResponse,
        )

    async def delete_connection(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove Google Scholar ID and queued papers from a user

        Source file: `api-server/src/controllers/google-scholar/v1/delete.controller.ts`
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/google-scholar/v1",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_report(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetReportResponse:
        """
        Get a full report of a user's Google Scholar sync (including lists of papers)

        Source file: `api-server/src/controllers/google-scholar/v1/report.controller.ts`
        """
        return await self._get(
            "/google-scholar/v1/report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetReportResponse,
        )

    async def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetStatusResponse:
        """
        Get status of user's Google Scholar sync

        Source file: `api-server/src/controllers/google-scholar/v1/status.controller.ts`
        """
        return await self._get(
            "/google-scholar/v1/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetStatusResponse,
        )

    async def resync(
        self,
        mode: Literal["all", "new"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ResyncResponse:
        """
        Start a new Google Scholar sync for this user

        Source file: `api-server/src/controllers/google-scholar/v1/resync.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mode:
            raise ValueError(f"Expected a non-empty value for `mode` but received {mode!r}")
        return await self._post(
            path_template("/google-scholar/v1/resync/{mode}", mode=mode),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ResyncResponse,
        )

    async def set_email(
        self,
        *,
        local_part: str,
        verify_account_email: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set the local-part of a user's Google Scholar institutional email and send a
        verification email to that address

        Source file:
        `api-server/src/controllers/google-scholar/v1/set-email.controller.ts`

        Args:
          local_part: Institutional email local-part

          verify_account_email: Send verification code to the user's primary email instead of the institutional
              email. Admin only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/google-scholar/v1/email",
            body=await async_maybe_transform(
                {
                    "local_part": local_part,
                    "verify_account_email": verify_account_email,
                },
                v1_set_email_params.V1SetEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def sync(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1SyncResponse:
        """
        Make some progress syncing a user's Google Scholar papers

        Source file: `api-server/src/controllers/google-scholar/v1/sync.controller.ts`
        """
        return await self._post(
            "/google-scholar/v1/sync",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1SyncResponse,
        )

    async def verify_email(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1VerifyEmailResponse:
        """
        Verify a user's Google Scholar email by entering the code sent to that email

        Source file: `api-server/src/controllers/google-scholar/v1/verify.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/google-scholar/v1/verify",
            body=await async_maybe_transform({"code": code}, v1_verify_email_params.V1VerifyEmailParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1VerifyEmailResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.connect = to_raw_response_wrapper(
            v1.connect,
        )
        self.delete_connection = to_raw_response_wrapper(
            v1.delete_connection,
        )
        self.get_report = to_raw_response_wrapper(
            v1.get_report,
        )
        self.get_status = to_raw_response_wrapper(
            v1.get_status,
        )
        self.resync = to_raw_response_wrapper(
            v1.resync,
        )
        self.set_email = to_raw_response_wrapper(
            v1.set_email,
        )
        self.sync = to_raw_response_wrapper(
            v1.sync,
        )
        self.verify_email = to_raw_response_wrapper(
            v1.verify_email,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.connect = async_to_raw_response_wrapper(
            v1.connect,
        )
        self.delete_connection = async_to_raw_response_wrapper(
            v1.delete_connection,
        )
        self.get_report = async_to_raw_response_wrapper(
            v1.get_report,
        )
        self.get_status = async_to_raw_response_wrapper(
            v1.get_status,
        )
        self.resync = async_to_raw_response_wrapper(
            v1.resync,
        )
        self.set_email = async_to_raw_response_wrapper(
            v1.set_email,
        )
        self.sync = async_to_raw_response_wrapper(
            v1.sync,
        )
        self.verify_email = async_to_raw_response_wrapper(
            v1.verify_email,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.connect = to_streamed_response_wrapper(
            v1.connect,
        )
        self.delete_connection = to_streamed_response_wrapper(
            v1.delete_connection,
        )
        self.get_report = to_streamed_response_wrapper(
            v1.get_report,
        )
        self.get_status = to_streamed_response_wrapper(
            v1.get_status,
        )
        self.resync = to_streamed_response_wrapper(
            v1.resync,
        )
        self.set_email = to_streamed_response_wrapper(
            v1.set_email,
        )
        self.sync = to_streamed_response_wrapper(
            v1.sync,
        )
        self.verify_email = to_streamed_response_wrapper(
            v1.verify_email,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.connect = async_to_streamed_response_wrapper(
            v1.connect,
        )
        self.delete_connection = async_to_streamed_response_wrapper(
            v1.delete_connection,
        )
        self.get_report = async_to_streamed_response_wrapper(
            v1.get_report,
        )
        self.get_status = async_to_streamed_response_wrapper(
            v1.get_status,
        )
        self.resync = async_to_streamed_response_wrapper(
            v1.resync,
        )
        self.set_email = async_to_streamed_response_wrapper(
            v1.set_email,
        )
        self.sync = async_to_streamed_response_wrapper(
            v1.sync,
        )
        self.verify_email = async_to_streamed_response_wrapper(
            v1.verify_email,
        )
