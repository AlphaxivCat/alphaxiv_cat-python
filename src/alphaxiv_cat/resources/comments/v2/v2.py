# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from .moderator import (
    ModeratorResource,
    AsyncModeratorResource,
    ModeratorResourceWithRawResponse,
    AsyncModeratorResourceWithRawResponse,
    ModeratorResourceWithStreamingResponse,
    AsyncModeratorResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.comments import v2_flag_params

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def moderator(self) -> ModeratorResource:
        return ModeratorResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)

    def delete(
        self,
        comment: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a comment by UUID

        Source file:
        `api-server/src/controllers/comments/v2/delete-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/comments/v2/{comment}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def downvote(
        self,
        comment: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Downvote a comment by UUID

        Source file:
        `api-server/src/controllers/comments/v2/downvote-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/comments/v2/{comment}/downvote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def flag(
        self,
        comment: str,
        *,
        reason: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Flag a comment for moderator review

        Source file: `api-server/src/controllers/comments/v2/flag-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/comments/v2/{comment}/flag",
            body=maybe_transform({"reason": reason}, v2_flag_params.V2FlagParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def toggle_endorse(
        self,
        comment: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Toggle author endorsement of a comment

        Source file:
        `api-server/src/controllers/comments/v2/toggle-comment-endorse.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/comments/v2/{comment}/endorse",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upvote(
        self,
        comment: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Upvote a comment by UUID

        Source file:
        `api-server/src/controllers/comments/v2/upvote-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/comments/v2/{comment}/upvote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def moderator(self) -> AsyncModeratorResource:
        return AsyncModeratorResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)

    async def delete(
        self,
        comment: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a comment by UUID

        Source file:
        `api-server/src/controllers/comments/v2/delete-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/comments/v2/{comment}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def downvote(
        self,
        comment: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Downvote a comment by UUID

        Source file:
        `api-server/src/controllers/comments/v2/downvote-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/comments/v2/{comment}/downvote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def flag(
        self,
        comment: str,
        *,
        reason: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Flag a comment for moderator review

        Source file: `api-server/src/controllers/comments/v2/flag-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/comments/v2/{comment}/flag",
            body=await async_maybe_transform({"reason": reason}, v2_flag_params.V2FlagParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def toggle_endorse(
        self,
        comment: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Toggle author endorsement of a comment

        Source file:
        `api-server/src/controllers/comments/v2/toggle-comment-endorse.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/comments/v2/{comment}/endorse",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upvote(
        self,
        comment: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Upvote a comment by UUID

        Source file:
        `api-server/src/controllers/comments/v2/upvote-comment.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/comments/v2/{comment}/upvote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.delete = to_raw_response_wrapper(
            v2.delete,
        )
        self.downvote = to_raw_response_wrapper(
            v2.downvote,
        )
        self.flag = to_raw_response_wrapper(
            v2.flag,
        )
        self.toggle_endorse = to_raw_response_wrapper(
            v2.toggle_endorse,
        )
        self.upvote = to_raw_response_wrapper(
            v2.upvote,
        )

    @cached_property
    def moderator(self) -> ModeratorResourceWithRawResponse:
        return ModeratorResourceWithRawResponse(self._v2.moderator)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.delete = async_to_raw_response_wrapper(
            v2.delete,
        )
        self.downvote = async_to_raw_response_wrapper(
            v2.downvote,
        )
        self.flag = async_to_raw_response_wrapper(
            v2.flag,
        )
        self.toggle_endorse = async_to_raw_response_wrapper(
            v2.toggle_endorse,
        )
        self.upvote = async_to_raw_response_wrapper(
            v2.upvote,
        )

    @cached_property
    def moderator(self) -> AsyncModeratorResourceWithRawResponse:
        return AsyncModeratorResourceWithRawResponse(self._v2.moderator)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.delete = to_streamed_response_wrapper(
            v2.delete,
        )
        self.downvote = to_streamed_response_wrapper(
            v2.downvote,
        )
        self.flag = to_streamed_response_wrapper(
            v2.flag,
        )
        self.toggle_endorse = to_streamed_response_wrapper(
            v2.toggle_endorse,
        )
        self.upvote = to_streamed_response_wrapper(
            v2.upvote,
        )

    @cached_property
    def moderator(self) -> ModeratorResourceWithStreamingResponse:
        return ModeratorResourceWithStreamingResponse(self._v2.moderator)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.delete = async_to_streamed_response_wrapper(
            v2.delete,
        )
        self.downvote = async_to_streamed_response_wrapper(
            v2.downvote,
        )
        self.flag = async_to_streamed_response_wrapper(
            v2.flag,
        )
        self.toggle_endorse = async_to_streamed_response_wrapper(
            v2.toggle_endorse,
        )
        self.upvote = async_to_streamed_response_wrapper(
            v2.upvote,
        )

    @cached_property
    def moderator(self) -> AsyncModeratorResourceWithStreamingResponse:
        return AsyncModeratorResourceWithStreamingResponse(self._v2.moderator)
