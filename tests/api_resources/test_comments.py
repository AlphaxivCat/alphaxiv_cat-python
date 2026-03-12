# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_edit(self, client: AlphaxivCat) -> None:
        comment = client.comments.edit(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            anchor_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            body="body",
            focus_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            highlight_color="#26fBC5dF",
            highlight_rects=[
                {
                    "page_index": 0,
                    "rects": [
                        {
                            "x1": 0,
                            "x2": 0,
                            "y1": 0,
                            "y2": 0,
                        }
                    ],
                }
            ],
            selected_text="selectedText",
            title="title",
        )
        assert comment is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_edit(self, client: AlphaxivCat) -> None:
        response = client.comments.with_raw_response.edit(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            anchor_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            body="body",
            focus_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            highlight_color="#26fBC5dF",
            highlight_rects=[
                {
                    "page_index": 0,
                    "rects": [
                        {
                            "x1": 0,
                            "x2": 0,
                            "y1": 0,
                            "y2": 0,
                        }
                    ],
                }
            ],
            selected_text="selectedText",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert comment is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_edit(self, client: AlphaxivCat) -> None:
        with client.comments.with_streaming_response.edit(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            anchor_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            body="body",
            focus_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            highlight_color="#26fBC5dF",
            highlight_rects=[
                {
                    "page_index": 0,
                    "rects": [
                        {
                            "x1": 0,
                            "x2": 0,
                            "y1": 0,
                            "y2": 0,
                        }
                    ],
                }
            ],
            selected_text="selectedText",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert comment is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_edit(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            client.comments.with_raw_response.edit(
                comment="",
                anchor_position={
                    "offset": 0,
                    "page_index": 0,
                    "span_index": 0,
                },
                body="body",
                focus_position={
                    "offset": 0,
                    "page_index": 0,
                    "span_index": 0,
                },
                highlight_color="#26fBC5dF",
                highlight_rects=[
                    {
                        "page_index": 0,
                        "rects": [
                            {
                                "x1": 0,
                                "x2": 0,
                                "y1": 0,
                                "y2": 0,
                            }
                        ],
                    }
                ],
                selected_text="selectedText",
                title="title",
            )


class TestAsyncComments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_edit(self, async_client: AsyncAlphaxivCat) -> None:
        comment = await async_client.comments.edit(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            anchor_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            body="body",
            focus_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            highlight_color="#26fBC5dF",
            highlight_rects=[
                {
                    "page_index": 0,
                    "rects": [
                        {
                            "x1": 0,
                            "x2": 0,
                            "y1": 0,
                            "y2": 0,
                        }
                    ],
                }
            ],
            selected_text="selectedText",
            title="title",
        )
        assert comment is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.comments.with_raw_response.edit(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            anchor_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            body="body",
            focus_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            highlight_color="#26fBC5dF",
            highlight_rects=[
                {
                    "page_index": 0,
                    "rects": [
                        {
                            "x1": 0,
                            "x2": 0,
                            "y1": 0,
                            "y2": 0,
                        }
                    ],
                }
            ],
            selected_text="selectedText",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert comment is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.comments.with_streaming_response.edit(
            comment="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            anchor_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            body="body",
            focus_position={
                "offset": 0,
                "page_index": 0,
                "span_index": 0,
            },
            highlight_color="#26fBC5dF",
            highlight_rects=[
                {
                    "page_index": 0,
                    "rects": [
                        {
                            "x1": 0,
                            "x2": 0,
                            "y1": 0,
                            "y2": 0,
                        }
                    ],
                }
            ],
            selected_text="selectedText",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert comment is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment` but received ''"):
            await async_client.comments.with_raw_response.edit(
                comment="",
                anchor_position={
                    "offset": 0,
                    "page_index": 0,
                    "span_index": 0,
                },
                body="body",
                focus_position={
                    "offset": 0,
                    "page_index": 0,
                    "span_index": 0,
                },
                highlight_color="#26fBC5dF",
                highlight_rects=[
                    {
                        "page_index": 0,
                        "rects": [
                            {
                                "x1": 0,
                                "x2": 0,
                                "y1": 0,
                                "y2": 0,
                            }
                        ],
                    }
                ],
                selected_text="selectedText",
                title="title",
            )
