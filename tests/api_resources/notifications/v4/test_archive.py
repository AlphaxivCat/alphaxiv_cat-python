# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.notifications.v4 import (
    ArchiveListResponse,
    ArchiveCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArchive:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: AlphaxivCat) -> None:
        archive = client.notifications.v4.archive.create(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(ArchiveCreateResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: AlphaxivCat) -> None:
        response = client.notifications.v4.archive.with_raw_response.create(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = response.parse()
        assert_matches_type(ArchiveCreateResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: AlphaxivCat) -> None:
        with client.notifications.v4.archive.with_streaming_response.create(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = response.parse()
            assert_matches_type(ArchiveCreateResponse, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: AlphaxivCat) -> None:
        archive = client.notifications.v4.archive.list()
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: AlphaxivCat) -> None:
        archive = client.notifications.v4.archive.list(
            before="before",
        )
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: AlphaxivCat) -> None:
        response = client.notifications.v4.archive.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = response.parse()
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: AlphaxivCat) -> None:
        with client.notifications.v4.archive.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = response.parse()
            assert_matches_type(ArchiveListResponse, archive, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncArchive:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAlphaxivCat) -> None:
        archive = await async_client.notifications.v4.archive.create(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(ArchiveCreateResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.notifications.v4.archive.with_raw_response.create(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = await response.parse()
        assert_matches_type(ArchiveCreateResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.notifications.v4.archive.with_streaming_response.create(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = await response.parse()
            assert_matches_type(ArchiveCreateResponse, archive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAlphaxivCat) -> None:
        archive = await async_client.notifications.v4.archive.list()
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        archive = await async_client.notifications.v4.archive.list(
            before="before",
        )
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.notifications.v4.archive.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        archive = await response.parse()
        assert_matches_type(ArchiveListResponse, archive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.notifications.v4.archive.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            archive = await response.parse()
            assert_matches_type(ArchiveListResponse, archive, path=["response"])

        assert cast(Any, response.is_closed) is True
