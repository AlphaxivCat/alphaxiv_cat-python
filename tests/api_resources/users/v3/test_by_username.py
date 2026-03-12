# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.users.v3 import ByUsernameGetUserResponse, ByUsernameGetProfilePageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestByUsername:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_profile_page(self, client: AlphaxivCat) -> None:
        by_username = client.users.v3.by_username.get_profile_page(
            "x",
        )
        assert_matches_type(ByUsernameGetProfilePageResponse, by_username, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_profile_page(self, client: AlphaxivCat) -> None:
        response = client.users.v3.by_username.with_raw_response.get_profile_page(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_username = response.parse()
        assert_matches_type(ByUsernameGetProfilePageResponse, by_username, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_profile_page(self, client: AlphaxivCat) -> None:
        with client.users.v3.by_username.with_streaming_response.get_profile_page(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_username = response.parse()
            assert_matches_type(ByUsernameGetProfilePageResponse, by_username, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_profile_page(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.users.v3.by_username.with_raw_response.get_profile_page(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_user(self, client: AlphaxivCat) -> None:
        by_username = client.users.v3.by_username.get_user(
            "x",
        )
        assert_matches_type(ByUsernameGetUserResponse, by_username, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_user(self, client: AlphaxivCat) -> None:
        response = client.users.v3.by_username.with_raw_response.get_user(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_username = response.parse()
        assert_matches_type(ByUsernameGetUserResponse, by_username, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_user(self, client: AlphaxivCat) -> None:
        with client.users.v3.by_username.with_streaming_response.get_user(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_username = response.parse()
            assert_matches_type(ByUsernameGetUserResponse, by_username, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_user(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.users.v3.by_username.with_raw_response.get_user(
                "",
            )


class TestAsyncByUsername:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_profile_page(self, async_client: AsyncAlphaxivCat) -> None:
        by_username = await async_client.users.v3.by_username.get_profile_page(
            "x",
        )
        assert_matches_type(ByUsernameGetProfilePageResponse, by_username, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_profile_page(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.by_username.with_raw_response.get_profile_page(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_username = await response.parse()
        assert_matches_type(ByUsernameGetProfilePageResponse, by_username, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_profile_page(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.by_username.with_streaming_response.get_profile_page(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_username = await response.parse()
            assert_matches_type(ByUsernameGetProfilePageResponse, by_username, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_profile_page(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.users.v3.by_username.with_raw_response.get_profile_page(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_user(self, async_client: AsyncAlphaxivCat) -> None:
        by_username = await async_client.users.v3.by_username.get_user(
            "x",
        )
        assert_matches_type(ByUsernameGetUserResponse, by_username, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_user(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.by_username.with_raw_response.get_user(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_username = await response.parse()
        assert_matches_type(ByUsernameGetUserResponse, by_username, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_user(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.by_username.with_streaming_response.get_user(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_username = await response.parse()
            assert_matches_type(ByUsernameGetUserResponse, by_username, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_user(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.users.v3.by_username.with_raw_response.get_user(
                "",
            )
