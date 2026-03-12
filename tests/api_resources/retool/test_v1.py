# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.retool import (
    V1GetTotalUserCountResponse,
    V1GetCumulativeUsersResponse,
    V1GetTotalPaperCountResponse,
    V1GetDailyNewAccountsResponse,
    V1GetTotalCommentCountResponse,
    V1GetDailyConversationsResponse,
    V1GetWeeklyPrivateNotesResponse,
    V1GetWeeklyPublicCommentsResponse,
    V1GetDailyUserChatMessagesResponse,
    V1GetTotalPrivateNotesCountResponse,
    V1GetWeeklyMessageCountsByUserResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_cumulative_users(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_cumulative_users()
        assert_matches_type(V1GetCumulativeUsersResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_cumulative_users(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_cumulative_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetCumulativeUsersResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_cumulative_users(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_cumulative_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetCumulativeUsersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_daily_conversations(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_daily_conversations()
        assert_matches_type(V1GetDailyConversationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_daily_conversations(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_daily_conversations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetDailyConversationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_daily_conversations(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_daily_conversations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetDailyConversationsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_daily_new_accounts(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_daily_new_accounts()
        assert_matches_type(V1GetDailyNewAccountsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_daily_new_accounts(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_daily_new_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetDailyNewAccountsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_daily_new_accounts(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_daily_new_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetDailyNewAccountsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_daily_user_chat_messages(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_daily_user_chat_messages()
        assert_matches_type(V1GetDailyUserChatMessagesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_daily_user_chat_messages(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_daily_user_chat_messages()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetDailyUserChatMessagesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_daily_user_chat_messages(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_daily_user_chat_messages() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetDailyUserChatMessagesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_total_comment_count(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_total_comment_count()
        assert_matches_type(V1GetTotalCommentCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_total_comment_count(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_total_comment_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetTotalCommentCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_total_comment_count(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_total_comment_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetTotalCommentCountResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_total_paper_count(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_total_paper_count()
        assert_matches_type(V1GetTotalPaperCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_total_paper_count(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_total_paper_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetTotalPaperCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_total_paper_count(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_total_paper_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetTotalPaperCountResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_total_private_notes_count(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_total_private_notes_count()
        assert_matches_type(V1GetTotalPrivateNotesCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_total_private_notes_count(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_total_private_notes_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetTotalPrivateNotesCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_total_private_notes_count(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_total_private_notes_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetTotalPrivateNotesCountResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_total_user_count(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_total_user_count()
        assert_matches_type(V1GetTotalUserCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_total_user_count(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_total_user_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetTotalUserCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_total_user_count(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_total_user_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetTotalUserCountResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_weekly_message_counts_by_user(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_weekly_message_counts_by_user()
        assert_matches_type(V1GetWeeklyMessageCountsByUserResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_weekly_message_counts_by_user(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_weekly_message_counts_by_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetWeeklyMessageCountsByUserResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_weekly_message_counts_by_user(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_weekly_message_counts_by_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetWeeklyMessageCountsByUserResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_weekly_private_notes(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_weekly_private_notes()
        assert_matches_type(V1GetWeeklyPrivateNotesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_weekly_private_notes(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_weekly_private_notes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetWeeklyPrivateNotesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_weekly_private_notes(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_weekly_private_notes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetWeeklyPrivateNotesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_weekly_public_comments(self, client: AlphaxivCat) -> None:
        v1 = client.retool.v1.get_weekly_public_comments()
        assert_matches_type(V1GetWeeklyPublicCommentsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_weekly_public_comments(self, client: AlphaxivCat) -> None:
        response = client.retool.v1.with_raw_response.get_weekly_public_comments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetWeeklyPublicCommentsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_weekly_public_comments(self, client: AlphaxivCat) -> None:
        with client.retool.v1.with_streaming_response.get_weekly_public_comments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetWeeklyPublicCommentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_cumulative_users(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_cumulative_users()
        assert_matches_type(V1GetCumulativeUsersResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_cumulative_users(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_cumulative_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetCumulativeUsersResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_cumulative_users(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_cumulative_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetCumulativeUsersResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_daily_conversations(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_daily_conversations()
        assert_matches_type(V1GetDailyConversationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_daily_conversations(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_daily_conversations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetDailyConversationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_daily_conversations(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_daily_conversations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetDailyConversationsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_daily_new_accounts(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_daily_new_accounts()
        assert_matches_type(V1GetDailyNewAccountsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_daily_new_accounts(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_daily_new_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetDailyNewAccountsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_daily_new_accounts(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_daily_new_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetDailyNewAccountsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_daily_user_chat_messages(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_daily_user_chat_messages()
        assert_matches_type(V1GetDailyUserChatMessagesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_daily_user_chat_messages(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_daily_user_chat_messages()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetDailyUserChatMessagesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_daily_user_chat_messages(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_daily_user_chat_messages() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetDailyUserChatMessagesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_total_comment_count(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_total_comment_count()
        assert_matches_type(V1GetTotalCommentCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_total_comment_count(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_total_comment_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetTotalCommentCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_total_comment_count(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_total_comment_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetTotalCommentCountResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_total_paper_count(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_total_paper_count()
        assert_matches_type(V1GetTotalPaperCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_total_paper_count(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_total_paper_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetTotalPaperCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_total_paper_count(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_total_paper_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetTotalPaperCountResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_total_private_notes_count(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_total_private_notes_count()
        assert_matches_type(V1GetTotalPrivateNotesCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_total_private_notes_count(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_total_private_notes_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetTotalPrivateNotesCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_total_private_notes_count(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_total_private_notes_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetTotalPrivateNotesCountResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_total_user_count(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_total_user_count()
        assert_matches_type(V1GetTotalUserCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_total_user_count(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_total_user_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetTotalUserCountResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_total_user_count(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_total_user_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetTotalUserCountResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_weekly_message_counts_by_user(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_weekly_message_counts_by_user()
        assert_matches_type(V1GetWeeklyMessageCountsByUserResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_weekly_message_counts_by_user(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_weekly_message_counts_by_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetWeeklyMessageCountsByUserResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_weekly_message_counts_by_user(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_weekly_message_counts_by_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetWeeklyMessageCountsByUserResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_weekly_private_notes(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_weekly_private_notes()
        assert_matches_type(V1GetWeeklyPrivateNotesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_weekly_private_notes(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_weekly_private_notes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetWeeklyPrivateNotesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_weekly_private_notes(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_weekly_private_notes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetWeeklyPrivateNotesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_weekly_public_comments(self, async_client: AsyncAlphaxivCat) -> None:
        v1 = await async_client.retool.v1.get_weekly_public_comments()
        assert_matches_type(V1GetWeeklyPublicCommentsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_weekly_public_comments(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.retool.v1.with_raw_response.get_weekly_public_comments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetWeeklyPublicCommentsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_weekly_public_comments(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.retool.v1.with_streaming_response.get_weekly_public_comments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetWeeklyPublicCommentsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
