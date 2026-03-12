# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import sitemap_list_users_params, sitemap_list_papers_params, sitemap_list_overviews_params
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
from ..types.sitemap_list_users_response import SitemapListUsersResponse
from ..types.sitemap_list_papers_response import SitemapListPapersResponse
from ..types.sitemap_list_overviews_response import SitemapListOverviewsResponse

__all__ = ["SitemapsResource", "AsyncSitemapsResource"]


class SitemapsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SitemapsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return SitemapsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SitemapsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return SitemapsResourceWithStreamingResponse(self)

    def list_overviews(
        self,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SitemapListOverviewsResponse:
        """
        Get paginated list of paper versions with AI overviews for sitemap generation

        Source file:
        `api-server/src/controllers/v1/sitemaps/get-overviews-for-sitemap.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/sitemaps/overviews",
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
                    sitemap_list_overviews_params.SitemapListOverviewsParams,
                ),
            ),
            cast_to=SitemapListOverviewsResponse,
        )

    def list_papers(
        self,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SitemapListPapersResponse:
        """Get paginated list of public papers for sitemap generation.

        Uses cursor caching
        for efficient deep pagination.

        Source file:
        `api-server/src/controllers/v1/sitemaps/get-papers-for-sitemap.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/sitemaps/papers",
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
                    sitemap_list_papers_params.SitemapListPapersParams,
                ),
            ),
            cast_to=SitemapListPapersResponse,
        )

    def list_users(
        self,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SitemapListUsersResponse:
        """
        Get paginated list of users for sitemap generation

        Source file:
        `api-server/src/controllers/v1/sitemaps/get-users-for-sitemap.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/sitemaps/users",
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
                    sitemap_list_users_params.SitemapListUsersParams,
                ),
            ),
            cast_to=SitemapListUsersResponse,
        )


class AsyncSitemapsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSitemapsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSitemapsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSitemapsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncSitemapsResourceWithStreamingResponse(self)

    async def list_overviews(
        self,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SitemapListOverviewsResponse:
        """
        Get paginated list of paper versions with AI overviews for sitemap generation

        Source file:
        `api-server/src/controllers/v1/sitemaps/get-overviews-for-sitemap.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/sitemaps/overviews",
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
                    sitemap_list_overviews_params.SitemapListOverviewsParams,
                ),
            ),
            cast_to=SitemapListOverviewsResponse,
        )

    async def list_papers(
        self,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SitemapListPapersResponse:
        """Get paginated list of public papers for sitemap generation.

        Uses cursor caching
        for efficient deep pagination.

        Source file:
        `api-server/src/controllers/v1/sitemaps/get-papers-for-sitemap.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/sitemaps/papers",
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
                    sitemap_list_papers_params.SitemapListPapersParams,
                ),
            ),
            cast_to=SitemapListPapersResponse,
        )

    async def list_users(
        self,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SitemapListUsersResponse:
        """
        Get paginated list of users for sitemap generation

        Source file:
        `api-server/src/controllers/v1/sitemaps/get-users-for-sitemap.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/sitemaps/users",
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
                    sitemap_list_users_params.SitemapListUsersParams,
                ),
            ),
            cast_to=SitemapListUsersResponse,
        )


class SitemapsResourceWithRawResponse:
    def __init__(self, sitemaps: SitemapsResource) -> None:
        self._sitemaps = sitemaps

        self.list_overviews = to_raw_response_wrapper(
            sitemaps.list_overviews,
        )
        self.list_papers = to_raw_response_wrapper(
            sitemaps.list_papers,
        )
        self.list_users = to_raw_response_wrapper(
            sitemaps.list_users,
        )


class AsyncSitemapsResourceWithRawResponse:
    def __init__(self, sitemaps: AsyncSitemapsResource) -> None:
        self._sitemaps = sitemaps

        self.list_overviews = async_to_raw_response_wrapper(
            sitemaps.list_overviews,
        )
        self.list_papers = async_to_raw_response_wrapper(
            sitemaps.list_papers,
        )
        self.list_users = async_to_raw_response_wrapper(
            sitemaps.list_users,
        )


class SitemapsResourceWithStreamingResponse:
    def __init__(self, sitemaps: SitemapsResource) -> None:
        self._sitemaps = sitemaps

        self.list_overviews = to_streamed_response_wrapper(
            sitemaps.list_overviews,
        )
        self.list_papers = to_streamed_response_wrapper(
            sitemaps.list_papers,
        )
        self.list_users = to_streamed_response_wrapper(
            sitemaps.list_users,
        )


class AsyncSitemapsResourceWithStreamingResponse:
    def __init__(self, sitemaps: AsyncSitemapsResource) -> None:
        self._sitemaps = sitemaps

        self.list_overviews = async_to_streamed_response_wrapper(
            sitemaps.list_overviews,
        )
        self.list_papers = async_to_streamed_response_wrapper(
            sitemaps.list_papers,
        )
        self.list_users = async_to_streamed_response_wrapper(
            sitemaps.list_users,
        )
