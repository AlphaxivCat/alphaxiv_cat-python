# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.api_keys import v1_create_params, v1_create_impersonation_params
from ...types.api_keys.v1_list_response import V1ListResponse
from ...types.api_keys.v1_create_response import V1CreateResponse
from ...types.api_keys.v1_revoke_response import V1RevokeResponse
from ...types.api_keys.v1_create_impersonation_response import V1CreateImpersonationResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        label: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1CreateResponse:
        """
        Create a new API key for the current user.

        Source file:
        `api-server/src/controllers/api-keys/v1/create-api-key.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api-keys/v1",
            body=maybe_transform({"label": label}, v1_create_params.V1CreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1CreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ListResponse:
        """
        List API keys for the current user.

        Source file: `api-server/src/controllers/api-keys/v1/get-api-keys.controller.ts`
        """
        return self._get(
            "/api-keys/v1",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResponse,
        )

    def create_impersonation(
        self,
        *,
        user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1CreateImpersonationResponse:
        """
        Create a new API key for the current user.

        Source file:
        `api-server/src/controllers/api-keys/v1/create-impersonation-api-key.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api-keys/v1/impersonate",
            body=maybe_transform({"user": user}, v1_create_impersonation_params.V1CreateImpersonationParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1CreateImpersonationResponse,
        )

    def revoke(
        self,
        api_key_id: Union[str, Literal["own"]],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RevokeResponse:
        """Revoke an API key for the authenticated user.

        No-op if already revoked.

        Source file:
        `api-server/src/controllers/api-keys/v1/revoke-api-key.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/api-keys/v1/{api_key_id}/revoke",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1RevokeResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        label: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1CreateResponse:
        """
        Create a new API key for the current user.

        Source file:
        `api-server/src/controllers/api-keys/v1/create-api-key.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api-keys/v1",
            body=await async_maybe_transform({"label": label}, v1_create_params.V1CreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1CreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1ListResponse:
        """
        List API keys for the current user.

        Source file: `api-server/src/controllers/api-keys/v1/get-api-keys.controller.ts`
        """
        return await self._get(
            "/api-keys/v1",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ListResponse,
        )

    async def create_impersonation(
        self,
        *,
        user: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1CreateImpersonationResponse:
        """
        Create a new API key for the current user.

        Source file:
        `api-server/src/controllers/api-keys/v1/create-impersonation-api-key.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api-keys/v1/impersonate",
            body=await async_maybe_transform(
                {"user": user}, v1_create_impersonation_params.V1CreateImpersonationParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1CreateImpersonationResponse,
        )

    async def revoke(
        self,
        api_key_id: Union[str, Literal["own"]],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RevokeResponse:
        """Revoke an API key for the authenticated user.

        No-op if already revoked.

        Source file:
        `api-server/src/controllers/api-keys/v1/revoke-api-key.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/api-keys/v1/{api_key_id}/revoke",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1RevokeResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.create = to_raw_response_wrapper(
            v1.create,
        )
        self.list = to_raw_response_wrapper(
            v1.list,
        )
        self.create_impersonation = to_raw_response_wrapper(
            v1.create_impersonation,
        )
        self.revoke = to_raw_response_wrapper(
            v1.revoke,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.create = async_to_raw_response_wrapper(
            v1.create,
        )
        self.list = async_to_raw_response_wrapper(
            v1.list,
        )
        self.create_impersonation = async_to_raw_response_wrapper(
            v1.create_impersonation,
        )
        self.revoke = async_to_raw_response_wrapper(
            v1.revoke,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.create = to_streamed_response_wrapper(
            v1.create,
        )
        self.list = to_streamed_response_wrapper(
            v1.list,
        )
        self.create_impersonation = to_streamed_response_wrapper(
            v1.create_impersonation,
        )
        self.revoke = to_streamed_response_wrapper(
            v1.revoke,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.create = async_to_streamed_response_wrapper(
            v1.create,
        )
        self.list = async_to_streamed_response_wrapper(
            v1.list,
        )
        self.create_impersonation = async_to_streamed_response_wrapper(
            v1.create_impersonation,
        )
        self.revoke = async_to_streamed_response_wrapper(
            v1.revoke,
        )
