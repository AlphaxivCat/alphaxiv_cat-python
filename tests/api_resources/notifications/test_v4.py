# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.notifications import V4ListNotificationsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV4:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_notifications(self, client: AlphaxivCat) -> None:
        v4 = client.notifications.v4.list_notifications()
        assert_matches_type(V4ListNotificationsResponse, v4, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_notifications(self, client: AlphaxivCat) -> None:
        response = client.notifications.v4.with_raw_response.list_notifications()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = response.parse()
        assert_matches_type(V4ListNotificationsResponse, v4, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_notifications(self, client: AlphaxivCat) -> None:
        with client.notifications.v4.with_streaming_response.list_notifications() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = response.parse()
            assert_matches_type(V4ListNotificationsResponse, v4, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_subscribe(self, client: AlphaxivCat) -> None:
        v4 = client.notifications.v4.subscribe(
            subscription={
                "endpoint": "https://example.com",
                "keys": {
                    "auth": "auth",
                    "p256dh": "p256dh",
                },
            },
        )
        assert v4 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_subscribe(self, client: AlphaxivCat) -> None:
        response = client.notifications.v4.with_raw_response.subscribe(
            subscription={
                "endpoint": "https://example.com",
                "keys": {
                    "auth": "auth",
                    "p256dh": "p256dh",
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = response.parse()
        assert v4 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_subscribe(self, client: AlphaxivCat) -> None:
        with client.notifications.v4.with_streaming_response.subscribe(
            subscription={
                "endpoint": "https://example.com",
                "keys": {
                    "auth": "auth",
                    "p256dh": "p256dh",
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = response.parse()
            assert v4 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unsubscribe(self, client: AlphaxivCat) -> None:
        v4 = client.notifications.v4.unsubscribe(
            endpoint="https://example.com",
        )
        assert v4 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unsubscribe(self, client: AlphaxivCat) -> None:
        response = client.notifications.v4.with_raw_response.unsubscribe(
            endpoint="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = response.parse()
        assert v4 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unsubscribe(self, client: AlphaxivCat) -> None:
        with client.notifications.v4.with_streaming_response.unsubscribe(
            endpoint="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = response.parse()
            assert v4 is None

        assert cast(Any, response.is_closed) is True


class TestAsyncV4:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_notifications(self, async_client: AsyncAlphaxivCat) -> None:
        v4 = await async_client.notifications.v4.list_notifications()
        assert_matches_type(V4ListNotificationsResponse, v4, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_notifications(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.notifications.v4.with_raw_response.list_notifications()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = await response.parse()
        assert_matches_type(V4ListNotificationsResponse, v4, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_notifications(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.notifications.v4.with_streaming_response.list_notifications() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = await response.parse()
            assert_matches_type(V4ListNotificationsResponse, v4, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_subscribe(self, async_client: AsyncAlphaxivCat) -> None:
        v4 = await async_client.notifications.v4.subscribe(
            subscription={
                "endpoint": "https://example.com",
                "keys": {
                    "auth": "auth",
                    "p256dh": "p256dh",
                },
            },
        )
        assert v4 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_subscribe(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.notifications.v4.with_raw_response.subscribe(
            subscription={
                "endpoint": "https://example.com",
                "keys": {
                    "auth": "auth",
                    "p256dh": "p256dh",
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = await response.parse()
        assert v4 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_subscribe(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.notifications.v4.with_streaming_response.subscribe(
            subscription={
                "endpoint": "https://example.com",
                "keys": {
                    "auth": "auth",
                    "p256dh": "p256dh",
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = await response.parse()
            assert v4 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unsubscribe(self, async_client: AsyncAlphaxivCat) -> None:
        v4 = await async_client.notifications.v4.unsubscribe(
            endpoint="https://example.com",
        )
        assert v4 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unsubscribe(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.notifications.v4.with_raw_response.unsubscribe(
            endpoint="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = await response.parse()
        assert v4 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unsubscribe(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.notifications.v4.with_streaming_response.unsubscribe(
            endpoint="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = await response.parse()
            assert v4 is None

        assert cast(Any, response.is_closed) is True
