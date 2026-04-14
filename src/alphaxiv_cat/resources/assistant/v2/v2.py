# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._streaming import Stream, AsyncStream
from ...._base_client import make_request_options
from ....types.assistant import v2_chat_params, v2_edit_chat_params, v2_get_chats_params, v2_get_url_metadata_params
from ....types.assistant.v2_get_chats_response import V2GetChatsResponse
from ....types.assistant.v2_get_url_metadata_response import V2GetURLMetadataResponse

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)

    def chat(
        self,
        *,
        files: Iterable[v2_chat_params.File],
        llm_chat_id: Optional[str],
        message: str,
        paper_version_id: Optional[str],
        parent_message_id: Optional[str],
        selection_page_range: Optional[Iterable[int]],
        thinking: Union[bool, str, None],
        web_search: Literal["off", "full"],
        assistant_variant: Literal["homepage", "paper", "folder", "landing", "folder-add-papers"] | Omit = omit,
        folder_add_papers: bool | Omit = omit,
        folder_id: str | Omit = omit,
        model: Literal[
            "claude-opus-4.5",
            "claude-opus-4.6",
            "claude-sonnet-4.5",
            "claude-sonnet-4.6",
            "gemini-2.5-flash",
            "gemini-2.5-pro",
            "gemini-3-flash",
            "gemini-3-pro",
            "gemini-3.1-pro",
            "glm-5-turbo",
            "glm-5.1",
            "gpt-5",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "kimi-k2.5",
            "mercury-2",
            "minimax-m2.5",
            "minimax-m2.7",
            "qwen-3.5",
            "aurelle-1",
            "fast",
            "smart",
            "pro",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
        ]
        | Omit = omit,
        plan: Literal["free", "pro"] | Omit = omit,
        signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[object]:
        """
        Send a message to the AI assistant and receive streaming responses

        Source file: `api-server/src/controllers/assistant/v2/chat.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/assistant/v2/chat",
            body=maybe_transform(
                {
                    "files": files,
                    "llm_chat_id": llm_chat_id,
                    "message": message,
                    "paper_version_id": paper_version_id,
                    "parent_message_id": parent_message_id,
                    "selection_page_range": selection_page_range,
                    "thinking": thinking,
                    "web_search": web_search,
                    "assistant_variant": assistant_variant,
                    "folder_add_papers": folder_add_papers,
                    "folder_id": folder_id,
                    "model": model,
                    "plan": plan,
                    "signature": signature,
                },
                v2_chat_params.V2ChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
            stream=True,
            stream_cls=Stream[object],
        )

    def delete_chat(
        self,
        llm_chat: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an llm chat by id

        Source file: `api-server/src/controllers/assistant/v2/delete-chat.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_chat:
            raise ValueError(f"Expected a non-empty value for `llm_chat` but received {llm_chat!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/assistant/v2/{llm_chat}", llm_chat=llm_chat),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def edit_chat(
        self,
        llm_chat: str,
        *,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Updates properties on an LlmChat.

        Currently only supports title

        Source file: `api-server/src/controllers/assistant/v2/edit-chat.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_chat:
            raise ValueError(f"Expected a non-empty value for `llm_chat` but received {llm_chat!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/assistant/v2/{llm_chat}", llm_chat=llm_chat),
            body=maybe_transform({"title": title}, v2_edit_chat_params.V2EditChatParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_chats(
        self,
        *,
        folder: str | Omit = omit,
        paper_version: str | Omit = omit,
        variant: Literal["homepage", "paper", "folder"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2GetChatsResponse:
        """
        Get llm chats for this user, filtered by variant, and optionally by paper
        version

        Source file: `api-server/src/controllers/assistant/v2/get-chats.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/assistant/v2",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "folder": folder,
                        "paper_version": paper_version,
                        "variant": variant,
                    },
                    v2_get_chats_params.V2GetChatsParams,
                ),
            ),
            cast_to=V2GetChatsResponse,
        )

    def get_url_metadata(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2GetURLMetadataResponse:
        """
        Fetch metadata (title and favicon) from a given URL

        Source file:
        `api-server/src/controllers/assistant/v2/get-url-metadata.controller.ts`

        Args:
          url: The URL to fetch metadata from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/assistant/v2/url-metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, v2_get_url_metadata_params.V2GetURLMetadataParams),
            ),
            cast_to=V2GetURLMetadataResponse,
        )


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)

    async def chat(
        self,
        *,
        files: Iterable[v2_chat_params.File],
        llm_chat_id: Optional[str],
        message: str,
        paper_version_id: Optional[str],
        parent_message_id: Optional[str],
        selection_page_range: Optional[Iterable[int]],
        thinking: Union[bool, str, None],
        web_search: Literal["off", "full"],
        assistant_variant: Literal["homepage", "paper", "folder", "landing", "folder-add-papers"] | Omit = omit,
        folder_add_papers: bool | Omit = omit,
        folder_id: str | Omit = omit,
        model: Literal[
            "claude-opus-4.5",
            "claude-opus-4.6",
            "claude-sonnet-4.5",
            "claude-sonnet-4.6",
            "gemini-2.5-flash",
            "gemini-2.5-pro",
            "gemini-3-flash",
            "gemini-3-pro",
            "gemini-3.1-pro",
            "glm-5-turbo",
            "glm-5.1",
            "gpt-5",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5.4",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            "kimi-k2.5",
            "mercury-2",
            "minimax-m2.5",
            "minimax-m2.7",
            "qwen-3.5",
            "aurelle-1",
            "fast",
            "smart",
            "pro",
            "claude-4.5-sonnet",
            "claude-4.6-sonnet",
        ]
        | Omit = omit,
        plan: Literal["free", "pro"] | Omit = omit,
        signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[object]:
        """
        Send a message to the AI assistant and receive streaming responses

        Source file: `api-server/src/controllers/assistant/v2/chat.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/assistant/v2/chat",
            body=await async_maybe_transform(
                {
                    "files": files,
                    "llm_chat_id": llm_chat_id,
                    "message": message,
                    "paper_version_id": paper_version_id,
                    "parent_message_id": parent_message_id,
                    "selection_page_range": selection_page_range,
                    "thinking": thinking,
                    "web_search": web_search,
                    "assistant_variant": assistant_variant,
                    "folder_add_papers": folder_add_papers,
                    "folder_id": folder_id,
                    "model": model,
                    "plan": plan,
                    "signature": signature,
                },
                v2_chat_params.V2ChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
            stream=True,
            stream_cls=AsyncStream[object],
        )

    async def delete_chat(
        self,
        llm_chat: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an llm chat by id

        Source file: `api-server/src/controllers/assistant/v2/delete-chat.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_chat:
            raise ValueError(f"Expected a non-empty value for `llm_chat` but received {llm_chat!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/assistant/v2/{llm_chat}", llm_chat=llm_chat),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def edit_chat(
        self,
        llm_chat: str,
        *,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Updates properties on an LlmChat.

        Currently only supports title

        Source file: `api-server/src/controllers/assistant/v2/edit-chat.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_chat:
            raise ValueError(f"Expected a non-empty value for `llm_chat` but received {llm_chat!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/assistant/v2/{llm_chat}", llm_chat=llm_chat),
            body=await async_maybe_transform({"title": title}, v2_edit_chat_params.V2EditChatParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_chats(
        self,
        *,
        folder: str | Omit = omit,
        paper_version: str | Omit = omit,
        variant: Literal["homepage", "paper", "folder"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2GetChatsResponse:
        """
        Get llm chats for this user, filtered by variant, and optionally by paper
        version

        Source file: `api-server/src/controllers/assistant/v2/get-chats.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/assistant/v2",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "folder": folder,
                        "paper_version": paper_version,
                        "variant": variant,
                    },
                    v2_get_chats_params.V2GetChatsParams,
                ),
            ),
            cast_to=V2GetChatsResponse,
        )

    async def get_url_metadata(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2GetURLMetadataResponse:
        """
        Fetch metadata (title and favicon) from a given URL

        Source file:
        `api-server/src/controllers/assistant/v2/get-url-metadata.controller.ts`

        Args:
          url: The URL to fetch metadata from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/assistant/v2/url-metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url": url}, v2_get_url_metadata_params.V2GetURLMetadataParams),
            ),
            cast_to=V2GetURLMetadataResponse,
        )


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.chat = to_raw_response_wrapper(
            v2.chat,
        )
        self.delete_chat = to_raw_response_wrapper(
            v2.delete_chat,
        )
        self.edit_chat = to_raw_response_wrapper(
            v2.edit_chat,
        )
        self.get_chats = to_raw_response_wrapper(
            v2.get_chats,
        )
        self.get_url_metadata = to_raw_response_wrapper(
            v2.get_url_metadata,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._v2.messages)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.chat = async_to_raw_response_wrapper(
            v2.chat,
        )
        self.delete_chat = async_to_raw_response_wrapper(
            v2.delete_chat,
        )
        self.edit_chat = async_to_raw_response_wrapper(
            v2.edit_chat,
        )
        self.get_chats = async_to_raw_response_wrapper(
            v2.get_chats,
        )
        self.get_url_metadata = async_to_raw_response_wrapper(
            v2.get_url_metadata,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._v2.messages)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.chat = to_streamed_response_wrapper(
            v2.chat,
        )
        self.delete_chat = to_streamed_response_wrapper(
            v2.delete_chat,
        )
        self.edit_chat = to_streamed_response_wrapper(
            v2.edit_chat,
        )
        self.get_chats = to_streamed_response_wrapper(
            v2.get_chats,
        )
        self.get_url_metadata = to_streamed_response_wrapper(
            v2.get_url_metadata,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._v2.messages)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.chat = async_to_streamed_response_wrapper(
            v2.chat,
        )
        self.delete_chat = async_to_streamed_response_wrapper(
            v2.delete_chat,
        )
        self.edit_chat = async_to_streamed_response_wrapper(
            v2.edit_chat,
        )
        self.get_chats = async_to_streamed_response_wrapper(
            v2.get_chats,
        )
        self.get_url_metadata = async_to_streamed_response_wrapper(
            v2.get_url_metadata,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._v2.messages)
