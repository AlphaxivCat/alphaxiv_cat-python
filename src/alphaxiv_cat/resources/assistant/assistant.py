# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .v2.v2 import (
    V2Resource,
    AsyncV2Resource,
    V2ResourceWithRawResponse,
    AsyncV2ResourceWithRawResponse,
    V2ResourceWithStreamingResponse,
    AsyncV2ResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.assistant_upload_file_response import AssistantUploadFileResponse

__all__ = ["AssistantResource", "AsyncAssistantResource"]


class AssistantResource(SyncAPIResource):
    @cached_property
    def v2(self) -> V2Resource:
        return V2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AssistantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AssistantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssistantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AssistantResourceWithStreamingResponse(self)

    def upload_file(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantUploadFileResponse:
        """
        Upload a file for use with the assistant (max 30MB)

        Source file: `api-server/src/controllers/v1/assistant/upload-file.controller.ts`
        """
        return self._post(
            "/v1/assistant/upload-file",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantUploadFileResponse,
        )


class AsyncAssistantResource(AsyncAPIResource):
    @cached_property
    def v2(self) -> AsyncV2Resource:
        return AsyncV2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssistantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssistantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssistantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncAssistantResourceWithStreamingResponse(self)

    async def upload_file(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantUploadFileResponse:
        """
        Upload a file for use with the assistant (max 30MB)

        Source file: `api-server/src/controllers/v1/assistant/upload-file.controller.ts`
        """
        return await self._post(
            "/v1/assistant/upload-file",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantUploadFileResponse,
        )


class AssistantResourceWithRawResponse:
    def __init__(self, assistant: AssistantResource) -> None:
        self._assistant = assistant

        self.upload_file = to_raw_response_wrapper(
            assistant.upload_file,
        )

    @cached_property
    def v2(self) -> V2ResourceWithRawResponse:
        return V2ResourceWithRawResponse(self._assistant.v2)


class AsyncAssistantResourceWithRawResponse:
    def __init__(self, assistant: AsyncAssistantResource) -> None:
        self._assistant = assistant

        self.upload_file = async_to_raw_response_wrapper(
            assistant.upload_file,
        )

    @cached_property
    def v2(self) -> AsyncV2ResourceWithRawResponse:
        return AsyncV2ResourceWithRawResponse(self._assistant.v2)


class AssistantResourceWithStreamingResponse:
    def __init__(self, assistant: AssistantResource) -> None:
        self._assistant = assistant

        self.upload_file = to_streamed_response_wrapper(
            assistant.upload_file,
        )

    @cached_property
    def v2(self) -> V2ResourceWithStreamingResponse:
        return V2ResourceWithStreamingResponse(self._assistant.v2)


class AsyncAssistantResourceWithStreamingResponse:
    def __init__(self, assistant: AsyncAssistantResource) -> None:
        self._assistant = assistant

        self.upload_file = async_to_streamed_response_wrapper(
            assistant.upload_file,
        )

    @cached_property
    def v2(self) -> AsyncV2ResourceWithStreamingResponse:
        return AsyncV2ResourceWithStreamingResponse(self._assistant.v2)
