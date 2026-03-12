# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.users import PreferenceGetFoldersPreferencesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_folders_preferences(self, client: AlphaxivCat) -> None:
        preference = client.users.preferences.get_folders_preferences()
        assert_matches_type(PreferenceGetFoldersPreferencesResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_folders_preferences(self, client: AlphaxivCat) -> None:
        response = client.users.preferences.with_raw_response.get_folders_preferences()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(PreferenceGetFoldersPreferencesResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_folders_preferences(self, client: AlphaxivCat) -> None:
        with client.users.preferences.with_streaming_response.get_folders_preferences() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(PreferenceGetFoldersPreferencesResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPreferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_folders_preferences(self, async_client: AsyncAlphaxivCat) -> None:
        preference = await async_client.users.preferences.get_folders_preferences()
        assert_matches_type(PreferenceGetFoldersPreferencesResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_folders_preferences(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.preferences.with_raw_response.get_folders_preferences()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(PreferenceGetFoldersPreferencesResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_folders_preferences(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.preferences.with_streaming_response.get_folders_preferences() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(PreferenceGetFoldersPreferencesResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True
