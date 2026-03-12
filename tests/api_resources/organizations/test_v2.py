# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.organizations import (
    V2SearchResponse,
    V2ListTopResponse,
    V2RetrieveByIDResponse,
    V2ToggleFollowResponse,
    V2RetrieveByNameResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_top(self, client: AlphaxivCat) -> None:
        v2 = client.organizations.v2.list_top()
        assert_matches_type(V2ListTopResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_top(self, client: AlphaxivCat) -> None:
        response = client.organizations.v2.with_raw_response.list_top()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ListTopResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_top(self, client: AlphaxivCat) -> None:
        with client.organizations.v2.with_streaming_response.list_top() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ListTopResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_id(self, client: AlphaxivCat) -> None:
        v2 = client.organizations.v2.retrieve_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2RetrieveByIDResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_id(self, client: AlphaxivCat) -> None:
        response = client.organizations.v2.with_raw_response.retrieve_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2RetrieveByIDResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_id(self, client: AlphaxivCat) -> None:
        with client.organizations.v2.with_streaming_response.retrieve_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2RetrieveByIDResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_by_id(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.organizations.v2.with_raw_response.retrieve_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_name(self, client: AlphaxivCat) -> None:
        v2 = client.organizations.v2.retrieve_by_name(
            "name",
        )
        assert_matches_type(V2RetrieveByNameResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_name(self, client: AlphaxivCat) -> None:
        response = client.organizations.v2.with_raw_response.retrieve_by_name(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2RetrieveByNameResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_name(self, client: AlphaxivCat) -> None:
        with client.organizations.v2.with_streaming_response.retrieve_by_name(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2RetrieveByNameResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_by_name(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.organizations.v2.with_raw_response.retrieve_by_name(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: AlphaxivCat) -> None:
        v2 = client.organizations.v2.search(
            q="q",
        )
        assert_matches_type(V2SearchResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: AlphaxivCat) -> None:
        response = client.organizations.v2.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2SearchResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: AlphaxivCat) -> None:
        with client.organizations.v2.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2SearchResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle_follow(self, client: AlphaxivCat) -> None:
        v2 = client.organizations.v2.toggle_follow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2ToggleFollowResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_toggle_follow(self, client: AlphaxivCat) -> None:
        response = client.organizations.v2.with_raw_response.toggle_follow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ToggleFollowResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_toggle_follow(self, client: AlphaxivCat) -> None:
        with client.organizations.v2.with_streaming_response.toggle_follow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ToggleFollowResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_toggle_follow(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.organizations.v2.with_raw_response.toggle_follow(
                "",
            )


class TestAsyncV2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_top(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.organizations.v2.list_top()
        assert_matches_type(V2ListTopResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_top(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.organizations.v2.with_raw_response.list_top()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ListTopResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_top(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.organizations.v2.with_streaming_response.list_top() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ListTopResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_id(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.organizations.v2.retrieve_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2RetrieveByIDResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_id(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.organizations.v2.with_raw_response.retrieve_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2RetrieveByIDResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_id(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.organizations.v2.with_streaming_response.retrieve_by_id(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2RetrieveByIDResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_by_id(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.organizations.v2.with_raw_response.retrieve_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_name(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.organizations.v2.retrieve_by_name(
            "name",
        )
        assert_matches_type(V2RetrieveByNameResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_name(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.organizations.v2.with_raw_response.retrieve_by_name(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2RetrieveByNameResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_name(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.organizations.v2.with_streaming_response.retrieve_by_name(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2RetrieveByNameResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_by_name(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.organizations.v2.with_raw_response.retrieve_by_name(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.organizations.v2.search(
            q="q",
        )
        assert_matches_type(V2SearchResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.organizations.v2.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2SearchResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.organizations.v2.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2SearchResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle_follow(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.organizations.v2.toggle_follow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2ToggleFollowResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_toggle_follow(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.organizations.v2.with_raw_response.toggle_follow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2ToggleFollowResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_toggle_follow(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.organizations.v2.with_streaming_response.toggle_follow(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ToggleFollowResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_toggle_follow(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.organizations.v2.with_raw_response.toggle_follow(
                "",
            )
