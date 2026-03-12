# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_monthly_digest(self, client: AlphaxivCat) -> None:
        email = client.admin.v1.emails.send_monthly_digest()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_monthly_digest_with_all_params(self, client: AlphaxivCat) -> None:
        email = client.admin.v1.emails.send_monthly_digest(
            role="admin",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_monthly_digest(self, client: AlphaxivCat) -> None:
        response = client.admin.v1.emails.with_raw_response.send_monthly_digest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_monthly_digest(self, client: AlphaxivCat) -> None:
        with client.admin.v1.emails.with_streaming_response.send_monthly_digest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_weekly_digest(self, client: AlphaxivCat) -> None:
        email = client.admin.v1.emails.send_weekly_digest()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_weekly_digest_with_all_params(self, client: AlphaxivCat) -> None:
        email = client.admin.v1.emails.send_weekly_digest(
            events=[
                {
                    "date": "date",
                    "description": "description",
                    "link": "link",
                    "title": "title",
                    "end_time_raw": "endTimeRaw",
                    "start_time_raw": "startTimeRaw",
                }
            ],
            intro_text="introText",
            role="admin",
            subject="subject",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_weekly_digest(self, client: AlphaxivCat) -> None:
        response = client.admin.v1.emails.with_raw_response.send_weekly_digest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_weekly_digest(self, client: AlphaxivCat) -> None:
        with client.admin.v1.emails.with_streaming_response.send_weekly_digest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_monthly_digest(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.admin.v1.emails.send_monthly_digest()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_monthly_digest_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.admin.v1.emails.send_monthly_digest(
            role="admin",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_monthly_digest(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.admin.v1.emails.with_raw_response.send_monthly_digest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_monthly_digest(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.admin.v1.emails.with_streaming_response.send_monthly_digest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_weekly_digest(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.admin.v1.emails.send_weekly_digest()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_weekly_digest_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.admin.v1.emails.send_weekly_digest(
            events=[
                {
                    "date": "date",
                    "description": "description",
                    "link": "link",
                    "title": "title",
                    "end_time_raw": "endTimeRaw",
                    "start_time_raw": "startTimeRaw",
                }
            ],
            intro_text="introText",
            role="admin",
            subject="subject",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_weekly_digest(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.admin.v1.emails.with_raw_response.send_weekly_digest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_weekly_digest(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.admin.v1.emails.with_streaming_response.send_weekly_digest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True
