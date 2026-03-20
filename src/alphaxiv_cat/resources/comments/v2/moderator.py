# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.comments.v2 import moderator_toggle_flags_params, moderator_send_feedback_params
from ....types.comments.v2.moderator_toggle_flags_response import ModeratorToggleFlagsResponse

__all__ = ["ModeratorResource", "AsyncModeratorResource"]


class ModeratorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModeratorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return ModeratorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModeratorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return ModeratorResourceWithStreamingResponse(self)

    def send_feedback(
        self,
        comment: str,
        *,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send moderator feedback to comment author

        Source file:
        `api-server/src/controllers/comments/v2/moderator-send-feedback.controller.ts`

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
            path_template("/comments/v2/{comment}/moderator/send-feedback", comment=comment),
            body=maybe_transform({"message": message}, moderator_send_feedback_params.ModeratorSendFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def toggle_flags(
        self,
        comment: str,
        *,
        addressed: bool | Omit = omit,
        closed: bool | Omit = omit,
        flag_addressed: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModeratorToggleFlagsResponse:
        """
        Toggle one (or more) of a set of comment moderation flags

        Source file:
        `api-server/src/controllers/comments/v2/toggle-comment-moderation-flag.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        return self._post(
            path_template("/comments/v2/{comment}/moderator/toggle-flags", comment=comment),
            body=maybe_transform(
                {
                    "addressed": addressed,
                    "closed": closed,
                    "flag_addressed": flag_addressed,
                },
                moderator_toggle_flags_params.ModeratorToggleFlagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModeratorToggleFlagsResponse,
        )


class AsyncModeratorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModeratorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModeratorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModeratorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/AlphaxivCat/alphaxiv_cat-python#with_streaming_response
        """
        return AsyncModeratorResourceWithStreamingResponse(self)

    async def send_feedback(
        self,
        comment: str,
        *,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send moderator feedback to comment author

        Source file:
        `api-server/src/controllers/comments/v2/moderator-send-feedback.controller.ts`

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
            path_template("/comments/v2/{comment}/moderator/send-feedback", comment=comment),
            body=await async_maybe_transform(
                {"message": message}, moderator_send_feedback_params.ModeratorSendFeedbackParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def toggle_flags(
        self,
        comment: str,
        *,
        addressed: bool | Omit = omit,
        closed: bool | Omit = omit,
        flag_addressed: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModeratorToggleFlagsResponse:
        """
        Toggle one (or more) of a set of comment moderation flags

        Source file:
        `api-server/src/controllers/comments/v2/toggle-comment-moderation-flag.controller.ts`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment:
            raise ValueError(f"Expected a non-empty value for `comment` but received {comment!r}")
        return await self._post(
            path_template("/comments/v2/{comment}/moderator/toggle-flags", comment=comment),
            body=await async_maybe_transform(
                {
                    "addressed": addressed,
                    "closed": closed,
                    "flag_addressed": flag_addressed,
                },
                moderator_toggle_flags_params.ModeratorToggleFlagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModeratorToggleFlagsResponse,
        )


class ModeratorResourceWithRawResponse:
    def __init__(self, moderator: ModeratorResource) -> None:
        self._moderator = moderator

        self.send_feedback = to_raw_response_wrapper(
            moderator.send_feedback,
        )
        self.toggle_flags = to_raw_response_wrapper(
            moderator.toggle_flags,
        )


class AsyncModeratorResourceWithRawResponse:
    def __init__(self, moderator: AsyncModeratorResource) -> None:
        self._moderator = moderator

        self.send_feedback = async_to_raw_response_wrapper(
            moderator.send_feedback,
        )
        self.toggle_flags = async_to_raw_response_wrapper(
            moderator.toggle_flags,
        )


class ModeratorResourceWithStreamingResponse:
    def __init__(self, moderator: ModeratorResource) -> None:
        self._moderator = moderator

        self.send_feedback = to_streamed_response_wrapper(
            moderator.send_feedback,
        )
        self.toggle_flags = to_streamed_response_wrapper(
            moderator.toggle_flags,
        )


class AsyncModeratorResourceWithStreamingResponse:
    def __init__(self, moderator: AsyncModeratorResource) -> None:
        self._moderator = moderator

        self.send_feedback = async_to_streamed_response_wrapper(
            moderator.send_feedback,
        )
        self.toggle_flags = async_to_streamed_response_wrapper(
            moderator.toggle_flags,
        )
