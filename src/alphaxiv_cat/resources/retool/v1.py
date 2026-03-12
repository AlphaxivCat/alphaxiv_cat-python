# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.retool.v1_get_cumulative_users_response import V1GetCumulativeUsersResponse
from ...types.retool.v1_get_total_user_count_response import V1GetTotalUserCountResponse
from ...types.retool.v1_get_total_paper_count_response import V1GetTotalPaperCountResponse
from ...types.retool.v1_get_daily_new_accounts_response import V1GetDailyNewAccountsResponse
from ...types.retool.v1_get_daily_conversations_response import V1GetDailyConversationsResponse
from ...types.retool.v1_get_total_comment_count_response import V1GetTotalCommentCountResponse
from ...types.retool.v1_get_weekly_private_notes_response import V1GetWeeklyPrivateNotesResponse
from ...types.retool.v1_get_weekly_public_comments_response import V1GetWeeklyPublicCommentsResponse
from ...types.retool.v1_get_daily_user_chat_messages_response import V1GetDailyUserChatMessagesResponse
from ...types.retool.v1_get_total_private_notes_count_response import V1GetTotalPrivateNotesCountResponse
from ...types.retool.v1_get_weekly_message_counts_by_user_response import V1GetWeeklyMessageCountsByUserResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def get_cumulative_users(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetCumulativeUsersResponse:
        """
        Get cumulative user count over time (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-cumulative-users.controller.ts`
        """
        return self._get(
            "/retool/v1/cumulative-users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetCumulativeUsersResponse,
        )

    def get_daily_conversations(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetDailyConversationsResponse:
        """
        Get daily conversation counts by variant (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-daily-conversations.controller.ts`
        """
        return self._get(
            "/retool/v1/daily-conversations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetDailyConversationsResponse,
        )

    def get_daily_new_accounts(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetDailyNewAccountsResponse:
        """
        Get daily new account counts (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-daily-new-accounts.controller.ts`
        """
        return self._get(
            "/retool/v1/daily-new-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetDailyNewAccountsResponse,
        )

    def get_daily_user_chat_messages(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetDailyUserChatMessagesResponse:
        """
        Get daily user chat message counts by variant (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-daily-user-chat-messages.controller.ts`
        """
        return self._get(
            "/retool/v1/daily-user-chat-messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetDailyUserChatMessagesResponse,
        )

    def get_total_comment_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTotalCommentCountResponse:
        """
        Get total count of all comments

        Source file:
        `api-server/src/controllers/retool/v1/get-total-comment-count.controller.ts`
        """
        return self._get(
            "/retool/v1/total-comment-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=float,
        )

    def get_total_paper_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTotalPaperCountResponse:
        """
        Get total count of public, non-blocked papers

        Source file:
        `api-server/src/controllers/retool/v1/get-total-paper-count.controller.ts`
        """
        return self._get(
            "/retool/v1/total-paper-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=float,
        )

    def get_total_private_notes_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTotalPrivateNotesCountResponse:
        """
        Get total count of private notes (comments with tag=personal)

        Source file:
        `api-server/src/controllers/retool/v1/get-total-private-notes-count.controller.ts`
        """
        return self._get(
            "/retool/v1/total-private-notes-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=float,
        )

    def get_total_user_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTotalUserCountResponse:
        """
        Get total count of non-deleted users

        Source file:
        `api-server/src/controllers/retool/v1/get-total-user-count.controller.ts`
        """
        return self._get(
            "/retool/v1/total-user-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=float,
        )

    def get_weekly_message_counts_by_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetWeeklyMessageCountsByUserResponse:
        """
        Get assistant input message counts per user for the last week, sorted by count
        descending

        Source file:
        `api-server/src/controllers/retool/v1/get-weekly-message-counts-by-user.controller.ts`
        """
        return self._get(
            "/retool/v1/weekly-message-counts-by-user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetWeeklyMessageCountsByUserResponse,
        )

    def get_weekly_private_notes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetWeeklyPrivateNotesResponse:
        """
        Get weekly private note counts (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-weekly-private-notes.controller.ts`
        """
        return self._get(
            "/retool/v1/weekly-private-notes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetWeeklyPrivateNotesResponse,
        )

    def get_weekly_public_comments(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetWeeklyPublicCommentsResponse:
        """
        Get weekly public comment counts (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-weekly-public-comments.controller.ts`
        """
        return self._get(
            "/retool/v1/weekly-public-comments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetWeeklyPublicCommentsResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def get_cumulative_users(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetCumulativeUsersResponse:
        """
        Get cumulative user count over time (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-cumulative-users.controller.ts`
        """
        return await self._get(
            "/retool/v1/cumulative-users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetCumulativeUsersResponse,
        )

    async def get_daily_conversations(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetDailyConversationsResponse:
        """
        Get daily conversation counts by variant (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-daily-conversations.controller.ts`
        """
        return await self._get(
            "/retool/v1/daily-conversations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetDailyConversationsResponse,
        )

    async def get_daily_new_accounts(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetDailyNewAccountsResponse:
        """
        Get daily new account counts (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-daily-new-accounts.controller.ts`
        """
        return await self._get(
            "/retool/v1/daily-new-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetDailyNewAccountsResponse,
        )

    async def get_daily_user_chat_messages(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetDailyUserChatMessagesResponse:
        """
        Get daily user chat message counts by variant (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-daily-user-chat-messages.controller.ts`
        """
        return await self._get(
            "/retool/v1/daily-user-chat-messages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetDailyUserChatMessagesResponse,
        )

    async def get_total_comment_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTotalCommentCountResponse:
        """
        Get total count of all comments

        Source file:
        `api-server/src/controllers/retool/v1/get-total-comment-count.controller.ts`
        """
        return await self._get(
            "/retool/v1/total-comment-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=float,
        )

    async def get_total_paper_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTotalPaperCountResponse:
        """
        Get total count of public, non-blocked papers

        Source file:
        `api-server/src/controllers/retool/v1/get-total-paper-count.controller.ts`
        """
        return await self._get(
            "/retool/v1/total-paper-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=float,
        )

    async def get_total_private_notes_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTotalPrivateNotesCountResponse:
        """
        Get total count of private notes (comments with tag=personal)

        Source file:
        `api-server/src/controllers/retool/v1/get-total-private-notes-count.controller.ts`
        """
        return await self._get(
            "/retool/v1/total-private-notes-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=float,
        )

    async def get_total_user_count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetTotalUserCountResponse:
        """
        Get total count of non-deleted users

        Source file:
        `api-server/src/controllers/retool/v1/get-total-user-count.controller.ts`
        """
        return await self._get(
            "/retool/v1/total-user-count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=float,
        )

    async def get_weekly_message_counts_by_user(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetWeeklyMessageCountsByUserResponse:
        """
        Get assistant input message counts per user for the last week, sorted by count
        descending

        Source file:
        `api-server/src/controllers/retool/v1/get-weekly-message-counts-by-user.controller.ts`
        """
        return await self._get(
            "/retool/v1/weekly-message-counts-by-user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetWeeklyMessageCountsByUserResponse,
        )

    async def get_weekly_private_notes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetWeeklyPrivateNotesResponse:
        """
        Get weekly private note counts (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-weekly-private-notes.controller.ts`
        """
        return await self._get(
            "/retool/v1/weekly-private-notes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetWeeklyPrivateNotesResponse,
        )

    async def get_weekly_public_comments(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetWeeklyPublicCommentsResponse:
        """
        Get weekly public comment counts (all time)

        Source file:
        `api-server/src/controllers/retool/v1/get-weekly-public-comments.controller.ts`
        """
        return await self._get(
            "/retool/v1/weekly-public-comments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1GetWeeklyPublicCommentsResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.get_cumulative_users = to_raw_response_wrapper(
            v1.get_cumulative_users,
        )
        self.get_daily_conversations = to_raw_response_wrapper(
            v1.get_daily_conversations,
        )
        self.get_daily_new_accounts = to_raw_response_wrapper(
            v1.get_daily_new_accounts,
        )
        self.get_daily_user_chat_messages = to_raw_response_wrapper(
            v1.get_daily_user_chat_messages,
        )
        self.get_total_comment_count = to_raw_response_wrapper(
            v1.get_total_comment_count,
        )
        self.get_total_paper_count = to_raw_response_wrapper(
            v1.get_total_paper_count,
        )
        self.get_total_private_notes_count = to_raw_response_wrapper(
            v1.get_total_private_notes_count,
        )
        self.get_total_user_count = to_raw_response_wrapper(
            v1.get_total_user_count,
        )
        self.get_weekly_message_counts_by_user = to_raw_response_wrapper(
            v1.get_weekly_message_counts_by_user,
        )
        self.get_weekly_private_notes = to_raw_response_wrapper(
            v1.get_weekly_private_notes,
        )
        self.get_weekly_public_comments = to_raw_response_wrapper(
            v1.get_weekly_public_comments,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.get_cumulative_users = async_to_raw_response_wrapper(
            v1.get_cumulative_users,
        )
        self.get_daily_conversations = async_to_raw_response_wrapper(
            v1.get_daily_conversations,
        )
        self.get_daily_new_accounts = async_to_raw_response_wrapper(
            v1.get_daily_new_accounts,
        )
        self.get_daily_user_chat_messages = async_to_raw_response_wrapper(
            v1.get_daily_user_chat_messages,
        )
        self.get_total_comment_count = async_to_raw_response_wrapper(
            v1.get_total_comment_count,
        )
        self.get_total_paper_count = async_to_raw_response_wrapper(
            v1.get_total_paper_count,
        )
        self.get_total_private_notes_count = async_to_raw_response_wrapper(
            v1.get_total_private_notes_count,
        )
        self.get_total_user_count = async_to_raw_response_wrapper(
            v1.get_total_user_count,
        )
        self.get_weekly_message_counts_by_user = async_to_raw_response_wrapper(
            v1.get_weekly_message_counts_by_user,
        )
        self.get_weekly_private_notes = async_to_raw_response_wrapper(
            v1.get_weekly_private_notes,
        )
        self.get_weekly_public_comments = async_to_raw_response_wrapper(
            v1.get_weekly_public_comments,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.get_cumulative_users = to_streamed_response_wrapper(
            v1.get_cumulative_users,
        )
        self.get_daily_conversations = to_streamed_response_wrapper(
            v1.get_daily_conversations,
        )
        self.get_daily_new_accounts = to_streamed_response_wrapper(
            v1.get_daily_new_accounts,
        )
        self.get_daily_user_chat_messages = to_streamed_response_wrapper(
            v1.get_daily_user_chat_messages,
        )
        self.get_total_comment_count = to_streamed_response_wrapper(
            v1.get_total_comment_count,
        )
        self.get_total_paper_count = to_streamed_response_wrapper(
            v1.get_total_paper_count,
        )
        self.get_total_private_notes_count = to_streamed_response_wrapper(
            v1.get_total_private_notes_count,
        )
        self.get_total_user_count = to_streamed_response_wrapper(
            v1.get_total_user_count,
        )
        self.get_weekly_message_counts_by_user = to_streamed_response_wrapper(
            v1.get_weekly_message_counts_by_user,
        )
        self.get_weekly_private_notes = to_streamed_response_wrapper(
            v1.get_weekly_private_notes,
        )
        self.get_weekly_public_comments = to_streamed_response_wrapper(
            v1.get_weekly_public_comments,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.get_cumulative_users = async_to_streamed_response_wrapper(
            v1.get_cumulative_users,
        )
        self.get_daily_conversations = async_to_streamed_response_wrapper(
            v1.get_daily_conversations,
        )
        self.get_daily_new_accounts = async_to_streamed_response_wrapper(
            v1.get_daily_new_accounts,
        )
        self.get_daily_user_chat_messages = async_to_streamed_response_wrapper(
            v1.get_daily_user_chat_messages,
        )
        self.get_total_comment_count = async_to_streamed_response_wrapper(
            v1.get_total_comment_count,
        )
        self.get_total_paper_count = async_to_streamed_response_wrapper(
            v1.get_total_paper_count,
        )
        self.get_total_private_notes_count = async_to_streamed_response_wrapper(
            v1.get_total_private_notes_count,
        )
        self.get_total_user_count = async_to_streamed_response_wrapper(
            v1.get_total_user_count,
        )
        self.get_weekly_message_counts_by_user = async_to_streamed_response_wrapper(
            v1.get_weekly_message_counts_by_user,
        )
        self.get_weekly_private_notes = async_to_streamed_response_wrapper(
            v1.get_weekly_private_notes,
        )
        self.get_weekly_public_comments = async_to_streamed_response_wrapper(
            v1.get_weekly_public_comments,
        )
