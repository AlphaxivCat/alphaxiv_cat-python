# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.papers.v3 import XMentionUpdateResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestXMentions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            x_mention = client.papers.v3.x_mentions.update(
                paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(XMentionUpdateResponse, x_mention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            x_mention = client.papers.v3.x_mentions.update(
                paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dry_run=True,
            )

        assert_matches_type(XMentionUpdateResponse, x_mention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.papers.v3.x_mentions.with_raw_response.update(
                paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x_mention = response.parse()
        assert_matches_type(XMentionUpdateResponse, x_mention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.papers.v3.x_mentions.with_streaming_response.update(
                paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                x_mention = response.parse()
                assert_matches_type(XMentionUpdateResponse, x_mention, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
                client.papers.v3.x_mentions.with_raw_response.update(
                    paper_group_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: AlphaxivCat) -> None:
        x_mention = client.papers.v3.x_mentions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert x_mention is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.x_mentions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x_mention = response.parse()
        assert x_mention is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AlphaxivCat) -> None:
        with client.papers.v3.x_mentions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x_mention = response.parse()
            assert x_mention is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            client.papers.v3.x_mentions.with_raw_response.delete(
                "",
            )


class TestAsyncXMentions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            x_mention = await async_client.papers.v3.x_mentions.update(
                paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(XMentionUpdateResponse, x_mention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            x_mention = await async_client.papers.v3.x_mentions.update(
                paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dry_run=True,
            )

        assert_matches_type(XMentionUpdateResponse, x_mention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.papers.v3.x_mentions.with_raw_response.update(
                paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x_mention = await response.parse()
        assert_matches_type(XMentionUpdateResponse, x_mention, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.papers.v3.x_mentions.with_streaming_response.update(
                paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                x_mention = await response.parse()
                assert_matches_type(XMentionUpdateResponse, x_mention, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
                await async_client.papers.v3.x_mentions.with_raw_response.update(
                    paper_group_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAlphaxivCat) -> None:
        x_mention = await async_client.papers.v3.x_mentions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert x_mention is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.x_mentions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x_mention = await response.parse()
        assert x_mention is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.x_mentions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x_mention = await response.parse()
            assert x_mention is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            await async_client.papers.v3.x_mentions.with_raw_response.delete(
                "",
            )
