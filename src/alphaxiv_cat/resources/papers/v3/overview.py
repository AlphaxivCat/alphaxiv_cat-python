# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....types.papers.v3.overview_retrieve_response import OverviewRetrieveResponse
from ....types.papers.v3.overview_retrieve_status_response import OverviewRetrieveStatusResponse

__all__ = ["OverviewResource", "AsyncOverviewResource"]


class OverviewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OverviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return OverviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return OverviewResourceWithStreamingResponse(self)

    def retrieve(
        self,
        language: Literal[
            "am",
            "ar",
            "az",
            "bg",
            "bn",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "et",
            "fa",
            "fi",
            "fr",
            "gu",
            "ha",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ka",
            "kn",
            "ko",
            "lt",
            "lv",
            "ml",
            "mr",
            "ms",
            "my",
            "ne",
            "nl",
            "no",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "si",
            "sk",
            "sl",
            "sr",
            "sv",
            "sw",
            "ta",
            "te",
            "th",
            "tl",
            "tr",
            "uk",
            "ur",
            "uz",
            "vi",
            "yo",
            "zh",
        ],
        *,
        paper_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverviewRetrieveResponse:
        """Retrieve paper version overview for given language.

        Does not create it if it
        doesn't exist

        Source file: `api-server/src/controllers/papers/v3/get-overviews.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_version:
            raise ValueError(f"Expected a non-empty value for `paper_version` but received {paper_version!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return self._get(
            f"/papers/v3/{paper_version}/overview/{language}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverviewRetrieveResponse,
        )

    def retrieve_status(
        self,
        paper_version: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverviewRetrieveStatusResponse:
        """
        Retrieve paper version status for overview generation and translations

        Source file:
        `api-server/src/controllers/papers/v3/get-overviews-status.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_version:
            raise ValueError(f"Expected a non-empty value for `paper_version` but received {paper_version!r}")
        return self._get(
            f"/papers/v3/{paper_version}/overview/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverviewRetrieveStatusResponse,
        )


class AsyncOverviewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOverviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOverviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncOverviewResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        language: Literal[
            "am",
            "ar",
            "az",
            "bg",
            "bn",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "et",
            "fa",
            "fi",
            "fr",
            "gu",
            "ha",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ka",
            "kn",
            "ko",
            "lt",
            "lv",
            "ml",
            "mr",
            "ms",
            "my",
            "ne",
            "nl",
            "no",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "si",
            "sk",
            "sl",
            "sr",
            "sv",
            "sw",
            "ta",
            "te",
            "th",
            "tl",
            "tr",
            "uk",
            "ur",
            "uz",
            "vi",
            "yo",
            "zh",
        ],
        *,
        paper_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverviewRetrieveResponse:
        """Retrieve paper version overview for given language.

        Does not create it if it
        doesn't exist

        Source file: `api-server/src/controllers/papers/v3/get-overviews.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_version:
            raise ValueError(f"Expected a non-empty value for `paper_version` but received {paper_version!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return await self._get(
            f"/papers/v3/{paper_version}/overview/{language}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverviewRetrieveResponse,
        )

    async def retrieve_status(
        self,
        paper_version: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OverviewRetrieveStatusResponse:
        """
        Retrieve paper version status for overview generation and translations

        Source file:
        `api-server/src/controllers/papers/v3/get-overviews-status.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_version:
            raise ValueError(f"Expected a non-empty value for `paper_version` but received {paper_version!r}")
        return await self._get(
            f"/papers/v3/{paper_version}/overview/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverviewRetrieveStatusResponse,
        )


class OverviewResourceWithRawResponse:
    def __init__(self, overview: OverviewResource) -> None:
        self._overview = overview

        self.retrieve = to_raw_response_wrapper(
            overview.retrieve,
        )
        self.retrieve_status = to_raw_response_wrapper(
            overview.retrieve_status,
        )


class AsyncOverviewResourceWithRawResponse:
    def __init__(self, overview: AsyncOverviewResource) -> None:
        self._overview = overview

        self.retrieve = async_to_raw_response_wrapper(
            overview.retrieve,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            overview.retrieve_status,
        )


class OverviewResourceWithStreamingResponse:
    def __init__(self, overview: OverviewResource) -> None:
        self._overview = overview

        self.retrieve = to_streamed_response_wrapper(
            overview.retrieve,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            overview.retrieve_status,
        )


class AsyncOverviewResourceWithStreamingResponse:
    def __init__(self, overview: AsyncOverviewResource) -> None:
        self._overview = overview

        self.retrieve = async_to_streamed_response_wrapper(
            overview.retrieve,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            overview.retrieve_status,
        )
