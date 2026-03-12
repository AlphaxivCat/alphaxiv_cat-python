# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, SequenceNotStr, not_given
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
from ...types.papers import private_create_params, private_update_metadata_params
from ...types.papers.private_create_response import PrivateCreateResponse

__all__ = ["PrivateResource", "AsyncPrivateResource"]


class PrivateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrivateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return PrivateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrivateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return PrivateResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content_type: str,
        file: str,
        filename: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateCreateResponse:
        """
        Upload a private PDF paper

        Source file:
        `api-server/src/controllers/v2/papers/upload-private-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/papers/private",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "file": file,
                    "filename": filename,
                },
                private_create_params.PrivateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrivateCreateResponse,
        )

    def update_metadata(
        self,
        paper_id: str,
        *,
        abstract: str,
        authors: Iterable[private_update_metadata_params.Author],
        bibtex: Optional[str],
        categories: SequenceNotStr[str],
        publication_date: float,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update metadata for a private paper

        Source file:
        `api-server/src/controllers/v2/papers/update-private-paper.controller.ts`

        Args:
          paper_id: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/v2/papers/private/{paper_id}/metadata",
            body=maybe_transform(
                {
                    "abstract": abstract,
                    "authors": authors,
                    "bibtex": bibtex,
                    "categories": categories,
                    "publication_date": publication_date,
                    "title": title,
                },
                private_update_metadata_params.PrivateUpdateMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPrivateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrivateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrivateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrivateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncPrivateResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content_type: str,
        file: str,
        filename: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrivateCreateResponse:
        """
        Upload a private PDF paper

        Source file:
        `api-server/src/controllers/v2/papers/upload-private-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/papers/private",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "file": file,
                    "filename": filename,
                },
                private_create_params.PrivateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrivateCreateResponse,
        )

    async def update_metadata(
        self,
        paper_id: str,
        *,
        abstract: str,
        authors: Iterable[private_update_metadata_params.Author],
        bibtex: Optional[str],
        categories: SequenceNotStr[str],
        publication_date: float,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update metadata for a private paper

        Source file:
        `api-server/src/controllers/v2/papers/update-private-paper.controller.ts`

        Args:
          paper_id: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/v2/papers/private/{paper_id}/metadata",
            body=await async_maybe_transform(
                {
                    "abstract": abstract,
                    "authors": authors,
                    "bibtex": bibtex,
                    "categories": categories,
                    "publication_date": publication_date,
                    "title": title,
                },
                private_update_metadata_params.PrivateUpdateMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PrivateResourceWithRawResponse:
    def __init__(self, private: PrivateResource) -> None:
        self._private = private

        self.create = to_raw_response_wrapper(
            private.create,
        )
        self.update_metadata = to_raw_response_wrapper(
            private.update_metadata,
        )


class AsyncPrivateResourceWithRawResponse:
    def __init__(self, private: AsyncPrivateResource) -> None:
        self._private = private

        self.create = async_to_raw_response_wrapper(
            private.create,
        )
        self.update_metadata = async_to_raw_response_wrapper(
            private.update_metadata,
        )


class PrivateResourceWithStreamingResponse:
    def __init__(self, private: PrivateResource) -> None:
        self._private = private

        self.create = to_streamed_response_wrapper(
            private.create,
        )
        self.update_metadata = to_streamed_response_wrapper(
            private.update_metadata,
        )


class AsyncPrivateResourceWithStreamingResponse:
    def __init__(self, private: AsyncPrivateResource) -> None:
        self._private = private

        self.create = async_to_streamed_response_wrapper(
            private.create,
        )
        self.update_metadata = async_to_streamed_response_wrapper(
            private.update_metadata,
        )
