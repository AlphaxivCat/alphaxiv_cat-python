# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing_extensions import Literal

import httpx

from .v2 import (
    V2Resource,
    AsyncV2Resource,
    V2ResourceWithRawResponse,
    AsyncV2ResourceWithRawResponse,
    V2ResourceWithStreamingResponse,
    AsyncV2ResourceWithStreamingResponse,
)
from .v3.v3 import (
    V3Resource,
    AsyncV3Resource,
    V3ResourceWithRawResponse,
    AsyncV3ResourceWithRawResponse,
    V3ResourceWithStreamingResponse,
    AsyncV3ResourceWithStreamingResponse,
)
from .ingest import (
    IngestResource,
    AsyncIngestResource,
    IngestResourceWithRawResponse,
    AsyncIngestResourceWithRawResponse,
    IngestResourceWithStreamingResponse,
    AsyncIngestResourceWithStreamingResponse,
)
from ...types import (
    paper_add_author_params,
    paper_admin_vote_params,
    paper_email_author_params,
    paper_process_metadata_params,
    paper_request_ai_latest_params,
    paper_set_github_repository_params,
    paper_process_abstract_embed_params,
)
from .private import (
    PrivateResource,
    AsyncPrivateResource,
    PrivateResourceWithRawResponse,
    AsyncPrivateResourceWithRawResponse,
    PrivateResourceWithStreamingResponse,
    AsyncPrivateResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .kickoff_daily_github_stars import (
    KickoffDailyGitHubStarsResource,
    AsyncKickoffDailyGitHubStarsResource,
    KickoffDailyGitHubStarsResourceWithRawResponse,
    AsyncKickoffDailyGitHubStarsResourceWithRawResponse,
    KickoffDailyGitHubStarsResourceWithStreamingResponse,
    AsyncKickoffDailyGitHubStarsResourceWithStreamingResponse,
)
from ...types.paper_vote_response import PaperVoteResponse
from ...types.paper_unclaim_response import PaperUnclaimResponse
from ...types.paper_add_author_response import PaperAddAuthorResponse
from ...types.paper_admin_vote_response import PaperAdminVoteResponse
from ...types.paper_kickoff_ai_response import PaperKickoffAIResponse
from ...types.paper_crx_pdf_hit_response import PaperCrxPdfHitResponse
from ...types.paper_email_author_response import PaperEmailAuthorResponse
from ...types.paper_crx_pdf_click_response import PaperCrxPdfClickResponse
from ...types.paper_toggle_follow_response import PaperToggleFollowResponse
from ...types.paper_get_paper_info_response import PaperGetPaperInfoResponse
from ...types.paper_kickoff_bibtex_response import PaperKickoffBibtexResponse
from ...types.paper_kickoff_github_response import PaperKickoffGitHubResponse
from ...types.paper_crx_abstract_hit_response import PaperCrxAbstractHitResponse
from ...types.paper_process_metadata_response import PaperProcessMetadataResponse
from ...types.paper_request_ai_latest_response import PaperRequestAILatestResponse
from ...types.paper_crx_abstract_click_response import PaperCrxAbstractClickResponse
from ...types.paper_get_crx_paper_info_response import PaperGetCrxPaperInfoResponse
from ...types.paper_kickoff_recent_papers_response import PaperKickoffRecentPapersResponse
from ...types.paper_set_github_repository_response import PaperSetGitHubRepositoryResponse
from ...types.paper_translate_ai_overview_response import PaperTranslateAIOverviewResponse
from ...types.paper_kickoff_abstract_embed_response import PaperKickoffAbstractEmbedResponse
from ...types.paper_process_abstract_embed_response import PaperProcessAbstractEmbedResponse
from ...types.paper_kickoff_paper_categorization_response import PaperKickoffPaperCategorizationResponse
from ...types.paper_request_ai_translation_latest_response import PaperRequestAITranslationLatestResponse

__all__ = ["PapersResource", "AsyncPapersResource"]


class PapersResource(SyncAPIResource):
    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def ingest(self) -> IngestResource:
        return IngestResource(self._client)

    @cached_property
    def private(self) -> PrivateResource:
        return PrivateResource(self._client)

    @cached_property
    def kickoff_daily_github_stars(self) -> KickoffDailyGitHubStarsResource:
        return KickoffDailyGitHubStarsResource(self._client)

    @cached_property
    def v3(self) -> V3Resource:
        return V3Resource(self._client)

    @cached_property
    def v2(self) -> V2Resource:
        return V2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> PapersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return PapersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PapersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return PapersResourceWithStreamingResponse(self)

    def add_author(
        self,
        paper_id: str,
        *,
        author_email: str,
        should_email: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperAddAuthorResponse:
        """
        Add a new author to a paper

        Source file: `api-server/src/controllers/v2/papers/add-new-author.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return self._post(
            path_template("/v2/papers/{paper_id}/add-author", paper_id=paper_id),
            body=maybe_transform(
                {
                    "author_email": author_email,
                    "should_email": should_email,
                },
                paper_add_author_params.PaperAddAuthorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperAddAuthorResponse,
        )

    def admin_vote(
        self,
        paper_id: str,
        *,
        entry: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperAdminVoteResponse:
        """
        Set paper vote count (admin only)

        Source file:
        `api-server/src/controllers/v2/papers/admin-vote-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return self._post(
            path_template("/v2/papers/{paper_id}/admin-vote", paper_id=paper_id),
            body=maybe_transform({"entry": entry}, paper_admin_vote_params.PaperAdminVoteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperAdminVoteResponse,
        )

    def crx_abstract_click(
        self,
        ref: str,
        *,
        pid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperCrxAbstractClickResponse:
        """
        Legacy route for v1 browser extensions to track abstract page clicks

        Source file:
        `api-server/src/controllers/v1/papers/crxabstractclick.controller.ts`

        Args:
          pid: Paper ID

          ref: Referrer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return self._get(
            path_template("/v1/papers/crxabstractclick/{pid}/{ref}", pid=pid, ref=ref),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperCrxAbstractClickResponse,
        )

    def crx_abstract_hit(
        self,
        pid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperCrxAbstractHitResponse:
        """
        Legacy route for v1 browser extensions to track abstract page hits

        Source file: `api-server/src/controllers/v1/papers/crxabstracthit.controller.ts`

        Args:
          pid: Paper ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        return self._get(
            path_template("/v1/papers/crxabstracthit/{pid}", pid=pid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperCrxAbstractHitResponse,
        )

    def crx_pdf_click(
        self,
        ref: str,
        *,
        pid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperCrxPdfClickResponse:
        """
        Legacy route for v1 browser extensions to track PDF page clicks

        Source file: `api-server/src/controllers/v1/papers/crxpdfclick.controller.ts`

        Args:
          pid: Paper ID

          ref: Referrer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return self._get(
            path_template("/v1/papers/crxpdfclick/{pid}/{ref}", pid=pid, ref=ref),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperCrxPdfClickResponse,
        )

    def crx_pdf_hit(
        self,
        pid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperCrxPdfHitResponse:
        """
        Legacy route for v1 browser extensions to track PDF page hits

        Source file: `api-server/src/controllers/v1/papers/crxpdfhit.controller.ts`

        Args:
          pid: Paper ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        return self._get(
            path_template("/v1/papers/crxpdfhit/{pid}", pid=pid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperCrxPdfHitResponse,
        )

    def email_author(
        self,
        paper_id: str,
        *,
        author_individual_email: str,
        email_author_name: str,
        paper_name: str,
        type: Literal["comment", "trending"],
        ignore_duplicate_error: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperEmailAuthorResponse:
        """
        Send email to individual author about paper comments or trending

        Source file:
        `api-server/src/controllers/v2/papers/email-individual-author.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return self._post(
            path_template("/v2/papers/{paper_id}/email-author", paper_id=paper_id),
            body=maybe_transform(
                {
                    "author_individual_email": author_individual_email,
                    "email_author_name": email_author_name,
                    "paper_name": paper_name,
                    "type": type,
                    "ignore_duplicate_error": ignore_duplicate_error,
                },
                paper_email_author_params.PaperEmailAuthorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperEmailAuthorResponse,
        )

    def get_crx_paper_info(
        self,
        pid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperGetCrxPaperInfoResponse:
        """
        Legacy route for v1 browser extensions to get paper information

        Source file:
        `api-server/src/controllers/v1/papers/getcrxpaperinfo.controller.ts`

        Args:
          pid: Paper ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        return self._get(
            path_template("/v1/papers/getcrxpaperinfo/{pid}", pid=pid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperGetCrxPaperInfoResponse,
        )

    def get_paper_info(
        self,
        pid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperGetPaperInfoResponse:
        """
        Legacy route for getting paper information from arXiv abstract pages

        Source file: `api-server/src/controllers/v1/papers/getpaperinfo.controller.ts`

        Args:
          pid: Paper ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        return self._get(
            path_template("/v1/papers/getpaperinfo/{pid}", pid=pid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperGetPaperInfoResponse,
        )

    def kickoff_abstract_embed(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffAbstractEmbedResponse:
        """
        Kickoff background job to generate abstract embeddings for paper versions

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-paper-version-abstract-embed.controller.ts`
        """
        return self._post(
            "/v2/papers/kickoff-paper-version-abstract-embed",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffAbstractEmbedResponse,
        )

    def kickoff_ai(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffAIResponse:
        """
        Kickoff background job to generate AI overviews for papers

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-paper-ai.controller.ts`
        """
        return self._post(
            "/v2/papers/kickoff-paper-ai",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffAIResponse,
        )

    def kickoff_bibtex(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffBibtexResponse:
        """
        Kickoff background job to generate bibtex for papers

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-paper-bibtex.controller.ts`
        """
        return self._post(
            "/v2/papers/kickoff-paper-bibtex",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffBibtexResponse,
        )

    def kickoff_github(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffGitHubResponse:
        """
        Kickoff background job to link papers with GitHub repositories

        Source file: `api-server/src/controllers/v2/papers/kickoff-github.controller.ts`
        """
        return self._post(
            "/v2/papers/kickoff-github",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffGitHubResponse,
        )

    def kickoff_paper_categorization(
        self,
        all: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffPaperCategorizationResponse:
        """
        Kickoff background job to categorize papers

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-paper-categorization.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not all:
            raise ValueError(f"Expected a non-empty value for `all` but received {all!r}")
        return self._post(
            path_template("/v2/papers/kickoff-paper-categorization/{all}", all=all),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffPaperCategorizationResponse,
        )

    def kickoff_recent_papers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffRecentPapersResponse:
        """
        Kickoff background job to ingest recent papers from arXiv

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-recent-papers.controller.ts`
        """
        return self._post(
            "/v2/papers/kickoff-recent-papers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffRecentPapersResponse,
        )

    def mark_viewed(
        self,
        upid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Track paper view event for analytics

        Source file:
        `api-server/src/controllers/v2/papers/mark-paper-view.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        return self._post(
            path_template("/v2/papers/{upid}/view", upid=upid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @typing_extensions.deprecated("deprecated")
    def process_abstract_embed(
        self,
        *,
        paper_version_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperProcessAbstractEmbedResponse:
        """
        Process abstract embedding for a paper version

        Source file:
        `api-server/src/controllers/v2/papers/process-paper-version-abstract-embed.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/papers/process-paper-version-abstract-embed",
            body=maybe_transform(
                {"paper_version_id": paper_version_id},
                paper_process_abstract_embed_params.PaperProcessAbstractEmbedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperProcessAbstractEmbedResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def process_metadata(
        self,
        *,
        metadata: paper_process_metadata_params.Metadata,
        universal_paper_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperProcessMetadataResponse:
        """
        Process various metadata for a paper (thumbnail, github, bibtex, etc.)

        Source file:
        `api-server/src/controllers/v2/papers/process-metadata.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/papers/process-metadata",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "universal_paper_id": universal_paper_id,
                },
                paper_process_metadata_params.PaperProcessMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperProcessMetadataResponse,
        )

    def request_ai_latest(
        self,
        upid: str,
        *,
        preferred_language: Literal[
            "am",
            "ar",
            "az",
            "bg",
            "bn",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "et",
            "fa",
            "fi",
            "fr",
            "gu",
            "ha",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ka",
            "kn",
            "ko",
            "lt",
            "lv",
            "ml",
            "mr",
            "ms",
            "my",
            "ne",
            "nl",
            "no",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "si",
            "sk",
            "sl",
            "sr",
            "sv",
            "sw",
            "ta",
            "te",
            "th",
            "tl",
            "tr",
            "uk",
            "ur",
            "uz",
            "vi",
            "yo",
            "zh",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperRequestAILatestResponse:
        """
        Request AI overview generation for the latest paper version

        Source file:
        `api-server/src/controllers/v2/papers/request-ai-latest.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        return self._post(
            path_template("/v2/papers/{upid}/request-ai", upid=upid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"preferred_language": preferred_language},
                    paper_request_ai_latest_params.PaperRequestAILatestParams,
                ),
            ),
            cast_to=PaperRequestAILatestResponse,
        )

    def request_ai_translation_latest(
        self,
        language: Literal[
            "am",
            "ar",
            "az",
            "bg",
            "bn",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "es",
            "et",
            "fa",
            "fi",
            "fr",
            "gu",
            "ha",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ka",
            "kn",
            "ko",
            "lt",
            "lv",
            "ml",
            "mr",
            "ms",
            "my",
            "ne",
            "nl",
            "no",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "si",
            "sk",
            "sl",
            "sr",
            "sv",
            "sw",
            "ta",
            "te",
            "th",
            "tl",
            "tr",
            "uk",
            "ur",
            "uz",
            "vi",
            "yo",
            "zh",
        ],
        *,
        upid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperRequestAITranslationLatestResponse:
        """
        Request AI overview translation for the latest paper version

        Source file:
        `api-server/src/controllers/v2/papers/request-ai-translation-latest.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return self._post(
            path_template("/v2/papers/{upid}/request-ai-translation/{language}", upid=upid, language=language),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperRequestAITranslationLatestResponse,
        )

    def set_github_repository(
        self,
        paper_id: str,
        *,
        github: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperSetGitHubRepositoryResponse:
        """
        Set GitHub repository for a paper

        Source file: `api-server/src/controllers/v2/papers/set-github.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return self._post(
            path_template("/v2/papers/{paper_id}/github", paper_id=paper_id),
            body=maybe_transform({"github": github}, paper_set_github_repository_params.PaperSetGitHubRepositoryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperSetGitHubRepositoryResponse,
        )

    def toggle_follow(
        self,
        paper_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperToggleFollowResponse:
        """
        Toggle paper follow status (add to Want to read folder or remove from all
        folders)

        Source file: `api-server/src/controllers/v2/papers/follow-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return self._post(
            path_template("/v2/papers/{paper_id}/follow", paper_id=paper_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperToggleFollowResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def translate_ai_overview(
        self,
        language: Literal[
            "am",
            "ar",
            "az",
            "bg",
            "bn",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "es",
            "et",
            "fa",
            "fi",
            "fr",
            "gu",
            "ha",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ka",
            "kn",
            "ko",
            "lt",
            "lv",
            "ml",
            "mr",
            "ms",
            "my",
            "ne",
            "nl",
            "no",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "si",
            "sk",
            "sl",
            "sr",
            "sv",
            "sw",
            "ta",
            "te",
            "th",
            "tl",
            "tr",
            "uk",
            "ur",
            "uz",
            "vi",
            "yo",
            "zh",
        ],
        *,
        paper_version_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperTranslateAIOverviewResponse:
        """
        Translate AI overview to specified language

        Source file:
        `api-server/src/controllers/v2/papers/translate-ai-overview.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_version_id:
            raise ValueError(f"Expected a non-empty value for `paper_version_id` but received {paper_version_id!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return self._post(
            path_template(
                "/v2/papers/translate-ai-overview/{paper_version_id}/{language}",
                paper_version_id=paper_version_id,
                language=language,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperTranslateAIOverviewResponse,
        )

    def unclaim(
        self,
        paper_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperUnclaimResponse:
        """
        Remove authorship claim from a paper

        Source file: `api-server/src/controllers/v2/papers/unclaim-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return self._post(
            path_template("/v2/papers/{paper_id}/unclaim", paper_id=paper_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperUnclaimResponse,
        )

    def vote(
        self,
        paper_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperVoteResponse:
        """
        Toggle vote for a paper

        Source file: `api-server/src/controllers/v2/papers/vote-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return self._post(
            path_template("/v2/papers/{paper_id}/vote", paper_id=paper_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperVoteResponse,
        )


class AsyncPapersResource(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def ingest(self) -> AsyncIngestResource:
        return AsyncIngestResource(self._client)

    @cached_property
    def private(self) -> AsyncPrivateResource:
        return AsyncPrivateResource(self._client)

    @cached_property
    def kickoff_daily_github_stars(self) -> AsyncKickoffDailyGitHubStarsResource:
        return AsyncKickoffDailyGitHubStarsResource(self._client)

    @cached_property
    def v3(self) -> AsyncV3Resource:
        return AsyncV3Resource(self._client)

    @cached_property
    def v2(self) -> AsyncV2Resource:
        return AsyncV2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPapersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPapersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPapersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncPapersResourceWithStreamingResponse(self)

    async def add_author(
        self,
        paper_id: str,
        *,
        author_email: str,
        should_email: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperAddAuthorResponse:
        """
        Add a new author to a paper

        Source file: `api-server/src/controllers/v2/papers/add-new-author.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return await self._post(
            path_template("/v2/papers/{paper_id}/add-author", paper_id=paper_id),
            body=await async_maybe_transform(
                {
                    "author_email": author_email,
                    "should_email": should_email,
                },
                paper_add_author_params.PaperAddAuthorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperAddAuthorResponse,
        )

    async def admin_vote(
        self,
        paper_id: str,
        *,
        entry: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperAdminVoteResponse:
        """
        Set paper vote count (admin only)

        Source file:
        `api-server/src/controllers/v2/papers/admin-vote-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return await self._post(
            path_template("/v2/papers/{paper_id}/admin-vote", paper_id=paper_id),
            body=await async_maybe_transform({"entry": entry}, paper_admin_vote_params.PaperAdminVoteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperAdminVoteResponse,
        )

    async def crx_abstract_click(
        self,
        ref: str,
        *,
        pid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperCrxAbstractClickResponse:
        """
        Legacy route for v1 browser extensions to track abstract page clicks

        Source file:
        `api-server/src/controllers/v1/papers/crxabstractclick.controller.ts`

        Args:
          pid: Paper ID

          ref: Referrer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return await self._get(
            path_template("/v1/papers/crxabstractclick/{pid}/{ref}", pid=pid, ref=ref),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperCrxAbstractClickResponse,
        )

    async def crx_abstract_hit(
        self,
        pid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperCrxAbstractHitResponse:
        """
        Legacy route for v1 browser extensions to track abstract page hits

        Source file: `api-server/src/controllers/v1/papers/crxabstracthit.controller.ts`

        Args:
          pid: Paper ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        return await self._get(
            path_template("/v1/papers/crxabstracthit/{pid}", pid=pid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperCrxAbstractHitResponse,
        )

    async def crx_pdf_click(
        self,
        ref: str,
        *,
        pid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperCrxPdfClickResponse:
        """
        Legacy route for v1 browser extensions to track PDF page clicks

        Source file: `api-server/src/controllers/v1/papers/crxpdfclick.controller.ts`

        Args:
          pid: Paper ID

          ref: Referrer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return await self._get(
            path_template("/v1/papers/crxpdfclick/{pid}/{ref}", pid=pid, ref=ref),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperCrxPdfClickResponse,
        )

    async def crx_pdf_hit(
        self,
        pid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperCrxPdfHitResponse:
        """
        Legacy route for v1 browser extensions to track PDF page hits

        Source file: `api-server/src/controllers/v1/papers/crxpdfhit.controller.ts`

        Args:
          pid: Paper ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        return await self._get(
            path_template("/v1/papers/crxpdfhit/{pid}", pid=pid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperCrxPdfHitResponse,
        )

    async def email_author(
        self,
        paper_id: str,
        *,
        author_individual_email: str,
        email_author_name: str,
        paper_name: str,
        type: Literal["comment", "trending"],
        ignore_duplicate_error: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperEmailAuthorResponse:
        """
        Send email to individual author about paper comments or trending

        Source file:
        `api-server/src/controllers/v2/papers/email-individual-author.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return await self._post(
            path_template("/v2/papers/{paper_id}/email-author", paper_id=paper_id),
            body=await async_maybe_transform(
                {
                    "author_individual_email": author_individual_email,
                    "email_author_name": email_author_name,
                    "paper_name": paper_name,
                    "type": type,
                    "ignore_duplicate_error": ignore_duplicate_error,
                },
                paper_email_author_params.PaperEmailAuthorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperEmailAuthorResponse,
        )

    async def get_crx_paper_info(
        self,
        pid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperGetCrxPaperInfoResponse:
        """
        Legacy route for v1 browser extensions to get paper information

        Source file:
        `api-server/src/controllers/v1/papers/getcrxpaperinfo.controller.ts`

        Args:
          pid: Paper ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        return await self._get(
            path_template("/v1/papers/getcrxpaperinfo/{pid}", pid=pid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperGetCrxPaperInfoResponse,
        )

    async def get_paper_info(
        self,
        pid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperGetPaperInfoResponse:
        """
        Legacy route for getting paper information from arXiv abstract pages

        Source file: `api-server/src/controllers/v1/papers/getpaperinfo.controller.ts`

        Args:
          pid: Paper ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pid:
            raise ValueError(f"Expected a non-empty value for `pid` but received {pid!r}")
        return await self._get(
            path_template("/v1/papers/getpaperinfo/{pid}", pid=pid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperGetPaperInfoResponse,
        )

    async def kickoff_abstract_embed(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffAbstractEmbedResponse:
        """
        Kickoff background job to generate abstract embeddings for paper versions

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-paper-version-abstract-embed.controller.ts`
        """
        return await self._post(
            "/v2/papers/kickoff-paper-version-abstract-embed",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffAbstractEmbedResponse,
        )

    async def kickoff_ai(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffAIResponse:
        """
        Kickoff background job to generate AI overviews for papers

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-paper-ai.controller.ts`
        """
        return await self._post(
            "/v2/papers/kickoff-paper-ai",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffAIResponse,
        )

    async def kickoff_bibtex(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffBibtexResponse:
        """
        Kickoff background job to generate bibtex for papers

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-paper-bibtex.controller.ts`
        """
        return await self._post(
            "/v2/papers/kickoff-paper-bibtex",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffBibtexResponse,
        )

    async def kickoff_github(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffGitHubResponse:
        """
        Kickoff background job to link papers with GitHub repositories

        Source file: `api-server/src/controllers/v2/papers/kickoff-github.controller.ts`
        """
        return await self._post(
            "/v2/papers/kickoff-github",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffGitHubResponse,
        )

    async def kickoff_paper_categorization(
        self,
        all: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffPaperCategorizationResponse:
        """
        Kickoff background job to categorize papers

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-paper-categorization.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not all:
            raise ValueError(f"Expected a non-empty value for `all` but received {all!r}")
        return await self._post(
            path_template("/v2/papers/kickoff-paper-categorization/{all}", all=all),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffPaperCategorizationResponse,
        )

    async def kickoff_recent_papers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperKickoffRecentPapersResponse:
        """
        Kickoff background job to ingest recent papers from arXiv

        Source file:
        `api-server/src/controllers/v2/papers/kickoff-recent-papers.controller.ts`
        """
        return await self._post(
            "/v2/papers/kickoff-recent-papers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperKickoffRecentPapersResponse,
        )

    async def mark_viewed(
        self,
        upid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Track paper view event for analytics

        Source file:
        `api-server/src/controllers/v2/papers/mark-paper-view.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        return await self._post(
            path_template("/v2/papers/{upid}/view", upid=upid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @typing_extensions.deprecated("deprecated")
    async def process_abstract_embed(
        self,
        *,
        paper_version_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperProcessAbstractEmbedResponse:
        """
        Process abstract embedding for a paper version

        Source file:
        `api-server/src/controllers/v2/papers/process-paper-version-abstract-embed.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/papers/process-paper-version-abstract-embed",
            body=await async_maybe_transform(
                {"paper_version_id": paper_version_id},
                paper_process_abstract_embed_params.PaperProcessAbstractEmbedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperProcessAbstractEmbedResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def process_metadata(
        self,
        *,
        metadata: paper_process_metadata_params.Metadata,
        universal_paper_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperProcessMetadataResponse:
        """
        Process various metadata for a paper (thumbnail, github, bibtex, etc.)

        Source file:
        `api-server/src/controllers/v2/papers/process-metadata.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/papers/process-metadata",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "universal_paper_id": universal_paper_id,
                },
                paper_process_metadata_params.PaperProcessMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperProcessMetadataResponse,
        )

    async def request_ai_latest(
        self,
        upid: str,
        *,
        preferred_language: Literal[
            "am",
            "ar",
            "az",
            "bg",
            "bn",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "et",
            "fa",
            "fi",
            "fr",
            "gu",
            "ha",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ka",
            "kn",
            "ko",
            "lt",
            "lv",
            "ml",
            "mr",
            "ms",
            "my",
            "ne",
            "nl",
            "no",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "si",
            "sk",
            "sl",
            "sr",
            "sv",
            "sw",
            "ta",
            "te",
            "th",
            "tl",
            "tr",
            "uk",
            "ur",
            "uz",
            "vi",
            "yo",
            "zh",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperRequestAILatestResponse:
        """
        Request AI overview generation for the latest paper version

        Source file:
        `api-server/src/controllers/v2/papers/request-ai-latest.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        return await self._post(
            path_template("/v2/papers/{upid}/request-ai", upid=upid),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"preferred_language": preferred_language},
                    paper_request_ai_latest_params.PaperRequestAILatestParams,
                ),
            ),
            cast_to=PaperRequestAILatestResponse,
        )

    async def request_ai_translation_latest(
        self,
        language: Literal[
            "am",
            "ar",
            "az",
            "bg",
            "bn",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "es",
            "et",
            "fa",
            "fi",
            "fr",
            "gu",
            "ha",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ka",
            "kn",
            "ko",
            "lt",
            "lv",
            "ml",
            "mr",
            "ms",
            "my",
            "ne",
            "nl",
            "no",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "si",
            "sk",
            "sl",
            "sr",
            "sv",
            "sw",
            "ta",
            "te",
            "th",
            "tl",
            "tr",
            "uk",
            "ur",
            "uz",
            "vi",
            "yo",
            "zh",
        ],
        *,
        upid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperRequestAITranslationLatestResponse:
        """
        Request AI overview translation for the latest paper version

        Source file:
        `api-server/src/controllers/v2/papers/request-ai-translation-latest.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upid:
            raise ValueError(f"Expected a non-empty value for `upid` but received {upid!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return await self._post(
            path_template("/v2/papers/{upid}/request-ai-translation/{language}", upid=upid, language=language),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperRequestAITranslationLatestResponse,
        )

    async def set_github_repository(
        self,
        paper_id: str,
        *,
        github: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperSetGitHubRepositoryResponse:
        """
        Set GitHub repository for a paper

        Source file: `api-server/src/controllers/v2/papers/set-github.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return await self._post(
            path_template("/v2/papers/{paper_id}/github", paper_id=paper_id),
            body=await async_maybe_transform(
                {"github": github}, paper_set_github_repository_params.PaperSetGitHubRepositoryParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperSetGitHubRepositoryResponse,
        )

    async def toggle_follow(
        self,
        paper_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperToggleFollowResponse:
        """
        Toggle paper follow status (add to Want to read folder or remove from all
        folders)

        Source file: `api-server/src/controllers/v2/papers/follow-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return await self._post(
            path_template("/v2/papers/{paper_id}/follow", paper_id=paper_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperToggleFollowResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def translate_ai_overview(
        self,
        language: Literal[
            "am",
            "ar",
            "az",
            "bg",
            "bn",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "es",
            "et",
            "fa",
            "fi",
            "fr",
            "gu",
            "ha",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ka",
            "kn",
            "ko",
            "lt",
            "lv",
            "ml",
            "mr",
            "ms",
            "my",
            "ne",
            "nl",
            "no",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "si",
            "sk",
            "sl",
            "sr",
            "sv",
            "sw",
            "ta",
            "te",
            "th",
            "tl",
            "tr",
            "uk",
            "ur",
            "uz",
            "vi",
            "yo",
            "zh",
        ],
        *,
        paper_version_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperTranslateAIOverviewResponse:
        """
        Translate AI overview to specified language

        Source file:
        `api-server/src/controllers/v2/papers/translate-ai-overview.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_version_id:
            raise ValueError(f"Expected a non-empty value for `paper_version_id` but received {paper_version_id!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return await self._post(
            path_template(
                "/v2/papers/translate-ai-overview/{paper_version_id}/{language}",
                paper_version_id=paper_version_id,
                language=language,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperTranslateAIOverviewResponse,
        )

    async def unclaim(
        self,
        paper_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperUnclaimResponse:
        """
        Remove authorship claim from a paper

        Source file: `api-server/src/controllers/v2/papers/unclaim-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return await self._post(
            path_template("/v2/papers/{paper_id}/unclaim", paper_id=paper_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperUnclaimResponse,
        )

    async def vote(
        self,
        paper_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaperVoteResponse:
        """
        Toggle vote for a paper

        Source file: `api-server/src/controllers/v2/papers/vote-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_id:
            raise ValueError(f"Expected a non-empty value for `paper_id` but received {paper_id!r}")
        return await self._post(
            path_template("/v2/papers/{paper_id}/vote", paper_id=paper_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaperVoteResponse,
        )


class PapersResourceWithRawResponse:
    def __init__(self, papers: PapersResource) -> None:
        self._papers = papers

        self.add_author = to_raw_response_wrapper(
            papers.add_author,
        )
        self.admin_vote = to_raw_response_wrapper(
            papers.admin_vote,
        )
        self.crx_abstract_click = to_raw_response_wrapper(
            papers.crx_abstract_click,
        )
        self.crx_abstract_hit = to_raw_response_wrapper(
            papers.crx_abstract_hit,
        )
        self.crx_pdf_click = to_raw_response_wrapper(
            papers.crx_pdf_click,
        )
        self.crx_pdf_hit = to_raw_response_wrapper(
            papers.crx_pdf_hit,
        )
        self.email_author = to_raw_response_wrapper(
            papers.email_author,
        )
        self.get_crx_paper_info = to_raw_response_wrapper(
            papers.get_crx_paper_info,
        )
        self.get_paper_info = to_raw_response_wrapper(
            papers.get_paper_info,
        )
        self.kickoff_abstract_embed = to_raw_response_wrapper(
            papers.kickoff_abstract_embed,
        )
        self.kickoff_ai = to_raw_response_wrapper(
            papers.kickoff_ai,
        )
        self.kickoff_bibtex = to_raw_response_wrapper(
            papers.kickoff_bibtex,
        )
        self.kickoff_github = to_raw_response_wrapper(
            papers.kickoff_github,
        )
        self.kickoff_paper_categorization = to_raw_response_wrapper(
            papers.kickoff_paper_categorization,
        )
        self.kickoff_recent_papers = to_raw_response_wrapper(
            papers.kickoff_recent_papers,
        )
        self.mark_viewed = to_raw_response_wrapper(
            papers.mark_viewed,
        )
        self.process_abstract_embed = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                papers.process_abstract_embed,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_metadata = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                papers.process_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.request_ai_latest = to_raw_response_wrapper(
            papers.request_ai_latest,
        )
        self.request_ai_translation_latest = to_raw_response_wrapper(
            papers.request_ai_translation_latest,
        )
        self.set_github_repository = to_raw_response_wrapper(
            papers.set_github_repository,
        )
        self.toggle_follow = to_raw_response_wrapper(
            papers.toggle_follow,
        )
        self.translate_ai_overview = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                papers.translate_ai_overview,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unclaim = to_raw_response_wrapper(
            papers.unclaim,
        )
        self.vote = to_raw_response_wrapper(
            papers.vote,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._papers.versions)

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._papers.metadata)

    @cached_property
    def ingest(self) -> IngestResourceWithRawResponse:
        return IngestResourceWithRawResponse(self._papers.ingest)

    @cached_property
    def private(self) -> PrivateResourceWithRawResponse:
        return PrivateResourceWithRawResponse(self._papers.private)

    @cached_property
    def kickoff_daily_github_stars(self) -> KickoffDailyGitHubStarsResourceWithRawResponse:
        return KickoffDailyGitHubStarsResourceWithRawResponse(self._papers.kickoff_daily_github_stars)

    @cached_property
    def v3(self) -> V3ResourceWithRawResponse:
        return V3ResourceWithRawResponse(self._papers.v3)

    @cached_property
    def v2(self) -> V2ResourceWithRawResponse:
        return V2ResourceWithRawResponse(self._papers.v2)


class AsyncPapersResourceWithRawResponse:
    def __init__(self, papers: AsyncPapersResource) -> None:
        self._papers = papers

        self.add_author = async_to_raw_response_wrapper(
            papers.add_author,
        )
        self.admin_vote = async_to_raw_response_wrapper(
            papers.admin_vote,
        )
        self.crx_abstract_click = async_to_raw_response_wrapper(
            papers.crx_abstract_click,
        )
        self.crx_abstract_hit = async_to_raw_response_wrapper(
            papers.crx_abstract_hit,
        )
        self.crx_pdf_click = async_to_raw_response_wrapper(
            papers.crx_pdf_click,
        )
        self.crx_pdf_hit = async_to_raw_response_wrapper(
            papers.crx_pdf_hit,
        )
        self.email_author = async_to_raw_response_wrapper(
            papers.email_author,
        )
        self.get_crx_paper_info = async_to_raw_response_wrapper(
            papers.get_crx_paper_info,
        )
        self.get_paper_info = async_to_raw_response_wrapper(
            papers.get_paper_info,
        )
        self.kickoff_abstract_embed = async_to_raw_response_wrapper(
            papers.kickoff_abstract_embed,
        )
        self.kickoff_ai = async_to_raw_response_wrapper(
            papers.kickoff_ai,
        )
        self.kickoff_bibtex = async_to_raw_response_wrapper(
            papers.kickoff_bibtex,
        )
        self.kickoff_github = async_to_raw_response_wrapper(
            papers.kickoff_github,
        )
        self.kickoff_paper_categorization = async_to_raw_response_wrapper(
            papers.kickoff_paper_categorization,
        )
        self.kickoff_recent_papers = async_to_raw_response_wrapper(
            papers.kickoff_recent_papers,
        )
        self.mark_viewed = async_to_raw_response_wrapper(
            papers.mark_viewed,
        )
        self.process_abstract_embed = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                papers.process_abstract_embed,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_metadata = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                papers.process_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.request_ai_latest = async_to_raw_response_wrapper(
            papers.request_ai_latest,
        )
        self.request_ai_translation_latest = async_to_raw_response_wrapper(
            papers.request_ai_translation_latest,
        )
        self.set_github_repository = async_to_raw_response_wrapper(
            papers.set_github_repository,
        )
        self.toggle_follow = async_to_raw_response_wrapper(
            papers.toggle_follow,
        )
        self.translate_ai_overview = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                papers.translate_ai_overview,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unclaim = async_to_raw_response_wrapper(
            papers.unclaim,
        )
        self.vote = async_to_raw_response_wrapper(
            papers.vote,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._papers.versions)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._papers.metadata)

    @cached_property
    def ingest(self) -> AsyncIngestResourceWithRawResponse:
        return AsyncIngestResourceWithRawResponse(self._papers.ingest)

    @cached_property
    def private(self) -> AsyncPrivateResourceWithRawResponse:
        return AsyncPrivateResourceWithRawResponse(self._papers.private)

    @cached_property
    def kickoff_daily_github_stars(self) -> AsyncKickoffDailyGitHubStarsResourceWithRawResponse:
        return AsyncKickoffDailyGitHubStarsResourceWithRawResponse(self._papers.kickoff_daily_github_stars)

    @cached_property
    def v3(self) -> AsyncV3ResourceWithRawResponse:
        return AsyncV3ResourceWithRawResponse(self._papers.v3)

    @cached_property
    def v2(self) -> AsyncV2ResourceWithRawResponse:
        return AsyncV2ResourceWithRawResponse(self._papers.v2)


class PapersResourceWithStreamingResponse:
    def __init__(self, papers: PapersResource) -> None:
        self._papers = papers

        self.add_author = to_streamed_response_wrapper(
            papers.add_author,
        )
        self.admin_vote = to_streamed_response_wrapper(
            papers.admin_vote,
        )
        self.crx_abstract_click = to_streamed_response_wrapper(
            papers.crx_abstract_click,
        )
        self.crx_abstract_hit = to_streamed_response_wrapper(
            papers.crx_abstract_hit,
        )
        self.crx_pdf_click = to_streamed_response_wrapper(
            papers.crx_pdf_click,
        )
        self.crx_pdf_hit = to_streamed_response_wrapper(
            papers.crx_pdf_hit,
        )
        self.email_author = to_streamed_response_wrapper(
            papers.email_author,
        )
        self.get_crx_paper_info = to_streamed_response_wrapper(
            papers.get_crx_paper_info,
        )
        self.get_paper_info = to_streamed_response_wrapper(
            papers.get_paper_info,
        )
        self.kickoff_abstract_embed = to_streamed_response_wrapper(
            papers.kickoff_abstract_embed,
        )
        self.kickoff_ai = to_streamed_response_wrapper(
            papers.kickoff_ai,
        )
        self.kickoff_bibtex = to_streamed_response_wrapper(
            papers.kickoff_bibtex,
        )
        self.kickoff_github = to_streamed_response_wrapper(
            papers.kickoff_github,
        )
        self.kickoff_paper_categorization = to_streamed_response_wrapper(
            papers.kickoff_paper_categorization,
        )
        self.kickoff_recent_papers = to_streamed_response_wrapper(
            papers.kickoff_recent_papers,
        )
        self.mark_viewed = to_streamed_response_wrapper(
            papers.mark_viewed,
        )
        self.process_abstract_embed = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                papers.process_abstract_embed,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_metadata = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                papers.process_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.request_ai_latest = to_streamed_response_wrapper(
            papers.request_ai_latest,
        )
        self.request_ai_translation_latest = to_streamed_response_wrapper(
            papers.request_ai_translation_latest,
        )
        self.set_github_repository = to_streamed_response_wrapper(
            papers.set_github_repository,
        )
        self.toggle_follow = to_streamed_response_wrapper(
            papers.toggle_follow,
        )
        self.translate_ai_overview = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                papers.translate_ai_overview,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unclaim = to_streamed_response_wrapper(
            papers.unclaim,
        )
        self.vote = to_streamed_response_wrapper(
            papers.vote,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._papers.versions)

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._papers.metadata)

    @cached_property
    def ingest(self) -> IngestResourceWithStreamingResponse:
        return IngestResourceWithStreamingResponse(self._papers.ingest)

    @cached_property
    def private(self) -> PrivateResourceWithStreamingResponse:
        return PrivateResourceWithStreamingResponse(self._papers.private)

    @cached_property
    def kickoff_daily_github_stars(self) -> KickoffDailyGitHubStarsResourceWithStreamingResponse:
        return KickoffDailyGitHubStarsResourceWithStreamingResponse(self._papers.kickoff_daily_github_stars)

    @cached_property
    def v3(self) -> V3ResourceWithStreamingResponse:
        return V3ResourceWithStreamingResponse(self._papers.v3)

    @cached_property
    def v2(self) -> V2ResourceWithStreamingResponse:
        return V2ResourceWithStreamingResponse(self._papers.v2)


class AsyncPapersResourceWithStreamingResponse:
    def __init__(self, papers: AsyncPapersResource) -> None:
        self._papers = papers

        self.add_author = async_to_streamed_response_wrapper(
            papers.add_author,
        )
        self.admin_vote = async_to_streamed_response_wrapper(
            papers.admin_vote,
        )
        self.crx_abstract_click = async_to_streamed_response_wrapper(
            papers.crx_abstract_click,
        )
        self.crx_abstract_hit = async_to_streamed_response_wrapper(
            papers.crx_abstract_hit,
        )
        self.crx_pdf_click = async_to_streamed_response_wrapper(
            papers.crx_pdf_click,
        )
        self.crx_pdf_hit = async_to_streamed_response_wrapper(
            papers.crx_pdf_hit,
        )
        self.email_author = async_to_streamed_response_wrapper(
            papers.email_author,
        )
        self.get_crx_paper_info = async_to_streamed_response_wrapper(
            papers.get_crx_paper_info,
        )
        self.get_paper_info = async_to_streamed_response_wrapper(
            papers.get_paper_info,
        )
        self.kickoff_abstract_embed = async_to_streamed_response_wrapper(
            papers.kickoff_abstract_embed,
        )
        self.kickoff_ai = async_to_streamed_response_wrapper(
            papers.kickoff_ai,
        )
        self.kickoff_bibtex = async_to_streamed_response_wrapper(
            papers.kickoff_bibtex,
        )
        self.kickoff_github = async_to_streamed_response_wrapper(
            papers.kickoff_github,
        )
        self.kickoff_paper_categorization = async_to_streamed_response_wrapper(
            papers.kickoff_paper_categorization,
        )
        self.kickoff_recent_papers = async_to_streamed_response_wrapper(
            papers.kickoff_recent_papers,
        )
        self.mark_viewed = async_to_streamed_response_wrapper(
            papers.mark_viewed,
        )
        self.process_abstract_embed = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                papers.process_abstract_embed,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_metadata = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                papers.process_metadata,  # pyright: ignore[reportDeprecated],
            )
        )
        self.request_ai_latest = async_to_streamed_response_wrapper(
            papers.request_ai_latest,
        )
        self.request_ai_translation_latest = async_to_streamed_response_wrapper(
            papers.request_ai_translation_latest,
        )
        self.set_github_repository = async_to_streamed_response_wrapper(
            papers.set_github_repository,
        )
        self.toggle_follow = async_to_streamed_response_wrapper(
            papers.toggle_follow,
        )
        self.translate_ai_overview = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                papers.translate_ai_overview,  # pyright: ignore[reportDeprecated],
            )
        )
        self.unclaim = async_to_streamed_response_wrapper(
            papers.unclaim,
        )
        self.vote = async_to_streamed_response_wrapper(
            papers.vote,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._papers.versions)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._papers.metadata)

    @cached_property
    def ingest(self) -> AsyncIngestResourceWithStreamingResponse:
        return AsyncIngestResourceWithStreamingResponse(self._papers.ingest)

    @cached_property
    def private(self) -> AsyncPrivateResourceWithStreamingResponse:
        return AsyncPrivateResourceWithStreamingResponse(self._papers.private)

    @cached_property
    def kickoff_daily_github_stars(self) -> AsyncKickoffDailyGitHubStarsResourceWithStreamingResponse:
        return AsyncKickoffDailyGitHubStarsResourceWithStreamingResponse(self._papers.kickoff_daily_github_stars)

    @cached_property
    def v3(self) -> AsyncV3ResourceWithStreamingResponse:
        return AsyncV3ResourceWithStreamingResponse(self._papers.v3)

    @cached_property
    def v2(self) -> AsyncV2ResourceWithStreamingResponse:
        return AsyncV2ResourceWithStreamingResponse(self._papers.v2)
