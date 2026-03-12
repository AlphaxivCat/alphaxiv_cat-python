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
from ....types.users.v3.citation_get_graph_response import CitationGetGraphResponse
from ....types.users.v3.citation_get_summary_response import CitationGetSummaryResponse

__all__ = ["CitationsResource", "AsyncCitationsResource"]


class CitationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return CitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return CitationsResourceWithStreamingResponse(self)

    def get_graph(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CitationGetGraphResponse:
        """
        Retrieve citation counts by year for a user

        Source file:
        `api-server/src/controllers/users/v3/get-citation-graph.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/users/v3/{id}/citations/graph",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CitationGetGraphResponse,
        )

    def get_summary(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CitationGetSummaryResponse:
        """
        Retrieve aggregated citation metrics for a user

        Source file:
        `api-server/src/controllers/users/v3/get-citation-summary.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/users/v3/{id}/citations/summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CitationGetSummaryResponse,
        )


class AsyncCitationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncCitationsResourceWithStreamingResponse(self)

    async def get_graph(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CitationGetGraphResponse:
        """
        Retrieve citation counts by year for a user

        Source file:
        `api-server/src/controllers/users/v3/get-citation-graph.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/users/v3/{id}/citations/graph",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CitationGetGraphResponse,
        )

    async def get_summary(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CitationGetSummaryResponse:
        """
        Retrieve aggregated citation metrics for a user

        Source file:
        `api-server/src/controllers/users/v3/get-citation-summary.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/users/v3/{id}/citations/summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CitationGetSummaryResponse,
        )


class CitationsResourceWithRawResponse:
    def __init__(self, citations: CitationsResource) -> None:
        self._citations = citations

        self.get_graph = to_raw_response_wrapper(
            citations.get_graph,
        )
        self.get_summary = to_raw_response_wrapper(
            citations.get_summary,
        )


class AsyncCitationsResourceWithRawResponse:
    def __init__(self, citations: AsyncCitationsResource) -> None:
        self._citations = citations

        self.get_graph = async_to_raw_response_wrapper(
            citations.get_graph,
        )
        self.get_summary = async_to_raw_response_wrapper(
            citations.get_summary,
        )


class CitationsResourceWithStreamingResponse:
    def __init__(self, citations: CitationsResource) -> None:
        self._citations = citations

        self.get_graph = to_streamed_response_wrapper(
            citations.get_graph,
        )
        self.get_summary = to_streamed_response_wrapper(
            citations.get_summary,
        )


class AsyncCitationsResourceWithStreamingResponse:
    def __init__(self, citations: AsyncCitationsResource) -> None:
        self._citations = citations

        self.get_graph = async_to_streamed_response_wrapper(
            citations.get_graph,
        )
        self.get_summary = async_to_streamed_response_wrapper(
            citations.get_summary,
        )
