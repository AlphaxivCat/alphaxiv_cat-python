# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.search.v2 import paper_fast_search_params
from ....types.search.v2.paper_fast_search_response import PaperFastSearchResponse

__all__ = ["PaperResource", "AsyncPaperResource"]


class PaperResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaperResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return PaperResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaperResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return PaperResourceWithStreamingResponse(self)

    def fast_search(
        self,
        *,
        include_private: Literal["true", "false"],
        q: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperFastSearchResponse:
        """
        Search for public and optionally private papers

        Source file:
        `api-server/src/controllers/search/v2/search-google-fast.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/v2/paper/fast",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_private": include_private,
                        "q": q,
                    },
                    paper_fast_search_params.PaperFastSearchParams,
                ),
            ),
            cast_to=PaperFastSearchResponse,
        )


class AsyncPaperResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaperResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaperResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaperResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncPaperResourceWithStreamingResponse(self)

    async def fast_search(
        self,
        *,
        include_private: Literal["true", "false"],
        q: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperFastSearchResponse:
        """
        Search for public and optionally private papers

        Source file:
        `api-server/src/controllers/search/v2/search-google-fast.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/v2/paper/fast",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_private": include_private,
                        "q": q,
                    },
                    paper_fast_search_params.PaperFastSearchParams,
                ),
            ),
            cast_to=PaperFastSearchResponse,
        )


class PaperResourceWithRawResponse:
    def __init__(self, paper: PaperResource) -> None:
        self._paper = paper

        self.fast_search = to_raw_response_wrapper(
            paper.fast_search,
        )


class AsyncPaperResourceWithRawResponse:
    def __init__(self, paper: AsyncPaperResource) -> None:
        self._paper = paper

        self.fast_search = async_to_raw_response_wrapper(
            paper.fast_search,
        )


class PaperResourceWithStreamingResponse:
    def __init__(self, paper: PaperResource) -> None:
        self._paper = paper

        self.fast_search = to_streamed_response_wrapper(
            paper.fast_search,
        )


class AsyncPaperResourceWithStreamingResponse:
    def __init__(self, paper: AsyncPaperResource) -> None:
        self._paper = paper

        self.fast_search = async_to_streamed_response_wrapper(
            paper.fast_search,
        )
