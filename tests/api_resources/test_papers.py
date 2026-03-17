# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types import (
    PaperVoteResponse,
    PaperUnclaimResponse,
    PaperAddAuthorResponse,
    PaperAdminVoteResponse,
    PaperCrxPdfHitResponse,
    PaperKickoffAIResponse,
    PaperCrxPdfClickResponse,
    PaperEmailAuthorResponse,
    PaperGetPaperInfoResponse,
    PaperToggleFollowResponse,
    PaperKickoffBibtexResponse,
    PaperKickoffGitHubResponse,
    PaperCrxAbstractHitResponse,
    PaperGetCrxPaperInfoResponse,
    PaperProcessMetadataResponse,
    PaperRequestAILatestResponse,
    PaperCrxAbstractClickResponse,
    PaperKickoffRecentPapersResponse,
    PaperSetGitHubRepositoryResponse,
    PaperTranslateAIOverviewResponse,
    PaperKickoffAbstractEmbedResponse,
    PaperProcessAbstractEmbedResponse,
    PaperKickoffPaperCategorizationResponse,
    PaperRequestAITranslationLatestResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPapers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_author(self, client: AlphaxivCat) -> None:
        paper = client.papers.add_author(
            paper_id="x",
            author_email="dev@stainless.com",
        )
        assert_matches_type(PaperAddAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_author_with_all_params(self, client: AlphaxivCat) -> None:
        paper = client.papers.add_author(
            paper_id="x",
            author_email="dev@stainless.com",
            should_email=True,
        )
        assert_matches_type(PaperAddAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_author(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.add_author(
            paper_id="x",
            author_email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperAddAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_author(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.add_author(
            paper_id="x",
            author_email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperAddAuthorResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_author(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            client.papers.with_raw_response.add_author(
                paper_id="",
                author_email="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_admin_vote(self, client: AlphaxivCat) -> None:
        paper = client.papers.admin_vote(
            paper_id="x",
            entry=0,
        )
        assert_matches_type(PaperAdminVoteResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_admin_vote(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.admin_vote(
            paper_id="x",
            entry=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperAdminVoteResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_admin_vote(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.admin_vote(
            paper_id="x",
            entry=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperAdminVoteResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_admin_vote(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            client.papers.with_raw_response.admin_vote(
                paper_id="",
                entry=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_crx_abstract_click(self, client: AlphaxivCat) -> None:
        paper = client.papers.crx_abstract_click(
            ref="ref",
            pid="pid",
        )
        assert_matches_type(PaperCrxAbstractClickResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_crx_abstract_click(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.crx_abstract_click(
            ref="ref",
            pid="pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperCrxAbstractClickResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_crx_abstract_click(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.crx_abstract_click(
            ref="ref",
            pid="pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperCrxAbstractClickResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_crx_abstract_click(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            client.papers.with_raw_response.crx_abstract_click(
                ref="ref",
                pid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ref` but received ''"):
            client.papers.with_raw_response.crx_abstract_click(
                ref="",
                pid="pid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_crx_abstract_hit(self, client: AlphaxivCat) -> None:
        paper = client.papers.crx_abstract_hit(
            "pid",
        )
        assert_matches_type(PaperCrxAbstractHitResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_crx_abstract_hit(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.crx_abstract_hit(
            "pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperCrxAbstractHitResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_crx_abstract_hit(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.crx_abstract_hit(
            "pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperCrxAbstractHitResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_crx_abstract_hit(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            client.papers.with_raw_response.crx_abstract_hit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_crx_pdf_click(self, client: AlphaxivCat) -> None:
        paper = client.papers.crx_pdf_click(
            ref="ref",
            pid="pid",
        )
        assert_matches_type(PaperCrxPdfClickResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_crx_pdf_click(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.crx_pdf_click(
            ref="ref",
            pid="pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperCrxPdfClickResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_crx_pdf_click(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.crx_pdf_click(
            ref="ref",
            pid="pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperCrxPdfClickResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_crx_pdf_click(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            client.papers.with_raw_response.crx_pdf_click(
                ref="ref",
                pid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ref` but received ''"):
            client.papers.with_raw_response.crx_pdf_click(
                ref="",
                pid="pid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_crx_pdf_hit(self, client: AlphaxivCat) -> None:
        paper = client.papers.crx_pdf_hit(
            "pid",
        )
        assert_matches_type(PaperCrxPdfHitResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_crx_pdf_hit(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.crx_pdf_hit(
            "pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperCrxPdfHitResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_crx_pdf_hit(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.crx_pdf_hit(
            "pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperCrxPdfHitResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_crx_pdf_hit(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            client.papers.with_raw_response.crx_pdf_hit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_email_author(self, client: AlphaxivCat) -> None:
        paper = client.papers.email_author(
            paper_id="x",
            author_individual_email="dev@stainless.com",
            email_author_name="emailAuthorName",
            paper_name="paperName",
            type="comment",
        )
        assert_matches_type(PaperEmailAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_email_author_with_all_params(self, client: AlphaxivCat) -> None:
        paper = client.papers.email_author(
            paper_id="x",
            author_individual_email="dev@stainless.com",
            email_author_name="emailAuthorName",
            paper_name="paperName",
            type="comment",
            ignore_duplicate_error=True,
        )
        assert_matches_type(PaperEmailAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_email_author(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.email_author(
            paper_id="x",
            author_individual_email="dev@stainless.com",
            email_author_name="emailAuthorName",
            paper_name="paperName",
            type="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperEmailAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_email_author(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.email_author(
            paper_id="x",
            author_individual_email="dev@stainless.com",
            email_author_name="emailAuthorName",
            paper_name="paperName",
            type="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperEmailAuthorResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_email_author(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            client.papers.with_raw_response.email_author(
                paper_id="",
                author_individual_email="dev@stainless.com",
                email_author_name="emailAuthorName",
                paper_name="paperName",
                type="comment",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_crx_paper_info(self, client: AlphaxivCat) -> None:
        paper = client.papers.get_crx_paper_info(
            "pid",
        )
        assert_matches_type(PaperGetCrxPaperInfoResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_crx_paper_info(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.get_crx_paper_info(
            "pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperGetCrxPaperInfoResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_crx_paper_info(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.get_crx_paper_info(
            "pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperGetCrxPaperInfoResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_crx_paper_info(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            client.papers.with_raw_response.get_crx_paper_info(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_paper_info(self, client: AlphaxivCat) -> None:
        paper = client.papers.get_paper_info(
            "pid",
        )
        assert_matches_type(PaperGetPaperInfoResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_paper_info(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.get_paper_info(
            "pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperGetPaperInfoResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_paper_info(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.get_paper_info(
            "pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperGetPaperInfoResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_paper_info(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            client.papers.with_raw_response.get_paper_info(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_abstract_embed(self, client: AlphaxivCat) -> None:
        paper = client.papers.kickoff_abstract_embed()
        assert_matches_type(PaperKickoffAbstractEmbedResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_abstract_embed(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.kickoff_abstract_embed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperKickoffAbstractEmbedResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_abstract_embed(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.kickoff_abstract_embed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperKickoffAbstractEmbedResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_ai(self, client: AlphaxivCat) -> None:
        paper = client.papers.kickoff_ai()
        assert_matches_type(PaperKickoffAIResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_ai(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.kickoff_ai()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperKickoffAIResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_ai(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.kickoff_ai() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperKickoffAIResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_bibtex(self, client: AlphaxivCat) -> None:
        paper = client.papers.kickoff_bibtex()
        assert_matches_type(PaperKickoffBibtexResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_bibtex(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.kickoff_bibtex()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperKickoffBibtexResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_bibtex(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.kickoff_bibtex() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperKickoffBibtexResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_github(self, client: AlphaxivCat) -> None:
        paper = client.papers.kickoff_github()
        assert_matches_type(PaperKickoffGitHubResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_github(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.kickoff_github()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperKickoffGitHubResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_github(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.kickoff_github() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperKickoffGitHubResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_paper_categorization(self, client: AlphaxivCat) -> None:
        paper = client.papers.kickoff_paper_categorization(
            "all",
        )
        assert_matches_type(PaperKickoffPaperCategorizationResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_paper_categorization(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.kickoff_paper_categorization(
            "all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperKickoffPaperCategorizationResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_paper_categorization(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.kickoff_paper_categorization(
            "all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperKickoffPaperCategorizationResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_kickoff_paper_categorization(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `all` but received ''"):
            client.papers.with_raw_response.kickoff_paper_categorization(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_recent_papers(self, client: AlphaxivCat) -> None:
        paper = client.papers.kickoff_recent_papers()
        assert_matches_type(PaperKickoffRecentPapersResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_recent_papers(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.kickoff_recent_papers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperKickoffRecentPapersResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_recent_papers(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.kickoff_recent_papers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperKickoffRecentPapersResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mark_viewed(self, client: AlphaxivCat) -> None:
        paper = client.papers.mark_viewed(
            "x",
        )
        assert_matches_type(object, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mark_viewed(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.mark_viewed(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(object, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mark_viewed(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.mark_viewed(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(object, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_mark_viewed(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            client.papers.with_raw_response.mark_viewed(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_abstract_embed(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper = client.papers.process_abstract_embed(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(PaperProcessAbstractEmbedResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process_abstract_embed(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.papers.with_raw_response.process_abstract_embed(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperProcessAbstractEmbedResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process_abstract_embed(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.papers.with_streaming_response.process_abstract_embed(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                paper = response.parse()
                assert_matches_type(PaperProcessAbstractEmbedResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_metadata(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper = client.papers.process_metadata(
                metadata={},
                universal_paper_id="universalPaperId",
            )

        assert_matches_type(PaperProcessMetadataResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_metadata_with_all_params(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper = client.papers.process_metadata(
                metadata={
                    "bibtex": True,
                    "custom_categories": True,
                    "embedding": True,
                    "github": True,
                    "organizations": True,
                    "overview": True,
                    "thumbnail": True,
                },
                universal_paper_id="universalPaperId",
            )

        assert_matches_type(PaperProcessMetadataResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process_metadata(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.papers.with_raw_response.process_metadata(
                metadata={},
                universal_paper_id="universalPaperId",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperProcessMetadataResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process_metadata(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.papers.with_streaming_response.process_metadata(
                metadata={},
                universal_paper_id="universalPaperId",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                paper = response.parse()
                assert_matches_type(PaperProcessMetadataResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_ai_latest(self, client: AlphaxivCat) -> None:
        paper = client.papers.request_ai_latest(
            upid="x",
        )
        assert_matches_type(PaperRequestAILatestResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_ai_latest_with_all_params(self, client: AlphaxivCat) -> None:
        paper = client.papers.request_ai_latest(
            upid="x",
            preferred_language="am",
        )
        assert_matches_type(PaperRequestAILatestResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_ai_latest(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.request_ai_latest(
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperRequestAILatestResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_ai_latest(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.request_ai_latest(
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperRequestAILatestResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request_ai_latest(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            client.papers.with_raw_response.request_ai_latest(
                upid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_ai_translation_latest(self, client: AlphaxivCat) -> None:
        paper = client.papers.request_ai_translation_latest(
            language="am",
            upid="x",
        )
        assert_matches_type(PaperRequestAITranslationLatestResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_ai_translation_latest(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.request_ai_translation_latest(
            language="am",
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperRequestAITranslationLatestResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_ai_translation_latest(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.request_ai_translation_latest(
            language="am",
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperRequestAITranslationLatestResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request_ai_translation_latest(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            client.papers.with_raw_response.request_ai_translation_latest(
                language="am",
                upid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_github_repository(self, client: AlphaxivCat) -> None:
        paper = client.papers.set_github_repository(
            paper_id="x",
            github="https://example.com",
        )
        assert_matches_type(PaperSetGitHubRepositoryResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_github_repository(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.set_github_repository(
            paper_id="x",
            github="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperSetGitHubRepositoryResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_github_repository(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.set_github_repository(
            paper_id="x",
            github="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperSetGitHubRepositoryResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_github_repository(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            client.papers.with_raw_response.set_github_repository(
                paper_id="",
                github="https://example.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle_follow(self, client: AlphaxivCat) -> None:
        paper = client.papers.toggle_follow(
            "x",
        )
        assert_matches_type(PaperToggleFollowResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_toggle_follow(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.toggle_follow(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperToggleFollowResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_toggle_follow(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.toggle_follow(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperToggleFollowResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_toggle_follow(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            client.papers.with_raw_response.toggle_follow(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_translate_ai_overview(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper = client.papers.translate_ai_overview(
                language="am",
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(PaperTranslateAIOverviewResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_translate_ai_overview(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.papers.with_raw_response.translate_ai_overview(
                language="am",
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperTranslateAIOverviewResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_translate_ai_overview(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.papers.with_streaming_response.translate_ai_overview(
                language="am",
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                paper = response.parse()
                assert_matches_type(PaperTranslateAIOverviewResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_translate_ai_overview(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_version_id` but received ''"):
                client.papers.with_raw_response.translate_ai_overview(
                    language="am",
                    paper_version_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unclaim(self, client: AlphaxivCat) -> None:
        paper = client.papers.unclaim(
            "x",
        )
        assert_matches_type(PaperUnclaimResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unclaim(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.unclaim(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperUnclaimResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unclaim(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.unclaim(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperUnclaimResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unclaim(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            client.papers.with_raw_response.unclaim(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_vote(self, client: AlphaxivCat) -> None:
        paper = client.papers.vote(
            "x",
        )
        assert_matches_type(PaperVoteResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_vote(self, client: AlphaxivCat) -> None:
        response = client.papers.with_raw_response.vote(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = response.parse()
        assert_matches_type(PaperVoteResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_vote(self, client: AlphaxivCat) -> None:
        with client.papers.with_streaming_response.vote(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = response.parse()
            assert_matches_type(PaperVoteResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_vote(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            client.papers.with_raw_response.vote(
                "",
            )


class TestAsyncPapers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_author(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.add_author(
            paper_id="x",
            author_email="dev@stainless.com",
        )
        assert_matches_type(PaperAddAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_author_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.add_author(
            paper_id="x",
            author_email="dev@stainless.com",
            should_email=True,
        )
        assert_matches_type(PaperAddAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_author(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.add_author(
            paper_id="x",
            author_email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperAddAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_author(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.add_author(
            paper_id="x",
            author_email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperAddAuthorResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_author(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            await async_client.papers.with_raw_response.add_author(
                paper_id="",
                author_email="dev@stainless.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_admin_vote(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.admin_vote(
            paper_id="x",
            entry=0,
        )
        assert_matches_type(PaperAdminVoteResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_admin_vote(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.admin_vote(
            paper_id="x",
            entry=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperAdminVoteResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_admin_vote(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.admin_vote(
            paper_id="x",
            entry=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperAdminVoteResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_admin_vote(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            await async_client.papers.with_raw_response.admin_vote(
                paper_id="",
                entry=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_crx_abstract_click(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.crx_abstract_click(
            ref="ref",
            pid="pid",
        )
        assert_matches_type(PaperCrxAbstractClickResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_crx_abstract_click(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.crx_abstract_click(
            ref="ref",
            pid="pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperCrxAbstractClickResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_crx_abstract_click(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.crx_abstract_click(
            ref="ref",
            pid="pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperCrxAbstractClickResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_crx_abstract_click(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            await async_client.papers.with_raw_response.crx_abstract_click(
                ref="ref",
                pid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ref` but received ''"):
            await async_client.papers.with_raw_response.crx_abstract_click(
                ref="",
                pid="pid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_crx_abstract_hit(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.crx_abstract_hit(
            "pid",
        )
        assert_matches_type(PaperCrxAbstractHitResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_crx_abstract_hit(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.crx_abstract_hit(
            "pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperCrxAbstractHitResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_crx_abstract_hit(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.crx_abstract_hit(
            "pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperCrxAbstractHitResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_crx_abstract_hit(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            await async_client.papers.with_raw_response.crx_abstract_hit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_crx_pdf_click(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.crx_pdf_click(
            ref="ref",
            pid="pid",
        )
        assert_matches_type(PaperCrxPdfClickResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_crx_pdf_click(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.crx_pdf_click(
            ref="ref",
            pid="pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperCrxPdfClickResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_crx_pdf_click(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.crx_pdf_click(
            ref="ref",
            pid="pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperCrxPdfClickResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_crx_pdf_click(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            await async_client.papers.with_raw_response.crx_pdf_click(
                ref="ref",
                pid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ref` but received ''"):
            await async_client.papers.with_raw_response.crx_pdf_click(
                ref="",
                pid="pid",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_crx_pdf_hit(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.crx_pdf_hit(
            "pid",
        )
        assert_matches_type(PaperCrxPdfHitResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_crx_pdf_hit(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.crx_pdf_hit(
            "pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperCrxPdfHitResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_crx_pdf_hit(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.crx_pdf_hit(
            "pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperCrxPdfHitResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_crx_pdf_hit(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            await async_client.papers.with_raw_response.crx_pdf_hit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_email_author(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.email_author(
            paper_id="x",
            author_individual_email="dev@stainless.com",
            email_author_name="emailAuthorName",
            paper_name="paperName",
            type="comment",
        )
        assert_matches_type(PaperEmailAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_email_author_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.email_author(
            paper_id="x",
            author_individual_email="dev@stainless.com",
            email_author_name="emailAuthorName",
            paper_name="paperName",
            type="comment",
            ignore_duplicate_error=True,
        )
        assert_matches_type(PaperEmailAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_email_author(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.email_author(
            paper_id="x",
            author_individual_email="dev@stainless.com",
            email_author_name="emailAuthorName",
            paper_name="paperName",
            type="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperEmailAuthorResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_email_author(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.email_author(
            paper_id="x",
            author_individual_email="dev@stainless.com",
            email_author_name="emailAuthorName",
            paper_name="paperName",
            type="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperEmailAuthorResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_email_author(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            await async_client.papers.with_raw_response.email_author(
                paper_id="",
                author_individual_email="dev@stainless.com",
                email_author_name="emailAuthorName",
                paper_name="paperName",
                type="comment",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_crx_paper_info(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.get_crx_paper_info(
            "pid",
        )
        assert_matches_type(PaperGetCrxPaperInfoResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_crx_paper_info(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.get_crx_paper_info(
            "pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperGetCrxPaperInfoResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_crx_paper_info(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.get_crx_paper_info(
            "pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperGetCrxPaperInfoResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_crx_paper_info(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            await async_client.papers.with_raw_response.get_crx_paper_info(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_paper_info(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.get_paper_info(
            "pid",
        )
        assert_matches_type(PaperGetPaperInfoResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_paper_info(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.get_paper_info(
            "pid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperGetPaperInfoResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_paper_info(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.get_paper_info(
            "pid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperGetPaperInfoResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_paper_info(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pid` but received ''"):
            await async_client.papers.with_raw_response.get_paper_info(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_abstract_embed(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.kickoff_abstract_embed()
        assert_matches_type(PaperKickoffAbstractEmbedResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_abstract_embed(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.kickoff_abstract_embed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperKickoffAbstractEmbedResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_abstract_embed(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.kickoff_abstract_embed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperKickoffAbstractEmbedResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_ai(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.kickoff_ai()
        assert_matches_type(PaperKickoffAIResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_ai(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.kickoff_ai()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperKickoffAIResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_ai(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.kickoff_ai() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperKickoffAIResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_bibtex(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.kickoff_bibtex()
        assert_matches_type(PaperKickoffBibtexResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_bibtex(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.kickoff_bibtex()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperKickoffBibtexResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_bibtex(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.kickoff_bibtex() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperKickoffBibtexResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_github(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.kickoff_github()
        assert_matches_type(PaperKickoffGitHubResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_github(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.kickoff_github()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperKickoffGitHubResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_github(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.kickoff_github() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperKickoffGitHubResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_paper_categorization(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.kickoff_paper_categorization(
            "all",
        )
        assert_matches_type(PaperKickoffPaperCategorizationResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_paper_categorization(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.kickoff_paper_categorization(
            "all",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperKickoffPaperCategorizationResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_paper_categorization(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.kickoff_paper_categorization(
            "all",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperKickoffPaperCategorizationResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_kickoff_paper_categorization(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `all` but received ''"):
            await async_client.papers.with_raw_response.kickoff_paper_categorization(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_recent_papers(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.kickoff_recent_papers()
        assert_matches_type(PaperKickoffRecentPapersResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_recent_papers(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.kickoff_recent_papers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperKickoffRecentPapersResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_recent_papers(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.kickoff_recent_papers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperKickoffRecentPapersResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mark_viewed(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.mark_viewed(
            "x",
        )
        assert_matches_type(object, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mark_viewed(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.mark_viewed(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(object, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mark_viewed(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.mark_viewed(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(object, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_mark_viewed(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            await async_client.papers.with_raw_response.mark_viewed(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_abstract_embed(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper = await async_client.papers.process_abstract_embed(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(PaperProcessAbstractEmbedResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process_abstract_embed(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.papers.with_raw_response.process_abstract_embed(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperProcessAbstractEmbedResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process_abstract_embed(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.papers.with_streaming_response.process_abstract_embed(
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                paper = await response.parse()
                assert_matches_type(PaperProcessAbstractEmbedResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper = await async_client.papers.process_metadata(
                metadata={},
                universal_paper_id="universalPaperId",
            )

        assert_matches_type(PaperProcessMetadataResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_metadata_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper = await async_client.papers.process_metadata(
                metadata={
                    "bibtex": True,
                    "custom_categories": True,
                    "embedding": True,
                    "github": True,
                    "organizations": True,
                    "overview": True,
                    "thumbnail": True,
                },
                universal_paper_id="universalPaperId",
            )

        assert_matches_type(PaperProcessMetadataResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.papers.with_raw_response.process_metadata(
                metadata={},
                universal_paper_id="universalPaperId",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperProcessMetadataResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process_metadata(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.papers.with_streaming_response.process_metadata(
                metadata={},
                universal_paper_id="universalPaperId",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                paper = await response.parse()
                assert_matches_type(PaperProcessMetadataResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_ai_latest(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.request_ai_latest(
            upid="x",
        )
        assert_matches_type(PaperRequestAILatestResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_ai_latest_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.request_ai_latest(
            upid="x",
            preferred_language="am",
        )
        assert_matches_type(PaperRequestAILatestResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_ai_latest(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.request_ai_latest(
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperRequestAILatestResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_ai_latest(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.request_ai_latest(
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperRequestAILatestResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request_ai_latest(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            await async_client.papers.with_raw_response.request_ai_latest(
                upid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_ai_translation_latest(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.request_ai_translation_latest(
            language="am",
            upid="x",
        )
        assert_matches_type(PaperRequestAITranslationLatestResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_ai_translation_latest(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.request_ai_translation_latest(
            language="am",
            upid="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperRequestAITranslationLatestResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_ai_translation_latest(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.request_ai_translation_latest(
            language="am",
            upid="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperRequestAITranslationLatestResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request_ai_translation_latest(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upid` but received ''"):
            await async_client.papers.with_raw_response.request_ai_translation_latest(
                language="am",
                upid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_github_repository(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.set_github_repository(
            paper_id="x",
            github="https://example.com",
        )
        assert_matches_type(PaperSetGitHubRepositoryResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_github_repository(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.set_github_repository(
            paper_id="x",
            github="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperSetGitHubRepositoryResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_github_repository(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.set_github_repository(
            paper_id="x",
            github="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperSetGitHubRepositoryResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_github_repository(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            await async_client.papers.with_raw_response.set_github_repository(
                paper_id="",
                github="https://example.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle_follow(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.toggle_follow(
            "x",
        )
        assert_matches_type(PaperToggleFollowResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_toggle_follow(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.toggle_follow(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperToggleFollowResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_toggle_follow(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.toggle_follow(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperToggleFollowResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_toggle_follow(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            await async_client.papers.with_raw_response.toggle_follow(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_translate_ai_overview(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            paper = await async_client.papers.translate_ai_overview(
                language="am",
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(PaperTranslateAIOverviewResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_translate_ai_overview(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.papers.with_raw_response.translate_ai_overview(
                language="am",
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperTranslateAIOverviewResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_translate_ai_overview(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.papers.with_streaming_response.translate_ai_overview(
                language="am",
                paper_version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                paper = await response.parse()
                assert_matches_type(PaperTranslateAIOverviewResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_translate_ai_overview(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_version_id` but received ''"):
                await async_client.papers.with_raw_response.translate_ai_overview(
                    language="am",
                    paper_version_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unclaim(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.unclaim(
            "x",
        )
        assert_matches_type(PaperUnclaimResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unclaim(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.unclaim(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperUnclaimResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unclaim(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.unclaim(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperUnclaimResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unclaim(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            await async_client.papers.with_raw_response.unclaim(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_vote(self, async_client: AsyncAlphaxivCat) -> None:
        paper = await async_client.papers.vote(
            "x",
        )
        assert_matches_type(PaperVoteResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_vote(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.papers.with_raw_response.vote(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        paper = await response.parse()
        assert_matches_type(PaperVoteResponse, paper, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_vote(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.papers.with_streaming_response.vote(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            paper = await response.parse()
            assert_matches_type(PaperVoteResponse, paper, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_vote(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `paper_id` but received ''"):
            await async_client.papers.with_raw_response.vote(
                "",
            )
