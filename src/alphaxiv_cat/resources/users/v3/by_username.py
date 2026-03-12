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
from ....types.users.v3.by_username_get_user_response import ByUsernameGetUserResponse
from ....types.users.v3.by_username_get_profile_page_response import ByUsernameGetProfilePageResponse

__all__ = ["ByUsernameResource", "AsyncByUsernameResource"]


class ByUsernameResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ByUsernameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return ByUsernameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ByUsernameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return ByUsernameResourceWithStreamingResponse(self)

    def get_profile_page(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ByUsernameGetProfilePageResponse:
        """
        This route is specifically for the Client's user page

        Source file:
        `api-server/src/controllers/users/v3/get-profile-page-by-username.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/v3/by-username/{username}/profile-page",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByUsernameGetProfilePageResponse,
        )

    def get_user(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ByUsernameGetUserResponse:
        """
        Retrieve a user's basic information given its username

        Source file:
        `api-server/src/controllers/users/v3/get-user-by-username.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/v3/by-username/{username}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByUsernameGetUserResponse,
        )


class AsyncByUsernameResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncByUsernameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncByUsernameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncByUsernameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncByUsernameResourceWithStreamingResponse(self)

    async def get_profile_page(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ByUsernameGetProfilePageResponse:
        """
        This route is specifically for the Client's user page

        Source file:
        `api-server/src/controllers/users/v3/get-profile-page-by-username.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/v3/by-username/{username}/profile-page",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByUsernameGetProfilePageResponse,
        )

    async def get_user(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ByUsernameGetUserResponse:
        """
        Retrieve a user's basic information given its username

        Source file:
        `api-server/src/controllers/users/v3/get-user-by-username.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/v3/by-username/{username}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByUsernameGetUserResponse,
        )


class ByUsernameResourceWithRawResponse:
    def __init__(self, by_username: ByUsernameResource) -> None:
        self._by_username = by_username

        self.get_profile_page = to_raw_response_wrapper(
            by_username.get_profile_page,
        )
        self.get_user = to_raw_response_wrapper(
            by_username.get_user,
        )


class AsyncByUsernameResourceWithRawResponse:
    def __init__(self, by_username: AsyncByUsernameResource) -> None:
        self._by_username = by_username

        self.get_profile_page = async_to_raw_response_wrapper(
            by_username.get_profile_page,
        )
        self.get_user = async_to_raw_response_wrapper(
            by_username.get_user,
        )


class ByUsernameResourceWithStreamingResponse:
    def __init__(self, by_username: ByUsernameResource) -> None:
        self._by_username = by_username

        self.get_profile_page = to_streamed_response_wrapper(
            by_username.get_profile_page,
        )
        self.get_user = to_streamed_response_wrapper(
            by_username.get_user,
        )


class AsyncByUsernameResourceWithStreamingResponse:
    def __init__(self, by_username: AsyncByUsernameResource) -> None:
        self._by_username = by_username

        self.get_profile_page = async_to_streamed_response_wrapper(
            by_username.get_profile_page,
        )
        self.get_user = async_to_streamed_response_wrapper(
            by_username.get_user,
        )
