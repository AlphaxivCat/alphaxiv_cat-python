# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.arxiv.v1 import LabRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLabs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: AlphaxivCat) -> None:
        lab = client.arxiv.v1.labs.retrieve(
            "unresolved",
        )
        assert_matches_type(LabRetrieveResponse, lab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: AlphaxivCat) -> None:
        response = client.arxiv.v1.labs.with_raw_response.retrieve(
            "unresolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lab = response.parse()
        assert_matches_type(LabRetrieveResponse, lab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: AlphaxivCat) -> None:
        with client.arxiv.v1.labs.with_streaming_response.retrieve(
            "unresolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lab = response.parse()
            assert_matches_type(LabRetrieveResponse, lab, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unresolved` but received ''"):
            client.arxiv.v1.labs.with_raw_response.retrieve(
                "",
            )


class TestAsyncLabs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        lab = await async_client.arxiv.v1.labs.retrieve(
            "unresolved",
        )
        assert_matches_type(LabRetrieveResponse, lab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.arxiv.v1.labs.with_raw_response.retrieve(
            "unresolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lab = await response.parse()
        assert_matches_type(LabRetrieveResponse, lab, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.arxiv.v1.labs.with_streaming_response.retrieve(
            "unresolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lab = await response.parse()
            assert_matches_type(LabRetrieveResponse, lab, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unresolved` but received ''"):
            await async_client.arxiv.v1.labs.with_raw_response.retrieve(
                "",
            )
