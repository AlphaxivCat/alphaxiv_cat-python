# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .paper_view_count import (
    PaperViewCountResource,
    AsyncPaperViewCountResource,
    PaperViewCountResourceWithRawResponse,
    AsyncPaperViewCountResourceWithRawResponse,
    PaperViewCountResourceWithStreamingResponse,
    AsyncPaperViewCountResourceWithStreamingResponse,
)

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def paper_view_count(self) -> PaperViewCountResource:
        return PaperViewCountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def paper_view_count(self) -> AsyncPaperViewCountResource:
        return AsyncPaperViewCountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def paper_view_count(self) -> PaperViewCountResourceWithRawResponse:
        return PaperViewCountResourceWithRawResponse(self._analytics.paper_view_count)


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def paper_view_count(self) -> AsyncPaperViewCountResourceWithRawResponse:
        return AsyncPaperViewCountResourceWithRawResponse(self._analytics.paper_view_count)


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def paper_view_count(self) -> PaperViewCountResourceWithStreamingResponse:
        return PaperViewCountResourceWithStreamingResponse(self._analytics.paper_view_count)


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def paper_view_count(self) -> AsyncPaperViewCountResourceWithStreamingResponse:
        return AsyncPaperViewCountResourceWithStreamingResponse(self._analytics.paper_view_count)
