# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .shared import (
    SharedResource,
    AsyncSharedResource,
    SharedResourceWithRawResponse,
    AsyncSharedResourceWithRawResponse,
    SharedResourceWithStreamingResponse,
    AsyncSharedResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.folders import (
    v3_create_params,
    v3_add_papers_params,
    v3_move_papers_params,
    v3_update_name_params,
    v3_remove_papers_params,
    v3_update_parent_params,
    v3_toggle_sharing_params,
)
from ....types.folders.v3_list_response import V3ListResponse
from ....types.folders.v3_create_response import V3CreateResponse
from ....types.folders.v3_add_papers_response import V3AddPapersResponse
from ....types.folders.v3_move_papers_response import V3MovePapersResponse
from ....types.folders.v3_toggle_sharing_response import V3ToggleSharingResponse

__all__ = ["V3Resource", "AsyncV3Resource"]


class V3Resource(SyncAPIResource):
    @cached_property
    def shared(self) -> SharedResource:
        return SharedResource(self._client)

    @cached_property
    def with_raw_response(self) -> V3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return V3ResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        folder_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3CreateResponse:
        """
        Create a new folder for the current user

        Source file: `api-server/src/controllers/folders/v3/create-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/folders/v3",
            body=maybe_transform({"folder_name": folder_name}, v3_create_params.V3CreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3CreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3ListResponse:
        """
        Get all folders for the current user

        Source file: `api-server/src/controllers/folders/v3/get-folders.controller.ts`
        """
        return self._get(
            "/folders/v3",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3ListResponse,
        )

    def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a folder

        Source file: `api-server/src/controllers/folders/v3/delete-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/folders/v3/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_papers(
        self,
        folder_id: str,
        *,
        paper_group_ids: SequenceNotStr[str] | Omit = omit,
        universal_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3AddPapersResponse:
        """
        Add papers to a folder (without removing from other folders)

        Source file:
        `api-server/src/controllers/folders/v3/add-papers-to-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._post(
            f"/folders/v3/{folder_id}/add-papers",
            body=maybe_transform(
                {
                    "paper_group_ids": paper_group_ids,
                    "universal_ids": universal_ids,
                },
                v3_add_papers_params.V3AddPapersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3AddPapersResponse,
        )

    def move_papers(
        self,
        folder_id: str,
        *,
        paper_group_ids: SequenceNotStr[str],
        from_folder_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3MovePapersResponse:
        """
        Move papers from source folder to destination folder

        Source file:
        `api-server/src/controllers/folders/v3/move-papers-to-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._post(
            f"/folders/v3/{folder_id}/move-papers",
            body=maybe_transform(
                {
                    "paper_group_ids": paper_group_ids,
                    "from_folder_id": from_folder_id,
                },
                v3_move_papers_params.V3MovePapersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3MovePapersResponse,
        )

    def remove_papers(
        self,
        folder_id: str,
        *,
        paper_group_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove papers from a specific folder

        Source file: `api-server/src/controllers/folders/v3/remove-papers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/folders/v3/{folder_id}/remove-papers",
            body=maybe_transform({"paper_group_ids": paper_group_ids}, v3_remove_papers_params.V3RemovePapersParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def toggle_sharing(
        self,
        folder_id: str,
        *,
        sharing_status: Literal["not_shared", "shared"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3ToggleSharingResponse:
        """
        Toggle whether a folder and all its descendant folders are shared or not

        Source file:
        `api-server/src/controllers/folders/v3/toggle-folder-sharing.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._patch(
            f"/folders/v3/{folder_id}/sharing",
            body=maybe_transform({"sharing_status": sharing_status}, v3_toggle_sharing_params.V3ToggleSharingParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3ToggleSharingResponse,
        )

    def update_name(
        self,
        folder_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Rename a folder

        Source file:
        `api-server/src/controllers/folders/v3/update-folder-name.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/folders/v3/{folder_id}",
            body=maybe_transform({"name": name}, v3_update_name_params.V3UpdateNameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_parent(
        self,
        folder_id: str,
        *,
        parent_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a folder's parent (for nesting)

        Source file:
        `api-server/src/controllers/folders/v3/update-folder-parent.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/folders/v3/{folder_id}/parent",
            body=maybe_transform({"parent_id": parent_id}, v3_update_parent_params.V3UpdateParentParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncV3Resource(AsyncAPIResource):
    @cached_property
    def shared(self) -> AsyncSharedResource:
        return AsyncSharedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV3ResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        folder_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3CreateResponse:
        """
        Create a new folder for the current user

        Source file: `api-server/src/controllers/folders/v3/create-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/folders/v3",
            body=await async_maybe_transform({"folder_name": folder_name}, v3_create_params.V3CreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3CreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3ListResponse:
        """
        Get all folders for the current user

        Source file: `api-server/src/controllers/folders/v3/get-folders.controller.ts`
        """
        return await self._get(
            "/folders/v3",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3ListResponse,
        )

    async def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a folder

        Source file: `api-server/src/controllers/folders/v3/delete-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/folders/v3/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_papers(
        self,
        folder_id: str,
        *,
        paper_group_ids: SequenceNotStr[str] | Omit = omit,
        universal_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3AddPapersResponse:
        """
        Add papers to a folder (without removing from other folders)

        Source file:
        `api-server/src/controllers/folders/v3/add-papers-to-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._post(
            f"/folders/v3/{folder_id}/add-papers",
            body=await async_maybe_transform(
                {
                    "paper_group_ids": paper_group_ids,
                    "universal_ids": universal_ids,
                },
                v3_add_papers_params.V3AddPapersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3AddPapersResponse,
        )

    async def move_papers(
        self,
        folder_id: str,
        *,
        paper_group_ids: SequenceNotStr[str],
        from_folder_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3MovePapersResponse:
        """
        Move papers from source folder to destination folder

        Source file:
        `api-server/src/controllers/folders/v3/move-papers-to-folder.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._post(
            f"/folders/v3/{folder_id}/move-papers",
            body=await async_maybe_transform(
                {
                    "paper_group_ids": paper_group_ids,
                    "from_folder_id": from_folder_id,
                },
                v3_move_papers_params.V3MovePapersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3MovePapersResponse,
        )

    async def remove_papers(
        self,
        folder_id: str,
        *,
        paper_group_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove papers from a specific folder

        Source file: `api-server/src/controllers/folders/v3/remove-papers.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/folders/v3/{folder_id}/remove-papers",
            body=await async_maybe_transform(
                {"paper_group_ids": paper_group_ids}, v3_remove_papers_params.V3RemovePapersParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def toggle_sharing(
        self,
        folder_id: str,
        *,
        sharing_status: Literal["not_shared", "shared"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V3ToggleSharingResponse:
        """
        Toggle whether a folder and all its descendant folders are shared or not

        Source file:
        `api-server/src/controllers/folders/v3/toggle-folder-sharing.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._patch(
            f"/folders/v3/{folder_id}/sharing",
            body=await async_maybe_transform(
                {"sharing_status": sharing_status}, v3_toggle_sharing_params.V3ToggleSharingParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3ToggleSharingResponse,
        )

    async def update_name(
        self,
        folder_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Rename a folder

        Source file:
        `api-server/src/controllers/folders/v3/update-folder-name.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/folders/v3/{folder_id}",
            body=await async_maybe_transform({"name": name}, v3_update_name_params.V3UpdateNameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_parent(
        self,
        folder_id: str,
        *,
        parent_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a folder's parent (for nesting)

        Source file:
        `api-server/src/controllers/folders/v3/update-folder-parent.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/folders/v3/{folder_id}/parent",
            body=await async_maybe_transform({"parent_id": parent_id}, v3_update_parent_params.V3UpdateParentParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class V3ResourceWithRawResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

        self.create = to_raw_response_wrapper(
            v3.create,
        )
        self.list = to_raw_response_wrapper(
            v3.list,
        )
        self.delete = to_raw_response_wrapper(
            v3.delete,
        )
        self.add_papers = to_raw_response_wrapper(
            v3.add_papers,
        )
        self.move_papers = to_raw_response_wrapper(
            v3.move_papers,
        )
        self.remove_papers = to_raw_response_wrapper(
            v3.remove_papers,
        )
        self.toggle_sharing = to_raw_response_wrapper(
            v3.toggle_sharing,
        )
        self.update_name = to_raw_response_wrapper(
            v3.update_name,
        )
        self.update_parent = to_raw_response_wrapper(
            v3.update_parent,
        )

    @cached_property
    def shared(self) -> SharedResourceWithRawResponse:
        return SharedResourceWithRawResponse(self._v3.shared)


class AsyncV3ResourceWithRawResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

        self.create = async_to_raw_response_wrapper(
            v3.create,
        )
        self.list = async_to_raw_response_wrapper(
            v3.list,
        )
        self.delete = async_to_raw_response_wrapper(
            v3.delete,
        )
        self.add_papers = async_to_raw_response_wrapper(
            v3.add_papers,
        )
        self.move_papers = async_to_raw_response_wrapper(
            v3.move_papers,
        )
        self.remove_papers = async_to_raw_response_wrapper(
            v3.remove_papers,
        )
        self.toggle_sharing = async_to_raw_response_wrapper(
            v3.toggle_sharing,
        )
        self.update_name = async_to_raw_response_wrapper(
            v3.update_name,
        )
        self.update_parent = async_to_raw_response_wrapper(
            v3.update_parent,
        )

    @cached_property
    def shared(self) -> AsyncSharedResourceWithRawResponse:
        return AsyncSharedResourceWithRawResponse(self._v3.shared)


class V3ResourceWithStreamingResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

        self.create = to_streamed_response_wrapper(
            v3.create,
        )
        self.list = to_streamed_response_wrapper(
            v3.list,
        )
        self.delete = to_streamed_response_wrapper(
            v3.delete,
        )
        self.add_papers = to_streamed_response_wrapper(
            v3.add_papers,
        )
        self.move_papers = to_streamed_response_wrapper(
            v3.move_papers,
        )
        self.remove_papers = to_streamed_response_wrapper(
            v3.remove_papers,
        )
        self.toggle_sharing = to_streamed_response_wrapper(
            v3.toggle_sharing,
        )
        self.update_name = to_streamed_response_wrapper(
            v3.update_name,
        )
        self.update_parent = to_streamed_response_wrapper(
            v3.update_parent,
        )

    @cached_property
    def shared(self) -> SharedResourceWithStreamingResponse:
        return SharedResourceWithStreamingResponse(self._v3.shared)


class AsyncV3ResourceWithStreamingResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

        self.create = async_to_streamed_response_wrapper(
            v3.create,
        )
        self.list = async_to_streamed_response_wrapper(
            v3.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            v3.delete,
        )
        self.add_papers = async_to_streamed_response_wrapper(
            v3.add_papers,
        )
        self.move_papers = async_to_streamed_response_wrapper(
            v3.move_papers,
        )
        self.remove_papers = async_to_streamed_response_wrapper(
            v3.remove_papers,
        )
        self.toggle_sharing = async_to_streamed_response_wrapper(
            v3.toggle_sharing,
        )
        self.update_name = async_to_streamed_response_wrapper(
            v3.update_name,
        )
        self.update_parent = async_to_streamed_response_wrapper(
            v3.update_parent,
        )

    @cached_property
    def shared(self) -> AsyncSharedResourceWithStreamingResponse:
        return AsyncSharedResourceWithStreamingResponse(self._v3.shared)
