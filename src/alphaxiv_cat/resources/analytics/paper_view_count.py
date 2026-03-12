# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Optional

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
from ...types.analytics import (
    paper_view_count_kickoff_job_params,
    paper_view_count_process_job_params,
    paper_view_count_ingest_event_params,
)
from ...types.analytics.paper_view_count_kickoff_job_response import PaperViewCountKickoffJobResponse
from ...types.analytics.paper_view_count_process_job_response import PaperViewCountProcessJobResponse
from ...types.analytics.paper_view_count_ingest_event_response import PaperViewCountIngestEventResponse

__all__ = ["PaperViewCountResource", "AsyncPaperViewCountResource"]


class PaperViewCountResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaperViewCountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return PaperViewCountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaperViewCountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return PaperViewCountResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def ingest_event(
        self,
        *,
        paper_id: str,
        created_at: str | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperViewCountIngestEventResponse:
        """
        Track a paper view event for analytics

        Source file:
        `api-server/src/controllers/v1/analytics/ingest-paper-view-count-event.controller.ts`

        Args:
          paper_id: Paper ID to track view for

          created_at: Optional timestamp for the view event

          user_id: Optional user ID who viewed the paper

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/analytics/paper-view-count/ingest",
            body=maybe_transform(
                {
                    "paper_id": paper_id,
                    "created_at": created_at,
                    "user_id": user_id,
                },
                paper_view_count_ingest_event_params.PaperViewCountIngestEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperViewCountIngestEventResponse,
        )

    def kickoff_job(
        self,
        *,
        type: str,
        like: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperViewCountKickoffJobResponse:
        """
        Kicks off a background job to aggregate paper view counts

        Source file:
        `api-server/src/controllers/v1/analytics/kickoff-paper-view-count-aggregation-job.controller.ts`

        Args:
          type: Time period filter: 'all' or number of days

          like: Optional filter for likes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/analytics/paper-view-count/kickoff-job",
            body=maybe_transform(
                {
                    "type": type,
                    "like": like,
                },
                paper_view_count_kickoff_job_params.PaperViewCountKickoffJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperViewCountKickoffJobResponse,
        )

    def process_job(
        self,
        *,
        paper_id: str,
        publication_date: str,
        like: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperViewCountProcessJobResponse:
        """
        Process view count aggregation for a specific paper

        Source file:
        `api-server/src/controllers/v1/analytics/process-paper-view-count-aggregation-job.controller.ts`

        Args:
          paper_id: Paper ID to process view counts for

          publication_date: Publication date for age decay calculation

          like: Whether to add noise to votes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/analytics/paper-view-count/process-job",
            body=maybe_transform(
                {
                    "paper_id": paper_id,
                    "publication_date": publication_date,
                    "like": like,
                },
                paper_view_count_process_job_params.PaperViewCountProcessJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperViewCountProcessJobResponse,
        )


class AsyncPaperViewCountResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaperViewCountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaperViewCountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaperViewCountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncPaperViewCountResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def ingest_event(
        self,
        *,
        paper_id: str,
        created_at: str | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperViewCountIngestEventResponse:
        """
        Track a paper view event for analytics

        Source file:
        `api-server/src/controllers/v1/analytics/ingest-paper-view-count-event.controller.ts`

        Args:
          paper_id: Paper ID to track view for

          created_at: Optional timestamp for the view event

          user_id: Optional user ID who viewed the paper

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/analytics/paper-view-count/ingest",
            body=await async_maybe_transform(
                {
                    "paper_id": paper_id,
                    "created_at": created_at,
                    "user_id": user_id,
                },
                paper_view_count_ingest_event_params.PaperViewCountIngestEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperViewCountIngestEventResponse,
        )

    async def kickoff_job(
        self,
        *,
        type: str,
        like: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperViewCountKickoffJobResponse:
        """
        Kicks off a background job to aggregate paper view counts

        Source file:
        `api-server/src/controllers/v1/analytics/kickoff-paper-view-count-aggregation-job.controller.ts`

        Args:
          type: Time period filter: 'all' or number of days

          like: Optional filter for likes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/analytics/paper-view-count/kickoff-job",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "like": like,
                },
                paper_view_count_kickoff_job_params.PaperViewCountKickoffJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperViewCountKickoffJobResponse,
        )

    async def process_job(
        self,
        *,
        paper_id: str,
        publication_date: str,
        like: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperViewCountProcessJobResponse:
        """
        Process view count aggregation for a specific paper

        Source file:
        `api-server/src/controllers/v1/analytics/process-paper-view-count-aggregation-job.controller.ts`

        Args:
          paper_id: Paper ID to process view counts for

          publication_date: Publication date for age decay calculation

          like: Whether to add noise to votes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/analytics/paper-view-count/process-job",
            body=await async_maybe_transform(
                {
                    "paper_id": paper_id,
                    "publication_date": publication_date,
                    "like": like,
                },
                paper_view_count_process_job_params.PaperViewCountProcessJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperViewCountProcessJobResponse,
        )


class PaperViewCountResourceWithRawResponse:
    def __init__(self, paper_view_count: PaperViewCountResource) -> None:
        self._paper_view_count = paper_view_count

        self.ingest_event = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                paper_view_count.ingest_event,  # pyright: ignore[reportDeprecated],
            )
        )
        self.kickoff_job = to_raw_response_wrapper(
            paper_view_count.kickoff_job,
        )
        self.process_job = to_raw_response_wrapper(
            paper_view_count.process_job,
        )


class AsyncPaperViewCountResourceWithRawResponse:
    def __init__(self, paper_view_count: AsyncPaperViewCountResource) -> None:
        self._paper_view_count = paper_view_count

        self.ingest_event = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                paper_view_count.ingest_event,  # pyright: ignore[reportDeprecated],
            )
        )
        self.kickoff_job = async_to_raw_response_wrapper(
            paper_view_count.kickoff_job,
        )
        self.process_job = async_to_raw_response_wrapper(
            paper_view_count.process_job,
        )


class PaperViewCountResourceWithStreamingResponse:
    def __init__(self, paper_view_count: PaperViewCountResource) -> None:
        self._paper_view_count = paper_view_count

        self.ingest_event = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                paper_view_count.ingest_event,  # pyright: ignore[reportDeprecated],
            )
        )
        self.kickoff_job = to_streamed_response_wrapper(
            paper_view_count.kickoff_job,
        )
        self.process_job = to_streamed_response_wrapper(
            paper_view_count.process_job,
        )


class AsyncPaperViewCountResourceWithStreamingResponse:
    def __init__(self, paper_view_count: AsyncPaperViewCountResource) -> None:
        self._paper_view_count = paper_view_count

        self.ingest_event = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                paper_view_count.ingest_event,  # pyright: ignore[reportDeprecated],
            )
        )
        self.kickoff_job = async_to_streamed_response_wrapper(
            paper_view_count.kickoff_job,
        )
        self.process_job = async_to_streamed_response_wrapper(
            paper_view_count.process_job,
        )
