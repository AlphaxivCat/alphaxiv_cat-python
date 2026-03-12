# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.papers.kickoff_daily_github_star_update_response import KickoffDailyGitHubStarUpdateResponse
from ...types.papers.kickoff_daily_github_star_kickoff_daily_github_stars_response import (
    KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse,
)

__all__ = ["KickoffDailyGitHubStarsResource", "AsyncKickoffDailyGitHubStarsResource"]


class KickoffDailyGitHubStarsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KickoffDailyGitHubStarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return KickoffDailyGitHubStarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KickoffDailyGitHubStarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return KickoffDailyGitHubStarsResourceWithStreamingResponse(self)

    def update(
        self,
        max: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KickoffDailyGitHubStarUpdateResponse:
        """
        Kickoff background job to update daily GitHub stars with max limit

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-daily-github-stars-max.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not max:
            raise ValueError(f"Expected a non-empty value for `max` but received {max!r}")
        return self._post(
            f"/v2/papers/kickoff-daily-github-stars/{max}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KickoffDailyGitHubStarUpdateResponse,
        )

    def kickoff_daily_github_stars(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse:
        """
        Kickoff background job to update daily GitHub stars

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-daily-github-stars.controller.ts`
        """
        return self._post(
            "/v2/papers/kickoff-daily-github-stars",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse,
        )


class AsyncKickoffDailyGitHubStarsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKickoffDailyGitHubStarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKickoffDailyGitHubStarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKickoffDailyGitHubStarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncKickoffDailyGitHubStarsResourceWithStreamingResponse(self)

    async def update(
        self,
        max: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KickoffDailyGitHubStarUpdateResponse:
        """
        Kickoff background job to update daily GitHub stars with max limit

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-daily-github-stars-max.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not max:
            raise ValueError(f"Expected a non-empty value for `max` but received {max!r}")
        return await self._post(
            f"/v2/papers/kickoff-daily-github-stars/{max}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KickoffDailyGitHubStarUpdateResponse,
        )

    async def kickoff_daily_github_stars(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse:
        """
        Kickoff background job to update daily GitHub stars

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-daily-github-stars.controller.ts`
        """
        return await self._post(
            "/v2/papers/kickoff-daily-github-stars",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse,
        )


class KickoffDailyGitHubStarsResourceWithRawResponse:
    def __init__(self, kickoff_daily_github_stars: KickoffDailyGitHubStarsResource) -> None:
        self._kickoff_daily_github_stars = kickoff_daily_github_stars

        self.update = to_raw_response_wrapper(
            kickoff_daily_github_stars.update,
        )
        self.kickoff_daily_github_stars = to_raw_response_wrapper(
            kickoff_daily_github_stars.kickoff_daily_github_stars,
        )


class AsyncKickoffDailyGitHubStarsResourceWithRawResponse:
    def __init__(self, kickoff_daily_github_stars: AsyncKickoffDailyGitHubStarsResource) -> None:
        self._kickoff_daily_github_stars = kickoff_daily_github_stars

        self.update = async_to_raw_response_wrapper(
            kickoff_daily_github_stars.update,
        )
        self.kickoff_daily_github_stars = async_to_raw_response_wrapper(
            kickoff_daily_github_stars.kickoff_daily_github_stars,
        )


class KickoffDailyGitHubStarsResourceWithStreamingResponse:
    def __init__(self, kickoff_daily_github_stars: KickoffDailyGitHubStarsResource) -> None:
        self._kickoff_daily_github_stars = kickoff_daily_github_stars

        self.update = to_streamed_response_wrapper(
            kickoff_daily_github_stars.update,
        )
        self.kickoff_daily_github_stars = to_streamed_response_wrapper(
            kickoff_daily_github_stars.kickoff_daily_github_stars,
        )


class AsyncKickoffDailyGitHubStarsResourceWithStreamingResponse:
    def __init__(self, kickoff_daily_github_stars: AsyncKickoffDailyGitHubStarsResource) -> None:
        self._kickoff_daily_github_stars = kickoff_daily_github_stars

        self.update = async_to_streamed_response_wrapper(
            kickoff_daily_github_stars.update,
        )
        self.kickoff_daily_github_stars = async_to_streamed_response_wrapper(
            kickoff_daily_github_stars.kickoff_daily_github_stars,
        )
