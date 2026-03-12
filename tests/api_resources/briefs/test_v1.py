# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.briefs import V1GenerateSpeechResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_speech(self, client: AlphaxivCat) -> None:
        v1 = client.briefs.v1.generate_speech(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )
        assert_matches_type(V1GenerateSpeechResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_speech(self, client: AlphaxivCat) -> None:
        response = client.briefs.v1.with_raw_response.generate_speech(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GenerateSpeechResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_speech(self, client: AlphaxivCat) -> None:
        with client.briefs.v1.with_streaming_response.generate_speech(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GenerateSpeechResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_speech(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.briefs.v1.generate_speech(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )
        assert_matches_type(V1GenerateSpeechResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_speech(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.briefs.v1.with_raw_response.generate_speech(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GenerateSpeechResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_speech(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.briefs.v1.with_streaming_response.generate_speech(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GenerateSpeechResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
