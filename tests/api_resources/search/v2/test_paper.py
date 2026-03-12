# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.search.v2 import PaperFastSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaper:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fast_search(self, client: AlphaxivCat) -> None:
        paper = client.search.v2.paper.fast_search(
            include_private="true",
            q="x",
        )
        assert_matches_type(PaperFastSearchResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fast_search(self, client: AlphaxivCat) -> None:
        response = client.search.v2.paper.with_raw_response.fast_search(
            include_private="true",
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperFastSearchResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fast_search(self, client: AlphaxivCat) -> None:
        with client.search.v2.paper.with_streaming_response.fast_search(
            include_private="true",
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperFastSearchResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaper:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fast_search(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.search.v2.paper.fast_search(
            include_private="true",
            q="x",
        )
        assert_matches_type(PaperFastSearchResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fast_search(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.search.v2.paper.with_raw_response.fast_search(
            include_private="true",
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperFastSearchResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fast_search(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.search.v2.paper.with_streaming_response.fast_search(
            include_private="true",
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperFastSearchResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True
