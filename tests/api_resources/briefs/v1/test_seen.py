# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.briefs.v1 import SeenGetSeenResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeen:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_seen(self, client: AlphaxivCat) -> None:
        seen = client.briefs.v1.seen.get_seen()
        assert_matches_type(SeenGetSeenResponse, seen, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_seen(self, client: AlphaxivCat) -> None:
        response = client.briefs.v1.seen.with_raw_response.get_seen()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seen = response.parse()
        assert_matches_type(SeenGetSeenResponse, seen, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_seen(self, client: AlphaxivCat) -> None:
        with client.briefs.v1.seen.with_streaming_response.get_seen() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seen = response.parse()
            assert_matches_type(SeenGetSeenResponse, seen, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mark_seen(self, client: AlphaxivCat) -> None:
        seen = client.briefs.v1.seen.mark_seen(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert seen is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mark_seen(self, client: AlphaxivCat) -> None:
        response = client.briefs.v1.seen.with_raw_response.mark_seen(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seen = response.parse()
        assert seen is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mark_seen(self, client: AlphaxivCat) -> None:
        with client.briefs.v1.seen.with_streaming_response.mark_seen(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seen = response.parse()
            assert seen is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSeen:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_seen(self, async_client: AsyncAlphaxivCat) -> None:
        seen = await async_client.briefs.v1.seen.get_seen()
        assert_matches_type(SeenGetSeenResponse, seen, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_seen(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.briefs.v1.seen.with_raw_response.get_seen()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seen = await response.parse()
        assert_matches_type(SeenGetSeenResponse, seen, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_seen(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.briefs.v1.seen.with_streaming_response.get_seen() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seen = await response.parse()
            assert_matches_type(SeenGetSeenResponse, seen, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mark_seen(self, async_client: AsyncAlphaxivCat) -> None:
        seen = await async_client.briefs.v1.seen.mark_seen(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert seen is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mark_seen(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.briefs.v1.seen.with_raw_response.mark_seen(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seen = await response.parse()
        assert seen is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mark_seen(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.briefs.v1.seen.with_streaming_response.mark_seen(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seen = await response.parse()
            assert seen is None

        assert cast(Any, response.is_closed) is True
