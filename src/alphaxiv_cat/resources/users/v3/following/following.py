# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .topics import (
    TopicsResource,
    AsyncTopicsResource,
    TopicsResourceWithRawResponse,
    AsyncTopicsResourceWithRawResponse,
    TopicsResourceWithStreamingResponse,
    AsyncTopicsResourceWithStreamingResponse,
)
from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.users.v3.following_list_response import FollowingListResponse

__all__ = ["FollowingResource", "AsyncFollowingResource"]


class FollowingResource(SyncAPIResource):
    @cached_property
    def topics(self) -> TopicsResource:
        return TopicsResource(self._client)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FollowingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return FollowingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FollowingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return FollowingResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowingListResponse:
        """
        List the users that the given user is following

        Source file:
        `api-server/src/controllers/users/v3/get-following-users.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/users/v3/{id}/following", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FollowingListResponse,
        )


class AsyncFollowingResource(AsyncAPIResource):
    @cached_property
    def topics(self) -> AsyncTopicsResource:
        return AsyncTopicsResource(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFollowingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFollowingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFollowingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncFollowingResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowingListResponse:
        """
        List the users that the given user is following

        Source file:
        `api-server/src/controllers/users/v3/get-following-users.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/users/v3/{id}/following", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FollowingListResponse,
        )


class FollowingResourceWithRawResponse:
    def __init__(self, following: FollowingResource) -> None:
        self._following = following

        self.list = to_raw_response_wrapper(
            following.list,
        )

    @cached_property
    def topics(self) -> TopicsResourceWithRawResponse:
        return TopicsResourceWithRawResponse(self._following.topics)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._following.organizations)


class AsyncFollowingResourceWithRawResponse:
    def __init__(self, following: AsyncFollowingResource) -> None:
        self._following = following

        self.list = async_to_raw_response_wrapper(
            following.list,
        )

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithRawResponse:
        return AsyncTopicsResourceWithRawResponse(self._following.topics)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._following.organizations)


class FollowingResourceWithStreamingResponse:
    def __init__(self, following: FollowingResource) -> None:
        self._following = following

        self.list = to_streamed_response_wrapper(
            following.list,
        )

    @cached_property
    def topics(self) -> TopicsResourceWithStreamingResponse:
        return TopicsResourceWithStreamingResponse(self._following.topics)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._following.organizations)


class AsyncFollowingResourceWithStreamingResponse:
    def __init__(self, following: AsyncFollowingResource) -> None:
        self._following = following

        self.list = async_to_streamed_response_wrapper(
            following.list,
        )

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithStreamingResponse:
        return AsyncTopicsResourceWithStreamingResponse(self._following.topics)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._following.organizations)
