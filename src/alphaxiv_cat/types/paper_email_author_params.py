# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaperEmailAuthorParams"]


class PaperEmailAuthorParams(TypedDict, total=False):
    author_individual_email: Required[Annotated[str, PropertyInfo(alias="authorIndividualEmail")]]

    email_author_name: Required[Annotated[str, PropertyInfo(alias="emailAuthorName")]]

    paper_name: Required[Annotated[str, PropertyInfo(alias="paperName")]]

    type: Required[Literal["comment", "trending"]]

    ignore_duplicate_error: Annotated[bool, PropertyInfo(alias="ignoreDuplicateError")]
