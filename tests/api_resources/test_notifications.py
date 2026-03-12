# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types import NotificationSendKickoffNotificationEmailsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_kickoff_notification_emails(self, client: AlphaxivCat) -> None:
        notification = client.notifications.send_kickoff_notification_emails()
        assert_matches_type(NotificationSendKickoffNotificationEmailsResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_kickoff_notification_emails(self, client: AlphaxivCat) -> None:
        response = client.notifications.with_raw_response.send_kickoff_notification_emails()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationSendKickoffNotificationEmailsResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_kickoff_notification_emails(self, client: AlphaxivCat) -> None:
        with client.notifications.with_streaming_response.send_kickoff_notification_emails() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationSendKickoffNotificationEmailsResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_kickoff_notification_emails(self, async_client: AsyncAlphaxivCat) -> None:
        notification = await async_client.notifications.send_kickoff_notification_emails()
        assert_matches_type(NotificationSendKickoffNotificationEmailsResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_kickoff_notification_emails(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.notifications.with_raw_response.send_kickoff_notification_emails()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationSendKickoffNotificationEmailsResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_kickoff_notification_emails(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.notifications.with_streaming_response.send_kickoff_notification_emails() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationSendKickoffNotificationEmailsResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True
