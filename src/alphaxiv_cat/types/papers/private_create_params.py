# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PrivateCreateParams"]


class PrivateCreateParams(TypedDict, total=False):
    content_type: Required[Annotated[str, PropertyInfo(alias="contentType")]]

    file: Required[str]

    filename: Required[str]
