# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.papers import (
    KickoffDailyGitHubStarUpdateResponse,
    KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKickoffDailyGitHubStars:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: AlphaxivCat) -> None:
        kickoff_daily_github_star = client.papers.kickoff_daily_github_stars.update(
            "max",
        )
        assert_matches_type(KickoffDailyGitHubStarUpdateResponse, kickoff_daily_github_star, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: AlphaxivCat) -> None:
        response = client.papers.kickoff_daily_github_stars.with_raw_response.update(
            "max",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kickoff_daily_github_star = response.parse()
        assert_matches_type(KickoffDailyGitHubStarUpdateResponse, kickoff_daily_github_star, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: AlphaxivCat) -> None:
        with client.papers.kickoff_daily_github_stars.with_streaming_response.update(
            "max",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kickoff_daily_github_star = response.parse()
            assert_matches_type(KickoffDailyGitHubStarUpdateResponse, kickoff_daily_github_star, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `max` but received ''"):
            client.papers.kickoff_daily_github_stars.with_raw_response.update(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_daily_github_stars(self, client: AlphaxivCat) -> None:
        kickoff_daily_github_star = client.papers.kickoff_daily_github_stars.kickoff_daily_github_stars()
        assert_matches_type(
            KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse, kickoff_daily_github_star, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_daily_github_stars(self, client: AlphaxivCat) -> None:
        response = client.papers.kickoff_daily_github_stars.with_raw_response.kickoff_daily_github_stars()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kickoff_daily_github_star = response.parse()
        assert_matches_type(
            KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse, kickoff_daily_github_star, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_daily_github_stars(self, client: AlphaxivCat) -> None:
        with client.papers.kickoff_daily_github_stars.with_streaming_response.kickoff_daily_github_stars() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kickoff_daily_github_star = response.parse()
            assert_matches_type(
                KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse, kickoff_daily_github_star, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncKickoffDailyGitHubStars:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAlphaxivCat) -> None:
        kickoff_daily_github_star = await async_client.papers.kickoff_daily_github_stars.update(
            "max",
        )
        assert_matches_type(KickoffDailyGitHubStarUpdateResponse, kickoff_daily_github_star, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.kickoff_daily_github_stars.with_raw_response.update(
            "max",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kickoff_daily_github_star = await response.parse()
        assert_matches_type(KickoffDailyGitHubStarUpdateResponse, kickoff_daily_github_star, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.kickoff_daily_github_stars.with_streaming_response.update(
            "max",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kickoff_daily_github_star = await response.parse()
            assert_matches_type(KickoffDailyGitHubStarUpdateResponse, kickoff_daily_github_star, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `max` but received ''"):
            await async_client.papers.kickoff_daily_github_stars.with_raw_response.update(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_daily_github_stars(self, async_client: AsyncAlphaxivCat) -> None:
        kickoff_daily_github_star = await async_client.papers.kickoff_daily_github_stars.kickoff_daily_github_stars()
        assert_matches_type(
            KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse, kickoff_daily_github_star, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_daily_github_stars(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.kickoff_daily_github_stars.with_raw_response.kickoff_daily_github_stars()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kickoff_daily_github_star = await response.parse()
        assert_matches_type(
            KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse, kickoff_daily_github_star, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_daily_github_stars(self, async_client: AsyncAlphaxivCat) -> None:
        async with (
            async_client.papers.kickoff_daily_github_stars.with_streaming_response.kickoff_daily_github_stars()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kickoff_daily_github_star = await response.parse()
            assert_matches_type(
                KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse, kickoff_daily_github_star, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
