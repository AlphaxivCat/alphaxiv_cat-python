# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ImplementationCreateParams"]


class ImplementationCreateParams(TypedDict, total=False):
    implementation_type: Required[
        Annotated[Literal["alphaxiv", "marimo", "author"], PropertyInfo(alias="implementationType")]
    ]

    url: Required[str]
