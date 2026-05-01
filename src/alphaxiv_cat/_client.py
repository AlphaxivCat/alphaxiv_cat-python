# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        mcp,
        admin,
        users,
        emails,
        events,
        papers,
        retool,
        search,
        folders,
        api_keys,
        comments,
        retrieve,
        sitemaps,
        analytics,
        assistant,
        well_known,
        notifications,
        organizations,
        google_scholar,
    )
    from .resources.emails import EmailsResource, AsyncEmailsResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.mcp.mcp import McpResource, AsyncMcpResource
    from .resources.sitemaps import SitemapsResource, AsyncSitemapsResource
    from .resources.well_known import WellKnownResource, AsyncWellKnownResource
    from .resources.admin.admin import AdminResource, AsyncAdminResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.papers.papers import PapersResource, AsyncPapersResource
    from .resources.retool.retool import RetoolResource, AsyncRetoolResource
    from .resources.search.search import SearchResource, AsyncSearchResource
    from .resources.folders.folders import FoldersResource, AsyncFoldersResource
    from .resources.api_keys.api_keys import APIKeysResource, AsyncAPIKeysResource
    from .resources.comments.comments import CommentsResource, AsyncCommentsResource
    from .resources.retrieve.retrieve import RetrieveResource, AsyncRetrieveResource
    from .resources.analytics.analytics import AnalyticsResource, AsyncAnalyticsResource
    from .resources.assistant.assistant import AssistantResource, AsyncAssistantResource
    from .resources.notifications.notifications import NotificationsResource, AsyncNotificationsResource
    from .resources.organizations.organizations import OrganizationsResource, AsyncOrganizationsResource
    from .resources.google_scholar.google_scholar import GoogleScholarResource, AsyncGoogleScholarResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "AlphaxivCat",
    "AsyncAlphaxivCat",
    "Client",
    "AsyncClient",
]


class AlphaxivCat(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous AlphaxivCat client instance.

        This automatically infers the `api_key` argument from the `ALPHAXIV_CAT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ALPHAXIV_CAT_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ALPHAXIV_CAT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.alphaxiv.org"

        custom_headers_env = os.environ.get("ALPHAXIV_CAT_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def papers(self) -> PapersResource:
        from .resources.papers import PapersResource

        return PapersResource(self)

    @cached_property
    def emails(self) -> EmailsResource:
        from .resources.emails import EmailsResource

        return EmailsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def assistant(self) -> AssistantResource:
        from .resources.assistant import AssistantResource

        return AssistantResource(self)

    @cached_property
    def folders(self) -> FoldersResource:
        from .resources.folders import FoldersResource

        return FoldersResource(self)

    @cached_property
    def comments(self) -> CommentsResource:
        from .resources.comments import CommentsResource

        return CommentsResource(self)

    @cached_property
    def analytics(self) -> AnalyticsResource:
        from .resources.analytics import AnalyticsResource

        return AnalyticsResource(self)

    @cached_property
    def search(self) -> SearchResource:
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        from .resources.organizations import OrganizationsResource

        return OrganizationsResource(self)

    @cached_property
    def google_scholar(self) -> GoogleScholarResource:
        from .resources.google_scholar import GoogleScholarResource

        return GoogleScholarResource(self)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        from .resources.api_keys import APIKeysResource

        return APIKeysResource(self)

    @cached_property
    def admin(self) -> AdminResource:
        from .resources.admin import AdminResource

        return AdminResource(self)

    @cached_property
    def notifications(self) -> NotificationsResource:
        from .resources.notifications import NotificationsResource

        return NotificationsResource(self)

    @cached_property
    def sitemaps(self) -> SitemapsResource:
        from .resources.sitemaps import SitemapsResource

        return SitemapsResource(self)

    @cached_property
    def retrieve(self) -> RetrieveResource:
        from .resources.retrieve import RetrieveResource

        return RetrieveResource(self)

    @cached_property
    def retool(self) -> RetoolResource:
        from .resources.retool import RetoolResource

        return RetoolResource(self)

    @cached_property
    def mcp(self) -> McpResource:
        from .resources.mcp import McpResource

        return McpResource(self)

    @cached_property
    def events(self) -> EventsResource:
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def well_known(self) -> WellKnownResource:
        from .resources.well_known import WellKnownResource

        return WellKnownResource(self)

    @cached_property
    def with_raw_response(self) -> AlphaxivCatWithRawResponse:
        return AlphaxivCatWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlphaxivCatWithStreamedResponse:
        return AlphaxivCatWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key if security.get("api_key", False) else {}),
        }

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncAlphaxivCat(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncAlphaxivCat client instance.

        This automatically infers the `api_key` argument from the `ALPHAXIV_CAT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ALPHAXIV_CAT_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ALPHAXIV_CAT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.alphaxiv.org"

        custom_headers_env = os.environ.get("ALPHAXIV_CAT_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def papers(self) -> AsyncPapersResource:
        from .resources.papers import AsyncPapersResource

        return AsyncPapersResource(self)

    @cached_property
    def emails(self) -> AsyncEmailsResource:
        from .resources.emails import AsyncEmailsResource

        return AsyncEmailsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def assistant(self) -> AsyncAssistantResource:
        from .resources.assistant import AsyncAssistantResource

        return AsyncAssistantResource(self)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        from .resources.folders import AsyncFoldersResource

        return AsyncFoldersResource(self)

    @cached_property
    def comments(self) -> AsyncCommentsResource:
        from .resources.comments import AsyncCommentsResource

        return AsyncCommentsResource(self)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        from .resources.analytics import AsyncAnalyticsResource

        return AsyncAnalyticsResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        from .resources.organizations import AsyncOrganizationsResource

        return AsyncOrganizationsResource(self)

    @cached_property
    def google_scholar(self) -> AsyncGoogleScholarResource:
        from .resources.google_scholar import AsyncGoogleScholarResource

        return AsyncGoogleScholarResource(self)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        from .resources.api_keys import AsyncAPIKeysResource

        return AsyncAPIKeysResource(self)

    @cached_property
    def admin(self) -> AsyncAdminResource:
        from .resources.admin import AsyncAdminResource

        return AsyncAdminResource(self)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        from .resources.notifications import AsyncNotificationsResource

        return AsyncNotificationsResource(self)

    @cached_property
    def sitemaps(self) -> AsyncSitemapsResource:
        from .resources.sitemaps import AsyncSitemapsResource

        return AsyncSitemapsResource(self)

    @cached_property
    def retrieve(self) -> AsyncRetrieveResource:
        from .resources.retrieve import AsyncRetrieveResource

        return AsyncRetrieveResource(self)

    @cached_property
    def retool(self) -> AsyncRetoolResource:
        from .resources.retool import AsyncRetoolResource

        return AsyncRetoolResource(self)

    @cached_property
    def mcp(self) -> AsyncMcpResource:
        from .resources.mcp import AsyncMcpResource

        return AsyncMcpResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def well_known(self) -> AsyncWellKnownResource:
        from .resources.well_known import AsyncWellKnownResource

        return AsyncWellKnownResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncAlphaxivCatWithRawResponse:
        return AsyncAlphaxivCatWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlphaxivCatWithStreamedResponse:
        return AsyncAlphaxivCatWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key if security.get("api_key", False) else {}),
        }

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AlphaxivCatWithRawResponse:
    _client: AlphaxivCat

    def __init__(self, client: AlphaxivCat) -> None:
        self._client = client

    @cached_property
    def papers(self) -> papers.PapersResourceWithRawResponse:
        from .resources.papers import PapersResourceWithRawResponse

        return PapersResourceWithRawResponse(self._client.papers)

    @cached_property
    def emails(self) -> emails.EmailsResourceWithRawResponse:
        from .resources.emails import EmailsResourceWithRawResponse

        return EmailsResourceWithRawResponse(self._client.emails)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def assistant(self) -> assistant.AssistantResourceWithRawResponse:
        from .resources.assistant import AssistantResourceWithRawResponse

        return AssistantResourceWithRawResponse(self._client.assistant)

    @cached_property
    def folders(self) -> folders.FoldersResourceWithRawResponse:
        from .resources.folders import FoldersResourceWithRawResponse

        return FoldersResourceWithRawResponse(self._client.folders)

    @cached_property
    def comments(self) -> comments.CommentsResourceWithRawResponse:
        from .resources.comments import CommentsResourceWithRawResponse

        return CommentsResourceWithRawResponse(self._client.comments)

    @cached_property
    def analytics(self) -> analytics.AnalyticsResourceWithRawResponse:
        from .resources.analytics import AnalyticsResourceWithRawResponse

        return AnalyticsResourceWithRawResponse(self._client.analytics)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        from .resources.organizations import OrganizationsResourceWithRawResponse

        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def google_scholar(self) -> google_scholar.GoogleScholarResourceWithRawResponse:
        from .resources.google_scholar import GoogleScholarResourceWithRawResponse

        return GoogleScholarResourceWithRawResponse(self._client.google_scholar)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithRawResponse:
        from .resources.api_keys import APIKeysResourceWithRawResponse

        return APIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def admin(self) -> admin.AdminResourceWithRawResponse:
        from .resources.admin import AdminResourceWithRawResponse

        return AdminResourceWithRawResponse(self._client.admin)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithRawResponse:
        from .resources.notifications import NotificationsResourceWithRawResponse

        return NotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def sitemaps(self) -> sitemaps.SitemapsResourceWithRawResponse:
        from .resources.sitemaps import SitemapsResourceWithRawResponse

        return SitemapsResourceWithRawResponse(self._client.sitemaps)

    @cached_property
    def retrieve(self) -> retrieve.RetrieveResourceWithRawResponse:
        from .resources.retrieve import RetrieveResourceWithRawResponse

        return RetrieveResourceWithRawResponse(self._client.retrieve)

    @cached_property
    def retool(self) -> retool.RetoolResourceWithRawResponse:
        from .resources.retool import RetoolResourceWithRawResponse

        return RetoolResourceWithRawResponse(self._client.retool)

    @cached_property
    def mcp(self) -> mcp.McpResourceWithRawResponse:
        from .resources.mcp import McpResourceWithRawResponse

        return McpResourceWithRawResponse(self._client.mcp)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def well_known(self) -> well_known.WellKnownResourceWithRawResponse:
        from .resources.well_known import WellKnownResourceWithRawResponse

        return WellKnownResourceWithRawResponse(self._client.well_known)


class AsyncAlphaxivCatWithRawResponse:
    _client: AsyncAlphaxivCat

    def __init__(self, client: AsyncAlphaxivCat) -> None:
        self._client = client

    @cached_property
    def papers(self) -> papers.AsyncPapersResourceWithRawResponse:
        from .resources.papers import AsyncPapersResourceWithRawResponse

        return AsyncPapersResourceWithRawResponse(self._client.papers)

    @cached_property
    def emails(self) -> emails.AsyncEmailsResourceWithRawResponse:
        from .resources.emails import AsyncEmailsResourceWithRawResponse

        return AsyncEmailsResourceWithRawResponse(self._client.emails)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def assistant(self) -> assistant.AsyncAssistantResourceWithRawResponse:
        from .resources.assistant import AsyncAssistantResourceWithRawResponse

        return AsyncAssistantResourceWithRawResponse(self._client.assistant)

    @cached_property
    def folders(self) -> folders.AsyncFoldersResourceWithRawResponse:
        from .resources.folders import AsyncFoldersResourceWithRawResponse

        return AsyncFoldersResourceWithRawResponse(self._client.folders)

    @cached_property
    def comments(self) -> comments.AsyncCommentsResourceWithRawResponse:
        from .resources.comments import AsyncCommentsResourceWithRawResponse

        return AsyncCommentsResourceWithRawResponse(self._client.comments)

    @cached_property
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithRawResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithRawResponse

        return AsyncAnalyticsResourceWithRawResponse(self._client.analytics)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithRawResponse

        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def google_scholar(self) -> google_scholar.AsyncGoogleScholarResourceWithRawResponse:
        from .resources.google_scholar import AsyncGoogleScholarResourceWithRawResponse

        return AsyncGoogleScholarResourceWithRawResponse(self._client.google_scholar)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithRawResponse:
        from .resources.api_keys import AsyncAPIKeysResourceWithRawResponse

        return AsyncAPIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def admin(self) -> admin.AsyncAdminResourceWithRawResponse:
        from .resources.admin import AsyncAdminResourceWithRawResponse

        return AsyncAdminResourceWithRawResponse(self._client.admin)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithRawResponse:
        from .resources.notifications import AsyncNotificationsResourceWithRawResponse

        return AsyncNotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def sitemaps(self) -> sitemaps.AsyncSitemapsResourceWithRawResponse:
        from .resources.sitemaps import AsyncSitemapsResourceWithRawResponse

        return AsyncSitemapsResourceWithRawResponse(self._client.sitemaps)

    @cached_property
    def retrieve(self) -> retrieve.AsyncRetrieveResourceWithRawResponse:
        from .resources.retrieve import AsyncRetrieveResourceWithRawResponse

        return AsyncRetrieveResourceWithRawResponse(self._client.retrieve)

    @cached_property
    def retool(self) -> retool.AsyncRetoolResourceWithRawResponse:
        from .resources.retool import AsyncRetoolResourceWithRawResponse

        return AsyncRetoolResourceWithRawResponse(self._client.retool)

    @cached_property
    def mcp(self) -> mcp.AsyncMcpResourceWithRawResponse:
        from .resources.mcp import AsyncMcpResourceWithRawResponse

        return AsyncMcpResourceWithRawResponse(self._client.mcp)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def well_known(self) -> well_known.AsyncWellKnownResourceWithRawResponse:
        from .resources.well_known import AsyncWellKnownResourceWithRawResponse

        return AsyncWellKnownResourceWithRawResponse(self._client.well_known)


class AlphaxivCatWithStreamedResponse:
    _client: AlphaxivCat

    def __init__(self, client: AlphaxivCat) -> None:
        self._client = client

    @cached_property
    def papers(self) -> papers.PapersResourceWithStreamingResponse:
        from .resources.papers import PapersResourceWithStreamingResponse

        return PapersResourceWithStreamingResponse(self._client.papers)

    @cached_property
    def emails(self) -> emails.EmailsResourceWithStreamingResponse:
        from .resources.emails import EmailsResourceWithStreamingResponse

        return EmailsResourceWithStreamingResponse(self._client.emails)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def assistant(self) -> assistant.AssistantResourceWithStreamingResponse:
        from .resources.assistant import AssistantResourceWithStreamingResponse

        return AssistantResourceWithStreamingResponse(self._client.assistant)

    @cached_property
    def folders(self) -> folders.FoldersResourceWithStreamingResponse:
        from .resources.folders import FoldersResourceWithStreamingResponse

        return FoldersResourceWithStreamingResponse(self._client.folders)

    @cached_property
    def comments(self) -> comments.CommentsResourceWithStreamingResponse:
        from .resources.comments import CommentsResourceWithStreamingResponse

        return CommentsResourceWithStreamingResponse(self._client.comments)

    @cached_property
    def analytics(self) -> analytics.AnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AnalyticsResourceWithStreamingResponse

        return AnalyticsResourceWithStreamingResponse(self._client.analytics)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        from .resources.organizations import OrganizationsResourceWithStreamingResponse

        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def google_scholar(self) -> google_scholar.GoogleScholarResourceWithStreamingResponse:
        from .resources.google_scholar import GoogleScholarResourceWithStreamingResponse

        return GoogleScholarResourceWithStreamingResponse(self._client.google_scholar)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithStreamingResponse:
        from .resources.api_keys import APIKeysResourceWithStreamingResponse

        return APIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def admin(self) -> admin.AdminResourceWithStreamingResponse:
        from .resources.admin import AdminResourceWithStreamingResponse

        return AdminResourceWithStreamingResponse(self._client.admin)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithStreamingResponse:
        from .resources.notifications import NotificationsResourceWithStreamingResponse

        return NotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def sitemaps(self) -> sitemaps.SitemapsResourceWithStreamingResponse:
        from .resources.sitemaps import SitemapsResourceWithStreamingResponse

        return SitemapsResourceWithStreamingResponse(self._client.sitemaps)

    @cached_property
    def retrieve(self) -> retrieve.RetrieveResourceWithStreamingResponse:
        from .resources.retrieve import RetrieveResourceWithStreamingResponse

        return RetrieveResourceWithStreamingResponse(self._client.retrieve)

    @cached_property
    def retool(self) -> retool.RetoolResourceWithStreamingResponse:
        from .resources.retool import RetoolResourceWithStreamingResponse

        return RetoolResourceWithStreamingResponse(self._client.retool)

    @cached_property
    def mcp(self) -> mcp.McpResourceWithStreamingResponse:
        from .resources.mcp import McpResourceWithStreamingResponse

        return McpResourceWithStreamingResponse(self._client.mcp)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def well_known(self) -> well_known.WellKnownResourceWithStreamingResponse:
        from .resources.well_known import WellKnownResourceWithStreamingResponse

        return WellKnownResourceWithStreamingResponse(self._client.well_known)


class AsyncAlphaxivCatWithStreamedResponse:
    _client: AsyncAlphaxivCat

    def __init__(self, client: AsyncAlphaxivCat) -> None:
        self._client = client

    @cached_property
    def papers(self) -> papers.AsyncPapersResourceWithStreamingResponse:
        from .resources.papers import AsyncPapersResourceWithStreamingResponse

        return AsyncPapersResourceWithStreamingResponse(self._client.papers)

    @cached_property
    def emails(self) -> emails.AsyncEmailsResourceWithStreamingResponse:
        from .resources.emails import AsyncEmailsResourceWithStreamingResponse

        return AsyncEmailsResourceWithStreamingResponse(self._client.emails)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def assistant(self) -> assistant.AsyncAssistantResourceWithStreamingResponse:
        from .resources.assistant import AsyncAssistantResourceWithStreamingResponse

        return AsyncAssistantResourceWithStreamingResponse(self._client.assistant)

    @cached_property
    def folders(self) -> folders.AsyncFoldersResourceWithStreamingResponse:
        from .resources.folders import AsyncFoldersResourceWithStreamingResponse

        return AsyncFoldersResourceWithStreamingResponse(self._client.folders)

    @cached_property
    def comments(self) -> comments.AsyncCommentsResourceWithStreamingResponse:
        from .resources.comments import AsyncCommentsResourceWithStreamingResponse

        return AsyncCommentsResourceWithStreamingResponse(self._client.comments)

    @cached_property
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithStreamingResponse

        return AsyncAnalyticsResourceWithStreamingResponse(self._client.analytics)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse

        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def google_scholar(self) -> google_scholar.AsyncGoogleScholarResourceWithStreamingResponse:
        from .resources.google_scholar import AsyncGoogleScholarResourceWithStreamingResponse

        return AsyncGoogleScholarResourceWithStreamingResponse(self._client.google_scholar)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithStreamingResponse:
        from .resources.api_keys import AsyncAPIKeysResourceWithStreamingResponse

        return AsyncAPIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def admin(self) -> admin.AsyncAdminResourceWithStreamingResponse:
        from .resources.admin import AsyncAdminResourceWithStreamingResponse

        return AsyncAdminResourceWithStreamingResponse(self._client.admin)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithStreamingResponse:
        from .resources.notifications import AsyncNotificationsResourceWithStreamingResponse

        return AsyncNotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def sitemaps(self) -> sitemaps.AsyncSitemapsResourceWithStreamingResponse:
        from .resources.sitemaps import AsyncSitemapsResourceWithStreamingResponse

        return AsyncSitemapsResourceWithStreamingResponse(self._client.sitemaps)

    @cached_property
    def retrieve(self) -> retrieve.AsyncRetrieveResourceWithStreamingResponse:
        from .resources.retrieve import AsyncRetrieveResourceWithStreamingResponse

        return AsyncRetrieveResourceWithStreamingResponse(self._client.retrieve)

    @cached_property
    def retool(self) -> retool.AsyncRetoolResourceWithStreamingResponse:
        from .resources.retool import AsyncRetoolResourceWithStreamingResponse

        return AsyncRetoolResourceWithStreamingResponse(self._client.retool)

    @cached_property
    def mcp(self) -> mcp.AsyncMcpResourceWithStreamingResponse:
        from .resources.mcp import AsyncMcpResourceWithStreamingResponse

        return AsyncMcpResourceWithStreamingResponse(self._client.mcp)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def well_known(self) -> well_known.AsyncWellKnownResourceWithStreamingResponse:
        from .resources.well_known import AsyncWellKnownResourceWithStreamingResponse

        return AsyncWellKnownResourceWithStreamingResponse(self._client.well_known)


Client = AlphaxivCat

AsyncClient = AsyncAlphaxivCat
