# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.users import (
    V3SearchResponse,
    V3GetActivityResponse,
    V3GetFollowersResponse,
    V3UploadAvatarResponse,
    V3GetUserByUuidResponse,
    V3UpdateProfileResponse,
    V3GetCurrentUserResponse,
    V3GetLeaderboardResponse,
    V3GetClaimedPapersResponse,
    V3GetViewedHistoryResponse,
    V3ToggleFollowUserResponse,
    V3UpdatePreferencesResponse,
    V3AutocompleteProfileResponse,
    V3GetFeaturedActivityResponse,
    V3ProcessNotificationEmailResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV3:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete_profile(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.autocomplete_profile(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3AutocompleteProfileResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_autocomplete_profile(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.autocomplete_profile(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3AutocompleteProfileResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_autocomplete_profile(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.autocomplete_profile(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3AutocompleteProfileResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_banner(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.delete_banner(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_banner(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.delete_banner(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_banner(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.delete_banner(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_banner(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `banner_id` but received ''"):
            client.users.v3.with_raw_response.delete_banner(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_own_user(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.delete_own_user()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_own_user(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.delete_own_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_own_user(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.delete_own_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_activity(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_activity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3GetActivityResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_activity_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_activity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort="date",
        )
        assert_matches_type(V3GetActivityResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_activity(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.get_activity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3GetActivityResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_activity(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.get_activity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3GetActivityResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_activity(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.v3.with_raw_response.get_activity(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_claimed_papers(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_claimed_papers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3GetClaimedPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_claimed_papers_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_claimed_papers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort="date",
        )
        assert_matches_type(V3GetClaimedPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_claimed_papers(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.get_claimed_papers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3GetClaimedPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_claimed_papers(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.get_claimed_papers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3GetClaimedPapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_claimed_papers(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.v3.with_raw_response.get_claimed_papers(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_current_user(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_current_user()
        assert_matches_type(V3GetCurrentUserResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_current_user(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.get_current_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3GetCurrentUserResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_current_user(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.get_current_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3GetCurrentUserResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_featured_activity(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_featured_activity(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3GetFeaturedActivityResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_featured_activity(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.get_featured_activity(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3GetFeaturedActivityResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_featured_activity(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.get_featured_activity(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3GetFeaturedActivityResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_featured_activity(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.v3.with_raw_response.get_featured_activity(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_followers(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_followers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3GetFollowersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_followers(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.get_followers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3GetFollowersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_followers(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.get_followers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3GetFollowersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_followers(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.v3.with_raw_response.get_followers(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_leaderboard(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_leaderboard()
        assert_matches_type(V3GetLeaderboardResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_leaderboard(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.get_leaderboard()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3GetLeaderboardResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_leaderboard(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.get_leaderboard() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3GetLeaderboardResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_user_by_uuid(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_user_by_uuid(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3GetUserByUuidResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_user_by_uuid(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.get_user_by_uuid(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3GetUserByUuidResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_user_by_uuid(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.get_user_by_uuid(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3GetUserByUuidResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_user_by_uuid(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.v3.with_raw_response.get_user_by_uuid(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_viewed_history(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_viewed_history()
        assert_matches_type(V3GetViewedHistoryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_viewed_history_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.get_viewed_history(
            offset="offset",
            search="search",
        )
        assert_matches_type(V3GetViewedHistoryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_viewed_history(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.get_viewed_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3GetViewedHistoryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_viewed_history(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.get_viewed_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3GetViewedHistoryResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_notification_email(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = client.users.v3.process_notification_email(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(V3ProcessNotificationEmailResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process_notification_email(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.users.v3.with_raw_response.process_notification_email(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3ProcessNotificationEmailResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process_notification_email(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.users.v3.with_streaming_response.process_notification_email(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = response.parse()
                assert_matches_type(V3ProcessNotificationEmailResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_process_notification_email(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                client.users.v3.with_raw_response.process_notification_email(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.search(
            q="x",
        )
        assert_matches_type(V3SearchResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.search(
            q="x",
            limit="limit",
        )
        assert_matches_type(V3SearchResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.search(
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3SearchResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.search(
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3SearchResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle_follow_user(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.toggle_follow_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3ToggleFollowUserResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_toggle_follow_user(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.toggle_follow_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3ToggleFollowUserResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_toggle_follow_user(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.toggle_follow_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3ToggleFollowUserResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_toggle_follow_user(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.v3.with_raw_response.toggle_follow_user(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_preferences(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.update_preferences()
        assert_matches_type(V3UpdatePreferencesResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_preferences_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.update_preferences(
            banners=[
                {
                    "link": "link",
                    "name": "name",
                    "type": "success",
                }
            ],
            base={
                "assistant_custom_styles": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "instructions": "x",
                        "name": "x",
                    }
                ],
                "assistant_style_selection": "default",
                "default_private_paper_sidebar_tab": "assistant",
                "default_public_paper_sidebar_tab": "comments",
                "feed_sort": "Hot",
                "is_dark_mode_enabled": True,
                "is_debug_mode_enabled": True,
                "is_members_sidebar_visible": True,
                "preferred_language": "am",
                "preferred_llm_model": "preferredLlmModel",
                "reading_mode_enabled": True,
                "show_model_thinking": True,
                "tooling_pane_width": 0,
                "web_search": "off",
            },
        )
        assert_matches_type(V3UpdatePreferencesResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_preferences(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.update_preferences()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3UpdatePreferencesResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_preferences(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.update_preferences() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3UpdatePreferencesResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_profile(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.update_profile()
        assert_matches_type(V3UpdateProfileResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_profile_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.update_profile(
            biography="biography",
            bluesky_username="blueskyUsername",
            github_username="githubUsername",
            institution="institution",
            linkedin_username="linkedinUsername",
            location="location",
            public_email="dev@stainless.com",
            real_name="x",
            username="username",
            x_username="xUsername",
        )
        assert_matches_type(V3UpdateProfileResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_profile(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.update_profile()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3UpdateProfileResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_profile(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.update_profile() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3UpdateProfileResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_avatar(self, client: AlphaxivCat) -> None:
        v3 = client.users.v3.upload_avatar()
        assert_matches_type(Optional[V3UploadAvatarResponse], v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload_avatar(self, client: AlphaxivCat) -> None:
        response = client.users.v3.with_raw_response.upload_avatar()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(Optional[V3UploadAvatarResponse], v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload_avatar(self, client: AlphaxivCat) -> None:
        with client.users.v3.with_streaming_response.upload_avatar() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(Optional[V3UploadAvatarResponse], v3, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV3:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete_profile(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.autocomplete_profile(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3AutocompleteProfileResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_autocomplete_profile(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.autocomplete_profile(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3AutocompleteProfileResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_autocomplete_profile(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.autocomplete_profile(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3AutocompleteProfileResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_banner(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.delete_banner(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_banner(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.delete_banner(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_banner(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.delete_banner(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_banner(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `banner_id` but received ''"):
            await async_client.users.v3.with_raw_response.delete_banner(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_own_user(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.delete_own_user()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_own_user(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.delete_own_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_own_user(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.delete_own_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_activity(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_activity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3GetActivityResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_activity_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_activity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort="date",
        )
        assert_matches_type(V3GetActivityResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_activity(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.get_activity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3GetActivityResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_activity(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.get_activity(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3GetActivityResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_activity(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.v3.with_raw_response.get_activity(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_claimed_papers(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_claimed_papers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3GetClaimedPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_claimed_papers_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_claimed_papers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort="date",
        )
        assert_matches_type(V3GetClaimedPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_claimed_papers(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.get_claimed_papers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3GetClaimedPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_claimed_papers(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.get_claimed_papers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3GetClaimedPapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_claimed_papers(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.v3.with_raw_response.get_claimed_papers(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_current_user(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_current_user()
        assert_matches_type(V3GetCurrentUserResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_current_user(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.get_current_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3GetCurrentUserResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_current_user(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.get_current_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3GetCurrentUserResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_featured_activity(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_featured_activity(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3GetFeaturedActivityResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_featured_activity(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.get_featured_activity(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3GetFeaturedActivityResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_featured_activity(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.get_featured_activity(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3GetFeaturedActivityResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_featured_activity(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.v3.with_raw_response.get_featured_activity(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_followers(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_followers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3GetFollowersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_followers(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.get_followers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3GetFollowersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_followers(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.get_followers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3GetFollowersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_followers(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.v3.with_raw_response.get_followers(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_leaderboard(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_leaderboard()
        assert_matches_type(V3GetLeaderboardResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_leaderboard(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.get_leaderboard()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3GetLeaderboardResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_leaderboard(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.get_leaderboard() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3GetLeaderboardResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_user_by_uuid(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_user_by_uuid(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3GetUserByUuidResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_user_by_uuid(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.get_user_by_uuid(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3GetUserByUuidResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_user_by_uuid(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.get_user_by_uuid(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3GetUserByUuidResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_user_by_uuid(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.v3.with_raw_response.get_user_by_uuid(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_viewed_history(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_viewed_history()
        assert_matches_type(V3GetViewedHistoryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_viewed_history_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.get_viewed_history(
            offset="offset",
            search="search",
        )
        assert_matches_type(V3GetViewedHistoryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_viewed_history(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.get_viewed_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3GetViewedHistoryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_viewed_history(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.get_viewed_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3GetViewedHistoryResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_notification_email(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = await async_client.users.v3.process_notification_email(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(V3ProcessNotificationEmailResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process_notification_email(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.users.v3.with_raw_response.process_notification_email(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3ProcessNotificationEmailResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process_notification_email(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.users.v3.with_streaming_response.process_notification_email(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = await response.parse()
                assert_matches_type(V3ProcessNotificationEmailResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_process_notification_email(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                await async_client.users.v3.with_raw_response.process_notification_email(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.search(
            q="x",
        )
        assert_matches_type(V3SearchResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.search(
            q="x",
            limit="limit",
        )
        assert_matches_type(V3SearchResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.search(
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3SearchResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.search(
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3SearchResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle_follow_user(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.toggle_follow_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3ToggleFollowUserResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_toggle_follow_user(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.toggle_follow_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3ToggleFollowUserResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_toggle_follow_user(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.toggle_follow_user(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3ToggleFollowUserResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_toggle_follow_user(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.v3.with_raw_response.toggle_follow_user(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_preferences(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.update_preferences()
        assert_matches_type(V3UpdatePreferencesResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_preferences_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.update_preferences(
            banners=[
                {
                    "link": "link",
                    "name": "name",
                    "type": "success",
                }
            ],
            base={
                "assistant_custom_styles": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "instructions": "x",
                        "name": "x",
                    }
                ],
                "assistant_style_selection": "default",
                "default_private_paper_sidebar_tab": "assistant",
                "default_public_paper_sidebar_tab": "comments",
                "feed_sort": "Hot",
                "is_dark_mode_enabled": True,
                "is_debug_mode_enabled": True,
                "is_members_sidebar_visible": True,
                "preferred_language": "am",
                "preferred_llm_model": "preferredLlmModel",
                "reading_mode_enabled": True,
                "show_model_thinking": True,
                "tooling_pane_width": 0,
                "web_search": "off",
            },
        )
        assert_matches_type(V3UpdatePreferencesResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_preferences(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.update_preferences()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3UpdatePreferencesResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_preferences(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.update_preferences() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3UpdatePreferencesResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_profile(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.update_profile()
        assert_matches_type(V3UpdateProfileResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_profile_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.update_profile(
            biography="biography",
            bluesky_username="blueskyUsername",
            github_username="githubUsername",
            institution="institution",
            linkedin_username="linkedinUsername",
            location="location",
            public_email="dev@stainless.com",
            real_name="x",
            username="username",
            x_username="xUsername",
        )
        assert_matches_type(V3UpdateProfileResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_profile(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.update_profile()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3UpdateProfileResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_profile(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.update_profile() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3UpdateProfileResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_avatar(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.users.v3.upload_avatar()
        assert_matches_type(Optional[V3UploadAvatarResponse], v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload_avatar(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.users.v3.with_raw_response.upload_avatar()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(Optional[V3UploadAvatarResponse], v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload_avatar(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.users.v3.with_streaming_response.upload_avatar() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(Optional[V3UploadAvatarResponse], v3, path=["response"])

        assert cast(Any, response.is_closed) is True
