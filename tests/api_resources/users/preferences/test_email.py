# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.users.preferences import EmailGetResponse, EmailUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmail:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: AlphaxivCat) -> None:
        email = client.users.preferences.email.update()
        assert_matches_type(EmailUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: AlphaxivCat) -> None:
        email = client.users.preferences.email.update(
            direct_notifications=True,
            relevant_activity=True,
        )
        assert_matches_type(EmailUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: AlphaxivCat) -> None:
        response = client.users.preferences.email.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: AlphaxivCat) -> None:
        with client.users.preferences.email.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailUpdateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: AlphaxivCat) -> None:
        email = client.users.preferences.email.get()
        assert_matches_type(EmailGetResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: AlphaxivCat) -> None:
        response = client.users.preferences.email.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailGetResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: AlphaxivCat) -> None:
        with client.users.preferences.email.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailGetResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmail:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.users.preferences.email.update()
        assert_matches_type(EmailUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.users.preferences.email.update(
            direct_notifications=True,
            relevant_activity=True,
        )
        assert_matches_type(EmailUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.preferences.email.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.preferences.email.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailUpdateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.users.preferences.email.get()
        assert_matches_type(EmailGetResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.preferences.email.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailGetResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.preferences.email.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailGetResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True
