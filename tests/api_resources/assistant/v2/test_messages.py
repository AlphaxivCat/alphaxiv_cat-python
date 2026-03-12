# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.assistant.v2 import MessageListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: AlphaxivCat) -> None:
        message = client.assistant.v2.messages.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: AlphaxivCat) -> None:
        response = client.assistant.v2.messages.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: AlphaxivCat) -> None:
        with client.assistant.v2.messages.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_chat` but received ''"):
            client.assistant.v2.messages.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_select(self, client: AlphaxivCat) -> None:
        message = client.assistant.v2.messages.select(
            message="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_select(self, client: AlphaxivCat) -> None:
        response = client.assistant.v2.messages.with_raw_response.select(
            message="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_select(self, client: AlphaxivCat) -> None:
        with client.assistant.v2.messages.with_streaming_response.select(
            message="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_select(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_chat` but received ''"):
            client.assistant.v2.messages.with_raw_response.select(
                message="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                llm_chat="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message` but received ''"):
            client.assistant.v2.messages.with_raw_response.select(
                message="",
                llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_feedback(self, client: AlphaxivCat) -> None:
        message = client.assistant.v2.messages.set_feedback(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback={"type": "upvote"},
        )
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_feedback_with_all_params(self, client: AlphaxivCat) -> None:
        message = client.assistant.v2.messages.set_feedback(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback={
                "type": "upvote",
                "category": "category",
                "details": "details",
            },
        )
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_feedback(self, client: AlphaxivCat) -> None:
        response = client.assistant.v2.messages.with_raw_response.set_feedback(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback={"type": "upvote"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_feedback(self, client: AlphaxivCat) -> None:
        with client.assistant.v2.messages.with_streaming_response.set_feedback(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback={"type": "upvote"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_feedback(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.assistant.v2.messages.with_raw_response.set_feedback(
                message_id="",
                feedback={"type": "upvote"},
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAlphaxivCat) -> None:
        message = await async_client.assistant.v2.messages.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.assistant.v2.messages.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.assistant.v2.messages.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_chat` but received ''"):
            await async_client.assistant.v2.messages.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_select(self, async_client: AsyncAlphaxivCat) -> None:
        message = await async_client.assistant.v2.messages.select(
            message="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_select(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.assistant.v2.messages.with_raw_response.select(
            message="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_select(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.assistant.v2.messages.with_streaming_response.select(
            message="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_select(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_chat` but received ''"):
            await async_client.assistant.v2.messages.with_raw_response.select(
                message="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                llm_chat="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message` but received ''"):
            await async_client.assistant.v2.messages.with_raw_response.select(
                message="",
                llm_chat="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_feedback(self, async_client: AsyncAlphaxivCat) -> None:
        message = await async_client.assistant.v2.messages.set_feedback(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback={"type": "upvote"},
        )
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_feedback_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        message = await async_client.assistant.v2.messages.set_feedback(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback={
                "type": "upvote",
                "category": "category",
                "details": "details",
            },
        )
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_feedback(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.assistant.v2.messages.with_raw_response.set_feedback(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback={"type": "upvote"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_feedback(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.assistant.v2.messages.with_streaming_response.set_feedback(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback={"type": "upvote"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_feedback(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.assistant.v2.messages.with_raw_response.set_feedback(
                message_id="",
                feedback={"type": "upvote"},
            )
