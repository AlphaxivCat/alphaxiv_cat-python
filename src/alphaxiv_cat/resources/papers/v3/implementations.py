# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.papers.v3 import implementation_create_params, implementation_delete_params
from ....types.papers.v3.implementation_list_response import ImplementationListResponse
from ....types.papers.v3.implementation_create_response import ImplementationCreateResponse

__all__ = ["ImplementationsResource", "AsyncImplementationsResource"]


class ImplementationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImplementationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return ImplementationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImplementationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return ImplementationsResourceWithStreamingResponse(self)

    def create(
        self,
        paper_group_id: str,
        *,
        implementation_type: Literal["alphaxiv", "marimo", "author"],
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImplementationCreateResponse:
        """
        Add an implementation (AlphaXiv, Marimo, Author, or Other)

        Source file:
        `api-server/src/controllers/papers/v3/add-implementation.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return self._post(
            f"/papers/v3/{paper_group_id}/implementations",
            body=maybe_transform(
                {
                    "implementation_type": implementation_type,
                    "url": url,
                },
                implementation_create_params.ImplementationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImplementationCreateResponse,
        )

    def list(
        self,
        paper_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImplementationListResponse:
        """
        Get all implementations for a paper (AlphaXiv, Marimo, Author, and Other)

        Source file:
        `api-server/src/controllers/papers/v3/get-implementations.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return self._get(
            f"/papers/v3/{paper_group_id}/implementations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImplementationListResponse,
        )

    def delete(
        self,
        implementation_id: str,
        *,
        paper_group_id: str,
        type: Literal["alphaxiv", "resource"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an implementation (AlphaXiv, Marimo, Author, or Other)

        Source file:
        `api-server/src/controllers/papers/v3/delete-implementation.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        if not implementation_id:
            raise ValueError(f"Expected a non-empty value for `implementation_id` but received {implementation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/papers/v3/{paper_group_id}/implementations/{implementation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, implementation_delete_params.ImplementationDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncImplementationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImplementationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImplementationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImplementationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncImplementationsResourceWithStreamingResponse(self)

    async def create(
        self,
        paper_group_id: str,
        *,
        implementation_type: Literal["alphaxiv", "marimo", "author"],
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImplementationCreateResponse:
        """
        Add an implementation (AlphaXiv, Marimo, Author, or Other)

        Source file:
        `api-server/src/controllers/papers/v3/add-implementation.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return await self._post(
            f"/papers/v3/{paper_group_id}/implementations",
            body=await async_maybe_transform(
                {
                    "implementation_type": implementation_type,
                    "url": url,
                },
                implementation_create_params.ImplementationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImplementationCreateResponse,
        )

    async def list(
        self,
        paper_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImplementationListResponse:
        """
        Get all implementations for a paper (AlphaXiv, Marimo, Author, and Other)

        Source file:
        `api-server/src/controllers/papers/v3/get-implementations.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return await self._get(
            f"/papers/v3/{paper_group_id}/implementations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImplementationListResponse,
        )

    async def delete(
        self,
        implementation_id: str,
        *,
        paper_group_id: str,
        type: Literal["alphaxiv", "resource"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an implementation (AlphaXiv, Marimo, Author, or Other)

        Source file:
        `api-server/src/controllers/papers/v3/delete-implementation.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        if not implementation_id:
            raise ValueError(f"Expected a non-empty value for `implementation_id` but received {implementation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/papers/v3/{paper_group_id}/implementations/{implementation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, implementation_delete_params.ImplementationDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class ImplementationsResourceWithRawResponse:
    def __init__(self, implementations: ImplementationsResource) -> None:
        self._implementations = implementations

        self.create = to_raw_response_wrapper(
            implementations.create,
        )
        self.list = to_raw_response_wrapper(
            implementations.list,
        )
        self.delete = to_raw_response_wrapper(
            implementations.delete,
        )


class AsyncImplementationsResourceWithRawResponse:
    def __init__(self, implementations: AsyncImplementationsResource) -> None:
        self._implementations = implementations

        self.create = async_to_raw_response_wrapper(
            implementations.create,
        )
        self.list = async_to_raw_response_wrapper(
            implementations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            implementations.delete,
        )


class ImplementationsResourceWithStreamingResponse:
    def __init__(self, implementations: ImplementationsResource) -> None:
        self._implementations = implementations

        self.create = to_streamed_response_wrapper(
            implementations.create,
        )
        self.list = to_streamed_response_wrapper(
            implementations.list,
        )
        self.delete = to_streamed_response_wrapper(
            implementations.delete,
        )


class AsyncImplementationsResourceWithStreamingResponse:
    def __init__(self, implementations: AsyncImplementationsResource) -> None:
        self._implementations = implementations

        self.create = async_to_streamed_response_wrapper(
            implementations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            implementations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            implementations.delete,
        )
