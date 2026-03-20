# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.papers import metadata_retrieve_latest_metadata_params, metadata_retrieve_version_metadata_params
from ...types.papers.metadata_retrieve_latest_metadata_response import MetadataRetrieveLatestMetadataResponse
from ...types.papers.metadata_retrieve_version_metadata_response import MetadataRetrieveVersionMetadataResponse

__all__ = ["MetadataResource", "AsyncMetadataResource"]


class MetadataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return MetadataResourceWithStreamingResponse(self)

    def retrieve_latest_metadata(
        self,
        upid: str,
        *,
        prevent_tracking: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetadataRetrieveLatestMetadataResponse:
        """
        Get metadata for latest paper version (deprecated, used by browser extension)

        Source file:
        `api-server/src/controllers/v2/papers/get-paper-metadata-latest.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        return self._get(
            path_template("/v2/papers/{upid}/metadata", upid=upid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"prevent_tracking": prevent_tracking},
                    metadata_retrieve_latest_metadata_params.MetadataRetrieveLatestMetadataParams,
                ),
            ),
            cast_to=MetadataRetrieveLatestMetadataResponse,
        )

    def retrieve_version_metadata(
        self,
        version_order: str,
        *,
        upid: str,
        prevent_tracking: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetadataRetrieveVersionMetadataResponse:
        """
        Get metadata for a specific paper version (deprecated, used by browser
        extension)

        Source file:
        `api-server/src/controllers/v2/papers/get-paper-metadata.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        if not version_order:
            raise ValueError(f"Expected a non-empty value for `version_order` but received {version_order!r}")
        return self._get(
            path_template(
                "/v2/papers/{upid}/metadata/versions/{version_order}", upid=upid, version_order=version_order
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"prevent_tracking": prevent_tracking},
                    metadata_retrieve_version_metadata_params.MetadataRetrieveVersionMetadataParams,
                ),
            ),
            cast_to=MetadataRetrieveVersionMetadataResponse,
        )


class AsyncMetadataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncMetadataResourceWithStreamingResponse(self)

    async def retrieve_latest_metadata(
        self,
        upid: str,
        *,
        prevent_tracking: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetadataRetrieveLatestMetadataResponse:
        """
        Get metadata for latest paper version (deprecated, used by browser extension)

        Source file:
        `api-server/src/controllers/v2/papers/get-paper-metadata-latest.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        return await self._get(
            path_template("/v2/papers/{upid}/metadata", upid=upid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"prevent_tracking": prevent_tracking},
                    metadata_retrieve_latest_metadata_params.MetadataRetrieveLatestMetadataParams,
                ),
            ),
            cast_to=MetadataRetrieveLatestMetadataResponse,
        )

    async def retrieve_version_metadata(
        self,
        version_order: str,
        *,
        upid: str,
        prevent_tracking: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetadataRetrieveVersionMetadataResponse:
        """
        Get metadata for a specific paper version (deprecated, used by browser
        extension)

        Source file:
        `api-server/src/controllers/v2/papers/get-paper-metadata.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        if not version_order:
            raise ValueError(f"Expected a non-empty value for `version_order` but received {version_order!r}")
        return await self._get(
            path_template(
                "/v2/papers/{upid}/metadata/versions/{version_order}", upid=upid, version_order=version_order
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"prevent_tracking": prevent_tracking},
                    metadata_retrieve_version_metadata_params.MetadataRetrieveVersionMetadataParams,
                ),
            ),
            cast_to=MetadataRetrieveVersionMetadataResponse,
        )


class MetadataResourceWithRawResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.retrieve_latest_metadata = to_raw_response_wrapper(
            metadata.retrieve_latest_metadata,
        )
        self.retrieve_version_metadata = to_raw_response_wrapper(
            metadata.retrieve_version_metadata,
        )


class AsyncMetadataResourceWithRawResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.retrieve_latest_metadata = async_to_raw_response_wrapper(
            metadata.retrieve_latest_metadata,
        )
        self.retrieve_version_metadata = async_to_raw_response_wrapper(
            metadata.retrieve_version_metadata,
        )


class MetadataResourceWithStreamingResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.retrieve_latest_metadata = to_streamed_response_wrapper(
            metadata.retrieve_latest_metadata,
        )
        self.retrieve_version_metadata = to_streamed_response_wrapper(
            metadata.retrieve_version_metadata,
        )


class AsyncMetadataResourceWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.retrieve_latest_metadata = async_to_streamed_response_wrapper(
            metadata.retrieve_latest_metadata,
        )
        self.retrieve_version_metadata = async_to_streamed_response_wrapper(
            metadata.retrieve_version_metadata,
        )
