# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.analytics import (
    PaperViewCountKickoffJobResponse,
    PaperViewCountProcessJobResponse,
    PaperViewCountIngestEventResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaperViewCount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_event(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper_view_count = client.analytics.paper_view_count.ingest_event(
                paper_id="paperId",
            )

        assert_matches_type(PaperViewCountIngestEventResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_event_with_all_params(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper_view_count = client.analytics.paper_view_count.ingest_event(
                paper_id="paperId",
                created_at="createdAt",
                user_id="userId",
            )

        assert_matches_type(PaperViewCountIngestEventResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest_event(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.analytics.paper_view_count.with_raw_response.ingest_event(
                paper_id="paperId",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper_view_count = response.parse()
        assert_matches_type(PaperViewCountIngestEventResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest_event(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.analytics.paper_view_count.with_streaming_response.ingest_event(
                paper_id="paperId",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                paper_view_count = response.parse()
                assert_matches_type(PaperViewCountIngestEventResponse, paper_view_count, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_job(self, client: AlphaxivCat) -> None:
        paper_view_count = client.analytics.paper_view_count.kickoff_job(
            type="type",
        )
        assert_matches_type(PaperViewCountKickoffJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_job_with_all_params(self, client: AlphaxivCat) -> None:
        paper_view_count = client.analytics.paper_view_count.kickoff_job(
            type="type",
            like="like",
        )
        assert_matches_type(PaperViewCountKickoffJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_job(self, client: AlphaxivCat) -> None:
        response = client.analytics.paper_view_count.with_raw_response.kickoff_job(
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper_view_count = response.parse()
        assert_matches_type(PaperViewCountKickoffJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_job(self, client: AlphaxivCat) -> None:
        with client.analytics.paper_view_count.with_streaming_response.kickoff_job(
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper_view_count = response.parse()
            assert_matches_type(PaperViewCountKickoffJobResponse, paper_view_count, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_job(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper_view_count = client.analytics.paper_view_count.process_job(
                paper_id="paperId",
                publication_date="publicationDate",
            )

        assert_matches_type(PaperViewCountProcessJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_job_with_all_params(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper_view_count = client.analytics.paper_view_count.process_job(
                paper_id="paperId",
                publication_date="publicationDate",
                like=True,
            )

        assert_matches_type(PaperViewCountProcessJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process_job(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.analytics.paper_view_count.with_raw_response.process_job(
                paper_id="paperId",
                publication_date="publicationDate",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper_view_count = response.parse()
        assert_matches_type(PaperViewCountProcessJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process_job(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.analytics.paper_view_count.with_streaming_response.process_job(
                paper_id="paperId",
                publication_date="publicationDate",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                paper_view_count = response.parse()
                assert_matches_type(PaperViewCountProcessJobResponse, paper_view_count, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaperViewCount:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_event(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper_view_count = await async_client.analytics.paper_view_count.ingest_event(
                paper_id="paperId",
            )

        assert_matches_type(PaperViewCountIngestEventResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_event_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper_view_count = await async_client.analytics.paper_view_count.ingest_event(
                paper_id="paperId",
                created_at="createdAt",
                user_id="userId",
            )

        assert_matches_type(PaperViewCountIngestEventResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest_event(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.analytics.paper_view_count.with_raw_response.ingest_event(
                paper_id="paperId",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper_view_count = await response.parse()
        assert_matches_type(PaperViewCountIngestEventResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest_event(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.analytics.paper_view_count.with_streaming_response.ingest_event(
                paper_id="paperId",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                paper_view_count = await response.parse()
                assert_matches_type(PaperViewCountIngestEventResponse, paper_view_count, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_job(self, async_client: AsyncAlphaxivCat) -> None:
        paper_view_count = await async_client.analytics.paper_view_count.kickoff_job(
            type="type",
        )
        assert_matches_type(PaperViewCountKickoffJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_job_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        paper_view_count = await async_client.analytics.paper_view_count.kickoff_job(
            type="type",
            like="like",
        )
        assert_matches_type(PaperViewCountKickoffJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_job(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.analytics.paper_view_count.with_raw_response.kickoff_job(
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper_view_count = await response.parse()
        assert_matches_type(PaperViewCountKickoffJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_job(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.analytics.paper_view_count.with_streaming_response.kickoff_job(
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper_view_count = await response.parse()
            assert_matches_type(PaperViewCountKickoffJobResponse, paper_view_count, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_job(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper_view_count = await async_client.analytics.paper_view_count.process_job(
                paper_id="paperId",
                publication_date="publicationDate",
            )

        assert_matches_type(PaperViewCountProcessJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_job_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper_view_count = await async_client.analytics.paper_view_count.process_job(
                paper_id="paperId",
                publication_date="publicationDate",
                like=True,
            )

        assert_matches_type(PaperViewCountProcessJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process_job(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.analytics.paper_view_count.with_raw_response.process_job(
                paper_id="paperId",
                publication_date="publicationDate",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper_view_count = await response.parse()
        assert_matches_type(PaperViewCountProcessJobResponse, paper_view_count, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process_job(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.analytics.paper_view_count.with_streaming_response.process_job(
                paper_id="paperId",
                publication_date="publicationDate",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                paper_view_count = await response.parse()
                assert_matches_type(PaperViewCountProcessJobResponse, paper_view_count, path=["response"])

        assert cast(Any, response.is_closed) is True
