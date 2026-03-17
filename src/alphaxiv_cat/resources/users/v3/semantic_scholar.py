# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

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
from ....types.users.v3.semantic_scholar_link_response import SemanticScholarLinkResponse
from ....types.users.v3.semantic_scholar_scrape_response import SemanticScholarScrapeResponse

__all__ = ["SemanticScholarResource", "AsyncSemanticScholarResource"]


class SemanticScholarResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SemanticScholarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return SemanticScholarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SemanticScholarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return SemanticScholarResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def link(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SemanticScholarLinkResponse:
        """
        Link a user's account to a Semantic Scholar profile based on claimed papers

        Source file:
        `api-server/src/controllers/users/v3/link-semantic-scholar.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/users/v3/{id}/semantic-scholar/link",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SemanticScholarLinkResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def scrape(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SemanticScholarScrapeResponse:
        """
        Refresh Semantic Scholar data for a linked user

        Source file:
        `api-server/src/controllers/users/v3/scrape-semantic-scholar.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/users/v3/{id}/semantic-scholar/scrape",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SemanticScholarScrapeResponse,
        )


class AsyncSemanticScholarResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSemanticScholarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSemanticScholarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSemanticScholarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncSemanticScholarResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def link(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SemanticScholarLinkResponse:
        """
        Link a user's account to a Semantic Scholar profile based on claimed papers

        Source file:
        `api-server/src/controllers/users/v3/link-semantic-scholar.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/users/v3/{id}/semantic-scholar/link",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SemanticScholarLinkResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def scrape(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SemanticScholarScrapeResponse:
        """
        Refresh Semantic Scholar data for a linked user

        Source file:
        `api-server/src/controllers/users/v3/scrape-semantic-scholar.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/users/v3/{id}/semantic-scholar/scrape",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SemanticScholarScrapeResponse,
        )


class SemanticScholarResourceWithRawResponse:
    def __init__(self, semantic_scholar: SemanticScholarResource) -> None:
        self._semantic_scholar = semantic_scholar

        self.link = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                semantic_scholar.link,  # pyright: ignore[reportDeprecated],
            )
        )
        self.scrape = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                semantic_scholar.scrape,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncSemanticScholarResourceWithRawResponse:
    def __init__(self, semantic_scholar: AsyncSemanticScholarResource) -> None:
        self._semantic_scholar = semantic_scholar

        self.link = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                semantic_scholar.link,  # pyright: ignore[reportDeprecated],
            )
        )
        self.scrape = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                semantic_scholar.scrape,  # pyright: ignore[reportDeprecated],
            )
        )


class SemanticScholarResourceWithStreamingResponse:
    def __init__(self, semantic_scholar: SemanticScholarResource) -> None:
        self._semantic_scholar = semantic_scholar

        self.link = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                semantic_scholar.link,  # pyright: ignore[reportDeprecated],
            )
        )
        self.scrape = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                semantic_scholar.scrape,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncSemanticScholarResourceWithStreamingResponse:
    def __init__(self, semantic_scholar: AsyncSemanticScholarResource) -> None:
        self._semantic_scholar = semantic_scholar

        self.link = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                semantic_scholar.link,  # pyright: ignore[reportDeprecated],
            )
        )
        self.scrape = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                semantic_scholar.scrape,  # pyright: ignore[reportDeprecated],
            )
        )
