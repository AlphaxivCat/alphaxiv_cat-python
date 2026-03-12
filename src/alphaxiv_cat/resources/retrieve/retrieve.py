# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RetrieveResource", "AsyncRetrieveResource"]


class RetrieveResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> RetrieveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return RetrieveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrieveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return RetrieveResourceWithStreamingResponse(self)


class AsyncRetrieveResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRetrieveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrieveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrieveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncRetrieveResourceWithStreamingResponse(self)


class RetrieveResourceWithRawResponse:
    def __init__(self, retrieve: RetrieveResource) -> None:
        self._retrieve = retrieve

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._retrieve.v1)


class AsyncRetrieveResourceWithRawResponse:
    def __init__(self, retrieve: AsyncRetrieveResource) -> None:
        self._retrieve = retrieve

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._retrieve.v1)


class RetrieveResourceWithStreamingResponse:
    def __init__(self, retrieve: RetrieveResource) -> None:
        self._retrieve = retrieve

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._retrieve.v1)


class AsyncRetrieveResourceWithStreamingResponse:
    def __init__(self, retrieve: AsyncRetrieveResource) -> None:
        self._retrieve = retrieve

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._retrieve.v1)
