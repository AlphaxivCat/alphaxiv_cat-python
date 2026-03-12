# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.papers import (
    MetadataRetrieveLatestMetadataResponse,
    MetadataRetrieveVersionMetadataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_latest_metadata(self, client: AlphaxivCat) -> None:
        metadata = client.papers.metadata.retrieve_latest_metadata(
            upid="x",
        )
        assert_matches_type(MetadataRetrieveLatestMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_latest_metadata_with_all_params(self, client: AlphaxivCat) -> None:
        metadata = client.papers.metadata.retrieve_latest_metadata(
            upid="x",
            prevent_tracking="preventTracking",
        )
        assert_matches_type(MetadataRetrieveLatestMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_latest_metadata(self, client: AlphaxivCat) -> None:
        response = client.papers.metadata.with_raw_response.retrieve_latest_metadata(
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataRetrieveLatestMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_latest_metadata(self, client: AlphaxivCat) -> None:
        with client.papers.metadata.with_streaming_response.retrieve_latest_metadata(
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataRetrieveLatestMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_latest_metadata(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            client.papers.metadata.with_raw_response.retrieve_latest_metadata(
                upid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_version_metadata(self, client: AlphaxivCat) -> None:
        metadata = client.papers.metadata.retrieve_version_metadata(
            version_order="x",
            upid="x",
        )
        assert_matches_type(MetadataRetrieveVersionMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_version_metadata_with_all_params(self, client: AlphaxivCat) -> None:
        metadata = client.papers.metadata.retrieve_version_metadata(
            version_order="x",
            upid="x",
            prevent_tracking="preventTracking",
        )
        assert_matches_type(MetadataRetrieveVersionMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_version_metadata(self, client: AlphaxivCat) -> None:
        response = client.papers.metadata.with_raw_response.retrieve_version_metadata(
            version_order="x",
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataRetrieveVersionMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_version_metadata(self, client: AlphaxivCat) -> None:
        with client.papers.metadata.with_streaming_response.retrieve_version_metadata(
            version_order="x",
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataRetrieveVersionMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_version_metadata(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            client.papers.metadata.with_raw_response.retrieve_version_metadata(
                version_order="x",
                upid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_order` but received ''"):
            client.papers.metadata.with_raw_response.retrieve_version_metadata(
                version_order="",
                upid="x",
            )


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_latest_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        metadata = await async_client.papers.metadata.retrieve_latest_metadata(
            upid="x",
        )
        assert_matches_type(MetadataRetrieveLatestMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_latest_metadata_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        metadata = await async_client.papers.metadata.retrieve_latest_metadata(
            upid="x",
            prevent_tracking="preventTracking",
        )
        assert_matches_type(MetadataRetrieveLatestMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_latest_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.metadata.with_raw_response.retrieve_latest_metadata(
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataRetrieveLatestMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_latest_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.metadata.with_streaming_response.retrieve_latest_metadata(
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataRetrieveLatestMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_latest_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            await async_client.papers.metadata.with_raw_response.retrieve_latest_metadata(
                upid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_version_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        metadata = await async_client.papers.metadata.retrieve_version_metadata(
            version_order="x",
            upid="x",
        )
        assert_matches_type(MetadataRetrieveVersionMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_version_metadata_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        metadata = await async_client.papers.metadata.retrieve_version_metadata(
            version_order="x",
            upid="x",
            prevent_tracking="preventTracking",
        )
        assert_matches_type(MetadataRetrieveVersionMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_version_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.metadata.with_raw_response.retrieve_version_metadata(
            version_order="x",
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataRetrieveVersionMetadataResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_version_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.metadata.with_streaming_response.retrieve_version_metadata(
            version_order="x",
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataRetrieveVersionMetadataResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_version_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            await async_client.papers.metadata.with_raw_response.retrieve_version_metadata(
                version_order="x",
                upid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_order` but received ''"):
            await async_client.papers.metadata.with_raw_response.retrieve_version_metadata(
                version_order="",
                upid="x",
            )
