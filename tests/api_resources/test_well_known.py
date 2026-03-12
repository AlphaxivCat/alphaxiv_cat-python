# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWellKnown:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_oauth_protected_resource(self, client: AlphaxivCat) -> None:
        well_known = client.well_known.retrieve_oauth_protected_resource()
        assert_matches_type(object, well_known, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_oauth_protected_resource(self, client: AlphaxivCat) -> None:
        response = client.well_known.with_raw_response.retrieve_oauth_protected_resource()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        well_known = response.parse()
        assert_matches_type(object, well_known, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_oauth_protected_resource(self, client: AlphaxivCat) -> None:
        with client.well_known.with_streaming_response.retrieve_oauth_protected_resource() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            well_known = response.parse()
            assert_matches_type(object, well_known, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWellKnown:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_oauth_protected_resource(self, async_client: AsyncAlphaxivCat) -> None:
        well_known = await async_client.well_known.retrieve_oauth_protected_resource()
        assert_matches_type(object, well_known, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_oauth_protected_resource(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.well_known.with_raw_response.retrieve_oauth_protected_resource()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        well_known = await response.parse()
        assert_matches_type(object, well_known, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_oauth_protected_resource(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.well_known.with_streaming_response.retrieve_oauth_protected_resource() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            well_known = await response.parse()
            assert_matches_type(object, well_known, path=["response"])

        assert cast(Any, response.is_closed) is True
