# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.admin import (
    V1GetModeratorFeedResponse,
    V1LookupUserByEmailResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_moderator_feed(self, client: AlphaxivCat) -> None:
        v1 = client.admin.v1.get_moderator_feed()
        assert_matches_type(V1GetModeratorFeedResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_moderator_feed_with_all_params(self, client: AlphaxivCat) -> None:
        v1 = client.admin.v1.get_moderator_feed(
            feed_type="all",
            page="page",
            page_size="pageSize",
        )
        assert_matches_type(V1GetModeratorFeedResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_moderator_feed(self, client: AlphaxivCat) -> None:
        response = client.admin.v1.with_raw_response.get_moderator_feed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetModeratorFeedResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_moderator_feed(self, client: AlphaxivCat) -> None:
        with client.admin.v1.with_streaming_response.get_moderator_feed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetModeratorFeedResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_user_by_email(self, client: AlphaxivCat) -> None:
        v1 = client.admin.v1.lookup_user_by_email(
            email="dev@stainless.com",
        )
        assert_matches_type(V1LookupUserByEmailResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup_user_by_email(self, client: AlphaxivCat) -> None:
        response = client.admin.v1.with_raw_response.lookup_user_by_email(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1LookupUserByEmailResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup_user_by_email(self, client: AlphaxivCat) -> None:
        with client.admin.v1.with_streaming_response.lookup_user_by_email(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1LookupUserByEmailResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_moderator_feed(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.admin.v1.get_moderator_feed()
        assert_matches_type(V1GetModeratorFeedResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_moderator_feed_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.admin.v1.get_moderator_feed(
            feed_type="all",
            page="page",
            page_size="pageSize",
        )
        assert_matches_type(V1GetModeratorFeedResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_moderator_feed(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.admin.v1.with_raw_response.get_moderator_feed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetModeratorFeedResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_moderator_feed(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.admin.v1.with_streaming_response.get_moderator_feed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetModeratorFeedResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_user_by_email(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.admin.v1.lookup_user_by_email(
            email="dev@stainless.com",
        )
        assert_matches_type(V1LookupUserByEmailResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup_user_by_email(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.admin.v1.with_raw_response.lookup_user_by_email(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1LookupUserByEmailResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup_user_by_email(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.admin.v1.with_streaming_response.lookup_user_by_email(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1LookupUserByEmailResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
