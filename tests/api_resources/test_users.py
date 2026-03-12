# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types import (
    UserGetPrivateNotesResponse,
    UserWeighWeeklyReputationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_private_notes(self, client: AlphaxivCat) -> None:
        user = client.users.get_private_notes(
            uid="uid",
        )
        assert_matches_type(UserGetPrivateNotesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_private_notes_with_all_params(self, client: AlphaxivCat) -> None:
        user = client.users.get_private_notes(
            uid="uid",
            limit="limit",
            page="page",
        )
        assert_matches_type(UserGetPrivateNotesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_private_notes(self, client: AlphaxivCat) -> None:
        response = client.users.with_raw_response.get_private_notes(
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserGetPrivateNotesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_private_notes(self, client: AlphaxivCat) -> None:
        with client.users.with_streaming_response.get_private_notes(
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserGetPrivateNotesResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_private_notes(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            client.users.with_raw_response.get_private_notes(
                uid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_weigh_weekly_reputation(self, client: AlphaxivCat) -> None:
        user = client.users.weigh_weekly_reputation()
        assert_matches_type(UserWeighWeeklyReputationResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_weigh_weekly_reputation(self, client: AlphaxivCat) -> None:
        response = client.users.with_raw_response.weigh_weekly_reputation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserWeighWeeklyReputationResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_weigh_weekly_reputation(self, client: AlphaxivCat) -> None:
        with client.users.with_streaming_response.weigh_weekly_reputation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserWeighWeeklyReputationResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_private_notes(self, async_client: AsyncAlphaxivCat) -> None:
        user = await async_client.users.get_private_notes(
            uid="uid",
        )
        assert_matches_type(UserGetPrivateNotesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_private_notes_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        user = await async_client.users.get_private_notes(
            uid="uid",
            limit="limit",
            page="page",
        )
        assert_matches_type(UserGetPrivateNotesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_private_notes(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.with_raw_response.get_private_notes(
            uid="uid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserGetPrivateNotesResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_private_notes(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.with_streaming_response.get_private_notes(
            uid="uid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserGetPrivateNotesResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_private_notes(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uid` but received ''"):
            await async_client.users.with_raw_response.get_private_notes(
                uid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_weigh_weekly_reputation(self, async_client: AsyncAlphaxivCat) -> None:
        user = await async_client.users.weigh_weekly_reputation()
        assert_matches_type(UserWeighWeeklyReputationResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_weigh_weekly_reputation(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.with_raw_response.weigh_weekly_reputation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserWeighWeeklyReputationResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_weigh_weekly_reputation(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.with_streaming_response.weigh_weekly_reputation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserWeighWeeklyReputationResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
