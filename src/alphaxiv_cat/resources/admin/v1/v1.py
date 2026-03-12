# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .emails import (
    EmailsResource,
    AsyncEmailsResource,
    EmailsResourceWithRawResponse,
    AsyncEmailsResourceWithRawResponse,
    EmailsResourceWithStreamingResponse,
    AsyncEmailsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.admin import v1_get_moderator_feed_params, v1_lookup_user_by_email_params
from ...._base_client import make_request_options
from ....types.admin.v1_get_moderator_feed_response import V1GetModeratorFeedResponse
from ....types.admin.v1_lookup_user_by_email_response import V1LookupUserByEmailResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def emails(self) -> EmailsResource:
        return EmailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def get_moderator_feed(
        self,
        *,
        feed_type: Literal["all", "flagged", "recent"] | Omit = omit,
        page: str | Omit = omit,
        page_size: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetModeratorFeedResponse:
        """
        Get page of comments for moderator feed

        Source file:
        `api-server/src/controllers/admin/v1/get-moderator-feed.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/v1/moderator-feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "feed_type": feed_type,
                        "page": page,
                        "page_size": page_size,
                    },
                    v1_get_moderator_feed_params.V1GetModeratorFeedParams,
                ),
            ),
            cast_to=V1GetModeratorFeedResponse,
        )

    def lookup_user_by_email(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1LookupUserByEmailResponse:
        """
        Look up a user by email address (admin only)

        Source file:
        `api-server/src/controllers/admin/v1/lookup-user-by-email.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/v1/lookup-user-by-email",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"email": email}, v1_lookup_user_by_email_params.V1LookupUserByEmailParams),
            ),
            cast_to=V1LookupUserByEmailResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def emails(self) -> AsyncEmailsResource:
        return AsyncEmailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def get_moderator_feed(
        self,
        *,
        feed_type: Literal["all", "flagged", "recent"] | Omit = omit,
        page: str | Omit = omit,
        page_size: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetModeratorFeedResponse:
        """
        Get page of comments for moderator feed

        Source file:
        `api-server/src/controllers/admin/v1/get-moderator-feed.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/v1/moderator-feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "feed_type": feed_type,
                        "page": page,
                        "page_size": page_size,
                    },
                    v1_get_moderator_feed_params.V1GetModeratorFeedParams,
                ),
            ),
            cast_to=V1GetModeratorFeedResponse,
        )

    async def lookup_user_by_email(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1LookupUserByEmailResponse:
        """
        Look up a user by email address (admin only)

        Source file:
        `api-server/src/controllers/admin/v1/lookup-user-by-email.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/v1/lookup-user-by-email",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"email": email}, v1_lookup_user_by_email_params.V1LookupUserByEmailParams
                ),
            ),
            cast_to=V1LookupUserByEmailResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.get_moderator_feed = to_raw_response_wrapper(
            v1.get_moderator_feed,
        )
        self.lookup_user_by_email = to_raw_response_wrapper(
            v1.lookup_user_by_email,
        )

    @cached_property
    def emails(self) -> EmailsResourceWithRawResponse:
        return EmailsResourceWithRawResponse(self._v1.emails)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.get_moderator_feed = async_to_raw_response_wrapper(
            v1.get_moderator_feed,
        )
        self.lookup_user_by_email = async_to_raw_response_wrapper(
            v1.lookup_user_by_email,
        )

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithRawResponse:
        return AsyncEmailsResourceWithRawResponse(self._v1.emails)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.get_moderator_feed = to_streamed_response_wrapper(
            v1.get_moderator_feed,
        )
        self.lookup_user_by_email = to_streamed_response_wrapper(
            v1.lookup_user_by_email,
        )

    @cached_property
    def emails(self) -> EmailsResourceWithStreamingResponse:
        return EmailsResourceWithStreamingResponse(self._v1.emails)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.get_moderator_feed = async_to_streamed_response_wrapper(
            v1.get_moderator_feed,
        )
        self.lookup_user_by_email = async_to_streamed_response_wrapper(
            v1.lookup_user_by_email,
        )

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithStreamingResponse:
        return AsyncEmailsResourceWithStreamingResponse(self._v1.emails)
