# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.papers.v3 import LegacyRetrieveResponse, LegacyRetrieveCommentsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLegacy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: AlphaxivCat) -> None:
        legacy = client.papers.v3.legacy.retrieve(
            "unresolved",
        )
        assert_matches_type(LegacyRetrieveResponse, legacy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.legacy.with_raw_response.retrieve(
            "unresolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legacy = response.parse()
        assert_matches_type(LegacyRetrieveResponse, legacy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: AlphaxivCat) -> None:
        with client.papers.v3.legacy.with_streaming_response.retrieve(
            "unresolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legacy = response.parse()
            assert_matches_type(LegacyRetrieveResponse, legacy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unresolved` but received ''"):
            client.papers.v3.legacy.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_comments(self, client: AlphaxivCat) -> None:
        legacy = client.papers.v3.legacy.retrieve_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LegacyRetrieveCommentsResponse, legacy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_comments(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.legacy.with_raw_response.retrieve_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legacy = response.parse()
        assert_matches_type(LegacyRetrieveCommentsResponse, legacy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_comments(self, client: AlphaxivCat) -> None:
        with client.papers.v3.legacy.with_streaming_response.retrieve_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legacy = response.parse()
            assert_matches_type(LegacyRetrieveCommentsResponse, legacy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_comments(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group` but received ''"):
            client.papers.v3.legacy.with_raw_response.retrieve_comments(
                "",
            )


class TestAsyncLegacy:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        legacy = await async_client.papers.v3.legacy.retrieve(
            "unresolved",
        )
        assert_matches_type(LegacyRetrieveResponse, legacy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.legacy.with_raw_response.retrieve(
            "unresolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legacy = await response.parse()
        assert_matches_type(LegacyRetrieveResponse, legacy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.legacy.with_streaming_response.retrieve(
            "unresolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legacy = await response.parse()
            assert_matches_type(LegacyRetrieveResponse, legacy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unresolved` but received ''"):
            await async_client.papers.v3.legacy.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_comments(self, async_client: AsyncAlphaxivCat) -> None:
        legacy = await async_client.papers.v3.legacy.retrieve_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LegacyRetrieveCommentsResponse, legacy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_comments(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.legacy.with_raw_response.retrieve_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legacy = await response.parse()
        assert_matches_type(LegacyRetrieveCommentsResponse, legacy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_comments(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.legacy.with_streaming_response.retrieve_comments(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legacy = await response.parse()
            assert_matches_type(LegacyRetrieveCommentsResponse, legacy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_comments(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group` but received ''"):
            await async_client.papers.v3.legacy.with_raw_response.retrieve_comments(
                "",
            )
