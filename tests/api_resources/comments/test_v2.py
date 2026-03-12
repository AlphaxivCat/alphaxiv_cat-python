# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: AlphaxivCat) -> None:
        v2 = client.comments.v2.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AlphaxivCat) -> None:
        response = client.comments.v2.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AlphaxivCat) -> None:
        with client.comments.v2.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            client.comments.v2.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_downvote(self, client: AlphaxivCat) -> None:
        v2 = client.comments.v2.downvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_downvote(self, client: AlphaxivCat) -> None:
        response = client.comments.v2.with_raw_response.downvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_downvote(self, client: AlphaxivCat) -> None:
        with client.comments.v2.with_streaming_response.downvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_downvote(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            client.comments.v2.with_raw_response.downvote(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_flag(self, client: AlphaxivCat) -> None:
        v2 = client.comments.v2.flag(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="reason",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_flag(self, client: AlphaxivCat) -> None:
        response = client.comments.v2.with_raw_response.flag(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="reason",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_flag(self, client: AlphaxivCat) -> None:
        with client.comments.v2.with_streaming_response.flag(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="reason",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_flag(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            client.comments.v2.with_raw_response.flag(
                comment="",
                reason="reason",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle_endorse(self, client: AlphaxivCat) -> None:
        v2 = client.comments.v2.toggle_endorse(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_toggle_endorse(self, client: AlphaxivCat) -> None:
        response = client.comments.v2.with_raw_response.toggle_endorse(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_toggle_endorse(self, client: AlphaxivCat) -> None:
        with client.comments.v2.with_streaming_response.toggle_endorse(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_toggle_endorse(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            client.comments.v2.with_raw_response.toggle_endorse(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upvote(self, client: AlphaxivCat) -> None:
        v2 = client.comments.v2.upvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upvote(self, client: AlphaxivCat) -> None:
        response = client.comments.v2.with_raw_response.upvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upvote(self, client: AlphaxivCat) -> None:
        with client.comments.v2.with_streaming_response.upvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upvote(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            client.comments.v2.with_raw_response.upvote(
                "",
            )


class TestAsyncV2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.comments.v2.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.comments.v2.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.comments.v2.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            await async_client.comments.v2.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_downvote(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.comments.v2.downvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_downvote(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.comments.v2.with_raw_response.downvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_downvote(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.comments.v2.with_streaming_response.downvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_downvote(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            await async_client.comments.v2.with_raw_response.downvote(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_flag(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.comments.v2.flag(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="reason",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_flag(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.comments.v2.with_raw_response.flag(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="reason",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_flag(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.comments.v2.with_streaming_response.flag(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="reason",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_flag(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            await async_client.comments.v2.with_raw_response.flag(
                comment="",
                reason="reason",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle_endorse(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.comments.v2.toggle_endorse(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_toggle_endorse(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.comments.v2.with_raw_response.toggle_endorse(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_toggle_endorse(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.comments.v2.with_streaming_response.toggle_endorse(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_toggle_endorse(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            await async_client.comments.v2.with_raw_response.toggle_endorse(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upvote(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.comments.v2.upvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upvote(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.comments.v2.with_raw_response.upvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upvote(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.comments.v2.with_streaming_response.upvote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upvote(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            await async_client.comments.v2.with_raw_response.upvote(
                "",
            )
