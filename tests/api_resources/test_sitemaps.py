# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types import (
    SitemapListUsersResponse,
    SitemapListPapersResponse,
    SitemapListOverviewsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSitemaps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_overviews(self, client: AlphaxivCat) -> None:
        sitemap = client.sitemaps.list_overviews()
        assert_matches_type(SitemapListOverviewsResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_overviews_with_all_params(self, client: AlphaxivCat) -> None:
        sitemap = client.sitemaps.list_overviews(
            limit="limit",
            page="page",
        )
        assert_matches_type(SitemapListOverviewsResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_overviews(self, client: AlphaxivCat) -> None:
        response = client.sitemaps.with_raw_response.list_overviews()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitemap = response.parse()
        assert_matches_type(SitemapListOverviewsResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_overviews(self, client: AlphaxivCat) -> None:
        with client.sitemaps.with_streaming_response.list_overviews() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitemap = response.parse()
            assert_matches_type(SitemapListOverviewsResponse, sitemap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_papers(self, client: AlphaxivCat) -> None:
        sitemap = client.sitemaps.list_papers()
        assert_matches_type(SitemapListPapersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_papers_with_all_params(self, client: AlphaxivCat) -> None:
        sitemap = client.sitemaps.list_papers(
            limit="limit",
            page="page",
        )
        assert_matches_type(SitemapListPapersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_papers(self, client: AlphaxivCat) -> None:
        response = client.sitemaps.with_raw_response.list_papers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitemap = response.parse()
        assert_matches_type(SitemapListPapersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_papers(self, client: AlphaxivCat) -> None:
        with client.sitemaps.with_streaming_response.list_papers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitemap = response.parse()
            assert_matches_type(SitemapListPapersResponse, sitemap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_users(self, client: AlphaxivCat) -> None:
        sitemap = client.sitemaps.list_users()
        assert_matches_type(SitemapListUsersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_users_with_all_params(self, client: AlphaxivCat) -> None:
        sitemap = client.sitemaps.list_users(
            limit="limit",
            page="page",
        )
        assert_matches_type(SitemapListUsersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_users(self, client: AlphaxivCat) -> None:
        response = client.sitemaps.with_raw_response.list_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitemap = response.parse()
        assert_matches_type(SitemapListUsersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_users(self, client: AlphaxivCat) -> None:
        with client.sitemaps.with_streaming_response.list_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitemap = response.parse()
            assert_matches_type(SitemapListUsersResponse, sitemap, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSitemaps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_overviews(self, async_client: AsyncAlphaxivCat) -> None:
        sitemap = await async_client.sitemaps.list_overviews()
        assert_matches_type(SitemapListOverviewsResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_overviews_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        sitemap = await async_client.sitemaps.list_overviews(
            limit="limit",
            page="page",
        )
        assert_matches_type(SitemapListOverviewsResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_overviews(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.sitemaps.with_raw_response.list_overviews()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitemap = await response.parse()
        assert_matches_type(SitemapListOverviewsResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_overviews(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.sitemaps.with_streaming_response.list_overviews() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitemap = await response.parse()
            assert_matches_type(SitemapListOverviewsResponse, sitemap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_papers(self, async_client: AsyncAlphaxivCat) -> None:
        sitemap = await async_client.sitemaps.list_papers()
        assert_matches_type(SitemapListPapersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_papers_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        sitemap = await async_client.sitemaps.list_papers(
            limit="limit",
            page="page",
        )
        assert_matches_type(SitemapListPapersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_papers(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.sitemaps.with_raw_response.list_papers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitemap = await response.parse()
        assert_matches_type(SitemapListPapersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_papers(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.sitemaps.with_streaming_response.list_papers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitemap = await response.parse()
            assert_matches_type(SitemapListPapersResponse, sitemap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_users(self, async_client: AsyncAlphaxivCat) -> None:
        sitemap = await async_client.sitemaps.list_users()
        assert_matches_type(SitemapListUsersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_users_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        sitemap = await async_client.sitemaps.list_users(
            limit="limit",
            page="page",
        )
        assert_matches_type(SitemapListUsersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_users(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.sitemaps.with_raw_response.list_users()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sitemap = await response.parse()
        assert_matches_type(SitemapListUsersResponse, sitemap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_users(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.sitemaps.with_streaming_response.list_users() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sitemap = await response.parse()
            assert_matches_type(SitemapListUsersResponse, sitemap, path=["response"])

        assert cast(Any, response.is_closed) is True
