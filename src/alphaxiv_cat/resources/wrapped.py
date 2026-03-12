# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.wrapped_retrieve_by_user_response import WrappedRetrieveByUserResponse

__all__ = ["WrappedResource", "AsyncWrappedResource"]


class WrappedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WrappedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return WrappedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WrappedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return WrappedResourceWithStreamingResponse(self)

    def retrieve_by_user(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WrappedRetrieveByUserResponse:
        """
        Get all wrapped data for a specific user across all years

        Source file:
        `api-server/src/controllers/wrapped/v1/get-wrapped-by-user.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/wrapped/v1/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WrappedRetrieveByUserResponse,
        )


class AsyncWrappedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWrappedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWrappedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWrappedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncWrappedResourceWithStreamingResponse(self)

    async def retrieve_by_user(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WrappedRetrieveByUserResponse:
        """
        Get all wrapped data for a specific user across all years

        Source file:
        `api-server/src/controllers/wrapped/v1/get-wrapped-by-user.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/wrapped/v1/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WrappedRetrieveByUserResponse,
        )


class WrappedResourceWithRawResponse:
    def __init__(self, wrapped: WrappedResource) -> None:
        self._wrapped = wrapped

        self.retrieve_by_user = to_raw_response_wrapper(
            wrapped.retrieve_by_user,
        )


class AsyncWrappedResourceWithRawResponse:
    def __init__(self, wrapped: AsyncWrappedResource) -> None:
        self._wrapped = wrapped

        self.retrieve_by_user = async_to_raw_response_wrapper(
            wrapped.retrieve_by_user,
        )


class WrappedResourceWithStreamingResponse:
    def __init__(self, wrapped: WrappedResource) -> None:
        self._wrapped = wrapped

        self.retrieve_by_user = to_streamed_response_wrapper(
            wrapped.retrieve_by_user,
        )


class AsyncWrappedResourceWithStreamingResponse:
    def __init__(self, wrapped: AsyncWrappedResource) -> None:
        self._wrapped = wrapped

        self.retrieve_by_user = async_to_streamed_response_wrapper(
            wrapped.retrieve_by_user,
        )
