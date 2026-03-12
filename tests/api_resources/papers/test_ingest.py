# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.papers import (
    IngestIngestLatestResponse,
    IngestIngestVersionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIngest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_latest(self, client: AlphaxivCat) -> None:
        ingest = client.papers.ingest.ingest_latest(
            upid="x",
        )
        assert_matches_type(IngestIngestLatestResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_latest_with_all_params(self, client: AlphaxivCat) -> None:
        ingest = client.papers.ingest.ingest_latest(
            upid="x",
            prevent_tracking="preventTracking",
        )
        assert_matches_type(IngestIngestLatestResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest_latest(self, client: AlphaxivCat) -> None:
        response = client.papers.ingest.with_raw_response.ingest_latest(
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest = response.parse()
        assert_matches_type(IngestIngestLatestResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest_latest(self, client: AlphaxivCat) -> None:
        with client.papers.ingest.with_streaming_response.ingest_latest(
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest = response.parse()
            assert_matches_type(IngestIngestLatestResponse, ingest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_ingest_latest(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            client.papers.ingest.with_raw_response.ingest_latest(
                upid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_version(self, client: AlphaxivCat) -> None:
        ingest = client.papers.ingest.ingest_version(
            version_label="x",
            upid="x",
        )
        assert_matches_type(IngestIngestVersionResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_version_with_all_params(self, client: AlphaxivCat) -> None:
        ingest = client.papers.ingest.ingest_version(
            version_label="x",
            upid="x",
            prevent_tracking="preventTracking",
        )
        assert_matches_type(IngestIngestVersionResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest_version(self, client: AlphaxivCat) -> None:
        response = client.papers.ingest.with_raw_response.ingest_version(
            version_label="x",
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest = response.parse()
        assert_matches_type(IngestIngestVersionResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest_version(self, client: AlphaxivCat) -> None:
        with client.papers.ingest.with_streaming_response.ingest_version(
            version_label="x",
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest = response.parse()
            assert_matches_type(IngestIngestVersionResponse, ingest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_ingest_version(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            client.papers.ingest.with_raw_response.ingest_version(
                version_label="x",
                upid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_label` but received ''"):
            client.papers.ingest.with_raw_response.ingest_version(
                version_label="",
                upid="x",
            )


class TestAsyncIngest:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_latest(self, async_client: AsyncAlphaxivCat) -> None:
        ingest = await async_client.papers.ingest.ingest_latest(
            upid="x",
        )
        assert_matches_type(IngestIngestLatestResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_latest_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        ingest = await async_client.papers.ingest.ingest_latest(
            upid="x",
            prevent_tracking="preventTracking",
        )
        assert_matches_type(IngestIngestLatestResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest_latest(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.ingest.with_raw_response.ingest_latest(
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest = await response.parse()
        assert_matches_type(IngestIngestLatestResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest_latest(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.ingest.with_streaming_response.ingest_latest(
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest = await response.parse()
            assert_matches_type(IngestIngestLatestResponse, ingest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_ingest_latest(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            await async_client.papers.ingest.with_raw_response.ingest_latest(
                upid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_version(self, async_client: AsyncAlphaxivCat) -> None:
        ingest = await async_client.papers.ingest.ingest_version(
            version_label="x",
            upid="x",
        )
        assert_matches_type(IngestIngestVersionResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_version_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        ingest = await async_client.papers.ingest.ingest_version(
            version_label="x",
            upid="x",
            prevent_tracking="preventTracking",
        )
        assert_matches_type(IngestIngestVersionResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest_version(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.ingest.with_raw_response.ingest_version(
            version_label="x",
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingest = await response.parse()
        assert_matches_type(IngestIngestVersionResponse, ingest, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest_version(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.ingest.with_streaming_response.ingest_version(
            version_label="x",
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingest = await response.parse()
            assert_matches_type(IngestIngestVersionResponse, ingest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_ingest_version(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            await async_client.papers.ingest.with_raw_response.ingest_version(
                version_label="x",
                upid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_label` but received ''"):
            await async_client.papers.ingest.with_raw_response.ingest_version(
                version_label="",
                upid="x",
            )
