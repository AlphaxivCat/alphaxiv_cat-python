# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.papers import ingest_ingest_latest_params, ingest_ingest_version_params
from ...types.papers.ingest_ingest_latest_response import IngestIngestLatestResponse
from ...types.papers.ingest_ingest_version_response import IngestIngestVersionResponse

__all__ = ["IngestResource", "AsyncIngestResource"]


class IngestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IngestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return IngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IngestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return IngestResourceWithStreamingResponse(self)

    def ingest_latest(
        self,
        upid: str,
        *,
        prevent_tracking: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IngestIngestLatestResponse:
        """
        Ingest latest paper version if it doesn't exist (deprecated, used by browser
        extension)

        Source file:
        `api-server/src/controllers/v2/papers/ingest-paper-latest.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        return self._get(
            f"/v2/papers/{upid}/ingest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"prevent_tracking": prevent_tracking}, ingest_ingest_latest_params.IngestIngestLatestParams
                ),
            ),
            cast_to=IngestIngestLatestResponse,
        )

    def ingest_version(
        self,
        version_label: str,
        *,
        upid: str,
        prevent_tracking: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IngestIngestVersionResponse:
        """
        Ingest a paper version if it doesn't exist (deprecated, used by browser
        extension)

        Source file: `api-server/src/controllers/v2/papers/ingest-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        if not version_label:
            raise ValueError(f"Expected a non-empty value for `version_label` but received {version_label!r}")
        return self._get(
            f"/v2/papers/{upid}/ingest/versions/{version_label}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"prevent_tracking": prevent_tracking}, ingest_ingest_version_params.IngestIngestVersionParams
                ),
            ),
            cast_to=IngestIngestVersionResponse,
        )


class AsyncIngestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIngestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIngestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncIngestResourceWithStreamingResponse(self)

    async def ingest_latest(
        self,
        upid: str,
        *,
        prevent_tracking: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IngestIngestLatestResponse:
        """
        Ingest latest paper version if it doesn't exist (deprecated, used by browser
        extension)

        Source file:
        `api-server/src/controllers/v2/papers/ingest-paper-latest.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        return await self._get(
            f"/v2/papers/{upid}/ingest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"prevent_tracking": prevent_tracking}, ingest_ingest_latest_params.IngestIngestLatestParams
                ),
            ),
            cast_to=IngestIngestLatestResponse,
        )

    async def ingest_version(
        self,
        version_label: str,
        *,
        upid: str,
        prevent_tracking: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IngestIngestVersionResponse:
        """
        Ingest a paper version if it doesn't exist (deprecated, used by browser
        extension)

        Source file: `api-server/src/controllers/v2/papers/ingest-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        if not version_label:
            raise ValueError(f"Expected a non-empty value for `version_label` but received {version_label!r}")
        return await self._get(
            f"/v2/papers/{upid}/ingest/versions/{version_label}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"prevent_tracking": prevent_tracking}, ingest_ingest_version_params.IngestIngestVersionParams
                ),
            ),
            cast_to=IngestIngestVersionResponse,
        )


class IngestResourceWithRawResponse:
    def __init__(self, ingest: IngestResource) -> None:
        self._ingest = ingest

        self.ingest_latest = to_raw_response_wrapper(
            ingest.ingest_latest,
        )
        self.ingest_version = to_raw_response_wrapper(
            ingest.ingest_version,
        )


class AsyncIngestResourceWithRawResponse:
    def __init__(self, ingest: AsyncIngestResource) -> None:
        self._ingest = ingest

        self.ingest_latest = async_to_raw_response_wrapper(
            ingest.ingest_latest,
        )
        self.ingest_version = async_to_raw_response_wrapper(
            ingest.ingest_version,
        )


class IngestResourceWithStreamingResponse:
    def __init__(self, ingest: IngestResource) -> None:
        self._ingest = ingest

        self.ingest_latest = to_streamed_response_wrapper(
            ingest.ingest_latest,
        )
        self.ingest_version = to_streamed_response_wrapper(
            ingest.ingest_version,
        )


class AsyncIngestResourceWithStreamingResponse:
    def __init__(self, ingest: AsyncIngestResource) -> None:
        self._ingest = ingest

        self.ingest_latest = async_to_streamed_response_wrapper(
            ingest.ingest_latest,
        )
        self.ingest_version = async_to_streamed_response_wrapper(
            ingest.ingest_version,
        )
