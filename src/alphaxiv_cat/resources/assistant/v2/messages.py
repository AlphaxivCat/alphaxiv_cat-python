# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....types.assistant.v2 import message_set_feedback_params
from ....types.assistant.v2.message_list_response import MessageListResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def list(
        self,
        llm_chat: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        Get all messages for an llm chat

        Source file:
        `api-server/src/controllers/assistant/v2/get-chat-messages.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_chat:
            raise ValueError(f"Expected a non-empty value for `llm_chat` but received {llm_chat!r}")
        return self._get(
            f"/assistant/v2/{llm_chat}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageListResponse,
        )

    def select(
        self,
        message: str,
        *,
        llm_chat: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Select an llm chat message by id

        Source file:
        `api-server/src/controllers/assistant/v2/select-message.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_chat:
            raise ValueError(f"Expected a non-empty value for `llm_chat` but received {llm_chat!r}")
        if not message:
            raise ValueError(f"Expected a non-empty value for `message` but received {message!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/assistant/v2/{llm_chat}/messages/{message}/select",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set_feedback(
        self,
        message_id: str,
        *,
        feedback: Optional[message_set_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set or update feedback for a message

        Source file:
        `api-server/src/controllers/assistant/v2/set-message-feedback.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/assistant/v2/messages/{message_id}/feedback",
            body=maybe_transform({"feedback": feedback}, message_set_feedback_params.MessageSetFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def list(
        self,
        llm_chat: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        Get all messages for an llm chat

        Source file:
        `api-server/src/controllers/assistant/v2/get-chat-messages.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_chat:
            raise ValueError(f"Expected a non-empty value for `llm_chat` but received {llm_chat!r}")
        return await self._get(
            f"/assistant/v2/{llm_chat}/messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageListResponse,
        )

    async def select(
        self,
        message: str,
        *,
        llm_chat: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Select an llm chat message by id

        Source file:
        `api-server/src/controllers/assistant/v2/select-message.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_chat:
            raise ValueError(f"Expected a non-empty value for `llm_chat` but received {llm_chat!r}")
        if not message:
            raise ValueError(f"Expected a non-empty value for `message` but received {message!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/assistant/v2/{llm_chat}/messages/{message}/select",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set_feedback(
        self,
        message_id: str,
        *,
        feedback: Optional[message_set_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set or update feedback for a message

        Source file:
        `api-server/src/controllers/assistant/v2/set-message-feedback.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/assistant/v2/messages/{message_id}/feedback",
            body=await async_maybe_transform(
                {"feedback": feedback}, message_set_feedback_params.MessageSetFeedbackParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.select = to_raw_response_wrapper(
            messages.select,
        )
        self.set_feedback = to_raw_response_wrapper(
            messages.set_feedback,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.select = async_to_raw_response_wrapper(
            messages.select,
        )
        self.set_feedback = async_to_raw_response_wrapper(
            messages.set_feedback,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.select = to_streamed_response_wrapper(
            messages.select,
        )
        self.set_feedback = to_streamed_response_wrapper(
            messages.set_feedback,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.select = async_to_streamed_response_wrapper(
            messages.select,
        )
        self.set_feedback = async_to_streamed_response_wrapper(
            messages.set_feedback,
        )
