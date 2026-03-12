# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1.v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ArxivResource", "AsyncArxivResource"]


class ArxivResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> ArxivResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return ArxivResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArxivResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return ArxivResourceWithStreamingResponse(self)


class AsyncArxivResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncArxivResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArxivResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArxivResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncArxivResourceWithStreamingResponse(self)


class ArxivResourceWithRawResponse:
    def __init__(self, arxiv: ArxivResource) -> None:
        self._arxiv = arxiv

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._arxiv.v1)


class AsyncArxivResourceWithRawResponse:
    def __init__(self, arxiv: AsyncArxivResource) -> None:
        self._arxiv = arxiv

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._arxiv.v1)


class ArxivResourceWithStreamingResponse:
    def __init__(self, arxiv: ArxivResource) -> None:
        self._arxiv = arxiv

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._arxiv.v1)


class AsyncArxivResourceWithStreamingResponse:
    def __init__(self, arxiv: AsyncArxivResource) -> None:
        self._arxiv = arxiv

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._arxiv.v1)
