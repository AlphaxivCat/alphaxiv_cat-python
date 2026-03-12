# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3RequestImplementationParams"]


class V3RequestImplementationParams(TypedDict, total=False):
    paper_title: Required[Annotated[str, PropertyInfo(alias="paperTitle")]]

    universal_paper_id: Required[Annotated[str, PropertyInfo(alias="universalPaperId")]]

    additional_info: Annotated[str, PropertyInfo(alias="additionalInfo")]
