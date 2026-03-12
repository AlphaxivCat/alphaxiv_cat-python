# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PaperFastSearchParams"]


class PaperFastSearchParams(TypedDict, total=False):
    include_private: Required[Annotated[Literal["true", "false"], PropertyInfo(alias="includePrivate")]]

    q: Required[str]
