# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.comments.v2 import (
    ModeratorToggleFlagsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModerator:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_feedback(self, client: AlphaxivCat) -> None:
        moderator = client.comments.v2.moderator.send_feedback(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
        )
        assert moderator is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_feedback(self, client: AlphaxivCat) -> None:
        response = client.comments.v2.moderator.with_raw_response.send_feedback(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderator = response.parse()
        assert moderator is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_feedback(self, client: AlphaxivCat) -> None:
        with client.comments.v2.moderator.with_streaming_response.send_feedback(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderator = response.parse()
            assert moderator is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send_feedback(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            client.comments.v2.moderator.with_raw_response.send_feedback(
                comment="",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle_flags(self, client: AlphaxivCat) -> None:
        moderator = client.comments.v2.moderator.toggle_flags(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ModeratorToggleFlagsResponse, moderator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle_flags_with_all_params(self, client: AlphaxivCat) -> None:
        moderator = client.comments.v2.moderator.toggle_flags(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            addressed=True,
            closed=True,
            flag_addressed=True,
        )
        assert_matches_type(ModeratorToggleFlagsResponse, moderator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_toggle_flags(self, client: AlphaxivCat) -> None:
        response = client.comments.v2.moderator.with_raw_response.toggle_flags(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderator = response.parse()
        assert_matches_type(ModeratorToggleFlagsResponse, moderator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_toggle_flags(self, client: AlphaxivCat) -> None:
        with client.comments.v2.moderator.with_streaming_response.toggle_flags(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderator = response.parse()
            assert_matches_type(ModeratorToggleFlagsResponse, moderator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_toggle_flags(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            client.comments.v2.moderator.with_raw_response.toggle_flags(
                comment="",
            )


class TestAsyncModerator:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_feedback(self, async_client: AsyncAlphaxivCat) -> None:
        moderator = await async_client.comments.v2.moderator.send_feedback(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
        )
        assert moderator is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_feedback(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.comments.v2.moderator.with_raw_response.send_feedback(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderator = await response.parse()
        assert moderator is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_feedback(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.comments.v2.moderator.with_streaming_response.send_feedback(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderator = await response.parse()
            assert moderator is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send_feedback(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            await async_client.comments.v2.moderator.with_raw_response.send_feedback(
                comment="",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle_flags(self, async_client: AsyncAlphaxivCat) -> None:
        moderator = await async_client.comments.v2.moderator.toggle_flags(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ModeratorToggleFlagsResponse, moderator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle_flags_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        moderator = await async_client.comments.v2.moderator.toggle_flags(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            addressed=True,
            closed=True,
            flag_addressed=True,
        )
        assert_matches_type(ModeratorToggleFlagsResponse, moderator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_toggle_flags(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.comments.v2.moderator.with_raw_response.toggle_flags(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderator = await response.parse()
        assert_matches_type(ModeratorToggleFlagsResponse, moderator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_toggle_flags(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.comments.v2.moderator.with_streaming_response.toggle_flags(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderator = await response.parse()
            assert_matches_type(ModeratorToggleFlagsResponse, moderator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_toggle_flags(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            await async_client.comments.v2.moderator.with_raw_response.toggle_flags(
                comment="",
            )
