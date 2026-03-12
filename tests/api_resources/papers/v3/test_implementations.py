# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.papers.v3 import (
    ImplementationListResponse,
    ImplementationCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImplementations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: AlphaxivCat) -> None:
        implementation = client.papers.v3.implementations.create(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            implementation_type="alphaxiv",
            url="https://example.com",
        )
        assert_matches_type(ImplementationCreateResponse, implementation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.implementations.with_raw_response.create(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            implementation_type="alphaxiv",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        implementation = response.parse()
        assert_matches_type(ImplementationCreateResponse, implementation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: AlphaxivCat) -> None:
        with client.papers.v3.implementations.with_streaming_response.create(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            implementation_type="alphaxiv",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            implementation = response.parse()
            assert_matches_type(ImplementationCreateResponse, implementation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            client.papers.v3.implementations.with_raw_response.create(
                paper_group_id="",
                implementation_type="alphaxiv",
                url="https://example.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: AlphaxivCat) -> None:
        implementation = client.papers.v3.implementations.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ImplementationListResponse, implementation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.implementations.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        implementation = response.parse()
        assert_matches_type(ImplementationListResponse, implementation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: AlphaxivCat) -> None:
        with client.papers.v3.implementations.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            implementation = response.parse()
            assert_matches_type(ImplementationListResponse, implementation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            client.papers.v3.implementations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: AlphaxivCat) -> None:
        implementation = client.papers.v3.implementations.delete(
            implementation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="alphaxiv",
        )
        assert implementation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.implementations.with_raw_response.delete(
            implementation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="alphaxiv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        implementation = response.parse()
        assert implementation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AlphaxivCat) -> None:
        with client.papers.v3.implementations.with_streaming_response.delete(
            implementation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="alphaxiv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            implementation = response.parse()
            assert implementation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            client.papers.v3.implementations.with_raw_response.delete(
                implementation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                paper_group_id="",
                type="alphaxiv",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `implementation_id` but received ''"):
            client.papers.v3.implementations.with_raw_response.delete(
                implementation_id="",
                paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                type="alphaxiv",
            )


class TestAsyncImplementations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAlphaxivCat) -> None:
        implementation = await async_client.papers.v3.implementations.create(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            implementation_type="alphaxiv",
            url="https://example.com",
        )
        assert_matches_type(ImplementationCreateResponse, implementation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.implementations.with_raw_response.create(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            implementation_type="alphaxiv",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        implementation = await response.parse()
        assert_matches_type(ImplementationCreateResponse, implementation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.implementations.with_streaming_response.create(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            implementation_type="alphaxiv",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            implementation = await response.parse()
            assert_matches_type(ImplementationCreateResponse, implementation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            await async_client.papers.v3.implementations.with_raw_response.create(
                paper_group_id="",
                implementation_type="alphaxiv",
                url="https://example.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAlphaxivCat) -> None:
        implementation = await async_client.papers.v3.implementations.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ImplementationListResponse, implementation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.implementations.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        implementation = await response.parse()
        assert_matches_type(ImplementationListResponse, implementation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.implementations.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            implementation = await response.parse()
            assert_matches_type(ImplementationListResponse, implementation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            await async_client.papers.v3.implementations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAlphaxivCat) -> None:
        implementation = await async_client.papers.v3.implementations.delete(
            implementation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="alphaxiv",
        )
        assert implementation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.implementations.with_raw_response.delete(
            implementation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="alphaxiv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        implementation = await response.parse()
        assert implementation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.implementations.with_streaming_response.delete(
            implementation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="alphaxiv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            implementation = await response.parse()
            assert implementation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            await async_client.papers.v3.implementations.with_raw_response.delete(
                implementation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                paper_group_id="",
                type="alphaxiv",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `implementation_id` but received ''"):
            await async_client.papers.v3.implementations.with_raw_response.delete(
                implementation_id="",
                paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                type="alphaxiv",
            )
