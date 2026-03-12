# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_project(self, client: AlphaxivCat) -> None:
        research = client.research.create_project(
            name="name",
        )
        assert_matches_type(str, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_project_with_all_params(self, client: AlphaxivCat) -> None:
        research = client.research.create_project(
            name="name",
            folder={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "delete": True,
            },
            initial_papers=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_project(self, client: AlphaxivCat) -> None:
        response = client.research.with_raw_response.create_project(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = response.parse()
        assert_matches_type(str, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_project(self, client: AlphaxivCat) -> None:
        with client.research.with_streaming_response.create_project(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = response.parse()
            assert_matches_type(str, research, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_project(self, async_client: AsyncAlphaxivCat) -> None:
        research = await async_client.research.create_project(
            name="name",
        )
        assert_matches_type(str, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_project_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        research = await async_client.research.create_project(
            name="name",
            folder={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "delete": True,
            },
            initial_papers=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_project(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.research.with_raw_response.create_project(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = await response.parse()
        assert_matches_type(str, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_project(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.research.with_streaming_response.create_project(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = await response.parse()
            assert_matches_type(str, research, path=["response"])

        assert cast(Any, response.is_closed) is True
