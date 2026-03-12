# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.google_scholar import (
    V1SyncResponse,
    V1ResyncResponse,
    V1ConnectResponse,
    V1GetReportResponse,
    V1GetStatusResponse,
    V1VerifyEmailResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect(self, client: AlphaxivCat) -> None:
        v1 = client.google_scholar.v1.connect(
            google_scholar_id="x",
        )
        assert_matches_type(V1ConnectResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: AlphaxivCat) -> None:
        response = client.google_scholar.v1.with_raw_response.connect(
            google_scholar_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ConnectResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: AlphaxivCat) -> None:
        with client.google_scholar.v1.with_streaming_response.connect(
            google_scholar_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ConnectResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_connection(self, client: AlphaxivCat) -> None:
        v1 = client.google_scholar.v1.delete_connection()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_connection(self, client: AlphaxivCat) -> None:
        response = client.google_scholar.v1.with_raw_response.delete_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_connection(self, client: AlphaxivCat) -> None:
        with client.google_scholar.v1.with_streaming_response.delete_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_report(self, client: AlphaxivCat) -> None:
        v1 = client.google_scholar.v1.get_report()
        assert_matches_type(V1GetReportResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_report(self, client: AlphaxivCat) -> None:
        response = client.google_scholar.v1.with_raw_response.get_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetReportResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_report(self, client: AlphaxivCat) -> None:
        with client.google_scholar.v1.with_streaming_response.get_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetReportResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: AlphaxivCat) -> None:
        v1 = client.google_scholar.v1.get_status()
        assert_matches_type(V1GetStatusResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: AlphaxivCat) -> None:
        response = client.google_scholar.v1.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetStatusResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: AlphaxivCat) -> None:
        with client.google_scholar.v1.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetStatusResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resync(self, client: AlphaxivCat) -> None:
        v1 = client.google_scholar.v1.resync(
            "all",
        )
        assert_matches_type(V1ResyncResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resync(self, client: AlphaxivCat) -> None:
        response = client.google_scholar.v1.with_raw_response.resync(
            "all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ResyncResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resync(self, client: AlphaxivCat) -> None:
        with client.google_scholar.v1.with_streaming_response.resync(
            "all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ResyncResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_email(self, client: AlphaxivCat) -> None:
        v1 = client.google_scholar.v1.set_email(
            local_part="localPart",
            verify_account_email=True,
        )
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_email(self, client: AlphaxivCat) -> None:
        response = client.google_scholar.v1.with_raw_response.set_email(
            local_part="localPart",
            verify_account_email=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_email(self, client: AlphaxivCat) -> None:
        with client.google_scholar.v1.with_streaming_response.set_email(
            local_part="localPart",
            verify_account_email=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync(self, client: AlphaxivCat) -> None:
        v1 = client.google_scholar.v1.sync()
        assert_matches_type(V1SyncResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sync(self, client: AlphaxivCat) -> None:
        response = client.google_scholar.v1.with_raw_response.sync()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1SyncResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sync(self, client: AlphaxivCat) -> None:
        with client.google_scholar.v1.with_streaming_response.sync() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1SyncResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_email(self, client: AlphaxivCat) -> None:
        v1 = client.google_scholar.v1.verify_email(
            code="xxxxxx",
        )
        assert_matches_type(V1VerifyEmailResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify_email(self, client: AlphaxivCat) -> None:
        response = client.google_scholar.v1.with_raw_response.verify_email(
            code="xxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1VerifyEmailResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify_email(self, client: AlphaxivCat) -> None:
        with client.google_scholar.v1.with_streaming_response.verify_email(
            code="xxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1VerifyEmailResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.google_scholar.v1.connect(
            google_scholar_id="x",
        )
        assert_matches_type(V1ConnectResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.google_scholar.v1.with_raw_response.connect(
            google_scholar_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ConnectResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.google_scholar.v1.with_streaming_response.connect(
            google_scholar_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ConnectResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_connection(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.google_scholar.v1.delete_connection()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_connection(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.google_scholar.v1.with_raw_response.delete_connection()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_connection(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.google_scholar.v1.with_streaming_response.delete_connection() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_report(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.google_scholar.v1.get_report()
        assert_matches_type(V1GetReportResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_report(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.google_scholar.v1.with_raw_response.get_report()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetReportResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_report(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.google_scholar.v1.with_streaming_response.get_report() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetReportResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.google_scholar.v1.get_status()
        assert_matches_type(V1GetStatusResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.google_scholar.v1.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetStatusResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.google_scholar.v1.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetStatusResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resync(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.google_scholar.v1.resync(
            "all",
        )
        assert_matches_type(V1ResyncResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resync(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.google_scholar.v1.with_raw_response.resync(
            "all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ResyncResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resync(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.google_scholar.v1.with_streaming_response.resync(
            "all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ResyncResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_email(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.google_scholar.v1.set_email(
            local_part="localPart",
            verify_account_email=True,
        )
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_email(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.google_scholar.v1.with_raw_response.set_email(
            local_part="localPart",
            verify_account_email=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_email(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.google_scholar.v1.with_streaming_response.set_email(
            local_part="localPart",
            verify_account_email=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.google_scholar.v1.sync()
        assert_matches_type(V1SyncResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.google_scholar.v1.with_raw_response.sync()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1SyncResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.google_scholar.v1.with_streaming_response.sync() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1SyncResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_email(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.google_scholar.v1.verify_email(
            code="xxxxxx",
        )
        assert_matches_type(V1VerifyEmailResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify_email(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.google_scholar.v1.with_raw_response.verify_email(
            code="xxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1VerifyEmailResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify_email(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.google_scholar.v1.with_streaming_response.verify_email(
            code="xxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1VerifyEmailResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
