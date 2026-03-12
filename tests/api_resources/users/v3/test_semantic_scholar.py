# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.users.v3 import SemanticScholarLinkResponse, SemanticScholarScrapeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSemanticScholar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_link(self, client: AlphaxivCat) -> None:
        semantic_scholar = client.users.v3.semantic_scholar.link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SemanticScholarLinkResponse, semantic_scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_link(self, client: AlphaxivCat) -> None:
        response = client.users.v3.semantic_scholar.with_raw_response.link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        semantic_scholar = response.parse()
        assert_matches_type(SemanticScholarLinkResponse, semantic_scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_link(self, client: AlphaxivCat) -> None:
        with client.users.v3.semantic_scholar.with_streaming_response.link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            semantic_scholar = response.parse()
            assert_matches_type(SemanticScholarLinkResponse, semantic_scholar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_link(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.v3.semantic_scholar.with_raw_response.link(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_scrape(self, client: AlphaxivCat) -> None:
        semantic_scholar = client.users.v3.semantic_scholar.scrape(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SemanticScholarScrapeResponse, semantic_scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_scrape(self, client: AlphaxivCat) -> None:
        response = client.users.v3.semantic_scholar.with_raw_response.scrape(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        semantic_scholar = response.parse()
        assert_matches_type(SemanticScholarScrapeResponse, semantic_scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_scrape(self, client: AlphaxivCat) -> None:
        with client.users.v3.semantic_scholar.with_streaming_response.scrape(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            semantic_scholar = response.parse()
            assert_matches_type(SemanticScholarScrapeResponse, semantic_scholar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_scrape(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.v3.semantic_scholar.with_raw_response.scrape(
                "",
            )


class TestAsyncSemanticScholar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_link(self, async_client: AsyncAlphaxivCat) -> None:
        semantic_scholar = await async_client.users.v3.semantic_scholar.link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SemanticScholarLinkResponse, semantic_scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_link(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.semantic_scholar.with_raw_response.link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        semantic_scholar = await response.parse()
        assert_matches_type(SemanticScholarLinkResponse, semantic_scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_link(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.semantic_scholar.with_streaming_response.link(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            semantic_scholar = await response.parse()
            assert_matches_type(SemanticScholarLinkResponse, semantic_scholar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_link(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.v3.semantic_scholar.with_raw_response.link(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_scrape(self, async_client: AsyncAlphaxivCat) -> None:
        semantic_scholar = await async_client.users.v3.semantic_scholar.scrape(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SemanticScholarScrapeResponse, semantic_scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_scrape(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.semantic_scholar.with_raw_response.scrape(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        semantic_scholar = await response.parse()
        assert_matches_type(SemanticScholarScrapeResponse, semantic_scholar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_scrape(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.semantic_scholar.with_streaming_response.scrape(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            semantic_scholar = await response.parse()
            assert_matches_type(SemanticScholarScrapeResponse, semantic_scholar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_scrape(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.v3.semantic_scholar.with_raw_response.scrape(
                "",
            )
