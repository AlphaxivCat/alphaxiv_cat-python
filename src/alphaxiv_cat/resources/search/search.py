# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .v2.v2 import (
    V2Resource,
    AsyncV2Resource,
    V2ResourceWithRawResponse,
    AsyncV2ResourceWithRawResponse,
    V2ResourceWithStreamingResponse,
    AsyncV2ResourceWithStreamingResponse,
)
from ...types import search_closest_topic_params, search_google_search_params
from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.search_closest_topic_response import SearchClosestTopicResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def v2(self) -> V2Resource:
        return V2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def closest_topic(
        self,
        *,
        input: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchClosestTopicResponse:
        """
        Find the closest matching topics/categories for a given input using AI

        Source file: `api-server/src/controllers/v1/search/closest-topic.controller.ts`

        Args:
          input: User input to match against categories

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/search/closest-topic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"input": input}, search_closest_topic_params.SearchClosestTopicParams),
            ),
            cast_to=SearchClosestTopicResponse,
        )

    def google_search(
        self,
        *,
        q: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Search for papers using Google and enrich results

        Source file: `api-server/src/controllers/v1/search/search-google.controller.ts`

        Args:
          q: Search query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/search/paper",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"q": q}, search_google_search_params.SearchGoogleSearchParams),
            ),
            cast_to=object,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def v2(self) -> AsyncV2Resource:
        return AsyncV2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def closest_topic(
        self,
        *,
        input: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchClosestTopicResponse:
        """
        Find the closest matching topics/categories for a given input using AI

        Source file: `api-server/src/controllers/v1/search/closest-topic.controller.ts`

        Args:
          input: User input to match against categories

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/search/closest-topic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"input": input}, search_closest_topic_params.SearchClosestTopicParams
                ),
            ),
            cast_to=SearchClosestTopicResponse,
        )

    async def google_search(
        self,
        *,
        q: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Search for papers using Google and enrich results

        Source file: `api-server/src/controllers/v1/search/search-google.controller.ts`

        Args:
          q: Search query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/search/paper",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"q": q}, search_google_search_params.SearchGoogleSearchParams),
            ),
            cast_to=object,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.closest_topic = to_raw_response_wrapper(
            search.closest_topic,
        )
        self.google_search = to_raw_response_wrapper(
            search.google_search,
        )

    @cached_property
    def v2(self) -> V2ResourceWithRawResponse:
        return V2ResourceWithRawResponse(self._search.v2)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.closest_topic = async_to_raw_response_wrapper(
            search.closest_topic,
        )
        self.google_search = async_to_raw_response_wrapper(
            search.google_search,
        )

    @cached_property
    def v2(self) -> AsyncV2ResourceWithRawResponse:
        return AsyncV2ResourceWithRawResponse(self._search.v2)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.closest_topic = to_streamed_response_wrapper(
            search.closest_topic,
        )
        self.google_search = to_streamed_response_wrapper(
            search.google_search,
        )

    @cached_property
    def v2(self) -> V2ResourceWithStreamingResponse:
        return V2ResourceWithStreamingResponse(self._search.v2)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.closest_topic = async_to_streamed_response_wrapper(
            search.closest_topic,
        )
        self.google_search = async_to_streamed_response_wrapper(
            search.google_search,
        )

    @cached_property
    def v2(self) -> AsyncV2ResourceWithStreamingResponse:
        return AsyncV2ResourceWithStreamingResponse(self._search.v2)
