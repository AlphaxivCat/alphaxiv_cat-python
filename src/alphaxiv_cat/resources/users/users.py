# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .v3.v3 import (
    V3Resource,
    AsyncV3Resource,
    V3ResourceWithRawResponse,
    AsyncV3ResourceWithRawResponse,
    V3ResourceWithStreamingResponse,
    AsyncV3ResourceWithStreamingResponse,
)
from ...types import user_get_private_notes_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .preferences.preferences import (
    PreferencesResource,
    AsyncPreferencesResource,
    PreferencesResourceWithRawResponse,
    AsyncPreferencesResourceWithRawResponse,
    PreferencesResourceWithStreamingResponse,
    AsyncPreferencesResourceWithStreamingResponse,
)
from ...types.user_get_private_notes_response import UserGetPrivateNotesResponse
from ...types.user_weigh_weekly_reputation_response import UserWeighWeeklyReputationResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def v3(self) -> V3Resource:
        return V3Resource(self._client)

    @cached_property
    def preferences(self) -> PreferencesResource:
        return PreferencesResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def get_private_notes(
        self,
        uid: str,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetPrivateNotesResponse:
        """
        Get private notes for a user with pagination

        Source file:
        `api-server/src/controllers/v1/users/get-private-notes.controller.ts`

        Args:
          uid: ignored field

          limit: Items per page (default: 10)

          page: Page number (default: 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return self._get(
            f"/v1/users/{uid}/notes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    user_get_private_notes_params.UserGetPrivateNotesParams,
                ),
            ),
            cast_to=UserGetPrivateNotesResponse,
        )

    def weigh_weekly_reputation(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserWeighWeeklyReputationResponse:
        """
        Calculates and updates weekly reputation weights for users

        Source file:
        `api-server/src/controllers/v1/users/weigh-weekly-reputation.controller.ts`
        """
        return self._post(
            "/v1/users/weigh-weekly-reputation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserWeighWeeklyReputationResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def v3(self) -> AsyncV3Resource:
        return AsyncV3Resource(self._client)

    @cached_property
    def preferences(self) -> AsyncPreferencesResource:
        return AsyncPreferencesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def get_private_notes(
        self,
        uid: str,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetPrivateNotesResponse:
        """
        Get private notes for a user with pagination

        Source file:
        `api-server/src/controllers/v1/users/get-private-notes.controller.ts`

        Args:
          uid: ignored field

          limit: Items per page (default: 10)

          page: Page number (default: 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uid:
            raise ValueError(f"Expected a non-empty value for `uid` but received {uid!r}")
        return await self._get(
            f"/v1/users/{uid}/notes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    user_get_private_notes_params.UserGetPrivateNotesParams,
                ),
            ),
            cast_to=UserGetPrivateNotesResponse,
        )

    async def weigh_weekly_reputation(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserWeighWeeklyReputationResponse:
        """
        Calculates and updates weekly reputation weights for users

        Source file:
        `api-server/src/controllers/v1/users/weigh-weekly-reputation.controller.ts`
        """
        return await self._post(
            "/v1/users/weigh-weekly-reputation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserWeighWeeklyReputationResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.get_private_notes = to_raw_response_wrapper(
            users.get_private_notes,
        )
        self.weigh_weekly_reputation = to_raw_response_wrapper(
            users.weigh_weekly_reputation,
        )

    @cached_property
    def v3(self) -> V3ResourceWithRawResponse:
        return V3ResourceWithRawResponse(self._users.v3)

    @cached_property
    def preferences(self) -> PreferencesResourceWithRawResponse:
        return PreferencesResourceWithRawResponse(self._users.preferences)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.get_private_notes = async_to_raw_response_wrapper(
            users.get_private_notes,
        )
        self.weigh_weekly_reputation = async_to_raw_response_wrapper(
            users.weigh_weekly_reputation,
        )

    @cached_property
    def v3(self) -> AsyncV3ResourceWithRawResponse:
        return AsyncV3ResourceWithRawResponse(self._users.v3)

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithRawResponse:
        return AsyncPreferencesResourceWithRawResponse(self._users.preferences)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.get_private_notes = to_streamed_response_wrapper(
            users.get_private_notes,
        )
        self.weigh_weekly_reputation = to_streamed_response_wrapper(
            users.weigh_weekly_reputation,
        )

    @cached_property
    def v3(self) -> V3ResourceWithStreamingResponse:
        return V3ResourceWithStreamingResponse(self._users.v3)

    @cached_property
    def preferences(self) -> PreferencesResourceWithStreamingResponse:
        return PreferencesResourceWithStreamingResponse(self._users.preferences)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.get_private_notes = async_to_streamed_response_wrapper(
            users.get_private_notes,
        )
        self.weigh_weekly_reputation = async_to_streamed_response_wrapper(
            users.weigh_weekly_reputation,
        )

    @cached_property
    def v3(self) -> AsyncV3ResourceWithStreamingResponse:
        return AsyncV3ResourceWithStreamingResponse(self._users.v3)

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithStreamingResponse:
        return AsyncPreferencesResourceWithStreamingResponse(self._users.preferences)
