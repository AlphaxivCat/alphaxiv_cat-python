# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .email import (
    EmailResource,
    AsyncEmailResource,
    EmailResourceWithRawResponse,
    AsyncEmailResourceWithRawResponse,
    EmailResourceWithStreamingResponse,
    AsyncEmailResourceWithStreamingResponse,
)
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
from ....types.users.preference_get_folders_preferences_response import PreferenceGetFoldersPreferencesResponse

__all__ = ["PreferencesResource", "AsyncPreferencesResource"]


class PreferencesResource(SyncAPIResource):
    @cached_property
    def email(self) -> EmailResource:
        return EmailResource(self._client)

    @cached_property
    def with_raw_response(self) -> PreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return PreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return PreferencesResourceWithStreamingResponse(self)

    def get_folders_preferences(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceGetFoldersPreferencesResponse:
        """
        Get folder preferences for the authenticated user

        Source file:
        `api-server/src/controllers/v2/users/get-folders-preferences.controller.ts`
        """
        return self._get(
            "/v2/users/preferences/folders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceGetFoldersPreferencesResponse,
        )


class AsyncPreferencesResource(AsyncAPIResource):
    @cached_property
    def email(self) -> AsyncEmailResource:
        return AsyncEmailResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncPreferencesResourceWithStreamingResponse(self)

    async def get_folders_preferences(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceGetFoldersPreferencesResponse:
        """
        Get folder preferences for the authenticated user

        Source file:
        `api-server/src/controllers/v2/users/get-folders-preferences.controller.ts`
        """
        return await self._get(
            "/v2/users/preferences/folders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceGetFoldersPreferencesResponse,
        )


class PreferencesResourceWithRawResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.get_folders_preferences = to_raw_response_wrapper(
            preferences.get_folders_preferences,
        )

    @cached_property
    def email(self) -> EmailResourceWithRawResponse:
        return EmailResourceWithRawResponse(self._preferences.email)


class AsyncPreferencesResourceWithRawResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.get_folders_preferences = async_to_raw_response_wrapper(
            preferences.get_folders_preferences,
        )

    @cached_property
    def email(self) -> AsyncEmailResourceWithRawResponse:
        return AsyncEmailResourceWithRawResponse(self._preferences.email)


class PreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.get_folders_preferences = to_streamed_response_wrapper(
            preferences.get_folders_preferences,
        )

    @cached_property
    def email(self) -> EmailResourceWithStreamingResponse:
        return EmailResourceWithStreamingResponse(self._preferences.email)


class AsyncPreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.get_folders_preferences = async_to_streamed_response_wrapper(
            preferences.get_folders_preferences,
        )

    @cached_property
    def email(self) -> AsyncEmailResourceWithStreamingResponse:
        return AsyncEmailResourceWithStreamingResponse(self._preferences.email)
