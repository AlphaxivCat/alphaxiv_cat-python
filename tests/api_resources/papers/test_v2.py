# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.papers import V2CommentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_comment(self, client: AlphaxivCat) -> None:
        v2 = client.papers.v2.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selected_text="selectedText",
            tag="anonymous",
            title="title",
        )
        assert_matches_type(V2CommentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_comment_with_all_params(self, client: AlphaxivCat) -> None:
        v2 = client.papers.v2.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selected_text="selectedText",
            tag="anonymous",
            title="title",
            highlight_color="#26fBC5dF",
        )
        assert_matches_type(V2CommentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_comment(self, client: AlphaxivCat) -> None:
        response = client.papers.v2.with_raw_response.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selected_text="selectedText",
            tag="anonymous",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2CommentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_comment(self, client: AlphaxivCat) -> None:
        with client.papers.v2.with_streaming_response.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selected_text="selectedText",
            tag="anonymous",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2CommentResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_comment(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.papers.v2.with_raw_response.comment(
                version="",
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
                parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                selected_text="selectedText",
                tag="anonymous",
                title="title",
            )


class TestAsyncV2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_comment(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.papers.v2.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selected_text="selectedText",
            tag="anonymous",
            title="title",
        )
        assert_matches_type(V2CommentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_comment_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v2 = await async_client.papers.v2.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selected_text="selectedText",
            tag="anonymous",
            title="title",
            highlight_color="#26fBC5dF",
        )
        assert_matches_type(V2CommentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_comment(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v2.with_raw_response.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selected_text="selectedText",
            tag="anonymous",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert_matches_type(V2CommentResponse, v2, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_comment(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v2.with_streaming_response.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            selected_text="selectedText",
            tag="anonymous",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2CommentResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_comment(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.papers.v2.with_raw_response.comment(
                version="",
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
                parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                selected_text="selectedText",
                tag="anonymous",
                title="title",
            )
