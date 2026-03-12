# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.papers import (
    VersionRequestAIOverviewResponse,
    VersionRequestAITranslationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_ai_overview(self, client: AlphaxivCat) -> None:
        version = client.papers.versions.request_ai_overview(
            version_order="x",
            upid="x",
        )
        assert_matches_type(VersionRequestAIOverviewResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_ai_overview_with_all_params(self, client: AlphaxivCat) -> None:
        version = client.papers.versions.request_ai_overview(
            version_order="x",
            upid="x",
            preferred_language="am",
        )
        assert_matches_type(VersionRequestAIOverviewResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_ai_overview(self, client: AlphaxivCat) -> None:
        response = client.papers.versions.with_raw_response.request_ai_overview(
            version_order="x",
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionRequestAIOverviewResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_ai_overview(self, client: AlphaxivCat) -> None:
        with client.papers.versions.with_streaming_response.request_ai_overview(
            version_order="x",
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionRequestAIOverviewResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request_ai_overview(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            client.papers.versions.with_raw_response.request_ai_overview(
                version_order="x",
                upid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_order` but received ''"):
            client.papers.versions.with_raw_response.request_ai_overview(
                version_order="",
                upid="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_ai_translation(self, client: AlphaxivCat) -> None:
        version = client.papers.versions.request_ai_translation(
            language="am",
            upid="x",
            version_order="x",
        )
        assert_matches_type(VersionRequestAITranslationResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_ai_translation(self, client: AlphaxivCat) -> None:
        response = client.papers.versions.with_raw_response.request_ai_translation(
            language="am",
            upid="x",
            version_order="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionRequestAITranslationResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_ai_translation(self, client: AlphaxivCat) -> None:
        with client.papers.versions.with_streaming_response.request_ai_translation(
            language="am",
            upid="x",
            version_order="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionRequestAITranslationResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request_ai_translation(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            client.papers.versions.with_raw_response.request_ai_translation(
                language="am",
                upid="",
                version_order="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_order` but received ''"):
            client.papers.versions.with_raw_response.request_ai_translation(
                language="am",
                upid="x",
                version_order="",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_ai_overview(self, async_client: AsyncAlphaxivCat) -> None:
        version = await async_client.papers.versions.request_ai_overview(
            version_order="x",
            upid="x",
        )
        assert_matches_type(VersionRequestAIOverviewResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_ai_overview_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        version = await async_client.papers.versions.request_ai_overview(
            version_order="x",
            upid="x",
            preferred_language="am",
        )
        assert_matches_type(VersionRequestAIOverviewResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_ai_overview(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.versions.with_raw_response.request_ai_overview(
            version_order="x",
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionRequestAIOverviewResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_ai_overview(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.versions.with_streaming_response.request_ai_overview(
            version_order="x",
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionRequestAIOverviewResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request_ai_overview(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            await async_client.papers.versions.with_raw_response.request_ai_overview(
                version_order="x",
                upid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_order` but received ''"):
            await async_client.papers.versions.with_raw_response.request_ai_overview(
                version_order="",
                upid="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_ai_translation(self, async_client: AsyncAlphaxivCat) -> None:
        version = await async_client.papers.versions.request_ai_translation(
            language="am",
            upid="x",
            version_order="x",
        )
        assert_matches_type(VersionRequestAITranslationResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_ai_translation(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.versions.with_raw_response.request_ai_translation(
            language="am",
            upid="x",
            version_order="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionRequestAITranslationResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_ai_translation(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.versions.with_streaming_response.request_ai_translation(
            language="am",
            upid="x",
            version_order="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionRequestAITranslationResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request_ai_translation(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            await async_client.papers.versions.with_raw_response.request_ai_translation(
                language="am",
                upid="",
                version_order="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_order` but received ''"):
            await async_client.papers.versions.with_raw_response.request_ai_translation(
                language="am",
                upid="x",
                version_order="",
            )
