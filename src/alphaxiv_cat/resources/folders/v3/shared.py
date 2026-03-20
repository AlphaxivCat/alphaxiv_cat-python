# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.folders.v3.shared_copy_response import SharedCopyResponse
from ....types.folders.v3.shared_retrieve_response import SharedRetrieveResponse

__all__ = ["SharedResource", "AsyncSharedResource"]


class SharedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SharedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return SharedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SharedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return SharedResourceWithStreamingResponse(self)

    def retrieve(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedRetrieveResponse:
        """
        Get a folder that has been shared publicly, including nested child folders

        Source file:
        `api-server/src/controllers/folders/v3/get-shared-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            path_template("/folders/v3/shared/{folder_id}", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedRetrieveResponse,
        )

    def copy(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedCopyResponse:
        """
        Copy a shared folder and all nested folders to your own library

        Source file:
        `api-server/src/controllers/folders/v3/copy-shared-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._post(
            path_template("/folders/v3/shared/{folder_id}/copy", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedCopyResponse,
        )


class AsyncSharedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSharedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSharedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSharedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncSharedResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedRetrieveResponse:
        """
        Get a folder that has been shared publicly, including nested child folders

        Source file:
        `api-server/src/controllers/folders/v3/get-shared-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            path_template("/folders/v3/shared/{folder_id}", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedRetrieveResponse,
        )

    async def copy(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedCopyResponse:
        """
        Copy a shared folder and all nested folders to your own library

        Source file:
        `api-server/src/controllers/folders/v3/copy-shared-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._post(
            path_template("/folders/v3/shared/{folder_id}/copy", folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedCopyResponse,
        )


class SharedResourceWithRawResponse:
    def __init__(self, shared: SharedResource) -> None:
        self._shared = shared

        self.retrieve = to_raw_response_wrapper(
            shared.retrieve,
        )
        self.copy = to_raw_response_wrapper(
            shared.copy,
        )


class AsyncSharedResourceWithRawResponse:
    def __init__(self, shared: AsyncSharedResource) -> None:
        self._shared = shared

        self.retrieve = async_to_raw_response_wrapper(
            shared.retrieve,
        )
        self.copy = async_to_raw_response_wrapper(
            shared.copy,
        )


class SharedResourceWithStreamingResponse:
    def __init__(self, shared: SharedResource) -> None:
        self._shared = shared

        self.retrieve = to_streamed_response_wrapper(
            shared.retrieve,
        )
        self.copy = to_streamed_response_wrapper(
            shared.copy,
        )


class AsyncSharedResourceWithStreamingResponse:
    def __init__(self, shared: AsyncSharedResource) -> None:
        self._shared = shared

        self.retrieve = async_to_streamed_response_wrapper(
            shared.retrieve,
        )
        self.copy = async_to_streamed_response_wrapper(
            shared.copy,
        )
