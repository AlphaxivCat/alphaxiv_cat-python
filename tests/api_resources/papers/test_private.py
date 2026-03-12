# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.papers import PrivateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrivate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: AlphaxivCat) -> None:
        private = client.papers.private.create(
            content_type="x",
            file="x",
            filename="x",
        )
        assert_matches_type(PrivateCreateResponse, private, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: AlphaxivCat) -> None:
        response = client.papers.private.with_raw_response.create(
            content_type="x",
            file="x",
            filename="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        private = response.parse()
        assert_matches_type(PrivateCreateResponse, private, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: AlphaxivCat) -> None:
        with client.papers.private.with_streaming_response.create(
            content_type="x",
            file="x",
            filename="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            private = response.parse()
            assert_matches_type(PrivateCreateResponse, private, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_metadata(self, client: AlphaxivCat) -> None:
        private = client.papers.private.update_metadata(
            paper_id="paperId",
            abstract="abstract",
            authors=[{"name": "x"}],
            bibtex="bibtex",
            categories=["string"],
            publication_date=0,
            title="x",
        )
        assert private is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_metadata(self, client: AlphaxivCat) -> None:
        response = client.papers.private.with_raw_response.update_metadata(
            paper_id="paperId",
            abstract="abstract",
            authors=[{"name": "x"}],
            bibtex="bibtex",
            categories=["string"],
            publication_date=0,
            title="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        private = response.parse()
        assert private is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_metadata(self, client: AlphaxivCat) -> None:
        with client.papers.private.with_streaming_response.update_metadata(
            paper_id="paperId",
            abstract="abstract",
            authors=[{"name": "x"}],
            bibtex="bibtex",
            categories=["string"],
            publication_date=0,
            title="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            private = response.parse()
            assert private is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_metadata(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            client.papers.private.with_raw_response.update_metadata(
                paper_id="",
                abstract="abstract",
                authors=[{"name": "x"}],
                bibtex="bibtex",
                categories=["string"],
                publication_date=0,
                title="x",
            )


class TestAsyncPrivate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAlphaxivCat) -> None:
        private = await async_client.papers.private.create(
            content_type="x",
            file="x",
            filename="x",
        )
        assert_matches_type(PrivateCreateResponse, private, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.private.with_raw_response.create(
            content_type="x",
            file="x",
            filename="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        private = await response.parse()
        assert_matches_type(PrivateCreateResponse, private, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.private.with_streaming_response.create(
            content_type="x",
            file="x",
            filename="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            private = await response.parse()
            assert_matches_type(PrivateCreateResponse, private, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        private = await async_client.papers.private.update_metadata(
            paper_id="paperId",
            abstract="abstract",
            authors=[{"name": "x"}],
            bibtex="bibtex",
            categories=["string"],
            publication_date=0,
            title="x",
        )
        assert private is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.private.with_raw_response.update_metadata(
            paper_id="paperId",
            abstract="abstract",
            authors=[{"name": "x"}],
            bibtex="bibtex",
            categories=["string"],
            publication_date=0,
            title="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        private = await response.parse()
        assert private is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.private.with_streaming_response.update_metadata(
            paper_id="paperId",
            abstract="abstract",
            authors=[{"name": "x"}],
            bibtex="bibtex",
            categories=["string"],
            publication_date=0,
            title="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            private = await response.parse()
            assert private is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            await async_client.papers.private.with_raw_response.update_metadata(
                paper_id="",
                abstract="abstract",
                authors=[{"name": "x"}],
                bibtex="bibtex",
                categories=["string"],
                publication_date=0,
                title="x",
            )
