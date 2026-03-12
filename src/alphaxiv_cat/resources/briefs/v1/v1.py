# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .seen import (
    SeenResource,
    AsyncSeenResource,
    SeenResourceWithRawResponse,
    AsyncSeenResourceWithRawResponse,
    SeenResourceWithStreamingResponse,
    AsyncSeenResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.briefs import v1_generate_speech_params
from ....types.briefs.v1_generate_speech_response import V1GenerateSpeechResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def seen(self) -> SeenResource:
        return SeenResource(self._client)

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

    def generate_speech(
        self,
        *,
        paper_group_id: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GenerateSpeechResponse:
        """Generates speech audio from brief summary text using ElevenLabs.

        Returns the
        CloudFront URL. Client should try the CDN URL first and only call this if it
        404s.

        Source file:
        `api-server/src/controllers/briefs/v1/generate-speech.controller.ts`

        Args:
          paper_group_id: Paper group ID for caching

          text: Text to convert to speech

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/briefs/v1/speech",
            body=maybe_transform(
                {
                    "paper_group_id": paper_group_id,
                    "text": text,
                },
                v1_generate_speech_params.V1GenerateSpeechParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GenerateSpeechResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def seen(self) -> AsyncSeenResource:
        return AsyncSeenResource(self._client)

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

    async def generate_speech(
        self,
        *,
        paper_group_id: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GenerateSpeechResponse:
        """Generates speech audio from brief summary text using ElevenLabs.

        Returns the
        CloudFront URL. Client should try the CDN URL first and only call this if it
        404s.

        Source file:
        `api-server/src/controllers/briefs/v1/generate-speech.controller.ts`

        Args:
          paper_group_id: Paper group ID for caching

          text: Text to convert to speech

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/briefs/v1/speech",
            body=await async_maybe_transform(
                {
                    "paper_group_id": paper_group_id,
                    "text": text,
                },
                v1_generate_speech_params.V1GenerateSpeechParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GenerateSpeechResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.generate_speech = to_raw_response_wrapper(
            v1.generate_speech,
        )

    @cached_property
    def seen(self) -> SeenResourceWithRawResponse:
        return SeenResourceWithRawResponse(self._v1.seen)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.generate_speech = async_to_raw_response_wrapper(
            v1.generate_speech,
        )

    @cached_property
    def seen(self) -> AsyncSeenResourceWithRawResponse:
        return AsyncSeenResourceWithRawResponse(self._v1.seen)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.generate_speech = to_streamed_response_wrapper(
            v1.generate_speech,
        )

    @cached_property
    def seen(self) -> SeenResourceWithStreamingResponse:
        return SeenResourceWithStreamingResponse(self._v1.seen)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.generate_speech = async_to_streamed_response_wrapper(
            v1.generate_speech,
        )

    @cached_property
    def seen(self) -> AsyncSeenResourceWithStreamingResponse:
        return AsyncSeenResourceWithStreamingResponse(self._v1.seen)
