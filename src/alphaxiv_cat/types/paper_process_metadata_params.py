# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaperProcessMetadataParams", "Metadata"]


class PaperProcessMetadataParams(TypedDict, total=False):
    metadata: Required[Metadata]

    universal_paper_id: Required[Annotated[str, PropertyInfo(alias="universalPaperId")]]


class Metadata(TypedDict, total=False):
    bibtex: bool

    custom_categories: bool

    embedding: bool

    github: bool

    organizations: bool

    overview: bool

    thumbnail: bool
