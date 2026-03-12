# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from .citations import (
    CitationsResource,
    AsyncCitationsResource,
    CitationsResourceWithRawResponse,
    AsyncCitationsResourceWithRawResponse,
    CitationsResourceWithStreamingResponse,
    AsyncCitationsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .by_username import (
    ByUsernameResource,
    AsyncByUsernameResource,
    ByUsernameResourceWithRawResponse,
    AsyncByUsernameResourceWithRawResponse,
    ByUsernameResourceWithStreamingResponse,
    AsyncByUsernameResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.users import (
    v3_search_params,
    v3_get_activity_params,
    v3_update_profile_params,
    v3_get_claimed_papers_params,
    v3_get_viewed_history_params,
    v3_update_preferences_params,
    v3_autocomplete_profile_params,
)
from ...._base_client import make_request_options
from .semantic_scholar import (
    SemanticScholarResource,
    AsyncSemanticScholarResource,
    SemanticScholarResourceWithRawResponse,
    AsyncSemanticScholarResourceWithRawResponse,
    SemanticScholarResourceWithStreamingResponse,
    AsyncSemanticScholarResourceWithStreamingResponse,
)
from .following.following import (
    FollowingResource,
    AsyncFollowingResource,
    FollowingResourceWithRawResponse,
    AsyncFollowingResourceWithRawResponse,
    FollowingResourceWithStreamingResponse,
    AsyncFollowingResourceWithStreamingResponse,
)
from ....types.users.v3_search_response import V3SearchResponse
from ....types.users.v3_get_activity_response import V3GetActivityResponse
from ....types.users.v3_get_followers_response import V3GetFollowersResponse
from ....types.users.v3_upload_avatar_response import V3UploadAvatarResponse
from ....types.users.v3_update_profile_response import V3UpdateProfileResponse
from ....types.users.v3_get_leaderboard_response import V3GetLeaderboardResponse
from ....types.users.v3_get_current_user_response import V3GetCurrentUserResponse
from ....types.users.v3_get_user_by_uuid_response import V3GetUserByUuidResponse
from ....types.users.v3_get_claimed_papers_response import V3GetClaimedPapersResponse
from ....types.users.v3_get_viewed_history_response import V3GetViewedHistoryResponse
from ....types.users.v3_toggle_follow_user_response import V3ToggleFollowUserResponse
from ....types.users.v3_update_preferences_response import V3UpdatePreferencesResponse
from ....types.users.v3_autocomplete_profile_response import V3AutocompleteProfileResponse
from ....types.users.v3_get_featured_activity_response import V3GetFeaturedActivityResponse
from ....types.users.v3_process_notification_email_response import V3ProcessNotificationEmailResponse

__all__ = ["V3Resource", "AsyncV3Resource"]


class V3Resource(SyncAPIResource):
    @cached_property
    def following(self) -> FollowingResource:
        return FollowingResource(self._client)

    @cached_property
    def by_username(self) -> ByUsernameResource:
        return ByUsernameResource(self._client)

    @cached_property
    def semantic_scholar(self) -> SemanticScholarResource:
        return SemanticScholarResource(self._client)

    @cached_property
    def citations(self) -> CitationsResource:
        return CitationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return V3ResourceWithStreamingResponse(self)

    def autocomplete_profile(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3AutocompleteProfileResponse:
        """
        Generate a biography and institution for a user using their claimed papers

        Source file:
        `api-server/src/controllers/users/v3/autocomplete-profile.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users/v3/autocomplete-profile",
            body=maybe_transform({"user_id": user_id}, v3_autocomplete_profile_params.V3AutocompleteProfileParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3AutocompleteProfileResponse,
        )

    def delete_banner(
        self,
        banner_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the given banner

        Source file: `api-server/src/controllers/users/v3/delete-banner.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not banner_id:
            raise ValueError(f"Expected a non-empty value for `banner_id` but received {banner_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/users/v3/banners/{banner_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_own_user(
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
        Deletes the user's account

        Source file: `api-server/src/controllers/users/v3/delete-own-user.controller.ts`
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/users/v3",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_activity(
        self,
        id: str,
        *,
        sort: Literal["date", "liked"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetActivityResponse:
        """
        Retrieve public activity timeline for a user

        Source file: `api-server/src/controllers/users/v3/get-activity.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/users/v3/{id}/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"sort": sort}, v3_get_activity_params.V3GetActivityParams),
            ),
            cast_to=V3GetActivityResponse,
        )

    def get_claimed_papers(
        self,
        id: str,
        *,
        sort: Literal["date", "liked", "citations"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetClaimedPapersResponse:
        """
        Retrieve the claimed papers for a user

        Source file:
        `api-server/src/controllers/users/v3/get-claimed-papers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/users/v3/{id}/claimed-papers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"sort": sort}, v3_get_claimed_papers_params.V3GetClaimedPapersParams),
            ),
            cast_to=V3GetClaimedPapersResponse,
        )

    def get_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetCurrentUserResponse:
        """
        Retrieve information about yourself

        Source file:
        `api-server/src/controllers/users/v3/get-current-user.controller.ts`
        """
        return self._get(
            "/users/v3",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetCurrentUserResponse,
        )

    def get_featured_activity(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetFeaturedActivityResponse:
        """
        Retrieve highlighted activity for a user

        Source file: `api-server/src/controllers/users/v3/get-featured.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/users/v3/{id}/featured",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetFeaturedActivityResponse,
        )

    def get_followers(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetFollowersResponse:
        """
        List the users following the specified user

        Source file: `api-server/src/controllers/users/v3/get-followers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/users/v3/{id}/followers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetFollowersResponse,
        )

    def get_leaderboard(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetLeaderboardResponse:
        """
        Retrieve weekly and all-time leaderboards for users ranked by reputation

        Source file: `api-server/src/controllers/users/v3/get-leaderboard.controller.ts`
        """
        return self._get(
            "/users/v3/leaderboard",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetLeaderboardResponse,
        )

    def get_user_by_uuid(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetUserByUuidResponse:
        """
        Retrieve a user's basic information given its UUID

        Source file: `api-server/src/controllers/users/v3/get-user.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/users/v3/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetUserByUuidResponse,
        )

    def get_viewed_history(
        self,
        *,
        offset: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetViewedHistoryResponse:
        """
        Retrieve the view history for the current user

        Source file:
        `api-server/src/controllers/users/v3/get-viewed-history.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/users/v3/viewed-history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "offset": offset,
                        "search": search,
                    },
                    v3_get_viewed_history_params.V3GetViewedHistoryParams,
                ),
            ),
            cast_to=V3GetViewedHistoryResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def process_notification_email(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3ProcessNotificationEmailResponse:
        """
        Send a notification digest email for the given user when necessary.

        Source file:
        `api-server/src/controllers/users/v3/process-notification-email.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/users/v3/{id}/process-notification-email",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3ProcessNotificationEmailResponse,
        )

    def search(
        self,
        *,
        q: str,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3SearchResponse:
        """
        Search for users by name, username, or institution

        Source file: `api-server/src/controllers/users/v3/search-users.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/users/v3/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                    },
                    v3_search_params.V3SearchParams,
                ),
            ),
            cast_to=V3SearchResponse,
        )

    def toggle_follow_user(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3ToggleFollowUserResponse:
        """
        Follow or unfollow another user

        Source file:
        `api-server/src/controllers/users/v3/toggle-follow-user.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/users/v3/{id}/follow",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3ToggleFollowUserResponse,
        )

    def update_preferences(
        self,
        *,
        banners: Iterable[v3_update_preferences_params.Banner] | Omit = omit,
        base: v3_update_preferences_params.Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3UpdatePreferencesResponse:
        """
        Update base or banner preferences for the authenticated user

        Source file:
        `api-server/src/controllers/users/v3/update-preferences.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/users/v3/preferences",
            body=maybe_transform(
                {
                    "banners": banners,
                    "base": base,
                },
                v3_update_preferences_params.V3UpdatePreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3UpdatePreferencesResponse,
        )

    def update_profile(
        self,
        *,
        biography: Optional[str] | Omit = omit,
        bluesky_username: Optional[str] | Omit = omit,
        github_username: Optional[str] | Omit = omit,
        institution: Optional[str] | Omit = omit,
        linkedin_username: Optional[str] | Omit = omit,
        location: Optional[str] | Omit = omit,
        public_email: Optional[str] | Omit = omit,
        real_name: str | Omit = omit,
        username: str | Omit = omit,
        x_username: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3UpdateProfileResponse:
        """
        Update profile details for the authenticated user

        Source file: `api-server/src/controllers/users/v3/update-profile.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/users/v3/profile",
            body=maybe_transform(
                {
                    "biography": biography,
                    "bluesky_username": bluesky_username,
                    "github_username": github_username,
                    "institution": institution,
                    "linkedin_username": linkedin_username,
                    "location": location,
                    "public_email": public_email,
                    "real_name": real_name,
                    "username": username,
                    "x_username": x_username,
                },
                v3_update_profile_params.V3UpdateProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3UpdateProfileResponse,
        )

    def upload_avatar(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[V3UploadAvatarResponse]:
        """
        Upload or remove the authenticated user's avatar image.

        Source file: `api-server/src/controllers/users/v3/upload-avatar.controller.ts`
        """
        return self._post(
            "/users/v3/avatar",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3UploadAvatarResponse,
        )


class AsyncV3Resource(AsyncAPIResource):
    @cached_property
    def following(self) -> AsyncFollowingResource:
        return AsyncFollowingResource(self._client)

    @cached_property
    def by_username(self) -> AsyncByUsernameResource:
        return AsyncByUsernameResource(self._client)

    @cached_property
    def semantic_scholar(self) -> AsyncSemanticScholarResource:
        return AsyncSemanticScholarResource(self._client)

    @cached_property
    def citations(self) -> AsyncCitationsResource:
        return AsyncCitationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV3ResourceWithStreamingResponse(self)

    async def autocomplete_profile(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3AutocompleteProfileResponse:
        """
        Generate a biography and institution for a user using their claimed papers

        Source file:
        `api-server/src/controllers/users/v3/autocomplete-profile.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users/v3/autocomplete-profile",
            body=await async_maybe_transform(
                {"user_id": user_id}, v3_autocomplete_profile_params.V3AutocompleteProfileParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3AutocompleteProfileResponse,
        )

    async def delete_banner(
        self,
        banner_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the given banner

        Source file: `api-server/src/controllers/users/v3/delete-banner.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not banner_id:
            raise ValueError(f"Expected a non-empty value for `banner_id` but received {banner_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/users/v3/banners/{banner_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_own_user(
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
        Deletes the user's account

        Source file: `api-server/src/controllers/users/v3/delete-own-user.controller.ts`
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/users/v3",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_activity(
        self,
        id: str,
        *,
        sort: Literal["date", "liked"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetActivityResponse:
        """
        Retrieve public activity timeline for a user

        Source file: `api-server/src/controllers/users/v3/get-activity.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/users/v3/{id}/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"sort": sort}, v3_get_activity_params.V3GetActivityParams),
            ),
            cast_to=V3GetActivityResponse,
        )

    async def get_claimed_papers(
        self,
        id: str,
        *,
        sort: Literal["date", "liked", "citations"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetClaimedPapersResponse:
        """
        Retrieve the claimed papers for a user

        Source file:
        `api-server/src/controllers/users/v3/get-claimed-papers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/users/v3/{id}/claimed-papers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"sort": sort}, v3_get_claimed_papers_params.V3GetClaimedPapersParams
                ),
            ),
            cast_to=V3GetClaimedPapersResponse,
        )

    async def get_current_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetCurrentUserResponse:
        """
        Retrieve information about yourself

        Source file:
        `api-server/src/controllers/users/v3/get-current-user.controller.ts`
        """
        return await self._get(
            "/users/v3",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetCurrentUserResponse,
        )

    async def get_featured_activity(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetFeaturedActivityResponse:
        """
        Retrieve highlighted activity for a user

        Source file: `api-server/src/controllers/users/v3/get-featured.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/users/v3/{id}/featured",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetFeaturedActivityResponse,
        )

    async def get_followers(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetFollowersResponse:
        """
        List the users following the specified user

        Source file: `api-server/src/controllers/users/v3/get-followers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/users/v3/{id}/followers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetFollowersResponse,
        )

    async def get_leaderboard(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetLeaderboardResponse:
        """
        Retrieve weekly and all-time leaderboards for users ranked by reputation

        Source file: `api-server/src/controllers/users/v3/get-leaderboard.controller.ts`
        """
        return await self._get(
            "/users/v3/leaderboard",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetLeaderboardResponse,
        )

    async def get_user_by_uuid(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetUserByUuidResponse:
        """
        Retrieve a user's basic information given its UUID

        Source file: `api-server/src/controllers/users/v3/get-user.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/users/v3/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetUserByUuidResponse,
        )

    async def get_viewed_history(
        self,
        *,
        offset: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3GetViewedHistoryResponse:
        """
        Retrieve the view history for the current user

        Source file:
        `api-server/src/controllers/users/v3/get-viewed-history.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/users/v3/viewed-history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "offset": offset,
                        "search": search,
                    },
                    v3_get_viewed_history_params.V3GetViewedHistoryParams,
                ),
            ),
            cast_to=V3GetViewedHistoryResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def process_notification_email(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3ProcessNotificationEmailResponse:
        """
        Send a notification digest email for the given user when necessary.

        Source file:
        `api-server/src/controllers/users/v3/process-notification-email.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/users/v3/{id}/process-notification-email",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3ProcessNotificationEmailResponse,
        )

    async def search(
        self,
        *,
        q: str,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3SearchResponse:
        """
        Search for users by name, username, or institution

        Source file: `api-server/src/controllers/users/v3/search-users.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/users/v3/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                    },
                    v3_search_params.V3SearchParams,
                ),
            ),
            cast_to=V3SearchResponse,
        )

    async def toggle_follow_user(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3ToggleFollowUserResponse:
        """
        Follow or unfollow another user

        Source file:
        `api-server/src/controllers/users/v3/toggle-follow-user.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/users/v3/{id}/follow",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3ToggleFollowUserResponse,
        )

    async def update_preferences(
        self,
        *,
        banners: Iterable[v3_update_preferences_params.Banner] | Omit = omit,
        base: v3_update_preferences_params.Base | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3UpdatePreferencesResponse:
        """
        Update base or banner preferences for the authenticated user

        Source file:
        `api-server/src/controllers/users/v3/update-preferences.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/users/v3/preferences",
            body=await async_maybe_transform(
                {
                    "banners": banners,
                    "base": base,
                },
                v3_update_preferences_params.V3UpdatePreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3UpdatePreferencesResponse,
        )

    async def update_profile(
        self,
        *,
        biography: Optional[str] | Omit = omit,
        bluesky_username: Optional[str] | Omit = omit,
        github_username: Optional[str] | Omit = omit,
        institution: Optional[str] | Omit = omit,
        linkedin_username: Optional[str] | Omit = omit,
        location: Optional[str] | Omit = omit,
        public_email: Optional[str] | Omit = omit,
        real_name: str | Omit = omit,
        username: str | Omit = omit,
        x_username: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3UpdateProfileResponse:
        """
        Update profile details for the authenticated user

        Source file: `api-server/src/controllers/users/v3/update-profile.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/users/v3/profile",
            body=await async_maybe_transform(
                {
                    "biography": biography,
                    "bluesky_username": bluesky_username,
                    "github_username": github_username,
                    "institution": institution,
                    "linkedin_username": linkedin_username,
                    "location": location,
                    "public_email": public_email,
                    "real_name": real_name,
                    "username": username,
                    "x_username": x_username,
                },
                v3_update_profile_params.V3UpdateProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3UpdateProfileResponse,
        )

    async def upload_avatar(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[V3UploadAvatarResponse]:
        """
        Upload or remove the authenticated user's avatar image.

        Source file: `api-server/src/controllers/users/v3/upload-avatar.controller.ts`
        """
        return await self._post(
            "/users/v3/avatar",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3UploadAvatarResponse,
        )


class V3ResourceWithRawResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

        self.autocomplete_profile = to_raw_response_wrapper(
            v3.autocomplete_profile,
        )
        self.delete_banner = to_raw_response_wrapper(
            v3.delete_banner,
        )
        self.delete_own_user = to_raw_response_wrapper(
            v3.delete_own_user,
        )
        self.get_activity = to_raw_response_wrapper(
            v3.get_activity,
        )
        self.get_claimed_papers = to_raw_response_wrapper(
            v3.get_claimed_papers,
        )
        self.get_current_user = to_raw_response_wrapper(
            v3.get_current_user,
        )
        self.get_featured_activity = to_raw_response_wrapper(
            v3.get_featured_activity,
        )
        self.get_followers = to_raw_response_wrapper(
            v3.get_followers,
        )
        self.get_leaderboard = to_raw_response_wrapper(
            v3.get_leaderboard,
        )
        self.get_user_by_uuid = to_raw_response_wrapper(
            v3.get_user_by_uuid,
        )
        self.get_viewed_history = to_raw_response_wrapper(
            v3.get_viewed_history,
        )
        self.process_notification_email = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                v3.process_notification_email,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = to_raw_response_wrapper(
            v3.search,
        )
        self.toggle_follow_user = to_raw_response_wrapper(
            v3.toggle_follow_user,
        )
        self.update_preferences = to_raw_response_wrapper(
            v3.update_preferences,
        )
        self.update_profile = to_raw_response_wrapper(
            v3.update_profile,
        )
        self.upload_avatar = to_raw_response_wrapper(
            v3.upload_avatar,
        )

    @cached_property
    def following(self) -> FollowingResourceWithRawResponse:
        return FollowingResourceWithRawResponse(self._v3.following)

    @cached_property
    def by_username(self) -> ByUsernameResourceWithRawResponse:
        return ByUsernameResourceWithRawResponse(self._v3.by_username)

    @cached_property
    def semantic_scholar(self) -> SemanticScholarResourceWithRawResponse:
        return SemanticScholarResourceWithRawResponse(self._v3.semantic_scholar)

    @cached_property
    def citations(self) -> CitationsResourceWithRawResponse:
        return CitationsResourceWithRawResponse(self._v3.citations)


class AsyncV3ResourceWithRawResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

        self.autocomplete_profile = async_to_raw_response_wrapper(
            v3.autocomplete_profile,
        )
        self.delete_banner = async_to_raw_response_wrapper(
            v3.delete_banner,
        )
        self.delete_own_user = async_to_raw_response_wrapper(
            v3.delete_own_user,
        )
        self.get_activity = async_to_raw_response_wrapper(
            v3.get_activity,
        )
        self.get_claimed_papers = async_to_raw_response_wrapper(
            v3.get_claimed_papers,
        )
        self.get_current_user = async_to_raw_response_wrapper(
            v3.get_current_user,
        )
        self.get_featured_activity = async_to_raw_response_wrapper(
            v3.get_featured_activity,
        )
        self.get_followers = async_to_raw_response_wrapper(
            v3.get_followers,
        )
        self.get_leaderboard = async_to_raw_response_wrapper(
            v3.get_leaderboard,
        )
        self.get_user_by_uuid = async_to_raw_response_wrapper(
            v3.get_user_by_uuid,
        )
        self.get_viewed_history = async_to_raw_response_wrapper(
            v3.get_viewed_history,
        )
        self.process_notification_email = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                v3.process_notification_email,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = async_to_raw_response_wrapper(
            v3.search,
        )
        self.toggle_follow_user = async_to_raw_response_wrapper(
            v3.toggle_follow_user,
        )
        self.update_preferences = async_to_raw_response_wrapper(
            v3.update_preferences,
        )
        self.update_profile = async_to_raw_response_wrapper(
            v3.update_profile,
        )
        self.upload_avatar = async_to_raw_response_wrapper(
            v3.upload_avatar,
        )

    @cached_property
    def following(self) -> AsyncFollowingResourceWithRawResponse:
        return AsyncFollowingResourceWithRawResponse(self._v3.following)

    @cached_property
    def by_username(self) -> AsyncByUsernameResourceWithRawResponse:
        return AsyncByUsernameResourceWithRawResponse(self._v3.by_username)

    @cached_property
    def semantic_scholar(self) -> AsyncSemanticScholarResourceWithRawResponse:
        return AsyncSemanticScholarResourceWithRawResponse(self._v3.semantic_scholar)

    @cached_property
    def citations(self) -> AsyncCitationsResourceWithRawResponse:
        return AsyncCitationsResourceWithRawResponse(self._v3.citations)


class V3ResourceWithStreamingResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

        self.autocomplete_profile = to_streamed_response_wrapper(
            v3.autocomplete_profile,
        )
        self.delete_banner = to_streamed_response_wrapper(
            v3.delete_banner,
        )
        self.delete_own_user = to_streamed_response_wrapper(
            v3.delete_own_user,
        )
        self.get_activity = to_streamed_response_wrapper(
            v3.get_activity,
        )
        self.get_claimed_papers = to_streamed_response_wrapper(
            v3.get_claimed_papers,
        )
        self.get_current_user = to_streamed_response_wrapper(
            v3.get_current_user,
        )
        self.get_featured_activity = to_streamed_response_wrapper(
            v3.get_featured_activity,
        )
        self.get_followers = to_streamed_response_wrapper(
            v3.get_followers,
        )
        self.get_leaderboard = to_streamed_response_wrapper(
            v3.get_leaderboard,
        )
        self.get_user_by_uuid = to_streamed_response_wrapper(
            v3.get_user_by_uuid,
        )
        self.get_viewed_history = to_streamed_response_wrapper(
            v3.get_viewed_history,
        )
        self.process_notification_email = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                v3.process_notification_email,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = to_streamed_response_wrapper(
            v3.search,
        )
        self.toggle_follow_user = to_streamed_response_wrapper(
            v3.toggle_follow_user,
        )
        self.update_preferences = to_streamed_response_wrapper(
            v3.update_preferences,
        )
        self.update_profile = to_streamed_response_wrapper(
            v3.update_profile,
        )
        self.upload_avatar = to_streamed_response_wrapper(
            v3.upload_avatar,
        )

    @cached_property
    def following(self) -> FollowingResourceWithStreamingResponse:
        return FollowingResourceWithStreamingResponse(self._v3.following)

    @cached_property
    def by_username(self) -> ByUsernameResourceWithStreamingResponse:
        return ByUsernameResourceWithStreamingResponse(self._v3.by_username)

    @cached_property
    def semantic_scholar(self) -> SemanticScholarResourceWithStreamingResponse:
        return SemanticScholarResourceWithStreamingResponse(self._v3.semantic_scholar)

    @cached_property
    def citations(self) -> CitationsResourceWithStreamingResponse:
        return CitationsResourceWithStreamingResponse(self._v3.citations)


class AsyncV3ResourceWithStreamingResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

        self.autocomplete_profile = async_to_streamed_response_wrapper(
            v3.autocomplete_profile,
        )
        self.delete_banner = async_to_streamed_response_wrapper(
            v3.delete_banner,
        )
        self.delete_own_user = async_to_streamed_response_wrapper(
            v3.delete_own_user,
        )
        self.get_activity = async_to_streamed_response_wrapper(
            v3.get_activity,
        )
        self.get_claimed_papers = async_to_streamed_response_wrapper(
            v3.get_claimed_papers,
        )
        self.get_current_user = async_to_streamed_response_wrapper(
            v3.get_current_user,
        )
        self.get_featured_activity = async_to_streamed_response_wrapper(
            v3.get_featured_activity,
        )
        self.get_followers = async_to_streamed_response_wrapper(
            v3.get_followers,
        )
        self.get_leaderboard = async_to_streamed_response_wrapper(
            v3.get_leaderboard,
        )
        self.get_user_by_uuid = async_to_streamed_response_wrapper(
            v3.get_user_by_uuid,
        )
        self.get_viewed_history = async_to_streamed_response_wrapper(
            v3.get_viewed_history,
        )
        self.process_notification_email = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                v3.process_notification_email,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = async_to_streamed_response_wrapper(
            v3.search,
        )
        self.toggle_follow_user = async_to_streamed_response_wrapper(
            v3.toggle_follow_user,
        )
        self.update_preferences = async_to_streamed_response_wrapper(
            v3.update_preferences,
        )
        self.update_profile = async_to_streamed_response_wrapper(
            v3.update_profile,
        )
        self.upload_avatar = async_to_streamed_response_wrapper(
            v3.upload_avatar,
        )

    @cached_property
    def following(self) -> AsyncFollowingResourceWithStreamingResponse:
        return AsyncFollowingResourceWithStreamingResponse(self._v3.following)

    @cached_property
    def by_username(self) -> AsyncByUsernameResourceWithStreamingResponse:
        return AsyncByUsernameResourceWithStreamingResponse(self._v3.by_username)

    @cached_property
    def semantic_scholar(self) -> AsyncSemanticScholarResourceWithStreamingResponse:
        return AsyncSemanticScholarResourceWithStreamingResponse(self._v3.semantic_scholar)

    @cached_property
    def citations(self) -> AsyncCitationsResourceWithStreamingResponse:
        return AsyncCitationsResourceWithStreamingResponse(self._v3.citations)
