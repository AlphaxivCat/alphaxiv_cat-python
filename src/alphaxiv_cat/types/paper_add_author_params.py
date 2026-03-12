# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaperAddAuthorParams"]


class PaperAddAuthorParams(TypedDict, total=False):
    author_email: Required[Annotated[str, PropertyInfo(alias="authorEmail")]]

    should_email: Annotated[bool, PropertyInfo(alias="shouldEmail")]
