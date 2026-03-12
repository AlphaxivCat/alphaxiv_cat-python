# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types import WrappedRetrieveByUserResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWrapped:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_user(self, client: AlphaxivCat) -> None:
        wrapped = client.wrapped.retrieve_by_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WrappedRetrieveByUserResponse, wrapped, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_user(self, client: AlphaxivCat) -> None:
        response = client.wrapped.with_raw_response.retrieve_by_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wrapped = response.parse()
        assert_matches_type(WrappedRetrieveByUserResponse, wrapped, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_user(self, client: AlphaxivCat) -> None:
        with client.wrapped.with_streaming_response.retrieve_by_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wrapped = response.parse()
            assert_matches_type(WrappedRetrieveByUserResponse, wrapped, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_by_user(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.wrapped.with_raw_response.retrieve_by_user(
                "",
            )


class TestAsyncWrapped:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_user(self, async_client: AsyncAlphaxivCat) -> None:
        wrapped = await async_client.wrapped.retrieve_by_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WrappedRetrieveByUserResponse, wrapped, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_user(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.wrapped.with_raw_response.retrieve_by_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wrapped = await response.parse()
        assert_matches_type(WrappedRetrieveByUserResponse, wrapped, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_user(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.wrapped.with_streaming_response.retrieve_by_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wrapped = await response.parse()
            assert_matches_type(WrappedRetrieveByUserResponse, wrapped, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_by_user(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.wrapped.with_raw_response.retrieve_by_user(
                "",
            )
