# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.assistant import (
    V2GetChatsResponse,
    V2GetURLMetadataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_chat(self, client: AlphaxivCat) -> None:
        v2_stream = client.assistant.v2.chat(
            files=[
                {
                    "content_type": "contentType",
                    "url": "https://example.com",
                }
            ],
            llm_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selection_page_range=[0, 0],
            thinking=True,
            web_search="off",
        )
        v2_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_chat_with_all_params(self, client: AlphaxivCat) -> None:
        v2_stream = client.assistant.v2.chat(
            files=[
                {
                    "content_type": "contentType",
                    "url": "https://example.com",
                }
            ],
            llm_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selection_page_range=[0, 0],
            thinking=True,
            web_search="off",
            assistant_variant="homepage",
            model="claude-opus-4.5",
            plan="free",
            signature="signature",
        )
        v2_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_chat(self, client: AlphaxivCat) -> None:
        response = client.assistant.v2.with_raw_response.chat(
            files=[
                {
                    "content_type": "contentType",
                    "url": "https://example.com",
                }
            ],
            llm_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selection_page_range=[0, 0],
            thinking=True,
            web_search="off",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_chat(self, client: AlphaxivCat) -> None:
        with client.assistant.v2.with_streaming_response.chat(
            files=[
                {
                    "content_type": "contentType",
                    "url": "https://example.com",
                }
            ],
            llm_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selection_page_range=[0, 0],
            thinking=True,
            web_search="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_chat(self, client: AlphaxivCat) -> None:
        v2 = client.assistant.v2.delete_chat(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_chat(self, client: AlphaxivCat) -> None:
        response = client.assistant.v2.with_raw_response.delete_chat(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_chat(self, client: AlphaxivCat) -> None:
        with client.assistant.v2.with_streaming_response.delete_chat(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_chat(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_chat` but received ''"):
            client.assistant.v2.with_raw_response.delete_chat(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_edit_chat(self, client: AlphaxivCat) -> None:
        v2 = client.assistant.v2.edit_chat(
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_edit_chat(self, client: AlphaxivCat) -> None:
        response = client.assistant.v2.with_raw_response.edit_chat(
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_edit_chat(self, client: AlphaxivCat) -> None:
        with client.assistant.v2.with_streaming_response.edit_chat(
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_edit_chat(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_chat` but received ''"):
            client.assistant.v2.with_raw_response.edit_chat(
                llm_chat="",
                title="title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_chats(self, client: AlphaxivCat) -> None:
        v2 = client.assistant.v2.get_chats()
        assert_matches_type(V2GetChatsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_chats_with_all_params(self, client: AlphaxivCat) -> None:
        v2 = client.assistant.v2.get_chats(
            paper_version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            variant="homepage",
        )
        assert_matches_type(V2GetChatsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_chats(self, client: AlphaxivCat) -> None:
        response = client.assistant.v2.with_raw_response.get_chats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2GetChatsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_chats(self, client: AlphaxivCat) -> None:
        with client.assistant.v2.with_streaming_response.get_chats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2GetChatsResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_url_metadata(self, client: AlphaxivCat) -> None:
        v2 = client.assistant.v2.get_url_metadata(
            url="https://example.com",
        )
        assert_matches_type(V2GetURLMetadataResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_url_metadata(self, client: AlphaxivCat) -> None:
        response = client.assistant.v2.with_raw_response.get_url_metadata(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2GetURLMetadataResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_url_metadata(self, client: AlphaxivCat) -> None:
        with client.assistant.v2.with_streaming_response.get_url_metadata(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2GetURLMetadataResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_chat(self, async_client: AsyncAlphaxivCat) -> None:
        v2_stream = await async_client.assistant.v2.chat(
            files=[
                {
                    "content_type": "contentType",
                    "url": "https://example.com",
                }
            ],
            llm_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selection_page_range=[0, 0],
            thinking=True,
            web_search="off",
        )
        await v2_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v2_stream = await async_client.assistant.v2.chat(
            files=[
                {
                    "content_type": "contentType",
                    "url": "https://example.com",
                }
            ],
            llm_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selection_page_range=[0, 0],
            thinking=True,
            web_search="off",
            assistant_variant="homepage",
            model="claude-opus-4.5",
            plan="free",
            signature="signature",
        )
        await v2_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.assistant.v2.with_raw_response.chat(
            files=[
                {
                    "content_type": "contentType",
                    "url": "https://example.com",
                }
            ],
            llm_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selection_page_range=[0, 0],
            thinking=True,
            web_search="off",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.assistant.v2.with_streaming_response.chat(
            files=[
                {
                    "content_type": "contentType",
                    "url": "https://example.com",
                }
            ],
            llm_chat_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selection_page_range=[0, 0],
            thinking=True,
            web_search="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_chat(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.assistant.v2.delete_chat(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_chat(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.assistant.v2.with_raw_response.delete_chat(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_chat(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.assistant.v2.with_streaming_response.delete_chat(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_chat(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_chat` but received ''"):
            await async_client.assistant.v2.with_raw_response.delete_chat(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_edit_chat(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.assistant.v2.edit_chat(
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_edit_chat(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.assistant.v2.with_raw_response.edit_chat(
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_edit_chat(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.assistant.v2.with_streaming_response.edit_chat(
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_edit_chat(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_chat` but received ''"):
            await async_client.assistant.v2.with_raw_response.edit_chat(
                llm_chat="",
                title="title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_chats(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.assistant.v2.get_chats()
        assert_matches_type(V2GetChatsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_chats_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.assistant.v2.get_chats(
            paper_version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            variant="homepage",
        )
        assert_matches_type(V2GetChatsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_chats(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.assistant.v2.with_raw_response.get_chats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2GetChatsResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_chats(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.assistant.v2.with_streaming_response.get_chats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2GetChatsResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_url_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.assistant.v2.get_url_metadata(
            url="https://example.com",
        )
        assert_matches_type(V2GetURLMetadataResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_url_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.assistant.v2.with_raw_response.get_url_metadata(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2GetURLMetadataResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_url_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.assistant.v2.with_streaming_response.get_url_metadata(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2GetURLMetadataResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True
