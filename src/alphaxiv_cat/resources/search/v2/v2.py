# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .paper import (
    PaperResource,
    AsyncPaperResource,
    PaperResourceWithRawResponse,
    AsyncPaperResourceWithRawResponse,
    PaperResourceWithStreamingResponse,
    AsyncPaperResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def paper(self) -> PaperResource:
        return PaperResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def paper(self) -> AsyncPaperResource:
        return AsyncPaperResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def paper(self) -> PaperResourceWithRawResponse:
        return PaperResourceWithRawResponse(self._v2.paper)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def paper(self) -> AsyncPaperResourceWithRawResponse:
        return AsyncPaperResourceWithRawResponse(self._v2.paper)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def paper(self) -> PaperResourceWithStreamingResponse:
        return PaperResourceWithStreamingResponse(self._v2.paper)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def paper(self) -> AsyncPaperResourceWithStreamingResponse:
        return AsyncPaperResourceWithStreamingResponse(self._v2.paper)
