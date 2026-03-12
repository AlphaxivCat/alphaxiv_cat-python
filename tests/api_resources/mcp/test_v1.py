# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_establish_connection(self, client: AlphaxivCat) -> None:
        v1_stream = client.mcp.v1.establish_connection()
        v1_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_establish_connection(self, client: AlphaxivCat) -> None:
        response = client.mcp.v1.with_raw_response.establish_connection()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_establish_connection(self, client: AlphaxivCat) -> None:
        with client.mcp.v1.with_streaming_response.establish_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_message(self, client: AlphaxivCat) -> None:
        v1 = client.mcp.v1.send_message()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_message_with_all_params(self, client: AlphaxivCat) -> None:
        v1 = client.mcp.v1.send_message(
            body={},
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_message(self, client: AlphaxivCat) -> None:
        response = client.mcp.v1.with_raw_response.send_message()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_message(self, client: AlphaxivCat) -> None:
        with client.mcp.v1.with_streaming_response.send_message() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_terminate_session(self, client: AlphaxivCat) -> None:
        v1 = client.mcp.v1.terminate_session()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_terminate_session(self, client: AlphaxivCat) -> None:
        response = client.mcp.v1.with_raw_response.terminate_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_terminate_session(self, client: AlphaxivCat) -> None:
        with client.mcp.v1.with_streaming_response.terminate_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_establish_connection(self, async_client: AsyncAlphaxivCat) -> None:
        v1_stream = await async_client.mcp.v1.establish_connection()
        await v1_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_establish_connection(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.mcp.v1.with_raw_response.establish_connection()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_establish_connection(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.mcp.v1.with_streaming_response.establish_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_message(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.mcp.v1.send_message()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_message_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.mcp.v1.send_message(
            body={},
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.mcp.v1.with_raw_response.send_message()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.mcp.v1.with_streaming_response.send_message() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_terminate_session(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.mcp.v1.terminate_session()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_terminate_session(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.mcp.v1.with_raw_response.terminate_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_terminate_session(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.mcp.v1.with_streaming_response.terminate_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True
