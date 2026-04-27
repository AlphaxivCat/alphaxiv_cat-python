# Papers

Types:

```python
from alphaxiv_cat.types import (
    PaperAddAuthorResponse,
    PaperAdminVoteResponse,
    PaperCrxAbstractClickResponse,
    PaperCrxAbstractHitResponse,
    PaperCrxPdfClickResponse,
    PaperCrxPdfHitResponse,
    PaperEmailAuthorResponse,
    PaperGetCrxPaperInfoResponse,
    PaperGetPaperInfoResponse,
    PaperKickoffAbstractEmbedResponse,
    PaperKickoffAIResponse,
    PaperKickoffBibtexResponse,
    PaperKickoffGitHubResponse,
    PaperKickoffPaperCategorizationResponse,
    PaperKickoffRecentPapersResponse,
    PaperProcessAbstractEmbedResponse,
    PaperProcessMetadataResponse,
    PaperRequestAILatestResponse,
    PaperRequestAITranslationLatestResponse,
    PaperSetGitHubRepositoryResponse,
    PaperToggleFollowResponse,
    PaperTranslateAIOverviewResponse,
    PaperUnclaimResponse,
    PaperVoteResponse,
)
```

Methods:

- <code title="post /v2/papers/{paperId}/add-author">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">add_author</a>(paper_id, \*\*<a href="src/alphaxiv_cat/types/paper_add_author_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/paper_add_author_response.py">PaperAddAuthorResponse</a></code>
- <code title="post /v2/papers/{paperId}/admin-vote">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">admin_vote</a>(paper_id, \*\*<a href="src/alphaxiv_cat/types/paper_admin_vote_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/paper_admin_vote_response.py">PaperAdminVoteResponse</a></code>
- <code title="get /v1/papers/crxabstractclick/{pid}/{ref}">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">crx_abstract_click</a>(ref, \*, pid) -> <a href="./src/alphaxiv_cat/types/paper_crx_abstract_click_response.py">PaperCrxAbstractClickResponse</a></code>
- <code title="get /v1/papers/crxabstracthit/{pid}">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">crx_abstract_hit</a>(pid) -> <a href="./src/alphaxiv_cat/types/paper_crx_abstract_hit_response.py">PaperCrxAbstractHitResponse</a></code>
- <code title="get /v1/papers/crxpdfclick/{pid}/{ref}">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">crx_pdf_click</a>(ref, \*, pid) -> <a href="./src/alphaxiv_cat/types/paper_crx_pdf_click_response.py">PaperCrxPdfClickResponse</a></code>
- <code title="get /v1/papers/crxpdfhit/{pid}">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">crx_pdf_hit</a>(pid) -> <a href="./src/alphaxiv_cat/types/paper_crx_pdf_hit_response.py">PaperCrxPdfHitResponse</a></code>
- <code title="post /v2/papers/{paperId}/email-author">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">email_author</a>(paper_id, \*\*<a href="src/alphaxiv_cat/types/paper_email_author_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/paper_email_author_response.py">PaperEmailAuthorResponse</a></code>
- <code title="get /v1/papers/getcrxpaperinfo/{pid}">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">get_crx_paper_info</a>(pid) -> <a href="./src/alphaxiv_cat/types/paper_get_crx_paper_info_response.py">PaperGetCrxPaperInfoResponse</a></code>
- <code title="get /v1/papers/getpaperinfo/{pid}">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">get_paper_info</a>(pid) -> <a href="./src/alphaxiv_cat/types/paper_get_paper_info_response.py">PaperGetPaperInfoResponse</a></code>
- <code title="post /v2/papers/kickoff-paper-version-abstract-embed">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">kickoff_abstract_embed</a>() -> <a href="./src/alphaxiv_cat/types/paper_kickoff_abstract_embed_response.py">PaperKickoffAbstractEmbedResponse</a></code>
- <code title="post /v2/papers/kickoff-paper-ai">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">kickoff_ai</a>() -> <a href="./src/alphaxiv_cat/types/paper_kickoff_ai_response.py">PaperKickoffAIResponse</a></code>
- <code title="post /v2/papers/kickoff-paper-bibtex">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">kickoff_bibtex</a>() -> <a href="./src/alphaxiv_cat/types/paper_kickoff_bibtex_response.py">PaperKickoffBibtexResponse</a></code>
- <code title="post /v2/papers/kickoff-github">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">kickoff_github</a>() -> <a href="./src/alphaxiv_cat/types/paper_kickoff_github_response.py">PaperKickoffGitHubResponse</a></code>
- <code title="post /v2/papers/kickoff-paper-categorization/{all}">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">kickoff_paper_categorization</a>(all) -> <a href="./src/alphaxiv_cat/types/paper_kickoff_paper_categorization_response.py">PaperKickoffPaperCategorizationResponse</a></code>
- <code title="post /v2/papers/kickoff-recent-papers">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">kickoff_recent_papers</a>() -> <a href="./src/alphaxiv_cat/types/paper_kickoff_recent_papers_response.py">PaperKickoffRecentPapersResponse</a></code>
- <code title="post /v2/papers/{upid}/view">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">mark_viewed</a>(upid) -> object</code>
- <code title="post /v2/papers/process-paper-version-abstract-embed">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">process_abstract_embed</a>(\*\*<a href="src/alphaxiv_cat/types/paper_process_abstract_embed_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/paper_process_abstract_embed_response.py">PaperProcessAbstractEmbedResponse</a></code>
- <code title="post /v2/papers/process-metadata">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">process_metadata</a>(\*\*<a href="src/alphaxiv_cat/types/paper_process_metadata_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/paper_process_metadata_response.py">PaperProcessMetadataResponse</a></code>
- <code title="post /v2/papers/{upid}/request-ai">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">request_ai_latest</a>(upid, \*\*<a href="src/alphaxiv_cat/types/paper_request_ai_latest_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/paper_request_ai_latest_response.py">PaperRequestAILatestResponse</a></code>
- <code title="post /v2/papers/{upid}/request-ai-translation/{language}">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">request_ai_translation_latest</a>(language, \*, upid) -> <a href="./src/alphaxiv_cat/types/paper_request_ai_translation_latest_response.py">PaperRequestAITranslationLatestResponse</a></code>
- <code title="post /v2/papers/{paperId}/github">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">set_github_repository</a>(paper_id, \*\*<a href="src/alphaxiv_cat/types/paper_set_github_repository_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/paper_set_github_repository_response.py">PaperSetGitHubRepositoryResponse</a></code>
- <code title="post /v2/papers/{paperId}/follow">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">toggle_follow</a>(paper_id) -> <a href="./src/alphaxiv_cat/types/paper_toggle_follow_response.py">PaperToggleFollowResponse</a></code>
- <code title="post /v2/papers/translate-ai-overview/{paperVersionId}/{language}">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">translate_ai_overview</a>(language, \*, paper_version_id) -> <a href="./src/alphaxiv_cat/types/paper_translate_ai_overview_response.py">PaperTranslateAIOverviewResponse</a></code>
- <code title="post /v2/papers/{paperId}/unclaim">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">unclaim</a>(paper_id) -> <a href="./src/alphaxiv_cat/types/paper_unclaim_response.py">PaperUnclaimResponse</a></code>
- <code title="post /v2/papers/{paperId}/vote">client.papers.<a href="./src/alphaxiv_cat/resources/papers/papers.py">vote</a>(paper_id) -> <a href="./src/alphaxiv_cat/types/paper_vote_response.py">PaperVoteResponse</a></code>

## Versions

Types:

```python
from alphaxiv_cat.types.papers import (
    VersionRequestAIOverviewResponse,
    VersionRequestAITranslationResponse,
)
```

Methods:

- <code title="post /v2/papers/{upid}/versions/{versionOrder}/request-ai">client.papers.versions.<a href="./src/alphaxiv_cat/resources/papers/versions.py">request_ai_overview</a>(version_order, \*, upid, \*\*<a href="src/alphaxiv_cat/types/papers/version_request_ai_overview_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/version_request_ai_overview_response.py">VersionRequestAIOverviewResponse</a></code>
- <code title="post /v2/papers/{upid}/versions/{versionOrder}/request-ai-translation/{language}">client.papers.versions.<a href="./src/alphaxiv_cat/resources/papers/versions.py">request_ai_translation</a>(language, \*, upid, version_order) -> <a href="./src/alphaxiv_cat/types/papers/version_request_ai_translation_response.py">VersionRequestAITranslationResponse</a></code>

## Metadata

Types:

```python
from alphaxiv_cat.types.papers import (
    MetadataRetrieveLatestMetadataResponse,
    MetadataRetrieveVersionMetadataResponse,
)
```

Methods:

- <code title="get /v2/papers/{upid}/metadata">client.papers.metadata.<a href="./src/alphaxiv_cat/resources/papers/metadata.py">retrieve_latest_metadata</a>(upid, \*\*<a href="src/alphaxiv_cat/types/papers/metadata_retrieve_latest_metadata_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/metadata_retrieve_latest_metadata_response.py">MetadataRetrieveLatestMetadataResponse</a></code>
- <code title="get /v2/papers/{upid}/metadata/versions/{versionOrder}">client.papers.metadata.<a href="./src/alphaxiv_cat/resources/papers/metadata.py">retrieve_version_metadata</a>(version_order, \*, upid, \*\*<a href="src/alphaxiv_cat/types/papers/metadata_retrieve_version_metadata_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/metadata_retrieve_version_metadata_response.py">MetadataRetrieveVersionMetadataResponse</a></code>

## Ingest

Types:

```python
from alphaxiv_cat.types.papers import IngestIngestLatestResponse, IngestIngestVersionResponse
```

Methods:

- <code title="get /v2/papers/{upid}/ingest">client.papers.ingest.<a href="./src/alphaxiv_cat/resources/papers/ingest.py">ingest_latest</a>(upid, \*\*<a href="src/alphaxiv_cat/types/papers/ingest_ingest_latest_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/ingest_ingest_latest_response.py">IngestIngestLatestResponse</a></code>
- <code title="get /v2/papers/{upid}/ingest/versions/{versionLabel}">client.papers.ingest.<a href="./src/alphaxiv_cat/resources/papers/ingest.py">ingest_version</a>(version_label, \*, upid, \*\*<a href="src/alphaxiv_cat/types/papers/ingest_ingest_version_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/ingest_ingest_version_response.py">IngestIngestVersionResponse</a></code>

## Private

Types:

```python
from alphaxiv_cat.types.papers import PrivateCreateResponse
```

Methods:

- <code title="post /v2/papers/private">client.papers.private.<a href="./src/alphaxiv_cat/resources/papers/private.py">create</a>(\*\*<a href="src/alphaxiv_cat/types/papers/private_create_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/private_create_response.py">PrivateCreateResponse</a></code>
- <code title="patch /v2/papers/private/{paperId}/metadata">client.papers.private.<a href="./src/alphaxiv_cat/resources/papers/private.py">update_metadata</a>(paper_id, \*\*<a href="src/alphaxiv_cat/types/papers/private_update_metadata_params.py">params</a>) -> None</code>

## KickoffDailyGitHubStars

Types:

```python
from alphaxiv_cat.types.papers import (
    KickoffDailyGitHubStarUpdateResponse,
    KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse,
)
```

Methods:

- <code title="post /v2/papers/kickoff-daily-github-stars/{max}">client.papers.kickoff_daily_github_stars.<a href="./src/alphaxiv_cat/resources/papers/kickoff_daily_github_stars.py">update</a>(max) -> <a href="./src/alphaxiv_cat/types/papers/kickoff_daily_github_star_update_response.py">KickoffDailyGitHubStarUpdateResponse</a></code>
- <code title="post /v2/papers/kickoff-daily-github-stars">client.papers.kickoff_daily_github_stars.<a href="./src/alphaxiv_cat/resources/papers/kickoff_daily_github_stars.py">kickoff_daily_github_stars</a>() -> <a href="./src/alphaxiv_cat/types/papers/kickoff_daily_github_star_kickoff_daily_github_stars_response.py">KickoffDailyGitHubStarKickoffDailyGitHubStarsResponse</a></code>

## V3

Types:

```python
from alphaxiv_cat.types.papers import (
    V3RetrieveResponse,
    V3CommentResponse,
    V3ImplementationResponse,
    V3KickoffThumbnailsTrendingPapersResponse,
    V3LikeResponse,
    V3PruneEmbeddingsByDateResponse,
    V3RequestImplementationResponse,
    V3RequestPodcastResponse,
    V3RetrieveAllResponse,
    V3RetrieveDiversePapersResponse,
    V3RetrieveFeedResponse,
    V3RetrieveFiguresResponse,
    V3RetrieveFullTextResponse,
    V3RetrieveGeoTrendsResponse,
    V3RetrieveMetricsResponse,
    V3RetrievePapersByCountryResponse,
    V3RetrievePreviewResponse,
    V3RetrieveSimilarPapersResponse,
    V3RetrieveUnrelatedResponse,
)
```

Methods:

- <code title="get /papers/v3/{unresolved}">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve</a>(unresolved) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_response.py">V3RetrieveResponse</a></code>
- <code title="post /papers/v3/{version}/comment">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">comment</a>(version, \*\*<a href="src/alphaxiv_cat/types/papers/v3_comment_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3_comment_response.py">V3CommentResponse</a></code>
- <code title="delete /papers/v3/votes">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">delete_votes</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_delete_votes_params.py">params</a>) -> None</code>
- <code title="post /papers/v3/{paperGroupId}/implementation">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">implementation</a>(paper_group_id, \*\*<a href="src/alphaxiv_cat/types/papers/v3_implementation_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3_implementation_response.py">V3ImplementationResponse</a></code>
- <code title="post /papers/v3/kickoff-paper-countries">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">kickoff_paper_countries</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_kickoff_paper_countries_params.py">params</a>) -> None</code>
- <code title="post /papers/v3/kickoff-paper-full-text">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">kickoff_paper_full_text</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_kickoff_paper_full_text_params.py">params</a>) -> None</code>
- <code title="post /papers/v3/kickoff-paper-podcasts">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">kickoff_paper_podcasts</a>() -> None</code>
- <code title="post /papers/v3/kickoff-thumbnails-trending-papers">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">kickoff_thumbnails_trending_papers</a>() -> <a href="./src/alphaxiv_cat/types/papers/v3_kickoff_thumbnails_trending_papers_response.py">V3KickoffThumbnailsTrendingPapersResponse</a></code>
- <code title="post /papers/v3/kickoff-x-mentions-sync">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">kickoff_x_mentions_sync</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_kickoff_x_mentions_sync_params.py">params</a>) -> None</code>
- <code title="post /papers/v3/{group}/like">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">like</a>(group) -> <a href="./src/alphaxiv_cat/types/papers/v3_like_response.py">V3LikeResponse</a></code>
- <code title="post /papers/v3/{paperGroupId}/podcast">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">podcast</a>(paper_group_id) -> None</code>
- <code title="post /papers/v3/{paperVersionId}/process-ai">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">process_ai</a>(paper_version_id, \*\*<a href="src/alphaxiv_cat/types/papers/v3_process_ai_params.py">params</a>) -> None</code>
- <code title="post /papers/v3/process-countries">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">process_countries</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_process_countries_params.py">params</a>) -> None</code>
- <code title="post /papers/v3/process-full-text">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">process_full_text</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_process_full_text_params.py">params</a>) -> None</code>
- <code title="post /papers/v3/prune-embeddings-by-date">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">prune_embeddings_by_date</a>() -> <a href="./src/alphaxiv_cat/types/papers/v3_prune_embeddings_by_date_response.py">V3PruneEmbeddingsByDateResponse</a></code>
- <code title="post /papers/v3/{group}/request-implementation">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">request_implementation</a>(group, \*\*<a href="src/alphaxiv_cat/types/papers/v3_request_implementation_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3_request_implementation_response.py">V3RequestImplementationResponse</a></code>
- <code title="post /papers/v3/{paperGroupId}/request-podcast">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">request_podcast</a>(paper_group_id) -> <a href="./src/alphaxiv_cat/types/papers/v3_request_podcast_response.py">V3RequestPodcastResponse</a></code>
- <code title="get /papers/v3/all">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_all</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_retrieve_all_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_all_response.py">V3RetrieveAllResponse</a></code>
- <code title="get /papers/v3/diverse-papers">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_diverse_papers</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_retrieve_diverse_papers_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_diverse_papers_response.py">V3RetrieveDiversePapersResponse</a></code>
- <code title="get /papers/v3/feed">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_feed</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_retrieve_feed_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_feed_response.py">V3RetrieveFeedResponse</a></code>
- <code title="get /papers/v3/{paperGroupId}/figures">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_figures</a>(paper_group_id) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_figures_response.py">V3RetrieveFiguresResponse</a></code>
- <code title="get /papers/v3/{paperVersion}/full-text">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_full_text</a>(paper_version) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_full_text_response.py">V3RetrieveFullTextResponse</a></code>
- <code title="get /papers/v3/geo-trends">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_geo_trends</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_retrieve_geo_trends_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_geo_trends_response.py">V3RetrieveGeoTrendsResponse</a></code>
- <code title="get /papers/v3/{unresolved}/metrics">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_metrics</a>(unresolved) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_metrics_response.py">V3RetrieveMetricsResponse</a></code>
- <code title="get /papers/v3/papers-by-country">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_papers_by_country</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_retrieve_papers_by_country_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_papers_by_country_response.py">V3RetrievePapersByCountryResponse</a></code>
- <code title="get /papers/v3/{id}/preview">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_preview</a>(id) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_preview_response.py">V3RetrievePreviewResponse</a></code>
- <code title="get /papers/v3/{id}/similar-papers">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_similar_papers</a>(id, \*\*<a href="src/alphaxiv_cat/types/papers/v3_retrieve_similar_papers_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_similar_papers_response.py">V3RetrieveSimilarPapersResponse</a></code>
- <code title="get /papers/v3/unrelated">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">retrieve_unrelated</a>(\*\*<a href="src/alphaxiv_cat/types/papers/v3_retrieve_unrelated_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3_retrieve_unrelated_response.py">V3RetrieveUnrelatedResponse</a></code>
- <code title="post /papers/v3/{group}/view">client.papers.v3.<a href="./src/alphaxiv_cat/resources/papers/v3/v3.py">view</a>(group) -> None</code>

### Legacy

Types:

```python
from alphaxiv_cat.types.papers.v3 import LegacyRetrieveResponse, LegacyRetrieveCommentsResponse
```

Methods:

- <code title="get /papers/v3/legacy/{unresolved}">client.papers.v3.legacy.<a href="./src/alphaxiv_cat/resources/papers/v3/legacy.py">retrieve</a>(unresolved) -> <a href="./src/alphaxiv_cat/types/papers/v3/legacy_retrieve_response.py">LegacyRetrieveResponse</a></code>
- <code title="get /papers/v3/legacy/{group}/comments">client.papers.v3.legacy.<a href="./src/alphaxiv_cat/resources/papers/v3/legacy.py">retrieve_comments</a>(group) -> <a href="./src/alphaxiv_cat/types/papers/v3/legacy_retrieve_comments_response.py">LegacyRetrieveCommentsResponse</a></code>

### Overview

Types:

```python
from alphaxiv_cat.types.papers.v3 import OverviewRetrieveResponse, OverviewRetrieveStatusResponse
```

Methods:

- <code title="get /papers/v3/{paperVersion}/overview/{language}">client.papers.v3.overview.<a href="./src/alphaxiv_cat/resources/papers/v3/overview.py">retrieve</a>(language, \*, paper_version) -> <a href="./src/alphaxiv_cat/types/papers/v3/overview_retrieve_response.py">OverviewRetrieveResponse</a></code>
- <code title="get /papers/v3/{paperVersion}/overview/status">client.papers.v3.overview.<a href="./src/alphaxiv_cat/resources/papers/v3/overview.py">retrieve_status</a>(paper_version) -> <a href="./src/alphaxiv_cat/types/papers/v3/overview_retrieve_status_response.py">OverviewRetrieveStatusResponse</a></code>

### Implementations

Types:

```python
from alphaxiv_cat.types.papers.v3 import ImplementationCreateResponse, ImplementationListResponse
```

Methods:

- <code title="post /papers/v3/{paperGroupId}/implementations">client.papers.v3.implementations.<a href="./src/alphaxiv_cat/resources/papers/v3/implementations.py">create</a>(paper_group_id, \*\*<a href="src/alphaxiv_cat/types/papers/v3/implementation_create_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3/implementation_create_response.py">ImplementationCreateResponse</a></code>
- <code title="get /papers/v3/{paperGroupId}/implementations">client.papers.v3.implementations.<a href="./src/alphaxiv_cat/resources/papers/v3/implementations.py">list</a>(paper_group_id) -> <a href="./src/alphaxiv_cat/types/papers/v3/implementation_list_response.py">ImplementationListResponse</a></code>
- <code title="delete /papers/v3/{paperGroupId}/implementations/{implementationId}">client.papers.v3.implementations.<a href="./src/alphaxiv_cat/resources/papers/v3/implementations.py">delete</a>(implementation_id, \*, paper_group_id, \*\*<a href="src/alphaxiv_cat/types/papers/v3/implementation_delete_params.py">params</a>) -> None</code>

### XMentions

Types:

```python
from alphaxiv_cat.types.papers.v3 import XMentionUpdateResponse
```

Methods:

- <code title="post /papers/v3/x-mentions/{paperGroupId}">client.papers.v3.x_mentions.<a href="./src/alphaxiv_cat/resources/papers/v3/x_mentions.py">update</a>(paper_group_id, \*\*<a href="src/alphaxiv_cat/types/papers/v3/x_mention_update_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v3/x_mention_update_response.py">XMentionUpdateResponse</a></code>
- <code title="delete /papers/v3/x-mentions/{paperGroupId}">client.papers.v3.x_mentions.<a href="./src/alphaxiv_cat/resources/papers/v3/x_mentions.py">delete</a>(paper_group_id) -> None</code>

## V2

Types:

```python
from alphaxiv_cat.types.papers import V2CommentResponse
```

Methods:

- <code title="post /papers/v2/{version}/comment">client.papers.v2.<a href="./src/alphaxiv_cat/resources/papers/v2.py">comment</a>(version, \*\*<a href="src/alphaxiv_cat/types/papers/v2_comment_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/papers/v2_comment_response.py">V2CommentResponse</a></code>

# Emails

Types:

```python
from alphaxiv_cat.types import (
    EmailCaptureBouncedEmailsResponse,
    EmailCaptureResendBouncedEmailResponse,
    EmailKickoffCommentUpdateResponse,
    EmailKickoffGeneralUpdateResponse,
    EmailProcessBouncedEmailResponse,
    EmailProcessCommentUpdateResponse,
    EmailProcessGeneralUpdateResponse,
)
```

Methods:

- <code title="post /v1/emails/capture-bounced-emails">client.emails.<a href="./src/alphaxiv_cat/resources/emails.py">capture_bounced_emails</a>(\*\*<a href="src/alphaxiv_cat/types/email_capture_bounced_emails_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/email_capture_bounced_emails_response.py">EmailCaptureBouncedEmailsResponse</a></code>
- <code title="post /v1/emails/capture-resend-bounced-email">client.emails.<a href="./src/alphaxiv_cat/resources/emails.py">capture_resend_bounced_email</a>(\*\*<a href="src/alphaxiv_cat/types/email_capture_resend_bounced_email_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/email_capture_resend_bounced_email_response.py">EmailCaptureResendBouncedEmailResponse</a></code>
- <code title="post /v1/emails/kickoff-comment-update/{role}/{window}/{custom}">client.emails.<a href="./src/alphaxiv_cat/resources/emails.py">kickoff_comment_update</a>(custom, \*, role, window) -> <a href="./src/alphaxiv_cat/types/email_kickoff_comment_update_response.py">EmailKickoffCommentUpdateResponse</a></code>
- <code title="post /v1/emails/kickoff-general-update/{role}">client.emails.<a href="./src/alphaxiv_cat/resources/emails.py">kickoff_general_update</a>(role) -> <a href="./src/alphaxiv_cat/types/email_kickoff_general_update_response.py">EmailKickoffGeneralUpdateResponse</a></code>
- <code title="post /v1/emails/process-bounced-email">client.emails.<a href="./src/alphaxiv_cat/resources/emails.py">process_bounced_email</a>(\*\*<a href="src/alphaxiv_cat/types/email_process_bounced_email_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/email_process_bounced_email_response.py">EmailProcessBouncedEmailResponse</a></code>
- <code title="post /v1/emails/process-comment-update">client.emails.<a href="./src/alphaxiv_cat/resources/emails.py">process_comment_update</a>(\*\*<a href="src/alphaxiv_cat/types/email_process_comment_update_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/email_process_comment_update_response.py">EmailProcessCommentUpdateResponse</a></code>
- <code title="post /v1/emails/process-general-update">client.emails.<a href="./src/alphaxiv_cat/resources/emails.py">process_general_update</a>(\*\*<a href="src/alphaxiv_cat/types/email_process_general_update_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/email_process_general_update_response.py">EmailProcessGeneralUpdateResponse</a></code>

# Users

Types:

```python
from alphaxiv_cat.types import UserGetPrivateNotesResponse, UserWeighWeeklyReputationResponse
```

Methods:

- <code title="get /v1/users/{uid}/notes">client.users.<a href="./src/alphaxiv_cat/resources/users/users.py">get_private_notes</a>(uid, \*\*<a href="src/alphaxiv_cat/types/user_get_private_notes_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/user_get_private_notes_response.py">UserGetPrivateNotesResponse</a></code>
- <code title="post /v1/users/weigh-weekly-reputation">client.users.<a href="./src/alphaxiv_cat/resources/users/users.py">weigh_weekly_reputation</a>() -> <a href="./src/alphaxiv_cat/types/user_weigh_weekly_reputation_response.py">UserWeighWeeklyReputationResponse</a></code>

## V3

Types:

```python
from alphaxiv_cat.types.users import (
    V3AutocompleteProfileResponse,
    V3GetActivityResponse,
    V3GetClaimedPapersResponse,
    V3GetCurrentUserResponse,
    V3GetFeaturedActivityResponse,
    V3GetFollowersResponse,
    V3GetLeaderboardResponse,
    V3GetUserByUuidResponse,
    V3GetViewedHistoryResponse,
    V3ProcessNotificationEmailResponse,
    V3SearchResponse,
    V3ToggleFollowUserResponse,
    V3UpdatePreferencesResponse,
    V3UpdateProfileResponse,
    V3UploadAvatarResponse,
)
```

Methods:

- <code title="post /users/v3/autocomplete-profile">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">autocomplete_profile</a>(\*\*<a href="src/alphaxiv_cat/types/users/v3_autocomplete_profile_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/users/v3_autocomplete_profile_response.py">V3AutocompleteProfileResponse</a></code>
- <code title="delete /users/v3/banners/{bannerId}">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">delete_banner</a>(banner_id) -> None</code>
- <code title="delete /users/v3">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">delete_own_user</a>() -> None</code>
- <code title="get /users/v3/{id}/activity">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">get_activity</a>(id, \*\*<a href="src/alphaxiv_cat/types/users/v3_get_activity_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/users/v3_get_activity_response.py">V3GetActivityResponse</a></code>
- <code title="get /users/v3/{id}/claimed-papers">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">get_claimed_papers</a>(id, \*\*<a href="src/alphaxiv_cat/types/users/v3_get_claimed_papers_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/users/v3_get_claimed_papers_response.py">V3GetClaimedPapersResponse</a></code>
- <code title="get /users/v3">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">get_current_user</a>() -> <a href="./src/alphaxiv_cat/types/users/v3_get_current_user_response.py">V3GetCurrentUserResponse</a></code>
- <code title="get /users/v3/{id}/featured">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">get_featured_activity</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3_get_featured_activity_response.py">V3GetFeaturedActivityResponse</a></code>
- <code title="get /users/v3/{id}/followers">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">get_followers</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3_get_followers_response.py">V3GetFollowersResponse</a></code>
- <code title="get /users/v3/leaderboard">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">get_leaderboard</a>() -> <a href="./src/alphaxiv_cat/types/users/v3_get_leaderboard_response.py">V3GetLeaderboardResponse</a></code>
- <code title="get /users/v3/{id}">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">get_user_by_uuid</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3_get_user_by_uuid_response.py">V3GetUserByUuidResponse</a></code>
- <code title="get /users/v3/viewed-history">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">get_viewed_history</a>(\*\*<a href="src/alphaxiv_cat/types/users/v3_get_viewed_history_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/users/v3_get_viewed_history_response.py">V3GetViewedHistoryResponse</a></code>
- <code title="post /users/v3/{id}/process-notification-email">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">process_notification_email</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3_process_notification_email_response.py">V3ProcessNotificationEmailResponse</a></code>
- <code title="get /users/v3/search">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">search</a>(\*\*<a href="src/alphaxiv_cat/types/users/v3_search_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/users/v3_search_response.py">V3SearchResponse</a></code>
- <code title="post /users/v3/{id}/follow">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">toggle_follow_user</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3_toggle_follow_user_response.py">V3ToggleFollowUserResponse</a></code>
- <code title="patch /users/v3/preferences">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">update_preferences</a>(\*\*<a href="src/alphaxiv_cat/types/users/v3_update_preferences_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/users/v3_update_preferences_response.py">V3UpdatePreferencesResponse</a></code>
- <code title="patch /users/v3/profile">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">update_profile</a>(\*\*<a href="src/alphaxiv_cat/types/users/v3_update_profile_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/users/v3_update_profile_response.py">V3UpdateProfileResponse</a></code>
- <code title="post /users/v3/avatar">client.users.v3.<a href="./src/alphaxiv_cat/resources/users/v3/v3.py">upload_avatar</a>() -> <a href="./src/alphaxiv_cat/types/users/v3_upload_avatar_response.py">Optional[V3UploadAvatarResponse]</a></code>

### Following

Types:

```python
from alphaxiv_cat.types.users.v3 import FollowingListResponse
```

Methods:

- <code title="get /users/v3/{id}/following">client.users.v3.following.<a href="./src/alphaxiv_cat/resources/users/v3/following/following.py">list</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3/following_list_response.py">FollowingListResponse</a></code>

#### Topics

Types:

```python
from alphaxiv_cat.types.users.v3.following import TopicListResponse, TopicToggleResponse
```

Methods:

- <code title="get /users/v3/{id}/following/topics">client.users.v3.following.topics.<a href="./src/alphaxiv_cat/resources/users/v3/following/topics.py">list</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3/following/topic_list_response.py">TopicListResponse</a></code>
- <code title="post /users/v3/{id}/following/topics/toggle">client.users.v3.following.topics.<a href="./src/alphaxiv_cat/resources/users/v3/following/topics.py">toggle</a>(id, \*\*<a href="src/alphaxiv_cat/types/users/v3/following/topic_toggle_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/users/v3/following/topic_toggle_response.py">TopicToggleResponse</a></code>

#### Organizations

Types:

```python
from alphaxiv_cat.types.users.v3.following import (
    OrganizationListResponse,
    OrganizationToggleResponse,
)
```

Methods:

- <code title="get /users/v3/{id}/following/organizations">client.users.v3.following.organizations.<a href="./src/alphaxiv_cat/resources/users/v3/following/organizations.py">list</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3/following/organization_list_response.py">OrganizationListResponse</a></code>
- <code title="post /users/v3/{id}/following/organizations/toggle">client.users.v3.following.organizations.<a href="./src/alphaxiv_cat/resources/users/v3/following/organizations.py">toggle</a>(id, \*\*<a href="src/alphaxiv_cat/types/users/v3/following/organization_toggle_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/users/v3/following/organization_toggle_response.py">OrganizationToggleResponse</a></code>

### ByUsername

Types:

```python
from alphaxiv_cat.types.users.v3 import ByUsernameGetProfilePageResponse, ByUsernameGetUserResponse
```

Methods:

- <code title="get /users/v3/by-username/{username}/profile-page">client.users.v3.by_username.<a href="./src/alphaxiv_cat/resources/users/v3/by_username.py">get_profile_page</a>(username) -> <a href="./src/alphaxiv_cat/types/users/v3/by_username_get_profile_page_response.py">ByUsernameGetProfilePageResponse</a></code>
- <code title="get /users/v3/by-username/{username}">client.users.v3.by_username.<a href="./src/alphaxiv_cat/resources/users/v3/by_username.py">get_user</a>(username) -> <a href="./src/alphaxiv_cat/types/users/v3/by_username_get_user_response.py">ByUsernameGetUserResponse</a></code>

### SemanticScholar

Types:

```python
from alphaxiv_cat.types.users.v3 import SemanticScholarLinkResponse, SemanticScholarScrapeResponse
```

Methods:

- <code title="post /users/v3/{id}/semantic-scholar/link">client.users.v3.semantic_scholar.<a href="./src/alphaxiv_cat/resources/users/v3/semantic_scholar.py">link</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3/semantic_scholar_link_response.py">SemanticScholarLinkResponse</a></code>
- <code title="post /users/v3/{id}/semantic-scholar/scrape">client.users.v3.semantic_scholar.<a href="./src/alphaxiv_cat/resources/users/v3/semantic_scholar.py">scrape</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3/semantic_scholar_scrape_response.py">SemanticScholarScrapeResponse</a></code>

### Citations

Types:

```python
from alphaxiv_cat.types.users.v3 import CitationGetGraphResponse, CitationGetSummaryResponse
```

Methods:

- <code title="get /users/v3/{id}/citations/graph">client.users.v3.citations.<a href="./src/alphaxiv_cat/resources/users/v3/citations.py">get_graph</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3/citation_get_graph_response.py">CitationGetGraphResponse</a></code>
- <code title="get /users/v3/{id}/citations/summary">client.users.v3.citations.<a href="./src/alphaxiv_cat/resources/users/v3/citations.py">get_summary</a>(id) -> <a href="./src/alphaxiv_cat/types/users/v3/citation_get_summary_response.py">CitationGetSummaryResponse</a></code>

## Preferences

Types:

```python
from alphaxiv_cat.types.users import PreferenceGetFoldersPreferencesResponse
```

Methods:

- <code title="get /v2/users/preferences/folders">client.users.preferences.<a href="./src/alphaxiv_cat/resources/users/preferences/preferences.py">get_folders_preferences</a>() -> <a href="./src/alphaxiv_cat/types/users/preference_get_folders_preferences_response.py">PreferenceGetFoldersPreferencesResponse</a></code>

### Email

Types:

```python
from alphaxiv_cat.types.users.preferences import EmailUpdateResponse, EmailGetResponse
```

Methods:

- <code title="put /v2/users/preferences/email">client.users.preferences.email.<a href="./src/alphaxiv_cat/resources/users/preferences/email.py">update</a>(\*\*<a href="src/alphaxiv_cat/types/users/preferences/email_update_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/users/preferences/email_update_response.py">EmailUpdateResponse</a></code>
- <code title="get /v2/users/preferences/email">client.users.preferences.email.<a href="./src/alphaxiv_cat/resources/users/preferences/email.py">get</a>() -> <a href="./src/alphaxiv_cat/types/users/preferences/email_get_response.py">EmailGetResponse</a></code>

# Assistant

Types:

```python
from alphaxiv_cat.types import AssistantUploadFileResponse
```

Methods:

- <code title="post /v1/assistant/upload-file">client.assistant.<a href="./src/alphaxiv_cat/resources/assistant/assistant.py">upload_file</a>() -> <a href="./src/alphaxiv_cat/types/assistant_upload_file_response.py">AssistantUploadFileResponse</a></code>

## V2

Types:

```python
from alphaxiv_cat.types.assistant import V2GetChatsResponse, V2GetURLMetadataResponse
```

Methods:

- <code title="post /assistant/v2/chat">client.assistant.v2.<a href="./src/alphaxiv_cat/resources/assistant/v2/v2.py">chat</a>(\*\*<a href="src/alphaxiv_cat/types/assistant/v2_chat_params.py">params</a>) -> object</code>
- <code title="delete /assistant/v2/{llmChat}">client.assistant.v2.<a href="./src/alphaxiv_cat/resources/assistant/v2/v2.py">delete_chat</a>(llm_chat) -> None</code>
- <code title="patch /assistant/v2/{llmChat}">client.assistant.v2.<a href="./src/alphaxiv_cat/resources/assistant/v2/v2.py">edit_chat</a>(llm_chat, \*\*<a href="src/alphaxiv_cat/types/assistant/v2_edit_chat_params.py">params</a>) -> None</code>
- <code title="get /assistant/v2">client.assistant.v2.<a href="./src/alphaxiv_cat/resources/assistant/v2/v2.py">get_chats</a>(\*\*<a href="src/alphaxiv_cat/types/assistant/v2_get_chats_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/assistant/v2_get_chats_response.py">V2GetChatsResponse</a></code>
- <code title="get /assistant/v2/url-metadata">client.assistant.v2.<a href="./src/alphaxiv_cat/resources/assistant/v2/v2.py">get_url_metadata</a>(\*\*<a href="src/alphaxiv_cat/types/assistant/v2_get_url_metadata_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/assistant/v2_get_url_metadata_response.py">V2GetURLMetadataResponse</a></code>

### Messages

Types:

```python
from alphaxiv_cat.types.assistant.v2 import MessageListResponse
```

Methods:

- <code title="get /assistant/v2/{llmChat}/messages">client.assistant.v2.messages.<a href="./src/alphaxiv_cat/resources/assistant/v2/messages.py">list</a>(llm_chat) -> <a href="./src/alphaxiv_cat/types/assistant/v2/message_list_response.py">MessageListResponse</a></code>
- <code title="post /assistant/v2/{llmChat}/messages/{message}/select">client.assistant.v2.messages.<a href="./src/alphaxiv_cat/resources/assistant/v2/messages.py">select</a>(message, \*, llm_chat) -> None</code>
- <code title="post /assistant/v2/messages/{messageId}/feedback">client.assistant.v2.messages.<a href="./src/alphaxiv_cat/resources/assistant/v2/messages.py">set_feedback</a>(message_id, \*\*<a href="src/alphaxiv_cat/types/assistant/v2/message_set_feedback_params.py">params</a>) -> None</code>

# Folders

## V3

Types:

```python
from alphaxiv_cat.types.folders import (
    V3CreateResponse,
    V3ListResponse,
    V3AddPapersResponse,
    V3MovePapersResponse,
    V3ToggleSharingResponse,
)
```

Methods:

- <code title="post /folders/v3">client.folders.v3.<a href="./src/alphaxiv_cat/resources/folders/v3/v3.py">create</a>(\*\*<a href="src/alphaxiv_cat/types/folders/v3_create_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/folders/v3_create_response.py">V3CreateResponse</a></code>
- <code title="get /folders/v3">client.folders.v3.<a href="./src/alphaxiv_cat/resources/folders/v3/v3.py">list</a>() -> <a href="./src/alphaxiv_cat/types/folders/v3_list_response.py">V3ListResponse</a></code>
- <code title="delete /folders/v3/{folderId}">client.folders.v3.<a href="./src/alphaxiv_cat/resources/folders/v3/v3.py">delete</a>(folder_id) -> None</code>
- <code title="post /folders/v3/{folderId}/add-papers">client.folders.v3.<a href="./src/alphaxiv_cat/resources/folders/v3/v3.py">add_papers</a>(folder_id, \*\*<a href="src/alphaxiv_cat/types/folders/v3_add_papers_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/folders/v3_add_papers_response.py">V3AddPapersResponse</a></code>
- <code title="post /folders/v3/{folderId}/move-papers">client.folders.v3.<a href="./src/alphaxiv_cat/resources/folders/v3/v3.py">move_papers</a>(folder_id, \*\*<a href="src/alphaxiv_cat/types/folders/v3_move_papers_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/folders/v3_move_papers_response.py">V3MovePapersResponse</a></code>
- <code title="post /folders/v3/{folderId}/remove-papers">client.folders.v3.<a href="./src/alphaxiv_cat/resources/folders/v3/v3.py">remove_papers</a>(folder_id, \*\*<a href="src/alphaxiv_cat/types/folders/v3_remove_papers_params.py">params</a>) -> None</code>
- <code title="patch /folders/v3/{folderId}/sharing">client.folders.v3.<a href="./src/alphaxiv_cat/resources/folders/v3/v3.py">toggle_sharing</a>(folder_id, \*\*<a href="src/alphaxiv_cat/types/folders/v3_toggle_sharing_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/folders/v3_toggle_sharing_response.py">V3ToggleSharingResponse</a></code>
- <code title="patch /folders/v3/{folderId}">client.folders.v3.<a href="./src/alphaxiv_cat/resources/folders/v3/v3.py">update_name</a>(folder_id, \*\*<a href="src/alphaxiv_cat/types/folders/v3_update_name_params.py">params</a>) -> None</code>
- <code title="patch /folders/v3/{folderId}/parent">client.folders.v3.<a href="./src/alphaxiv_cat/resources/folders/v3/v3.py">update_parent</a>(folder_id, \*\*<a href="src/alphaxiv_cat/types/folders/v3_update_parent_params.py">params</a>) -> None</code>

### Shared

Types:

```python
from alphaxiv_cat.types.folders.v3 import SharedRetrieveResponse, SharedCopyResponse
```

Methods:

- <code title="get /folders/v3/shared/{folderId}">client.folders.v3.shared.<a href="./src/alphaxiv_cat/resources/folders/v3/shared.py">retrieve</a>(folder_id) -> <a href="./src/alphaxiv_cat/types/folders/v3/shared_retrieve_response.py">SharedRetrieveResponse</a></code>
- <code title="post /folders/v3/shared/{folderId}/copy">client.folders.v3.shared.<a href="./src/alphaxiv_cat/resources/folders/v3/shared.py">copy</a>(folder_id) -> <a href="./src/alphaxiv_cat/types/folders/v3/shared_copy_response.py">SharedCopyResponse</a></code>

# Comments

Methods:

- <code title="patch /comments/v1/{comment}">client.comments.<a href="./src/alphaxiv_cat/resources/comments/comments.py">edit</a>(comment, \*\*<a href="src/alphaxiv_cat/types/comment_edit_params.py">params</a>) -> None</code>

## V2

Methods:

- <code title="delete /comments/v2/{comment}">client.comments.v2.<a href="./src/alphaxiv_cat/resources/comments/v2/v2.py">delete</a>(comment) -> None</code>
- <code title="post /comments/v2/{comment}/downvote">client.comments.v2.<a href="./src/alphaxiv_cat/resources/comments/v2/v2.py">downvote</a>(comment) -> None</code>
- <code title="post /comments/v2/{comment}/flag">client.comments.v2.<a href="./src/alphaxiv_cat/resources/comments/v2/v2.py">flag</a>(comment, \*\*<a href="src/alphaxiv_cat/types/comments/v2_flag_params.py">params</a>) -> None</code>
- <code title="post /comments/v2/{comment}/endorse">client.comments.v2.<a href="./src/alphaxiv_cat/resources/comments/v2/v2.py">toggle_endorse</a>(comment) -> None</code>
- <code title="post /comments/v2/{comment}/upvote">client.comments.v2.<a href="./src/alphaxiv_cat/resources/comments/v2/v2.py">upvote</a>(comment) -> None</code>

### Moderator

Types:

```python
from alphaxiv_cat.types.comments.v2 import ModeratorToggleFlagsResponse
```

Methods:

- <code title="post /comments/v2/{comment}/moderator/send-feedback">client.comments.v2.moderator.<a href="./src/alphaxiv_cat/resources/comments/v2/moderator.py">send_feedback</a>(comment, \*\*<a href="src/alphaxiv_cat/types/comments/v2/moderator_send_feedback_params.py">params</a>) -> None</code>
- <code title="post /comments/v2/{comment}/moderator/toggle-flags">client.comments.v2.moderator.<a href="./src/alphaxiv_cat/resources/comments/v2/moderator.py">toggle_flags</a>(comment, \*\*<a href="src/alphaxiv_cat/types/comments/v2/moderator_toggle_flags_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/comments/v2/moderator_toggle_flags_response.py">ModeratorToggleFlagsResponse</a></code>

# Analytics

## PaperViewCount

Types:

```python
from alphaxiv_cat.types.analytics import (
    PaperViewCountIngestEventResponse,
    PaperViewCountKickoffJobResponse,
    PaperViewCountProcessJobResponse,
)
```

Methods:

- <code title="post /v1/analytics/paper-view-count/ingest">client.analytics.paper_view_count.<a href="./src/alphaxiv_cat/resources/analytics/paper_view_count.py">ingest_event</a>(\*\*<a href="src/alphaxiv_cat/types/analytics/paper_view_count_ingest_event_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/analytics/paper_view_count_ingest_event_response.py">PaperViewCountIngestEventResponse</a></code>
- <code title="post /v1/analytics/paper-view-count/kickoff-job">client.analytics.paper_view_count.<a href="./src/alphaxiv_cat/resources/analytics/paper_view_count.py">kickoff_job</a>(\*\*<a href="src/alphaxiv_cat/types/analytics/paper_view_count_kickoff_job_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/analytics/paper_view_count_kickoff_job_response.py">PaperViewCountKickoffJobResponse</a></code>
- <code title="post /v1/analytics/paper-view-count/process-job">client.analytics.paper_view_count.<a href="./src/alphaxiv_cat/resources/analytics/paper_view_count.py">process_job</a>(\*\*<a href="src/alphaxiv_cat/types/analytics/paper_view_count_process_job_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/analytics/paper_view_count_process_job_response.py">PaperViewCountProcessJobResponse</a></code>

# Search

Types:

```python
from alphaxiv_cat.types import SearchClosestTopicResponse
```

Methods:

- <code title="get /v1/search/closest-topic">client.search.<a href="./src/alphaxiv_cat/resources/search/search.py">closest_topic</a>(\*\*<a href="src/alphaxiv_cat/types/search_closest_topic_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/search_closest_topic_response.py">SearchClosestTopicResponse</a></code>
- <code title="get /v1/search/paper">client.search.<a href="./src/alphaxiv_cat/resources/search/search.py">google_search</a>(\*\*<a href="src/alphaxiv_cat/types/search_google_search_params.py">params</a>) -> object</code>

## V2

### Paper

Types:

```python
from alphaxiv_cat.types.search.v2 import PaperFastSearchResponse
```

Methods:

- <code title="get /search/v2/paper/fast">client.search.v2.paper.<a href="./src/alphaxiv_cat/resources/search/v2/paper.py">fast_search</a>(\*\*<a href="src/alphaxiv_cat/types/search/v2/paper_fast_search_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/search/v2/paper_fast_search_response.py">PaperFastSearchResponse</a></code>

# Organizations

## V2

Types:

```python
from alphaxiv_cat.types.organizations import (
    V2ListTopResponse,
    V2RetrieveByIDResponse,
    V2RetrieveByNameResponse,
    V2SearchResponse,
    V2ToggleFollowResponse,
)
```

Methods:

- <code title="get /organizations/v2/top">client.organizations.v2.<a href="./src/alphaxiv_cat/resources/organizations/v2.py">list_top</a>() -> <a href="./src/alphaxiv_cat/types/organizations/v2_list_top_response.py">V2ListTopResponse</a></code>
- <code title="get /organizations/v2/{id}">client.organizations.v2.<a href="./src/alphaxiv_cat/resources/organizations/v2.py">retrieve_by_id</a>(id) -> <a href="./src/alphaxiv_cat/types/organizations/v2_retrieve_by_id_response.py">V2RetrieveByIDResponse</a></code>
- <code title="get /organizations/v2/by-name/{name}">client.organizations.v2.<a href="./src/alphaxiv_cat/resources/organizations/v2.py">retrieve_by_name</a>(name) -> <a href="./src/alphaxiv_cat/types/organizations/v2_retrieve_by_name_response.py">V2RetrieveByNameResponse</a></code>
- <code title="get /organizations/v2/search">client.organizations.v2.<a href="./src/alphaxiv_cat/resources/organizations/v2.py">search</a>(\*\*<a href="src/alphaxiv_cat/types/organizations/v2_search_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/organizations/v2_search_response.py">V2SearchResponse</a></code>
- <code title="post /organizations/v2/{id}/toggle">client.organizations.v2.<a href="./src/alphaxiv_cat/resources/organizations/v2.py">toggle_follow</a>(id) -> <a href="./src/alphaxiv_cat/types/organizations/v2_toggle_follow_response.py">V2ToggleFollowResponse</a></code>

# GoogleScholar

## V1

Types:

```python
from alphaxiv_cat.types.google_scholar import (
    V1ConnectResponse,
    V1GetReportResponse,
    V1GetStatusResponse,
    V1ResyncResponse,
    V1SyncResponse,
    V1VerifyEmailResponse,
)
```

Methods:

- <code title="post /google-scholar/v1">client.google_scholar.v1.<a href="./src/alphaxiv_cat/resources/google_scholar/v1.py">connect</a>(\*\*<a href="src/alphaxiv_cat/types/google_scholar/v1_connect_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/google_scholar/v1_connect_response.py">V1ConnectResponse</a></code>
- <code title="delete /google-scholar/v1">client.google_scholar.v1.<a href="./src/alphaxiv_cat/resources/google_scholar/v1.py">delete_connection</a>() -> None</code>
- <code title="get /google-scholar/v1/report">client.google_scholar.v1.<a href="./src/alphaxiv_cat/resources/google_scholar/v1.py">get_report</a>() -> <a href="./src/alphaxiv_cat/types/google_scholar/v1_get_report_response.py">V1GetReportResponse</a></code>
- <code title="get /google-scholar/v1/status">client.google_scholar.v1.<a href="./src/alphaxiv_cat/resources/google_scholar/v1.py">get_status</a>() -> <a href="./src/alphaxiv_cat/types/google_scholar/v1_get_status_response.py">V1GetStatusResponse</a></code>
- <code title="post /google-scholar/v1/resync/{mode}">client.google_scholar.v1.<a href="./src/alphaxiv_cat/resources/google_scholar/v1.py">resync</a>(mode) -> <a href="./src/alphaxiv_cat/types/google_scholar/v1_resync_response.py">V1ResyncResponse</a></code>
- <code title="put /google-scholar/v1/email">client.google_scholar.v1.<a href="./src/alphaxiv_cat/resources/google_scholar/v1.py">set_email</a>(\*\*<a href="src/alphaxiv_cat/types/google_scholar/v1_set_email_params.py">params</a>) -> None</code>
- <code title="post /google-scholar/v1/sync">client.google_scholar.v1.<a href="./src/alphaxiv_cat/resources/google_scholar/v1.py">sync</a>() -> <a href="./src/alphaxiv_cat/types/google_scholar/v1_sync_response.py">V1SyncResponse</a></code>
- <code title="post /google-scholar/v1/verify">client.google_scholar.v1.<a href="./src/alphaxiv_cat/resources/google_scholar/v1.py">verify_email</a>(\*\*<a href="src/alphaxiv_cat/types/google_scholar/v1_verify_email_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/google_scholar/v1_verify_email_response.py">V1VerifyEmailResponse</a></code>

# APIKeys

## V1

Types:

```python
from alphaxiv_cat.types.api_keys import (
    V1CreateResponse,
    V1ListResponse,
    V1CreateImpersonationResponse,
    V1RevokeResponse,
)
```

Methods:

- <code title="post /api-keys/v1">client.api_keys.v1.<a href="./src/alphaxiv_cat/resources/api_keys/v1.py">create</a>(\*\*<a href="src/alphaxiv_cat/types/api_keys/v1_create_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/api_keys/v1_create_response.py">V1CreateResponse</a></code>
- <code title="get /api-keys/v1">client.api_keys.v1.<a href="./src/alphaxiv_cat/resources/api_keys/v1.py">list</a>() -> <a href="./src/alphaxiv_cat/types/api_keys/v1_list_response.py">V1ListResponse</a></code>
- <code title="post /api-keys/v1/impersonate">client.api_keys.v1.<a href="./src/alphaxiv_cat/resources/api_keys/v1.py">create_impersonation</a>(\*\*<a href="src/alphaxiv_cat/types/api_keys/v1_create_impersonation_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/api_keys/v1_create_impersonation_response.py">V1CreateImpersonationResponse</a></code>
- <code title="post /api-keys/v1/{apiKeyId}/revoke">client.api_keys.v1.<a href="./src/alphaxiv_cat/resources/api_keys/v1.py">revoke</a>(api_key_id) -> <a href="./src/alphaxiv_cat/types/api_keys/v1_revoke_response.py">V1RevokeResponse</a></code>

# Admin

## V1

Types:

```python
from alphaxiv_cat.types.admin import V1GetModeratorFeedResponse, V1LookupUserByEmailResponse
```

Methods:

- <code title="get /admin/v1/moderator-feed">client.admin.v1.<a href="./src/alphaxiv_cat/resources/admin/v1/v1.py">get_moderator_feed</a>(\*\*<a href="src/alphaxiv_cat/types/admin/v1_get_moderator_feed_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/admin/v1_get_moderator_feed_response.py">V1GetModeratorFeedResponse</a></code>
- <code title="get /admin/v1/lookup-user-by-email">client.admin.v1.<a href="./src/alphaxiv_cat/resources/admin/v1/v1.py">lookup_user_by_email</a>(\*\*<a href="src/alphaxiv_cat/types/admin/v1_lookup_user_by_email_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/admin/v1_lookup_user_by_email_response.py">V1LookupUserByEmailResponse</a></code>

### Emails

Methods:

- <code title="post /admin/v1/emails/send-monthly-digest">client.admin.v1.emails.<a href="./src/alphaxiv_cat/resources/admin/v1/emails.py">send_monthly_digest</a>(\*\*<a href="src/alphaxiv_cat/types/admin/v1/email_send_monthly_digest_params.py">params</a>) -> None</code>
- <code title="post /admin/v1/emails/send-weekly-digest">client.admin.v1.emails.<a href="./src/alphaxiv_cat/resources/admin/v1/emails.py">send_weekly_digest</a>(\*\*<a href="src/alphaxiv_cat/types/admin/v1/email_send_weekly_digest_params.py">params</a>) -> None</code>

# Notifications

Types:

```python
from alphaxiv_cat.types import NotificationSendKickoffNotificationEmailsResponse
```

Methods:

- <code title="post /v2/notifications/kickoff-notification-emails">client.notifications.<a href="./src/alphaxiv_cat/resources/notifications/notifications.py">send_kickoff_notification_emails</a>() -> <a href="./src/alphaxiv_cat/types/notification_send_kickoff_notification_emails_response.py">NotificationSendKickoffNotificationEmailsResponse</a></code>

## V4

Types:

```python
from alphaxiv_cat.types.notifications import V4ListNotificationsResponse
```

Methods:

- <code title="get /notifications/v4">client.notifications.v4.<a href="./src/alphaxiv_cat/resources/notifications/v4/v4.py">list_notifications</a>() -> <a href="./src/alphaxiv_cat/types/notifications/v4_list_notifications_response.py">V4ListNotificationsResponse</a></code>
- <code title="post /notifications/v4/subscribe">client.notifications.v4.<a href="./src/alphaxiv_cat/resources/notifications/v4/v4.py">subscribe</a>(\*\*<a href="src/alphaxiv_cat/types/notifications/v4_subscribe_params.py">params</a>) -> None</code>
- <code title="post /notifications/v4/unsubscribe">client.notifications.v4.<a href="./src/alphaxiv_cat/resources/notifications/v4/v4.py">unsubscribe</a>(\*\*<a href="src/alphaxiv_cat/types/notifications/v4_unsubscribe_params.py">params</a>) -> None</code>

### Archive

Types:

```python
from alphaxiv_cat.types.notifications.v4 import ArchiveCreateResponse, ArchiveListResponse
```

Methods:

- <code title="post /notifications/v4/archive">client.notifications.v4.archive.<a href="./src/alphaxiv_cat/resources/notifications/v4/archive.py">create</a>(\*\*<a href="src/alphaxiv_cat/types/notifications/v4/archive_create_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/notifications/v4/archive_create_response.py">ArchiveCreateResponse</a></code>
- <code title="get /notifications/v4/archive">client.notifications.v4.archive.<a href="./src/alphaxiv_cat/resources/notifications/v4/archive.py">list</a>(\*\*<a href="src/alphaxiv_cat/types/notifications/v4/archive_list_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/notifications/v4/archive_list_response.py">ArchiveListResponse</a></code>

# Sitemaps

Types:

```python
from alphaxiv_cat.types import (
    SitemapListOverviewsResponse,
    SitemapListPapersResponse,
    SitemapListUsersResponse,
)
```

Methods:

- <code title="get /v1/sitemaps/overviews">client.sitemaps.<a href="./src/alphaxiv_cat/resources/sitemaps.py">list_overviews</a>(\*\*<a href="src/alphaxiv_cat/types/sitemap_list_overviews_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/sitemap_list_overviews_response.py">SitemapListOverviewsResponse</a></code>
- <code title="get /v1/sitemaps/papers">client.sitemaps.<a href="./src/alphaxiv_cat/resources/sitemaps.py">list_papers</a>(\*\*<a href="src/alphaxiv_cat/types/sitemap_list_papers_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/sitemap_list_papers_response.py">SitemapListPapersResponse</a></code>
- <code title="get /v1/sitemaps/users">client.sitemaps.<a href="./src/alphaxiv_cat/resources/sitemaps.py">list_users</a>(\*\*<a href="src/alphaxiv_cat/types/sitemap_list_users_params.py">params</a>) -> <a href="./src/alphaxiv_cat/types/sitemap_list_users_response.py">SitemapListUsersResponse</a></code>

# Retrieve

## V1

Methods:

- <code title="get /retrieve/v1/top-papers">client.retrieve.v1.<a href="./src/alphaxiv_cat/resources/retrieve/v1.py">get_top_papers</a>(\*\*<a href="src/alphaxiv_cat/types/retrieve/v1_get_top_papers_params.py">params</a>) -> object</code>

# Retool

## V1

Types:

```python
from alphaxiv_cat.types.retool import (
    V1GetCumulativeUsersResponse,
    V1GetDailyConversationsResponse,
    V1GetDailyNewAccountsResponse,
    V1GetDailyUserChatMessagesResponse,
    V1GetTotalCommentCountResponse,
    V1GetTotalPaperCountResponse,
    V1GetTotalPrivateNotesCountResponse,
    V1GetTotalUserCountResponse,
    V1GetWeeklyMessageCountsByUserResponse,
    V1GetWeeklyPrivateNotesResponse,
    V1GetWeeklyPublicCommentsResponse,
)
```

Methods:

- <code title="get /retool/v1/cumulative-users">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_cumulative_users</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_cumulative_users_response.py">V1GetCumulativeUsersResponse</a></code>
- <code title="get /retool/v1/daily-conversations">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_daily_conversations</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_daily_conversations_response.py">V1GetDailyConversationsResponse</a></code>
- <code title="get /retool/v1/daily-new-accounts">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_daily_new_accounts</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_daily_new_accounts_response.py">V1GetDailyNewAccountsResponse</a></code>
- <code title="get /retool/v1/daily-user-chat-messages">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_daily_user_chat_messages</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_daily_user_chat_messages_response.py">V1GetDailyUserChatMessagesResponse</a></code>
- <code title="get /retool/v1/total-comment-count">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_total_comment_count</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_total_comment_count_response.py">V1GetTotalCommentCountResponse</a></code>
- <code title="get /retool/v1/total-paper-count">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_total_paper_count</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_total_paper_count_response.py">V1GetTotalPaperCountResponse</a></code>
- <code title="get /retool/v1/total-private-notes-count">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_total_private_notes_count</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_total_private_notes_count_response.py">V1GetTotalPrivateNotesCountResponse</a></code>
- <code title="get /retool/v1/total-user-count">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_total_user_count</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_total_user_count_response.py">V1GetTotalUserCountResponse</a></code>
- <code title="get /retool/v1/weekly-message-counts-by-user">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_weekly_message_counts_by_user</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_weekly_message_counts_by_user_response.py">V1GetWeeklyMessageCountsByUserResponse</a></code>
- <code title="get /retool/v1/weekly-private-notes">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_weekly_private_notes</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_weekly_private_notes_response.py">V1GetWeeklyPrivateNotesResponse</a></code>
- <code title="get /retool/v1/weekly-public-comments">client.retool.v1.<a href="./src/alphaxiv_cat/resources/retool/v1.py">get_weekly_public_comments</a>() -> <a href="./src/alphaxiv_cat/types/retool/v1_get_weekly_public_comments_response.py">V1GetWeeklyPublicCommentsResponse</a></code>

# Research

Types:

```python
from alphaxiv_cat.types import ResearchCreateProjectResponse
```

Methods:

- <code title="post /research/v1">client.research.<a href="./src/alphaxiv_cat/resources/research.py">create_project</a>(\*\*<a href="src/alphaxiv_cat/types/research_create_project_params.py">params</a>) -> str</code>

# Mcp

## V1

Methods:

- <code title="get /mcp/v1">client.mcp.v1.<a href="./src/alphaxiv_cat/resources/mcp/v1.py">establish_connection</a>() -> object</code>
- <code title="post /mcp/v1">client.mcp.v1.<a href="./src/alphaxiv_cat/resources/mcp/v1.py">send_message</a>(\*\*<a href="src/alphaxiv_cat/types/mcp/v1_send_message_params.py">params</a>) -> object</code>
- <code title="delete /mcp/v1">client.mcp.v1.<a href="./src/alphaxiv_cat/resources/mcp/v1.py">terminate_session</a>() -> None</code>

# Events

Types:

```python
from alphaxiv_cat.types import EventListResponse
```

Methods:

- <code title="get /events/v1">client.events.<a href="./src/alphaxiv_cat/resources/events.py">list</a>() -> <a href="./src/alphaxiv_cat/types/event_list_response.py">EventListResponse</a></code>

# WellKnown

Methods:

- <code title="get /.well-known/oauth-protected-resource">client.well_known.<a href="./src/alphaxiv_cat/resources/well_known.py">retrieve_oauth_protected_resource</a>() -> object</code>
