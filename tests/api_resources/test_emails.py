# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types import (
    EmailProcessBouncedEmailResponse,
    EmailCaptureBouncedEmailsResponse,
    EmailKickoffCommentUpdateResponse,
    EmailKickoffGeneralUpdateResponse,
    EmailProcessCommentUpdateResponse,
    EmailProcessGeneralUpdateResponse,
    EmailCaptureResendBouncedEmailResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_capture_bounced_emails(self, client: AlphaxivCat) -> None:
        email = client.emails.capture_bounced_emails(
            message="Message",
            type="Type",
        )
        assert_matches_type(EmailCaptureBouncedEmailsResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_capture_bounced_emails(self, client: AlphaxivCat) -> None:
        response = client.emails.with_raw_response.capture_bounced_emails(
            message="Message",
            type="Type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailCaptureBouncedEmailsResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_capture_bounced_emails(self, client: AlphaxivCat) -> None:
        with client.emails.with_streaming_response.capture_bounced_emails(
            message="Message",
            type="Type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailCaptureBouncedEmailsResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_capture_resend_bounced_email(self, client: AlphaxivCat) -> None:
        email = client.emails.capture_resend_bounced_email(
            data={},
            type="type",
        )
        assert_matches_type(EmailCaptureResendBouncedEmailResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_capture_resend_bounced_email_with_all_params(self, client: AlphaxivCat) -> None:
        email = client.emails.capture_resend_bounced_email(
            data={"to": ["string"]},
            type="type",
        )
        assert_matches_type(EmailCaptureResendBouncedEmailResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_capture_resend_bounced_email(self, client: AlphaxivCat) -> None:
        response = client.emails.with_raw_response.capture_resend_bounced_email(
            data={},
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailCaptureResendBouncedEmailResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_capture_resend_bounced_email(self, client: AlphaxivCat) -> None:
        with client.emails.with_streaming_response.capture_resend_bounced_email(
            data={},
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailCaptureResendBouncedEmailResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_comment_update(self, client: AlphaxivCat) -> None:
        email = client.emails.kickoff_comment_update(
            custom="true",
            role="role",
            window="window",
        )
        assert_matches_type(EmailKickoffCommentUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_comment_update(self, client: AlphaxivCat) -> None:
        response = client.emails.with_raw_response.kickoff_comment_update(
            custom="true",
            role="role",
            window="window",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailKickoffCommentUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_comment_update(self, client: AlphaxivCat) -> None:
        with client.emails.with_streaming_response.kickoff_comment_update(
            custom="true",
            role="role",
            window="window",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailKickoffCommentUpdateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_kickoff_comment_update(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role` but received ''"):
            client.emails.with_raw_response.kickoff_comment_update(
                custom="true",
                role="",
                window="window",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `window` but received ''"):
            client.emails.with_raw_response.kickoff_comment_update(
                custom="true",
                role="role",
                window="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_kickoff_general_update(self, client: AlphaxivCat) -> None:
        email = client.emails.kickoff_general_update(
            "role",
        )
        assert_matches_type(EmailKickoffGeneralUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_kickoff_general_update(self, client: AlphaxivCat) -> None:
        response = client.emails.with_raw_response.kickoff_general_update(
            "role",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailKickoffGeneralUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_kickoff_general_update(self, client: AlphaxivCat) -> None:
        with client.emails.with_streaming_response.kickoff_general_update(
            "role",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailKickoffGeneralUpdateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_kickoff_general_update(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role` but received ''"):
            client.emails.with_raw_response.kickoff_general_update(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_bounced_email(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            email = client.emails.process_bounced_email(
                email="dev@stainless.com",
            )

        assert_matches_type(EmailProcessBouncedEmailResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process_bounced_email(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.emails.with_raw_response.process_bounced_email(
                email="dev@stainless.com",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailProcessBouncedEmailResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process_bounced_email(self, client: AlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            with client.emails.with_streaming_response.process_bounced_email(
                email="dev@stainless.com",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                email = response.parse()
                assert_matches_type(EmailProcessBouncedEmailResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_comment_update(self, client: AlphaxivCat) -> None:
        email = client.emails.process_comment_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailProcessCommentUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_comment_update_with_all_params(self, client: AlphaxivCat) -> None:
        email = client.emails.process_comment_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_content={
                "events": [
                    {
                        "date": "date",
                        "description": "description",
                        "link": "link",
                        "title": "title",
                        "end_time_raw": "endTimeRaw",
                        "start_time_raw": "startTimeRaw",
                    }
                ],
                "intro_text": "introText",
                "subject": "subject",
            },
        )
        assert_matches_type(EmailProcessCommentUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process_comment_update(self, client: AlphaxivCat) -> None:
        response = client.emails.with_raw_response.process_comment_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailProcessCommentUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process_comment_update(self, client: AlphaxivCat) -> None:
        with client.emails.with_streaming_response.process_comment_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailProcessCommentUpdateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_process_general_update(self, client: AlphaxivCat) -> None:
        email = client.emails.process_general_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailProcessGeneralUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_process_general_update(self, client: AlphaxivCat) -> None:
        response = client.emails.with_raw_response.process_general_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailProcessGeneralUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_process_general_update(self, client: AlphaxivCat) -> None:
        with client.emails.with_streaming_response.process_general_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailProcessGeneralUpdateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_capture_bounced_emails(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.emails.capture_bounced_emails(
            message="Message",
            type="Type",
        )
        assert_matches_type(EmailCaptureBouncedEmailsResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_capture_bounced_emails(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.emails.with_raw_response.capture_bounced_emails(
            message="Message",
            type="Type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailCaptureBouncedEmailsResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_capture_bounced_emails(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.emails.with_streaming_response.capture_bounced_emails(
            message="Message",
            type="Type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailCaptureBouncedEmailsResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_capture_resend_bounced_email(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.emails.capture_resend_bounced_email(
            data={},
            type="type",
        )
        assert_matches_type(EmailCaptureResendBouncedEmailResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_capture_resend_bounced_email_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.emails.capture_resend_bounced_email(
            data={"to": ["string"]},
            type="type",
        )
        assert_matches_type(EmailCaptureResendBouncedEmailResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_capture_resend_bounced_email(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.emails.with_raw_response.capture_resend_bounced_email(
            data={},
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailCaptureResendBouncedEmailResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_capture_resend_bounced_email(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.emails.with_streaming_response.capture_resend_bounced_email(
            data={},
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailCaptureResendBouncedEmailResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_comment_update(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.emails.kickoff_comment_update(
            custom="true",
            role="role",
            window="window",
        )
        assert_matches_type(EmailKickoffCommentUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_comment_update(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.emails.with_raw_response.kickoff_comment_update(
            custom="true",
            role="role",
            window="window",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailKickoffCommentUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_comment_update(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.emails.with_streaming_response.kickoff_comment_update(
            custom="true",
            role="role",
            window="window",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailKickoffCommentUpdateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_kickoff_comment_update(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role` but received ''"):
            await async_client.emails.with_raw_response.kickoff_comment_update(
                custom="true",
                role="",
                window="window",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `window` but received ''"):
            await async_client.emails.with_raw_response.kickoff_comment_update(
                custom="true",
                role="role",
                window="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_kickoff_general_update(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.emails.kickoff_general_update(
            "role",
        )
        assert_matches_type(EmailKickoffGeneralUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_kickoff_general_update(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.emails.with_raw_response.kickoff_general_update(
            "role",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailKickoffGeneralUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_kickoff_general_update(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.emails.with_streaming_response.kickoff_general_update(
            "role",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailKickoffGeneralUpdateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_kickoff_general_update(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `role` but received ''"):
            await async_client.emails.with_raw_response.kickoff_general_update(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_bounced_email(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            email = await async_client.emails.process_bounced_email(
                email="dev@stainless.com",
            )

        assert_matches_type(EmailProcessBouncedEmailResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process_bounced_email(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.emails.with_raw_response.process_bounced_email(
                email="dev@stainless.com",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailProcessBouncedEmailResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process_bounced_email(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.emails.with_streaming_response.process_bounced_email(
                email="dev@stainless.com",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                email = await response.parse()
                assert_matches_type(EmailProcessBouncedEmailResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_comment_update(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.emails.process_comment_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailProcessCommentUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_comment_update_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.emails.process_comment_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_content={
                "events": [
                    {
                        "date": "date",
                        "description": "description",
                        "link": "link",
                        "title": "title",
                        "end_time_raw": "endTimeRaw",
                        "start_time_raw": "startTimeRaw",
                    }
                ],
                "intro_text": "introText",
                "subject": "subject",
            },
        )
        assert_matches_type(EmailProcessCommentUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process_comment_update(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.emails.with_raw_response.process_comment_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailProcessCommentUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process_comment_update(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.emails.with_streaming_response.process_comment_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailProcessCommentUpdateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_process_general_update(self, async_client: AsyncAlphaxivCat) -> None:
        email = await async_client.emails.process_general_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EmailProcessGeneralUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_process_general_update(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.emails.with_raw_response.process_general_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailProcessGeneralUpdateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_process_general_update(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.emails.with_streaming_response.process_general_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailProcessGeneralUpdateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True
