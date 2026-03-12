# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from alphaxiv_cat import AlphaxivCat, AsyncAlphaxivCat
from alphaxiv_cat.types.folders import (
    V3ListResponse,
    V3CreateResponse,
    V3AddPapersResponse,
    V3MovePapersResponse,
    V3ToggleSharingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV3:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.create(
            folder_name="x",
        )
        assert_matches_type(V3CreateResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: AlphaxivCat) -> None:
        response = client.folders.v3.with_raw_response.create(
            folder_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3CreateResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: AlphaxivCat) -> None:
        with client.folders.v3.with_streaming_response.create(
            folder_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3CreateResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.list()
        assert_matches_type(V3ListResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: AlphaxivCat) -> None:
        response = client.folders.v3.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3ListResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: AlphaxivCat) -> None:
        with client.folders.v3.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3ListResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AlphaxivCat) -> None:
        response = client.folders.v3.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AlphaxivCat) -> None:
        with client.folders.v3.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.v3.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_papers(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.add_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3AddPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_papers_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.add_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            universal_ids=["string"],
        )
        assert_matches_type(V3AddPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_papers(self, client: AlphaxivCat) -> None:
        response = client.folders.v3.with_raw_response.add_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3AddPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_papers(self, client: AlphaxivCat) -> None:
        with client.folders.v3.with_streaming_response.add_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3AddPapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_papers(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.v3.with_raw_response.add_papers(
                folder_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_move_papers(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.move_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V3MovePapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_move_papers_with_all_params(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.move_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            from_folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3MovePapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_move_papers(self, client: AlphaxivCat) -> None:
        response = client.folders.v3.with_raw_response.move_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3MovePapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_move_papers(self, client: AlphaxivCat) -> None:
        with client.folders.v3.with_streaming_response.move_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3MovePapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_move_papers(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.v3.with_raw_response.move_papers(
                folder_id="",
                paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_papers(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.remove_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_papers(self, client: AlphaxivCat) -> None:
        response = client.folders.v3.with_raw_response.remove_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_papers(self, client: AlphaxivCat) -> None:
        with client.folders.v3.with_streaming_response.remove_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_papers(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.v3.with_raw_response.remove_papers(
                folder_id="",
                paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle_sharing(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.toggle_sharing(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sharing_status="not_shared",
        )
        assert_matches_type(V3ToggleSharingResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_toggle_sharing(self, client: AlphaxivCat) -> None:
        response = client.folders.v3.with_raw_response.toggle_sharing(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sharing_status="not_shared",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3ToggleSharingResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_toggle_sharing(self, client: AlphaxivCat) -> None:
        with client.folders.v3.with_streaming_response.toggle_sharing(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sharing_status="not_shared",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3ToggleSharingResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_toggle_sharing(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.v3.with_raw_response.toggle_sharing(
                folder_id="",
                sharing_status="not_shared",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_name(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.update_name(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_name(self, client: AlphaxivCat) -> None:
        response = client.folders.v3.with_raw_response.update_name(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_name(self, client: AlphaxivCat) -> None:
        with client.folders.v3.with_streaming_response.update_name(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_name(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.v3.with_raw_response.update_name(
                folder_id="",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_parent(self, client: AlphaxivCat) -> None:
        v3 = client.folders.v3.update_parent(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_parent(self, client: AlphaxivCat) -> None:
        response = client.folders.v3.with_raw_response.update_parent(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_parent(self, client: AlphaxivCat) -> None:
        with client.folders.v3.with_streaming_response.update_parent(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_parent(self, client: AlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.v3.with_raw_response.update_parent(
                folder_id="",
                parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncV3:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.create(
            folder_name="x",
        )
        assert_matches_type(V3CreateResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.folders.v3.with_raw_response.create(
            folder_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3CreateResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.folders.v3.with_streaming_response.create(
            folder_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3CreateResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.list()
        assert_matches_type(V3ListResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.folders.v3.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3ListResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.folders.v3.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3ListResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.folders.v3.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.folders.v3.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.v3.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_papers(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.add_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3AddPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_papers_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.add_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            universal_ids=["string"],
        )
        assert_matches_type(V3AddPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_papers(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.folders.v3.with_raw_response.add_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3AddPapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_papers(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.folders.v3.with_streaming_response.add_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3AddPapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_papers(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.v3.with_raw_response.add_papers(
                folder_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_move_papers(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.move_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V3MovePapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_move_papers_with_all_params(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.move_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            from_folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V3MovePapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_move_papers(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.folders.v3.with_raw_response.move_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3MovePapersResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_move_papers(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.folders.v3.with_streaming_response.move_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3MovePapersResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_move_papers(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.v3.with_raw_response.move_papers(
                folder_id="",
                paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_papers(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.remove_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_papers(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.folders.v3.with_raw_response.remove_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_papers(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.folders.v3.with_streaming_response.remove_papers(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_papers(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.v3.with_raw_response.remove_papers(
                folder_id="",
                paper_group_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle_sharing(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.toggle_sharing(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sharing_status="not_shared",
        )
        assert_matches_type(V3ToggleSharingResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_toggle_sharing(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.folders.v3.with_raw_response.toggle_sharing(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sharing_status="not_shared",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3ToggleSharingResponse, v3, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_toggle_sharing(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.folders.v3.with_streaming_response.toggle_sharing(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sharing_status="not_shared",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3ToggleSharingResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_toggle_sharing(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.v3.with_raw_response.toggle_sharing(
                folder_id="",
                sharing_status="not_shared",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_name(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.update_name(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_name(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.folders.v3.with_raw_response.update_name(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_name(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.folders.v3.with_streaming_response.update_name(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_name(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.v3.with_raw_response.update_name(
                folder_id="",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_parent(self, async_client: AsyncAlphaxivCat) -> None:
        v3 = await async_client.folders.v3.update_parent(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_parent(self, async_client: AsyncAlphaxivCat) -> None:
        response = await async_client.folders.v3.with_raw_response.update_parent(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert v3 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_parent(self, async_client: AsyncAlphaxivCat) -> None:
        async with async_client.folders.v3.with_streaming_response.update_parent(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert v3 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_parent(self, async_client: AsyncAlphaxivCat) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.v3.with_raw_response.update_parent(
                folder_id="",
                parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
