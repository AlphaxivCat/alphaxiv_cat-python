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
from ....types.arxiv.v1.lab_retrieve_response import LabRetrieveResponse

__all__ = ["LabsResource", "AsyncLabsResource"]


class LabsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return LabsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return LabsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        unresolved: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabRetrieveResponse:
        """
        Gets data necessary to render arXiv labs.

        Source file:
        `api-server/src/controllers/arxiv/v1/get-arxiv-labs-data.controller.ts`

        Args:
          unresolved: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unresolved:
            raise ValueError(f"Expected a non-empty value for `unresolved` but received {unresolved!r}")
        return self._get(
            f"/arxiv/v1/{unresolved}/labs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabRetrieveResponse,
        )


class AsyncLabsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncLabsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        unresolved: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabRetrieveResponse:
        """
        Gets data necessary to render arXiv labs.

        Source file:
        `api-server/src/controllers/arxiv/v1/get-arxiv-labs-data.controller.ts`

        Args:
          unresolved: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unresolved:
            raise ValueError(f"Expected a non-empty value for `unresolved` but received {unresolved!r}")
        return await self._get(
            f"/arxiv/v1/{unresolved}/labs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabRetrieveResponse,
        )


class LabsResourceWithRawResponse:
    def __init__(self, labs: LabsResource) -> None:
        self._labs = labs

        self.retrieve = to_raw_response_wrapper(
            labs.retrieve,
        )


class AsyncLabsResourceWithRawResponse:
    def __init__(self, labs: AsyncLabsResource) -> None:
        self._labs = labs

        self.retrieve = async_to_raw_response_wrapper(
            labs.retrieve,
        )


class LabsResourceWithStreamingResponse:
    def __init__(self, labs: LabsResource) -> None:
        self._labs = labs

        self.retrieve = to_streamed_response_wrapper(
            labs.retrieve,
        )


class AsyncLabsResourceWithStreamingResponse:
    def __init__(self, labs: AsyncLabsResource) -> None:
        self._labs = labs

        self.retrieve = async_to_streamed_response_wrapper(
            labs.retrieve,
        )
