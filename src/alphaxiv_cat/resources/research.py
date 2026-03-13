# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import research_create_project_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ResearchResource", "AsyncResearchResource"]


class ResearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return ResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return ResearchResourceWithStreamingResponse(self)

    def create_project(
        self,
        *,
        name: str,
        folder: Optional[research_create_project_params.Folder] | Omit = omit,
        initial_papers: SequenceNotStr[str] | Omit = omit,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Create a research project

        Source file:
        `api-server/src/controllers/research/v1/create-project.controller.ts`

        Args:
          folder: Prefill the project with a set of research papers.

          initial_papers: Add these papers to the group on init

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/research/v1",
            body=maybe_transform(
                {
                    "name": name,
                    "folder": folder,
                    "initial_papers": initial_papers,
                    "parent_id": parent_id,
                },
                research_create_project_params.ResearchCreateProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncResearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncResearchResourceWithStreamingResponse(self)

    async def create_project(
        self,
        *,
        name: str,
        folder: Optional[research_create_project_params.Folder] | Omit = omit,
        initial_papers: SequenceNotStr[str] | Omit = omit,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Create a research project

        Source file:
        `api-server/src/controllers/research/v1/create-project.controller.ts`

        Args:
          folder: Prefill the project with a set of research papers.

          initial_papers: Add these papers to the group on init

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/research/v1",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "folder": folder,
                    "initial_papers": initial_papers,
                    "parent_id": parent_id,
                },
                research_create_project_params.ResearchCreateProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ResearchResourceWithRawResponse:
    def __init__(self, research: ResearchResource) -> None:
        self._research = research

        self.create_project = to_raw_response_wrapper(
            research.create_project,
        )


class AsyncResearchResourceWithRawResponse:
    def __init__(self, research: AsyncResearchResource) -> None:
        self._research = research

        self.create_project = async_to_raw_response_wrapper(
            research.create_project,
        )


class ResearchResourceWithStreamingResponse:
    def __init__(self, research: ResearchResource) -> None:
        self._research = research

        self.create_project = to_streamed_response_wrapper(
            research.create_project,
        )


class AsyncResearchResourceWithStreamingResponse:
    def __init__(self, research: AsyncResearchResource) -> None:
        self._research = research

        self.create_project = async_to_streamed_response_wrapper(
            research.create_project,
        )
