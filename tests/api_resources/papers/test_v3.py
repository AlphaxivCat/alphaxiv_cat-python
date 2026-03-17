# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.papers import (
    V3LikeResponse,
    V3CommentResponse,
    V3RetrieveResponse,
    V3RetrieveAllResponse,
    V3RetrieveFeedResponse,
    V3ImplementationResponse,
    V3RequestPodcastResponse,
    V3RetrieveFiguresResponse,
    V3RetrieveMetricsResponse,
    V3RetrievePreviewResponse,
    V3RetrieveFullTextResponse,
    V3RetrieveGeoTrendsResponse,
    V3RetrieveUnrelatedResponse,
    V3PruneEmbeddingsByDateResponse,
    V3RequestImplementationResponse,
    V3RetrieveDiversePapersResponse,
    V3RetrieveSimilarPapersResponse,
    V3RetrievePapersByCountryResponse,
    V3KickoffThumbnailsTrendingPapersResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV3:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve(
            "unresolved",
        )
        assert_matches_type(V3RetrieveResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve(
            "unresolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve(
            "unresolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unresolved` but received ''"):
            client.papers.v3.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_comment(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag="anonymous",
        )
        assert_matches_type(V3CommentResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_comment_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag="anonymous",
            body="body",
            parent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
        )
        assert_matches_type(V3CommentResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_comment(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag="anonymous",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3CommentResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_comment(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag="anonymous",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3CommentResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_comment(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.papers.v3.with_raw_response.comment(
                version="",
                tag="anonymous",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_votes(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.delete_votes()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_votes_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.delete_votes(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_votes(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.delete_votes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_votes(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.delete_votes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_implementation(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.implementation(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            url="url",
        )
        assert_matches_type(V3ImplementationResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_implementation(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.implementation(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3ImplementationResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_implementation(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.implementation(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3ImplementationResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_implementation(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            client.papers.v3.with_raw_response.implementation(
                paper_group_id="",
                url="url",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_paper_countries(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.kickoff_paper_countries()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_paper_countries_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.kickoff_paper_countries(
            batch=1,
            max_papers=1,
            months=1,
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_paper_countries(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.kickoff_paper_countries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_paper_countries(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.kickoff_paper_countries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_paper_full_text(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.kickoff_paper_full_text()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_paper_full_text_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.kickoff_paper_full_text(
            max_papers=1,
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_paper_full_text(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.kickoff_paper_full_text()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_paper_full_text(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.kickoff_paper_full_text() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_paper_podcasts(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.kickoff_paper_podcasts()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_paper_podcasts(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.kickoff_paper_podcasts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_paper_podcasts(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.kickoff_paper_podcasts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_thumbnails_trending_papers(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.kickoff_thumbnails_trending_papers()
        assert_matches_type(V3KickoffThumbnailsTrendingPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_thumbnails_trending_papers(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.kickoff_thumbnails_trending_papers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3KickoffThumbnailsTrendingPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_thumbnails_trending_papers(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.kickoff_thumbnails_trending_papers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3KickoffThumbnailsTrendingPapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_x_mentions_sync(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.kickoff_x_mentions_sync()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_x_mentions_sync_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.kickoff_x_mentions_sync(
            dry_run=True,
            limit=1,
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_x_mentions_sync(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.kickoff_x_mentions_sync()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_x_mentions_sync(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.kickoff_x_mentions_sync() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_like(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.like(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3LikeResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_like(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.like(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3LikeResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_like(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.like(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3LikeResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_like(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group` but received ''"):
            client.papers.v3.with_raw_response.like(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_podcast(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = client.papers.v3.podcast(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_podcast(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.papers.v3.with_raw_response.podcast(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_podcast(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.papers.v3.with_streaming_response.podcast(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = response.parse()
                assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_podcast(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
                client.papers.v3.with_raw_response.podcast(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_ai(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = client.papers.v3.process_ai(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_ai_with_all_params(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = client.papers.v3.process_ai(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                preferred_language="am",
            )

        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process_ai(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.papers.v3.with_raw_response.process_ai(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process_ai(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.papers.v3.with_streaming_response.process_ai(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = response.parse()
                assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_process_ai(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_version_id` but received ''"):
                client.papers.v3.with_raw_response.process_ai(
                    paper_version_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_countries(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = client.papers.v3.process_countries(
                universal_paper_ids=["string"],
            )

        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process_countries(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.papers.v3.with_raw_response.process_countries(
                universal_paper_ids=["string"],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process_countries(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.papers.v3.with_streaming_response.process_countries(
                universal_paper_ids=["string"],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = response.parse()
                assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_full_text(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = client.papers.v3.process_full_text(
                paper_version_id="paperVersionId",
            )

        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process_full_text(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.papers.v3.with_raw_response.process_full_text(
                paper_version_id="paperVersionId",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process_full_text(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.papers.v3.with_streaming_response.process_full_text(
                paper_version_id="paperVersionId",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = response.parse()
                assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_prune_embeddings_by_date(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = client.papers.v3.prune_embeddings_by_date()

        assert_matches_type(V3PruneEmbeddingsByDateResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_prune_embeddings_by_date(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.papers.v3.with_raw_response.prune_embeddings_by_date()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3PruneEmbeddingsByDateResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_prune_embeddings_by_date(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.papers.v3.with_streaming_response.prune_embeddings_by_date() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = response.parse()
                assert_matches_type(V3PruneEmbeddingsByDateResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_implementation(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.request_implementation(
            group="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_title="paperTitle",
            universal_paper_id="universalPaperId",
        )
        assert_matches_type(V3RequestImplementationResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_implementation_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.request_implementation(
            group="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_title="paperTitle",
            universal_paper_id="universalPaperId",
            additional_info="additionalInfo",
        )
        assert_matches_type(V3RequestImplementationResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_implementation(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.request_implementation(
            group="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_title="paperTitle",
            universal_paper_id="universalPaperId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RequestImplementationResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_implementation(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.request_implementation(
            group="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_title="paperTitle",
            universal_paper_id="universalPaperId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RequestImplementationResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request_implementation(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group` but received ''"):
            client.papers.v3.with_raw_response.request_implementation(
                group="",
                paper_title="paperTitle",
                universal_paper_id="universalPaperId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_podcast(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.request_podcast(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3RequestPodcastResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_podcast(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.request_podcast(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RequestPodcastResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_podcast(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.request_podcast(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RequestPodcastResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request_podcast(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            client.papers.v3.with_raw_response.request_podcast(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_all(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_all()
        assert_matches_type(V3RetrieveAllResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_all_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_all(
            limit="limit",
            skip="skip",
        )
        assert_matches_type(V3RetrieveAllResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_all(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveAllResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_all(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveAllResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_diverse_papers(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_diverse_papers(
            topics="topics",
        )
        assert_matches_type(V3RetrieveDiversePapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_diverse_papers(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_diverse_papers(
            topics="topics",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveDiversePapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_diverse_papers(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_diverse_papers(
            topics="topics",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveDiversePapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_feed(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_feed(
            interval="3 Days",
            page_num="pageNum",
            page_size="pageSize",
            sort="Hot",
        )
        assert_matches_type(V3RetrieveFeedResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_feed_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_feed(
            interval="3 Days",
            page_num="pageNum",
            page_size="pageSize",
            sort="Hot",
            exclude_seen_briefs="true",
            organizations="organizations",
            require_summary="true",
            source="GitHub",
            topics="topics",
            universal_id="universalId",
        )
        assert_matches_type(V3RetrieveFeedResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_feed(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_feed(
            interval="3 Days",
            page_num="pageNum",
            page_size="pageSize",
            sort="Hot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveFeedResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_feed(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_feed(
            interval="3 Days",
            page_num="pageNum",
            page_size="pageSize",
            sort="Hot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveFeedResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_figures(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_figures(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3RetrieveFiguresResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_figures(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_figures(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveFiguresResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_figures(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_figures(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveFiguresResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_figures(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            client.papers.v3.with_raw_response.retrieve_figures(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_full_text(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_full_text(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3RetrieveFullTextResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_full_text(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_full_text(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveFullTextResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_full_text(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_full_text(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveFullTextResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_full_text(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_version` but received ''"):
            client.papers.v3.with_raw_response.retrieve_full_text(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_geo_trends(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_geo_trends()
        assert_matches_type(V3RetrieveGeoTrendsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_geo_trends_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_geo_trends(
            collaboration_limit="collaborationLimit",
            paper_limit="paperLimit",
            past_months="pastMonths",
            repo_limit="repoLimit",
            top_countries="topCountries",
        )
        assert_matches_type(V3RetrieveGeoTrendsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_geo_trends(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_geo_trends()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveGeoTrendsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_geo_trends(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_geo_trends() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveGeoTrendsResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_metrics(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_metrics(
            "unresolved",
        )
        assert_matches_type(V3RetrieveMetricsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_metrics(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_metrics(
            "unresolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveMetricsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_metrics(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_metrics(
            "unresolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveMetricsResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_metrics(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unresolved` but received ''"):
            client.papers.v3.with_raw_response.retrieve_metrics(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_papers_by_country(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_papers_by_country()
        assert_matches_type(V3RetrievePapersByCountryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_papers_by_country_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_papers_by_country(
            country="country",
            limit="limit",
        )
        assert_matches_type(V3RetrievePapersByCountryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_papers_by_country(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_papers_by_country()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrievePapersByCountryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_papers_by_country(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_papers_by_country() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrievePapersByCountryResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_preview(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_preview(
            "id",
        )
        assert_matches_type(V3RetrievePreviewResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_preview(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_preview(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrievePreviewResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_preview(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_preview(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrievePreviewResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_preview(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.papers.v3.with_raw_response.retrieve_preview(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_similar_papers(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_similar_papers(
            id="id",
        )
        assert_matches_type(V3RetrieveSimilarPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_similar_papers_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_similar_papers(
            id="id",
            exclude="exclude",
            exclude_likes="false",
            interval="3 Days",
            limit="limit",
        )
        assert_matches_type(V3RetrieveSimilarPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_similar_papers(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_similar_papers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveSimilarPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_similar_papers(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_similar_papers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveSimilarPapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_similar_papers(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.papers.v3.with_raw_response.retrieve_similar_papers(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_unrelated(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.retrieve_unrelated(
            limit="limit",
            papers="papers",
            topics="topics",
        )
        assert_matches_type(V3RetrieveUnrelatedResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_unrelated(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.retrieve_unrelated(
            limit="limit",
            papers="papers",
            topics="topics",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3RetrieveUnrelatedResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_unrelated(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.retrieve_unrelated(
            limit="limit",
            papers="papers",
            topics="topics",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3RetrieveUnrelatedResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_view(self, client: AlphaxivCat) -> None:
        v3 = client.papers.v3.view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_view(self, client: AlphaxivCat) -> None:
        response = client.papers.v3.with_raw_response.view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_view(self, client: AlphaxivCat) -> None:
        with client.papers.v3.with_streaming_response.view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_view(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group` but received ''"):
            client.papers.v3.with_raw_response.view(
                "",
            )


class TestAsyncV3:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve(
            "unresolved",
        )
        assert_matches_type(V3RetrieveResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve(
            "unresolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve(
            "unresolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unresolved` but received ''"):
            await async_client.papers.v3.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_comment(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag="anonymous",
        )
        assert_matches_type(V3CommentResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_comment_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag="anonymous",
            body="body",
            parent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="title",
        )
        assert_matches_type(V3CommentResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_comment(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag="anonymous",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3CommentResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_comment(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.comment(
            version="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tag="anonymous",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3CommentResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_comment(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.papers.v3.with_raw_response.comment(
                version="",
                tag="anonymous",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_votes(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.delete_votes()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_votes_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.delete_votes(
            body=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_votes(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.delete_votes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_votes(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.delete_votes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_implementation(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.implementation(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            url="url",
        )
        assert_matches_type(V3ImplementationResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_implementation(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.implementation(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3ImplementationResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_implementation(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.implementation(
            paper_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3ImplementationResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_implementation(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            await async_client.papers.v3.with_raw_response.implementation(
                paper_group_id="",
                url="url",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_paper_countries(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.kickoff_paper_countries()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_paper_countries_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.kickoff_paper_countries(
            batch=1,
            max_papers=1,
            months=1,
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_paper_countries(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.kickoff_paper_countries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_paper_countries(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.kickoff_paper_countries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_paper_full_text(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.kickoff_paper_full_text()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_paper_full_text_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.kickoff_paper_full_text(
            max_papers=1,
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_paper_full_text(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.kickoff_paper_full_text()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_paper_full_text(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.kickoff_paper_full_text() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_paper_podcasts(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.kickoff_paper_podcasts()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_paper_podcasts(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.kickoff_paper_podcasts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_paper_podcasts(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.kickoff_paper_podcasts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_thumbnails_trending_papers(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.kickoff_thumbnails_trending_papers()
        assert_matches_type(V3KickoffThumbnailsTrendingPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_thumbnails_trending_papers(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.kickoff_thumbnails_trending_papers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3KickoffThumbnailsTrendingPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_thumbnails_trending_papers(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.kickoff_thumbnails_trending_papers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3KickoffThumbnailsTrendingPapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_x_mentions_sync(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.kickoff_x_mentions_sync()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_x_mentions_sync_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.kickoff_x_mentions_sync(
            dry_run=True,
            limit=1,
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_x_mentions_sync(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.kickoff_x_mentions_sync()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_x_mentions_sync(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.kickoff_x_mentions_sync() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_like(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.like(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3LikeResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_like(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.like(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3LikeResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_like(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.like(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3LikeResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_like(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group` but received ''"):
            await async_client.papers.v3.with_raw_response.like(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_podcast(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = await async_client.papers.v3.podcast(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_podcast(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.papers.v3.with_raw_response.podcast(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_podcast(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.papers.v3.with_streaming_response.podcast(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = await response.parse()
                assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_podcast(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
                await async_client.papers.v3.with_raw_response.podcast(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_ai(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = await async_client.papers.v3.process_ai(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_ai_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = await async_client.papers.v3.process_ai(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                preferred_language="am",
            )

        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process_ai(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.papers.v3.with_raw_response.process_ai(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process_ai(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.papers.v3.with_streaming_response.process_ai(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = await response.parse()
                assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_process_ai(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_version_id` but received ''"):
                await async_client.papers.v3.with_raw_response.process_ai(
                    paper_version_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_countries(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = await async_client.papers.v3.process_countries(
                universal_paper_ids=["string"],
            )

        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process_countries(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.papers.v3.with_raw_response.process_countries(
                universal_paper_ids=["string"],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process_countries(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.papers.v3.with_streaming_response.process_countries(
                universal_paper_ids=["string"],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = await response.parse()
                assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_full_text(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = await async_client.papers.v3.process_full_text(
                paper_version_id="paperVersionId",
            )

        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process_full_text(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.papers.v3.with_raw_response.process_full_text(
                paper_version_id="paperVersionId",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process_full_text(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.papers.v3.with_streaming_response.process_full_text(
                paper_version_id="paperVersionId",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = await response.parse()
                assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_prune_embeddings_by_date(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            v3 = await async_client.papers.v3.prune_embeddings_by_date()

        assert_matches_type(V3PruneEmbeddingsByDateResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_prune_embeddings_by_date(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.papers.v3.with_raw_response.prune_embeddings_by_date()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3PruneEmbeddingsByDateResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_prune_embeddings_by_date(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.papers.v3.with_streaming_response.prune_embeddings_by_date() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                v3 = await response.parse()
                assert_matches_type(V3PruneEmbeddingsByDateResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_implementation(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.request_implementation(
            group="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_title="paperTitle",
            universal_paper_id="universalPaperId",
        )
        assert_matches_type(V3RequestImplementationResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_implementation_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.request_implementation(
            group="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_title="paperTitle",
            universal_paper_id="universalPaperId",
            additional_info="additionalInfo",
        )
        assert_matches_type(V3RequestImplementationResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_implementation(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.request_implementation(
            group="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_title="paperTitle",
            universal_paper_id="universalPaperId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RequestImplementationResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_implementation(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.request_implementation(
            group="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_title="paperTitle",
            universal_paper_id="universalPaperId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RequestImplementationResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request_implementation(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group` but received ''"):
            await async_client.papers.v3.with_raw_response.request_implementation(
                group="",
                paper_title="paperTitle",
                universal_paper_id="universalPaperId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_podcast(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.request_podcast(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3RequestPodcastResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_podcast(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.request_podcast(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RequestPodcastResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_podcast(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.request_podcast(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RequestPodcastResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request_podcast(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            await async_client.papers.v3.with_raw_response.request_podcast(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_all(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_all()
        assert_matches_type(V3RetrieveAllResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_all_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_all(
            limit="limit",
            skip="skip",
        )
        assert_matches_type(V3RetrieveAllResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_all(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveAllResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_all(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveAllResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_diverse_papers(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_diverse_papers(
            topics="topics",
        )
        assert_matches_type(V3RetrieveDiversePapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_diverse_papers(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_diverse_papers(
            topics="topics",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveDiversePapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_diverse_papers(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_diverse_papers(
            topics="topics",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveDiversePapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_feed(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_feed(
            interval="3 Days",
            page_num="pageNum",
            page_size="pageSize",
            sort="Hot",
        )
        assert_matches_type(V3RetrieveFeedResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_feed_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_feed(
            interval="3 Days",
            page_num="pageNum",
            page_size="pageSize",
            sort="Hot",
            exclude_seen_briefs="true",
            organizations="organizations",
            require_summary="true",
            source="GitHub",
            topics="topics",
            universal_id="universalId",
        )
        assert_matches_type(V3RetrieveFeedResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_feed(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_feed(
            interval="3 Days",
            page_num="pageNum",
            page_size="pageSize",
            sort="Hot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveFeedResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_feed(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_feed(
            interval="3 Days",
            page_num="pageNum",
            page_size="pageSize",
            sort="Hot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveFeedResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_figures(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_figures(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3RetrieveFiguresResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_figures(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_figures(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveFiguresResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_figures(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_figures(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveFiguresResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_figures(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_group_id` but received ''"):
            await async_client.papers.v3.with_raw_response.retrieve_figures(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_full_text(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_full_text(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3RetrieveFullTextResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_full_text(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_full_text(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveFullTextResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_full_text(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_full_text(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveFullTextResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_full_text(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_version` but received ''"):
            await async_client.papers.v3.with_raw_response.retrieve_full_text(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_geo_trends(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_geo_trends()
        assert_matches_type(V3RetrieveGeoTrendsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_geo_trends_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_geo_trends(
            collaboration_limit="collaborationLimit",
            paper_limit="paperLimit",
            past_months="pastMonths",
            repo_limit="repoLimit",
            top_countries="topCountries",
        )
        assert_matches_type(V3RetrieveGeoTrendsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_geo_trends(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_geo_trends()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveGeoTrendsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_geo_trends(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_geo_trends() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveGeoTrendsResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_metrics(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_metrics(
            "unresolved",
        )
        assert_matches_type(V3RetrieveMetricsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_metrics(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_metrics(
            "unresolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveMetricsResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_metrics(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_metrics(
            "unresolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveMetricsResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_metrics(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `unresolved` but received ''"):
            await async_client.papers.v3.with_raw_response.retrieve_metrics(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_papers_by_country(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_papers_by_country()
        assert_matches_type(V3RetrievePapersByCountryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_papers_by_country_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_papers_by_country(
            country="country",
            limit="limit",
        )
        assert_matches_type(V3RetrievePapersByCountryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_papers_by_country(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_papers_by_country()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrievePapersByCountryResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_papers_by_country(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_papers_by_country() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrievePapersByCountryResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_preview(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_preview(
            "id",
        )
        assert_matches_type(V3RetrievePreviewResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_preview(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_preview(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrievePreviewResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_preview(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_preview(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrievePreviewResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_preview(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.papers.v3.with_raw_response.retrieve_preview(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_similar_papers(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_similar_papers(
            id="id",
        )
        assert_matches_type(V3RetrieveSimilarPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_similar_papers_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_similar_papers(
            id="id",
            exclude="exclude",
            exclude_likes="false",
            interval="3 Days",
            limit="limit",
        )
        assert_matches_type(V3RetrieveSimilarPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_similar_papers(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_similar_papers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveSimilarPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_similar_papers(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_similar_papers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveSimilarPapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_similar_papers(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.papers.v3.with_raw_response.retrieve_similar_papers(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_unrelated(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.retrieve_unrelated(
            limit="limit",
            papers="papers",
            topics="topics",
        )
        assert_matches_type(V3RetrieveUnrelatedResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_unrelated(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.retrieve_unrelated(
            limit="limit",
            papers="papers",
            topics="topics",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3RetrieveUnrelatedResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_unrelated(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.retrieve_unrelated(
            limit="limit",
            papers="papers",
            topics="topics",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3RetrieveUnrelatedResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_view(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.papers.v3.view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_view(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.v3.with_raw_response.view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_view(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.v3.with_streaming_response.view(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_view(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group` but received ''"):
            await async_client.papers.v3.with_raw_response.view(
                "",
            )
