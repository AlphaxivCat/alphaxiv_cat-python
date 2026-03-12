# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types import AssistantUploadFileResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssistant:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_file(self, client: AlphaxivCat) -> None:
        assistant = client.assistant.upload_file()
        assert_matches_type(AssistantUploadFileResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload_file(self, client: AlphaxivCat) -> None:
        response = client.assistant.with_raw_response.upload_file()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantUploadFileResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload_file(self, client: AlphaxivCat) -> None:
        with client.assistant.with_streaming_response.upload_file() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantUploadFileResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssistant:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_file(self, async_client: AsyncAlphaxivCat) -> None:
        assistant = await async_client.assistant.upload_file()
        assert_matches_type(AssistantUploadFileResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload_file(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.assistant.with_raw_response.upload_file()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantUploadFileResponse, assistant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload_file(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.assistant.with_streaming_response.upload_file() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantUploadFileResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True
