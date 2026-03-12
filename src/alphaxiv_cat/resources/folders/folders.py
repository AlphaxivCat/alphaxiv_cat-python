# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v3.v3 import (
    V3Resource,
    AsyncV3Resource,
    V3ResourceWithRawResponse,
    AsyncV3ResourceWithRawResponse,
    V3ResourceWithStreamingResponse,
    AsyncV3ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def v3(self) -> V3Resource:
        return V3Resource(self._client)

    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return FoldersResourceWithStreamingResponse(self)


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def v3(self) -> AsyncV3Resource:
        return AsyncV3Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncFoldersResourceWithStreamingResponse(self)


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

    @cached_property
    def v3(self) -> V3ResourceWithRawResponse:
        return V3ResourceWithRawResponse(self._folders.v3)


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

    @cached_property
    def v3(self) -> AsyncV3ResourceWithRawResponse:
        return AsyncV3ResourceWithRawResponse(self._folders.v3)


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

    @cached_property
    def v3(self) -> V3ResourceWithStreamingResponse:
        return V3ResourceWithStreamingResponse(self._folders.v3)


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

    @cached_property
    def v3(self) -> AsyncV3ResourceWithStreamingResponse:
        return AsyncV3ResourceWithStreamingResponse(self._folders.v3)
