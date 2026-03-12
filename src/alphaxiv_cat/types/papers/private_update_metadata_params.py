# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PrivateUpdateMetadataParams", "Author"]


class PrivateUpdateMetadataParams(TypedDict, total=False):
    abstract: Required[str]

    authors: Required[Iterable[Author]]

    bibtex: Required[Optional[str]]

    categories: Required[SequenceNotStr[str]]

    publication_date: Required[Annotated[float, PropertyInfo(alias="publicationDate")]]

    title: Required[str]


class Author(TypedDict, total=False):
    name: Required[str]
