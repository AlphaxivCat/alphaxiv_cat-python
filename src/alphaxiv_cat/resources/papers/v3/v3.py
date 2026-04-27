# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Optional
from typing_extensions import Literal

import httpx

from .legacy import (
    LegacyResource,
    AsyncLegacyResource,
    LegacyResourceWithRawResponse,
    AsyncLegacyResourceWithRawResponse,
    LegacyResourceWithStreamingResponse,
    AsyncLegacyResourceWithStreamingResponse,
)
from .overview import (
    OverviewResource,
    AsyncOverviewResource,
    OverviewResourceWithRawResponse,
    AsyncOverviewResourceWithRawResponse,
    OverviewResourceWithStreamingResponse,
    AsyncOverviewResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .x_mentions import (
    XMentionsResource,
    AsyncXMentionsResource,
    XMentionsResourceWithRawResponse,
    AsyncXMentionsResourceWithRawResponse,
    XMentionsResourceWithStreamingResponse,
    AsyncXMentionsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.papers import (
    v3_comment_params,
    v3_process_ai_params,
    v3_retrieve_all_params,
    v3_retrieve_feed_params,
    v3_implementation_params,
    v3_process_countries_params,
    v3_process_full_text_params,
    v3_retrieve_unrelated_params,
    v3_retrieve_geo_trends_params,
    v3_request_implementation_params,
    v3_kickoff_paper_countries_params,
    v3_kickoff_paper_full_text_params,
    v3_kickoff_x_mentions_sync_params,
    v3_retrieve_diverse_papers_params,
    v3_retrieve_similar_papers_params,
    v3_retrieve_papers_by_country_params,
)
from .implementations import (
    ImplementationsResource,
    AsyncImplementationsResource,
    ImplementationsResourceWithRawResponse,
    AsyncImplementationsResourceWithRawResponse,
    ImplementationsResourceWithStreamingResponse,
    AsyncImplementationsResourceWithStreamingResponse,
)
from ....types.papers.v3_like_response import V3LikeResponse
from ....types.papers.v3_comment_response import V3CommentResponse
from ....types.papers.v3_retrieve_response import V3RetrieveResponse
from ....types.papers.v3_retrieve_all_response import V3RetrieveAllResponse
from ....types.papers.v3_retrieve_feed_response import V3RetrieveFeedResponse
from ....types.papers.v3_implementation_response import V3ImplementationResponse
from ....types.papers.v3_request_podcast_response import V3RequestPodcastResponse
from ....types.papers.v3_retrieve_figures_response import V3RetrieveFiguresResponse
from ....types.papers.v3_retrieve_metrics_response import V3RetrieveMetricsResponse
from ....types.papers.v3_retrieve_preview_response import V3RetrievePreviewResponse
from ....types.papers.v3_retrieve_full_text_response import V3RetrieveFullTextResponse
from ....types.papers.v3_retrieve_unrelated_response import V3RetrieveUnrelatedResponse
from ....types.papers.v3_retrieve_geo_trends_response import V3RetrieveGeoTrendsResponse
from ....types.papers.v3_request_implementation_response import V3RequestImplementationResponse
from ....types.papers.v3_retrieve_diverse_papers_response import V3RetrieveDiversePapersResponse
from ....types.papers.v3_retrieve_similar_papers_response import V3RetrieveSimilarPapersResponse
from ....types.papers.v3_prune_embeddings_by_date_response import V3PruneEmbeddingsByDateResponse
from ....types.papers.v3_retrieve_papers_by_country_response import V3RetrievePapersByCountryResponse
from ....types.papers.v3_kickoff_thumbnails_trending_papers_response import V3KickoffThumbnailsTrendingPapersResponse

__all__ = ["V3Resource", "AsyncV3Resource"]


class V3Resource(SyncAPIResource):
    @cached_property
    def legacy(self) -> LegacyResource:
        return LegacyResource(self._client)

    @cached_property
    def overview(self) -> OverviewResource:
        return OverviewResource(self._client)

    @cached_property
    def implementations(self) -> ImplementationsResource:
        return ImplementationsResource(self._client)

    @cached_property
    def x_mentions(self) -> XMentionsResource:
        return XMentionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return V3ResourceWithStreamingResponse(self)

    def retrieve(
        self,
        unresolved: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveResponse:
        """Retrieve paper version metadata.

        Fetches from ArXiv if needed.

        Source file: `api-server/src/controllers/papers/v3/get-paper.controller.ts`

        Args:
          unresolved: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unresolved:
            raise ValueError(f"Expected a non-empty value for `unresolved` but received {unresolved!r}")
        return self._get(
            path_template("/papers/v3/{unresolved}", unresolved=unresolved),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RetrieveResponse,
        )

    def comment(
        self,
        version: str,
        *,
        tag: Literal["anonymous", "general", "personal", "research", "resources"],
        body: Optional[str] | Omit = omit,
        parent: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3CommentResponse:
        """
        Create a public comment or private note on a paper.

        Source file: `api-server/src/controllers/papers/v3/post-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._post(
            path_template("/papers/v3/{version}/comment", version=version),
            body=maybe_transform(
                {
                    "tag": tag,
                    "body": body,
                    "parent": parent,
                    "title": title,
                },
                v3_comment_params.V3CommentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3CommentResponse,
        )

    def delete_votes(
        self,
        *,
        body: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove votes from many papers at once

        Source file:
        `api-server/src/controllers/papers/v3/remove-vote-batch.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/papers/v3/votes",
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def implementation(
        self,
        paper_group_id: str,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3ImplementationResponse:
        """
        Create or update an implementation for a paper group

        Source file:
        `api-server/src/controllers/papers/v3/create-or-update-implementation.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return self._post(
            path_template("/papers/v3/{paper_group_id}/implementation", paper_group_id=paper_group_id),
            body=maybe_transform({"url": url}, v3_implementation_params.V3ImplementationParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3ImplementationResponse,
        )

    def kickoff_paper_countries(
        self,
        *,
        batch: float | Omit = omit,
        max_papers: float | Omit = omit,
        months: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Kickoff paper countries processing for hot papers

        Source file:
        `api-server/src/controllers/papers/v3/kickoff-paper-countries.controller.ts`

        Args:
          batch: Number of papers to process in each batch

          max_papers: Maximum number of papers to process

          months: Only process papers at least this many months old

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/papers/v3/kickoff-paper-countries",
            body=maybe_transform(
                {
                    "batch": batch,
                    "max_papers": max_papers,
                    "months": months,
                },
                v3_kickoff_paper_countries_params.V3KickoffPaperCountriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def kickoff_paper_full_text(
        self,
        *,
        max_papers: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Kickoff paper full text processing for recent papers

        Source file:
        `api-server/src/controllers/papers/v3/kickoff-paper-full-text.controller.ts`

        Args:
          max_papers: Maximum number of paper versions to process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/papers/v3/kickoff-paper-full-text",
            body=maybe_transform(
                {"max_papers": max_papers}, v3_kickoff_paper_full_text_params.V3KickoffPaperFullTextParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def kickoff_paper_podcasts(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Kickoff paper podcasts on Uptash for a subset of paper groups

        Source file:
        `api-server/src/controllers/papers/v3/kickoff-paper-podcasts.controller.ts`
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/papers/v3/kickoff-paper-podcasts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def kickoff_thumbnails_trending_papers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3KickoffThumbnailsTrendingPapersResponse:
        """
        Kickoff background job to generate thumbnails for trending papers

        Source file:
        `api-server/src/controllers/papers/v3/kickoff-thumbnails-trending-papers.controller.ts`
        """
        return self._post(
            "/papers/v3/kickoff-thumbnails-trending-papers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3KickoffThumbnailsTrendingPapersResponse,
        )

    def kickoff_x_mentions_sync(
        self,
        *,
        dry_run: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Kickoff X mentions sync for hot papers.

        Uses x-mentions-sync-queue with
        parallelism=1 and built-in delays.

        Source file:
        `api-server/src/controllers/papers/v3/kickoff-x-mentions-sync.controller.ts`

        Args:
          dry_run: If true, only logs papers without queuing

          limit: Number of hot papers to sync (default: 500)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/papers/v3/kickoff-x-mentions-sync",
            body=maybe_transform(
                {
                    "dry_run": dry_run,
                    "limit": limit,
                },
                v3_kickoff_x_mentions_sync_params.V3KickoffXMentionsSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def like(
        self,
        group: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3LikeResponse:
        """
        Toggle your like status on a paper group

        Source file: `api-server/src/controllers/papers/v3/like-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group:
            raise ValueError(f"Expected a non-empty value for `group` but received {group!r}")
        return self._post(
            path_template("/papers/v3/{group}/like", group=group),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3LikeResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def podcast(
        self,
        paper_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Generates a podcast for a paper group

        Source file:
        `api-server/src/controllers/papers/v3/generate-paper-podcast.controller.ts`

        Args:
          paper_group_id: Paper Group ID to generate a podcast for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/papers/v3/{paper_group_id}/podcast", paper_group_id=paper_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def process_ai(
        self,
        paper_version_id: str,
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
    ) -> None:
        """
        Generates AI overviews for a paper version

        Source file: `api-server/src/controllers/papers/v3/process-ai.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_version_id:
            raise ValueError(f"Expected a non-empty value for `paper_version_id` but received {paper_version_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/papers/v3/{paper_version_id}/process-ai", paper_version_id=paper_version_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"preferred_language": preferred_language}, v3_process_ai_params.V3ProcessAIParams
                ),
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def process_countries(
        self,
        *,
        universal_paper_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Processes and generates country metadata for papers based on institutional
        affiliations

        Source file:
        `api-server/src/controllers/papers/v3/process-countries.controller.ts`

        Args:
          universal_paper_ids: Array of universal paper IDs (versionless)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/papers/v3/process-countries",
            body=maybe_transform(
                {"universal_paper_ids": universal_paper_ids}, v3_process_countries_params.V3ProcessCountriesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def process_full_text(
        self,
        *,
        paper_version_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Processes and extracts full text from paper PDFs for indexing and search

        Source file:
        `api-server/src/controllers/papers/v3/process-full-text.controller.ts`

        Args:
          paper_version_id: Paper version ID to process for full text extraction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/papers/v3/process-full-text",
            body=maybe_transform(
                {"paper_version_id": paper_version_id}, v3_process_full_text_params.V3ProcessFullTextParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def prune_embeddings_by_date(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3PruneEmbeddingsByDateResponse:
        """
        Clear 'is_last_X_days' flags from paper embeddings that have become too old

        Source file:
        `api-server/src/controllers/papers/v3/prune-embeddings-by-date.controller.ts`
        """
        return self._post(
            "/papers/v3/prune-embeddings-by-date",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3PruneEmbeddingsByDateResponse,
        )

    def request_implementation(
        self,
        group: str,
        *,
        paper_title: str,
        universal_paper_id: str,
        additional_info: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RequestImplementationResponse:
        """
        Toggle your implementation request status on a paper group

        Source file:
        `api-server/src/controllers/papers/v3/request-paper-implementation.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group:
            raise ValueError(f"Expected a non-empty value for `group` but received {group!r}")
        return self._post(
            path_template("/papers/v3/{group}/request-implementation", group=group),
            body=maybe_transform(
                {
                    "paper_title": paper_title,
                    "universal_paper_id": universal_paper_id,
                    "additional_info": additional_info,
                },
                v3_request_implementation_params.V3RequestImplementationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RequestImplementationResponse,
        )

    def request_podcast(
        self,
        paper_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RequestPodcastResponse:
        """
        Request podcast generation for a paper group

        Source file:
        `api-server/src/controllers/papers/v3/request-podcast.controller.ts`

        Args:
          paper_group_id: Paper Group ID to generate a podcast for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return self._post(
            path_template("/papers/v3/{paper_group_id}/request-podcast", paper_group_id=paper_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RequestPodcastResponse,
        )

    def retrieve_all(
        self,
        *,
        limit: str | Omit = omit,
        skip: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveAllResponse:
        """
        Get all paper universal IDs sorted by most recent publication date

        Source file: `api-server/src/controllers/papers/v3/get-all-papers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/papers/v3/all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    v3_retrieve_all_params.V3RetrieveAllParams,
                ),
            ),
            cast_to=V3RetrieveAllResponse,
        )

    def retrieve_diverse_papers(
        self,
        *,
        topics: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveDiversePapersResponse:
        """
        Get an initial batch of diverse papers on the given topics for recommendations

        Source file: `api-server/src/controllers/papers/v3/diverse-papers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/papers/v3/diverse-papers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"topics": topics}, v3_retrieve_diverse_papers_params.V3RetrieveDiversePapersParams
                ),
            ),
            cast_to=V3RetrieveDiversePapersResponse,
        )

    def retrieve_feed(
        self,
        *,
        interval: Literal["3 Days", "7 Days", "30 Days", "90 Days", "All time"],
        page_num: str,
        page_size: str,
        sort: Literal["Hot", "Comments", "Views", "Likes", "GitHub", "Twitter (X)", "Recommended"],
        organizations: str | Omit = omit,
        source: Literal["GitHub", "Twitter (X)"] | Omit = omit,
        topics: str | Omit = omit,
        universal_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveFeedResponse:
        """
        Get an optionally filtered list of papers for the main feed

        Source file: `api-server/src/controllers/papers/v3/feed.controller.ts`

        Args:
          universal_id: A versionless universal paper ID (e.g. 1706.03762)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/papers/v3/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "interval": interval,
                        "page_num": page_num,
                        "page_size": page_size,
                        "sort": sort,
                        "organizations": organizations,
                        "source": source,
                        "topics": topics,
                        "universal_id": universal_id,
                    },
                    v3_retrieve_feed_params.V3RetrieveFeedParams,
                ),
            ),
            cast_to=V3RetrieveFeedResponse,
        )

    def retrieve_figures(
        self,
        paper_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveFiguresResponse:
        """
        Get list of figure URLs for a paper

        Source file:
        `api-server/src/controllers/papers/v3/get-paper-figures.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return self._get(
            path_template("/papers/v3/{paper_group_id}/figures", paper_group_id=paper_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RetrieveFiguresResponse,
        )

    def retrieve_full_text(
        self,
        paper_version: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveFullTextResponse:
        """
        Get the full extracted text of a paper, page by page

        Source file: `api-server/src/controllers/papers/v3/get-full-text.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_version:
            raise ValueError(f"Expected a non-empty value for `paper_version` but received {paper_version!r}")
        return self._get(
            path_template("/papers/v3/{paper_version}/full-text", paper_version=paper_version),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RetrieveFullTextResponse,
        )

    def retrieve_geo_trends(
        self,
        *,
        collaboration_limit: str | Omit = omit,
        paper_limit: str | Omit = omit,
        past_months: str | Omit = omit,
        repo_limit: str | Omit = omit,
        top_countries: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveGeoTrendsResponse:
        """
        Retrieve geographical trends and analytics data for papers

        Source file: `api-server/src/controllers/papers/v3/get-geo-trends.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/papers/v3/geo-trends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collaboration_limit": collaboration_limit,
                        "paper_limit": paper_limit,
                        "past_months": past_months,
                        "repo_limit": repo_limit,
                        "top_countries": top_countries,
                    },
                    v3_retrieve_geo_trends_params.V3RetrieveGeoTrendsParams,
                ),
            ),
            cast_to=V3RetrieveGeoTrendsResponse,
        )

    def retrieve_metrics(
        self,
        unresolved: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveMetricsResponse:
        """
        Retrieve metrics for a paper (comments count, upvotes, views)

        Source file: `api-server/src/controllers/papers/v3/get-metrics.controller.ts`

        Args:
          unresolved: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unresolved:
            raise ValueError(f"Expected a non-empty value for `unresolved` but received {unresolved!r}")
        return self._get(
            path_template("/papers/v3/{unresolved}/metrics", unresolved=unresolved),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RetrieveMetricsResponse,
        )

    def retrieve_papers_by_country(
        self,
        *,
        country: str | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrievePapersByCountryResponse:
        """
        Retrieve top papers by country with optional country filter

        Source file:
        `api-server/src/controllers/papers/v3/get-papers-by-country.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/papers/v3/papers-by-country",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "limit": limit,
                    },
                    v3_retrieve_papers_by_country_params.V3RetrievePapersByCountryParams,
                ),
            ),
            cast_to=V3RetrievePapersByCountryResponse,
        )

    def retrieve_preview(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrievePreviewResponse:
        """
        Retrieve paper data for paper preview cards

        Source file:
        `api-server/src/controllers/papers/v3/get-paper-preview.controller.ts`

        Args:
          id: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/papers/v3/{id}/preview", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RetrievePreviewResponse,
        )

    def retrieve_similar_papers(
        self,
        id: str,
        *,
        exclude: str | Omit = omit,
        exclude_likes: Literal["false", "true"] | Omit = omit,
        interval: Literal["3 Days", "7 Days", "30 Days", "90 Days", "All time"] | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveSimilarPapersResponse:
        """
        Get papers semantically similar to the selected one

        Source file:
        `api-server/src/controllers/papers/v3/get-similar-papers.controller.ts`

        Args:
          id: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/papers/v3/{id}/similar-papers", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude": exclude,
                        "exclude_likes": exclude_likes,
                        "interval": interval,
                        "limit": limit,
                    },
                    v3_retrieve_similar_papers_params.V3RetrieveSimilarPapersParams,
                ),
            ),
            cast_to=V3RetrieveSimilarPapersResponse,
        )

    def retrieve_unrelated(
        self,
        *,
        limit: str,
        papers: str,
        topics: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveUnrelatedResponse:
        """
        Get some papers on the provided topics that are unrelated to the provided papers

        Source file:
        `api-server/src/controllers/papers/v3/unrelated-papers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/papers/v3/unrelated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "papers": papers,
                        "topics": topics,
                    },
                    v3_retrieve_unrelated_params.V3RetrieveUnrelatedParams,
                ),
            ),
            cast_to=V3RetrieveUnrelatedResponse,
        )

    def view(
        self,
        group: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Track paper view event for analytics

        Source file:
        `api-server/src/controllers/papers/v3/mark-paper-view.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group:
            raise ValueError(f"Expected a non-empty value for `group` but received {group!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/papers/v3/{group}/view", group=group),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncV3Resource(AsyncAPIResource):
    @cached_property
    def legacy(self) -> AsyncLegacyResource:
        return AsyncLegacyResource(self._client)

    @cached_property
    def overview(self) -> AsyncOverviewResource:
        return AsyncOverviewResource(self._client)

    @cached_property
    def implementations(self) -> AsyncImplementationsResource:
        return AsyncImplementationsResource(self._client)

    @cached_property
    def x_mentions(self) -> AsyncXMentionsResource:
        return AsyncXMentionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV3ResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        unresolved: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveResponse:
        """Retrieve paper version metadata.

        Fetches from ArXiv if needed.

        Source file: `api-server/src/controllers/papers/v3/get-paper.controller.ts`

        Args:
          unresolved: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unresolved:
            raise ValueError(f"Expected a non-empty value for `unresolved` but received {unresolved!r}")
        return await self._get(
            path_template("/papers/v3/{unresolved}", unresolved=unresolved),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RetrieveResponse,
        )

    async def comment(
        self,
        version: str,
        *,
        tag: Literal["anonymous", "general", "personal", "research", "resources"],
        body: Optional[str] | Omit = omit,
        parent: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3CommentResponse:
        """
        Create a public comment or private note on a paper.

        Source file: `api-server/src/controllers/papers/v3/post-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return await self._post(
            path_template("/papers/v3/{version}/comment", version=version),
            body=await async_maybe_transform(
                {
                    "tag": tag,
                    "body": body,
                    "parent": parent,
                    "title": title,
                },
                v3_comment_params.V3CommentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3CommentResponse,
        )

    async def delete_votes(
        self,
        *,
        body: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove votes from many papers at once

        Source file:
        `api-server/src/controllers/papers/v3/remove-vote-batch.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/papers/v3/votes",
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def implementation(
        self,
        paper_group_id: str,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3ImplementationResponse:
        """
        Create or update an implementation for a paper group

        Source file:
        `api-server/src/controllers/papers/v3/create-or-update-implementation.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return await self._post(
            path_template("/papers/v3/{paper_group_id}/implementation", paper_group_id=paper_group_id),
            body=await async_maybe_transform({"url": url}, v3_implementation_params.V3ImplementationParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3ImplementationResponse,
        )

    async def kickoff_paper_countries(
        self,
        *,
        batch: float | Omit = omit,
        max_papers: float | Omit = omit,
        months: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Kickoff paper countries processing for hot papers

        Source file:
        `api-server/src/controllers/papers/v3/kickoff-paper-countries.controller.ts`

        Args:
          batch: Number of papers to process in each batch

          max_papers: Maximum number of papers to process

          months: Only process papers at least this many months old

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/papers/v3/kickoff-paper-countries",
            body=await async_maybe_transform(
                {
                    "batch": batch,
                    "max_papers": max_papers,
                    "months": months,
                },
                v3_kickoff_paper_countries_params.V3KickoffPaperCountriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def kickoff_paper_full_text(
        self,
        *,
        max_papers: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Kickoff paper full text processing for recent papers

        Source file:
        `api-server/src/controllers/papers/v3/kickoff-paper-full-text.controller.ts`

        Args:
          max_papers: Maximum number of paper versions to process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/papers/v3/kickoff-paper-full-text",
            body=await async_maybe_transform(
                {"max_papers": max_papers}, v3_kickoff_paper_full_text_params.V3KickoffPaperFullTextParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def kickoff_paper_podcasts(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Kickoff paper podcasts on Uptash for a subset of paper groups

        Source file:
        `api-server/src/controllers/papers/v3/kickoff-paper-podcasts.controller.ts`
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/papers/v3/kickoff-paper-podcasts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def kickoff_thumbnails_trending_papers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3KickoffThumbnailsTrendingPapersResponse:
        """
        Kickoff background job to generate thumbnails for trending papers

        Source file:
        `api-server/src/controllers/papers/v3/kickoff-thumbnails-trending-papers.controller.ts`
        """
        return await self._post(
            "/papers/v3/kickoff-thumbnails-trending-papers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3KickoffThumbnailsTrendingPapersResponse,
        )

    async def kickoff_x_mentions_sync(
        self,
        *,
        dry_run: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Kickoff X mentions sync for hot papers.

        Uses x-mentions-sync-queue with
        parallelism=1 and built-in delays.

        Source file:
        `api-server/src/controllers/papers/v3/kickoff-x-mentions-sync.controller.ts`

        Args:
          dry_run: If true, only logs papers without queuing

          limit: Number of hot papers to sync (default: 500)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/papers/v3/kickoff-x-mentions-sync",
            body=await async_maybe_transform(
                {
                    "dry_run": dry_run,
                    "limit": limit,
                },
                v3_kickoff_x_mentions_sync_params.V3KickoffXMentionsSyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def like(
        self,
        group: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3LikeResponse:
        """
        Toggle your like status on a paper group

        Source file: `api-server/src/controllers/papers/v3/like-paper.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group:
            raise ValueError(f"Expected a non-empty value for `group` but received {group!r}")
        return await self._post(
            path_template("/papers/v3/{group}/like", group=group),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3LikeResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def podcast(
        self,
        paper_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Generates a podcast for a paper group

        Source file:
        `api-server/src/controllers/papers/v3/generate-paper-podcast.controller.ts`

        Args:
          paper_group_id: Paper Group ID to generate a podcast for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/papers/v3/{paper_group_id}/podcast", paper_group_id=paper_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def process_ai(
        self,
        paper_version_id: str,
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
    ) -> None:
        """
        Generates AI overviews for a paper version

        Source file: `api-server/src/controllers/papers/v3/process-ai.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_version_id:
            raise ValueError(f"Expected a non-empty value for `paper_version_id` but received {paper_version_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/papers/v3/{paper_version_id}/process-ai", paper_version_id=paper_version_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"preferred_language": preferred_language}, v3_process_ai_params.V3ProcessAIParams
                ),
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def process_countries(
        self,
        *,
        universal_paper_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Processes and generates country metadata for papers based on institutional
        affiliations

        Source file:
        `api-server/src/controllers/papers/v3/process-countries.controller.ts`

        Args:
          universal_paper_ids: Array of universal paper IDs (versionless)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/papers/v3/process-countries",
            body=await async_maybe_transform(
                {"universal_paper_ids": universal_paper_ids}, v3_process_countries_params.V3ProcessCountriesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def process_full_text(
        self,
        *,
        paper_version_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Processes and extracts full text from paper PDFs for indexing and search

        Source file:
        `api-server/src/controllers/papers/v3/process-full-text.controller.ts`

        Args:
          paper_version_id: Paper version ID to process for full text extraction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/papers/v3/process-full-text",
            body=await async_maybe_transform(
                {"paper_version_id": paper_version_id}, v3_process_full_text_params.V3ProcessFullTextParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def prune_embeddings_by_date(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3PruneEmbeddingsByDateResponse:
        """
        Clear 'is_last_X_days' flags from paper embeddings that have become too old

        Source file:
        `api-server/src/controllers/papers/v3/prune-embeddings-by-date.controller.ts`
        """
        return await self._post(
            "/papers/v3/prune-embeddings-by-date",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3PruneEmbeddingsByDateResponse,
        )

    async def request_implementation(
        self,
        group: str,
        *,
        paper_title: str,
        universal_paper_id: str,
        additional_info: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RequestImplementationResponse:
        """
        Toggle your implementation request status on a paper group

        Source file:
        `api-server/src/controllers/papers/v3/request-paper-implementation.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group:
            raise ValueError(f"Expected a non-empty value for `group` but received {group!r}")
        return await self._post(
            path_template("/papers/v3/{group}/request-implementation", group=group),
            body=await async_maybe_transform(
                {
                    "paper_title": paper_title,
                    "universal_paper_id": universal_paper_id,
                    "additional_info": additional_info,
                },
                v3_request_implementation_params.V3RequestImplementationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RequestImplementationResponse,
        )

    async def request_podcast(
        self,
        paper_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RequestPodcastResponse:
        """
        Request podcast generation for a paper group

        Source file:
        `api-server/src/controllers/papers/v3/request-podcast.controller.ts`

        Args:
          paper_group_id: Paper Group ID to generate a podcast for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return await self._post(
            path_template("/papers/v3/{paper_group_id}/request-podcast", paper_group_id=paper_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RequestPodcastResponse,
        )

    async def retrieve_all(
        self,
        *,
        limit: str | Omit = omit,
        skip: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveAllResponse:
        """
        Get all paper universal IDs sorted by most recent publication date

        Source file: `api-server/src/controllers/papers/v3/get-all-papers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/papers/v3/all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    v3_retrieve_all_params.V3RetrieveAllParams,
                ),
            ),
            cast_to=V3RetrieveAllResponse,
        )

    async def retrieve_diverse_papers(
        self,
        *,
        topics: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveDiversePapersResponse:
        """
        Get an initial batch of diverse papers on the given topics for recommendations

        Source file: `api-server/src/controllers/papers/v3/diverse-papers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/papers/v3/diverse-papers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"topics": topics}, v3_retrieve_diverse_papers_params.V3RetrieveDiversePapersParams
                ),
            ),
            cast_to=V3RetrieveDiversePapersResponse,
        )

    async def retrieve_feed(
        self,
        *,
        interval: Literal["3 Days", "7 Days", "30 Days", "90 Days", "All time"],
        page_num: str,
        page_size: str,
        sort: Literal["Hot", "Comments", "Views", "Likes", "GitHub", "Twitter (X)", "Recommended"],
        organizations: str | Omit = omit,
        source: Literal["GitHub", "Twitter (X)"] | Omit = omit,
        topics: str | Omit = omit,
        universal_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveFeedResponse:
        """
        Get an optionally filtered list of papers for the main feed

        Source file: `api-server/src/controllers/papers/v3/feed.controller.ts`

        Args:
          universal_id: A versionless universal paper ID (e.g. 1706.03762)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/papers/v3/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "interval": interval,
                        "page_num": page_num,
                        "page_size": page_size,
                        "sort": sort,
                        "organizations": organizations,
                        "source": source,
                        "topics": topics,
                        "universal_id": universal_id,
                    },
                    v3_retrieve_feed_params.V3RetrieveFeedParams,
                ),
            ),
            cast_to=V3RetrieveFeedResponse,
        )

    async def retrieve_figures(
        self,
        paper_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveFiguresResponse:
        """
        Get list of figure URLs for a paper

        Source file:
        `api-server/src/controllers/papers/v3/get-paper-figures.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_group_id:
            raise ValueError(f"Expected a non-empty value for `paper_group_id` but received {paper_group_id!r}")
        return await self._get(
            path_template("/papers/v3/{paper_group_id}/figures", paper_group_id=paper_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RetrieveFiguresResponse,
        )

    async def retrieve_full_text(
        self,
        paper_version: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveFullTextResponse:
        """
        Get the full extracted text of a paper, page by page

        Source file: `api-server/src/controllers/papers/v3/get-full-text.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not paper_version:
            raise ValueError(f"Expected a non-empty value for `paper_version` but received {paper_version!r}")
        return await self._get(
            path_template("/papers/v3/{paper_version}/full-text", paper_version=paper_version),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RetrieveFullTextResponse,
        )

    async def retrieve_geo_trends(
        self,
        *,
        collaboration_limit: str | Omit = omit,
        paper_limit: str | Omit = omit,
        past_months: str | Omit = omit,
        repo_limit: str | Omit = omit,
        top_countries: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveGeoTrendsResponse:
        """
        Retrieve geographical trends and analytics data for papers

        Source file: `api-server/src/controllers/papers/v3/get-geo-trends.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/papers/v3/geo-trends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "collaboration_limit": collaboration_limit,
                        "paper_limit": paper_limit,
                        "past_months": past_months,
                        "repo_limit": repo_limit,
                        "top_countries": top_countries,
                    },
                    v3_retrieve_geo_trends_params.V3RetrieveGeoTrendsParams,
                ),
            ),
            cast_to=V3RetrieveGeoTrendsResponse,
        )

    async def retrieve_metrics(
        self,
        unresolved: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveMetricsResponse:
        """
        Retrieve metrics for a paper (comments count, upvotes, views)

        Source file: `api-server/src/controllers/papers/v3/get-metrics.controller.ts`

        Args:
          unresolved: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not unresolved:
            raise ValueError(f"Expected a non-empty value for `unresolved` but received {unresolved!r}")
        return await self._get(
            path_template("/papers/v3/{unresolved}/metrics", unresolved=unresolved),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RetrieveMetricsResponse,
        )

    async def retrieve_papers_by_country(
        self,
        *,
        country: str | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrievePapersByCountryResponse:
        """
        Retrieve top papers by country with optional country filter

        Source file:
        `api-server/src/controllers/papers/v3/get-papers-by-country.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/papers/v3/papers-by-country",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "limit": limit,
                    },
                    v3_retrieve_papers_by_country_params.V3RetrievePapersByCountryParams,
                ),
            ),
            cast_to=V3RetrievePapersByCountryResponse,
        )

    async def retrieve_preview(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrievePreviewResponse:
        """
        Retrieve paper data for paper preview cards

        Source file:
        `api-server/src/controllers/papers/v3/get-paper-preview.controller.ts`

        Args:
          id: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/papers/v3/{id}/preview", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3RetrievePreviewResponse,
        )

    async def retrieve_similar_papers(
        self,
        id: str,
        *,
        exclude: str | Omit = omit,
        exclude_likes: Literal["false", "true"] | Omit = omit,
        interval: Literal["3 Days", "7 Days", "30 Days", "90 Days", "All time"] | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveSimilarPapersResponse:
        """
        Get papers semantically similar to the selected one

        Source file:
        `api-server/src/controllers/papers/v3/get-similar-papers.controller.ts`

        Args:
          id: An Unresolved Paper ID (UUID, ArXiv ID, or Versioned ArXiv ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/papers/v3/{id}/similar-papers", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exclude": exclude,
                        "exclude_likes": exclude_likes,
                        "interval": interval,
                        "limit": limit,
                    },
                    v3_retrieve_similar_papers_params.V3RetrieveSimilarPapersParams,
                ),
            ),
            cast_to=V3RetrieveSimilarPapersResponse,
        )

    async def retrieve_unrelated(
        self,
        *,
        limit: str,
        papers: str,
        topics: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3RetrieveUnrelatedResponse:
        """
        Get some papers on the provided topics that are unrelated to the provided papers

        Source file:
        `api-server/src/controllers/papers/v3/unrelated-papers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/papers/v3/unrelated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "papers": papers,
                        "topics": topics,
                    },
                    v3_retrieve_unrelated_params.V3RetrieveUnrelatedParams,
                ),
            ),
            cast_to=V3RetrieveUnrelatedResponse,
        )

    async def view(
        self,
        group: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Track paper view event for analytics

        Source file:
        `api-server/src/controllers/papers/v3/mark-paper-view.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group:
            raise ValueError(f"Expected a non-empty value for `group` but received {group!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/papers/v3/{group}/view", group=group),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class V3ResourceWithRawResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

        self.retrieve = to_raw_response_wrapper(
            v3.retrieve,
        )
        self.comment = to_raw_response_wrapper(
            v3.comment,
        )
        self.delete_votes = to_raw_response_wrapper(
            v3.delete_votes,
        )
        self.implementation = to_raw_response_wrapper(
            v3.implementation,
        )
        self.kickoff_paper_countries = to_raw_response_wrapper(
            v3.kickoff_paper_countries,
        )
        self.kickoff_paper_full_text = to_raw_response_wrapper(
            v3.kickoff_paper_full_text,
        )
        self.kickoff_paper_podcasts = to_raw_response_wrapper(
            v3.kickoff_paper_podcasts,
        )
        self.kickoff_thumbnails_trending_papers = to_raw_response_wrapper(
            v3.kickoff_thumbnails_trending_papers,
        )
        self.kickoff_x_mentions_sync = to_raw_response_wrapper(
            v3.kickoff_x_mentions_sync,
        )
        self.like = to_raw_response_wrapper(
            v3.like,
        )
        self.podcast = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                v3.podcast,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_ai = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                v3.process_ai,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_countries = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                v3.process_countries,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_full_text = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                v3.process_full_text,  # pyright: ignore[reportDeprecated],
            )
        )
        self.prune_embeddings_by_date = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                v3.prune_embeddings_by_date,  # pyright: ignore[reportDeprecated],
            )
        )
        self.request_implementation = to_raw_response_wrapper(
            v3.request_implementation,
        )
        self.request_podcast = to_raw_response_wrapper(
            v3.request_podcast,
        )
        self.retrieve_all = to_raw_response_wrapper(
            v3.retrieve_all,
        )
        self.retrieve_diverse_papers = to_raw_response_wrapper(
            v3.retrieve_diverse_papers,
        )
        self.retrieve_feed = to_raw_response_wrapper(
            v3.retrieve_feed,
        )
        self.retrieve_figures = to_raw_response_wrapper(
            v3.retrieve_figures,
        )
        self.retrieve_full_text = to_raw_response_wrapper(
            v3.retrieve_full_text,
        )
        self.retrieve_geo_trends = to_raw_response_wrapper(
            v3.retrieve_geo_trends,
        )
        self.retrieve_metrics = to_raw_response_wrapper(
            v3.retrieve_metrics,
        )
        self.retrieve_papers_by_country = to_raw_response_wrapper(
            v3.retrieve_papers_by_country,
        )
        self.retrieve_preview = to_raw_response_wrapper(
            v3.retrieve_preview,
        )
        self.retrieve_similar_papers = to_raw_response_wrapper(
            v3.retrieve_similar_papers,
        )
        self.retrieve_unrelated = to_raw_response_wrapper(
            v3.retrieve_unrelated,
        )
        self.view = to_raw_response_wrapper(
            v3.view,
        )

    @cached_property
    def legacy(self) -> LegacyResourceWithRawResponse:
        return LegacyResourceWithRawResponse(self._v3.legacy)

    @cached_property
    def overview(self) -> OverviewResourceWithRawResponse:
        return OverviewResourceWithRawResponse(self._v3.overview)

    @cached_property
    def implementations(self) -> ImplementationsResourceWithRawResponse:
        return ImplementationsResourceWithRawResponse(self._v3.implementations)

    @cached_property
    def x_mentions(self) -> XMentionsResourceWithRawResponse:
        return XMentionsResourceWithRawResponse(self._v3.x_mentions)


class AsyncV3ResourceWithRawResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

        self.retrieve = async_to_raw_response_wrapper(
            v3.retrieve,
        )
        self.comment = async_to_raw_response_wrapper(
            v3.comment,
        )
        self.delete_votes = async_to_raw_response_wrapper(
            v3.delete_votes,
        )
        self.implementation = async_to_raw_response_wrapper(
            v3.implementation,
        )
        self.kickoff_paper_countries = async_to_raw_response_wrapper(
            v3.kickoff_paper_countries,
        )
        self.kickoff_paper_full_text = async_to_raw_response_wrapper(
            v3.kickoff_paper_full_text,
        )
        self.kickoff_paper_podcasts = async_to_raw_response_wrapper(
            v3.kickoff_paper_podcasts,
        )
        self.kickoff_thumbnails_trending_papers = async_to_raw_response_wrapper(
            v3.kickoff_thumbnails_trending_papers,
        )
        self.kickoff_x_mentions_sync = async_to_raw_response_wrapper(
            v3.kickoff_x_mentions_sync,
        )
        self.like = async_to_raw_response_wrapper(
            v3.like,
        )
        self.podcast = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                v3.podcast,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_ai = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                v3.process_ai,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_countries = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                v3.process_countries,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_full_text = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                v3.process_full_text,  # pyright: ignore[reportDeprecated],
            )
        )
        self.prune_embeddings_by_date = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                v3.prune_embeddings_by_date,  # pyright: ignore[reportDeprecated],
            )
        )
        self.request_implementation = async_to_raw_response_wrapper(
            v3.request_implementation,
        )
        self.request_podcast = async_to_raw_response_wrapper(
            v3.request_podcast,
        )
        self.retrieve_all = async_to_raw_response_wrapper(
            v3.retrieve_all,
        )
        self.retrieve_diverse_papers = async_to_raw_response_wrapper(
            v3.retrieve_diverse_papers,
        )
        self.retrieve_feed = async_to_raw_response_wrapper(
            v3.retrieve_feed,
        )
        self.retrieve_figures = async_to_raw_response_wrapper(
            v3.retrieve_figures,
        )
        self.retrieve_full_text = async_to_raw_response_wrapper(
            v3.retrieve_full_text,
        )
        self.retrieve_geo_trends = async_to_raw_response_wrapper(
            v3.retrieve_geo_trends,
        )
        self.retrieve_metrics = async_to_raw_response_wrapper(
            v3.retrieve_metrics,
        )
        self.retrieve_papers_by_country = async_to_raw_response_wrapper(
            v3.retrieve_papers_by_country,
        )
        self.retrieve_preview = async_to_raw_response_wrapper(
            v3.retrieve_preview,
        )
        self.retrieve_similar_papers = async_to_raw_response_wrapper(
            v3.retrieve_similar_papers,
        )
        self.retrieve_unrelated = async_to_raw_response_wrapper(
            v3.retrieve_unrelated,
        )
        self.view = async_to_raw_response_wrapper(
            v3.view,
        )

    @cached_property
    def legacy(self) -> AsyncLegacyResourceWithRawResponse:
        return AsyncLegacyResourceWithRawResponse(self._v3.legacy)

    @cached_property
    def overview(self) -> AsyncOverviewResourceWithRawResponse:
        return AsyncOverviewResourceWithRawResponse(self._v3.overview)

    @cached_property
    def implementations(self) -> AsyncImplementationsResourceWithRawResponse:
        return AsyncImplementationsResourceWithRawResponse(self._v3.implementations)

    @cached_property
    def x_mentions(self) -> AsyncXMentionsResourceWithRawResponse:
        return AsyncXMentionsResourceWithRawResponse(self._v3.x_mentions)


class V3ResourceWithStreamingResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

        self.retrieve = to_streamed_response_wrapper(
            v3.retrieve,
        )
        self.comment = to_streamed_response_wrapper(
            v3.comment,
        )
        self.delete_votes = to_streamed_response_wrapper(
            v3.delete_votes,
        )
        self.implementation = to_streamed_response_wrapper(
            v3.implementation,
        )
        self.kickoff_paper_countries = to_streamed_response_wrapper(
            v3.kickoff_paper_countries,
        )
        self.kickoff_paper_full_text = to_streamed_response_wrapper(
            v3.kickoff_paper_full_text,
        )
        self.kickoff_paper_podcasts = to_streamed_response_wrapper(
            v3.kickoff_paper_podcasts,
        )
        self.kickoff_thumbnails_trending_papers = to_streamed_response_wrapper(
            v3.kickoff_thumbnails_trending_papers,
        )
        self.kickoff_x_mentions_sync = to_streamed_response_wrapper(
            v3.kickoff_x_mentions_sync,
        )
        self.like = to_streamed_response_wrapper(
            v3.like,
        )
        self.podcast = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                v3.podcast,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_ai = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                v3.process_ai,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_countries = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                v3.process_countries,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_full_text = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                v3.process_full_text,  # pyright: ignore[reportDeprecated],
            )
        )
        self.prune_embeddings_by_date = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                v3.prune_embeddings_by_date,  # pyright: ignore[reportDeprecated],
            )
        )
        self.request_implementation = to_streamed_response_wrapper(
            v3.request_implementation,
        )
        self.request_podcast = to_streamed_response_wrapper(
            v3.request_podcast,
        )
        self.retrieve_all = to_streamed_response_wrapper(
            v3.retrieve_all,
        )
        self.retrieve_diverse_papers = to_streamed_response_wrapper(
            v3.retrieve_diverse_papers,
        )
        self.retrieve_feed = to_streamed_response_wrapper(
            v3.retrieve_feed,
        )
        self.retrieve_figures = to_streamed_response_wrapper(
            v3.retrieve_figures,
        )
        self.retrieve_full_text = to_streamed_response_wrapper(
            v3.retrieve_full_text,
        )
        self.retrieve_geo_trends = to_streamed_response_wrapper(
            v3.retrieve_geo_trends,
        )
        self.retrieve_metrics = to_streamed_response_wrapper(
            v3.retrieve_metrics,
        )
        self.retrieve_papers_by_country = to_streamed_response_wrapper(
            v3.retrieve_papers_by_country,
        )
        self.retrieve_preview = to_streamed_response_wrapper(
            v3.retrieve_preview,
        )
        self.retrieve_similar_papers = to_streamed_response_wrapper(
            v3.retrieve_similar_papers,
        )
        self.retrieve_unrelated = to_streamed_response_wrapper(
            v3.retrieve_unrelated,
        )
        self.view = to_streamed_response_wrapper(
            v3.view,
        )

    @cached_property
    def legacy(self) -> LegacyResourceWithStreamingResponse:
        return LegacyResourceWithStreamingResponse(self._v3.legacy)

    @cached_property
    def overview(self) -> OverviewResourceWithStreamingResponse:
        return OverviewResourceWithStreamingResponse(self._v3.overview)

    @cached_property
    def implementations(self) -> ImplementationsResourceWithStreamingResponse:
        return ImplementationsResourceWithStreamingResponse(self._v3.implementations)

    @cached_property
    def x_mentions(self) -> XMentionsResourceWithStreamingResponse:
        return XMentionsResourceWithStreamingResponse(self._v3.x_mentions)


class AsyncV3ResourceWithStreamingResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

        self.retrieve = async_to_streamed_response_wrapper(
            v3.retrieve,
        )
        self.comment = async_to_streamed_response_wrapper(
            v3.comment,
        )
        self.delete_votes = async_to_streamed_response_wrapper(
            v3.delete_votes,
        )
        self.implementation = async_to_streamed_response_wrapper(
            v3.implementation,
        )
        self.kickoff_paper_countries = async_to_streamed_response_wrapper(
            v3.kickoff_paper_countries,
        )
        self.kickoff_paper_full_text = async_to_streamed_response_wrapper(
            v3.kickoff_paper_full_text,
        )
        self.kickoff_paper_podcasts = async_to_streamed_response_wrapper(
            v3.kickoff_paper_podcasts,
        )
        self.kickoff_thumbnails_trending_papers = async_to_streamed_response_wrapper(
            v3.kickoff_thumbnails_trending_papers,
        )
        self.kickoff_x_mentions_sync = async_to_streamed_response_wrapper(
            v3.kickoff_x_mentions_sync,
        )
        self.like = async_to_streamed_response_wrapper(
            v3.like,
        )
        self.podcast = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                v3.podcast,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_ai = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                v3.process_ai,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_countries = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                v3.process_countries,  # pyright: ignore[reportDeprecated],
            )
        )
        self.process_full_text = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                v3.process_full_text,  # pyright: ignore[reportDeprecated],
            )
        )
        self.prune_embeddings_by_date = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                v3.prune_embeddings_by_date,  # pyright: ignore[reportDeprecated],
            )
        )
        self.request_implementation = async_to_streamed_response_wrapper(
            v3.request_implementation,
        )
        self.request_podcast = async_to_streamed_response_wrapper(
            v3.request_podcast,
        )
        self.retrieve_all = async_to_streamed_response_wrapper(
            v3.retrieve_all,
        )
        self.retrieve_diverse_papers = async_to_streamed_response_wrapper(
            v3.retrieve_diverse_papers,
        )
        self.retrieve_feed = async_to_streamed_response_wrapper(
            v3.retrieve_feed,
        )
        self.retrieve_figures = async_to_streamed_response_wrapper(
            v3.retrieve_figures,
        )
        self.retrieve_full_text = async_to_streamed_response_wrapper(
            v3.retrieve_full_text,
        )
        self.retrieve_geo_trends = async_to_streamed_response_wrapper(
            v3.retrieve_geo_trends,
        )
        self.retrieve_metrics = async_to_streamed_response_wrapper(
            v3.retrieve_metrics,
        )
        self.retrieve_papers_by_country = async_to_streamed_response_wrapper(
            v3.retrieve_papers_by_country,
        )
        self.retrieve_preview = async_to_streamed_response_wrapper(
            v3.retrieve_preview,
        )
        self.retrieve_similar_papers = async_to_streamed_response_wrapper(
            v3.retrieve_similar_papers,
        )
        self.retrieve_unrelated = async_to_streamed_response_wrapper(
            v3.retrieve_unrelated,
        )
        self.view = async_to_streamed_response_wrapper(
            v3.view,
        )

    @cached_property
    def legacy(self) -> AsyncLegacyResourceWithStreamingResponse:
        return AsyncLegacyResourceWithStreamingResponse(self._v3.legacy)

    @cached_property
    def overview(self) -> AsyncOverviewResourceWithStreamingResponse:
        return AsyncOverviewResourceWithStreamingResponse(self._v3.overview)

    @cached_property
    def implementations(self) -> AsyncImplementationsResourceWithStreamingResponse:
        return AsyncImplementationsResourceWithStreamingResponse(self._v3.implementations)

    @cached_property
    def x_mentions(self) -> AsyncXMentionsResourceWithStreamingResponse:
        return AsyncXMentionsResourceWithStreamingResponse(self._v3.x_mentions)
