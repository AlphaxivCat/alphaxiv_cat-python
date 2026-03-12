# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ResearchCreateProjectParams", "Folder"]


class ResearchCreateProjectParams(TypedDict, total=False):
    name: Required[str]

    folder: Optional[Folder]
    """Prefill the project with a set of research papers."""

    initial_papers: Annotated[SequenceNotStr[str], PropertyInfo(alias="initialPapers")]
    """Add these papers to the group on init"""

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]


class Folder(TypedDict, total=False):
    """Prefill the project with a set of research papers."""

    id: Required[str]

    delete: Required[bool]
    """If set true, the folder is deleted after copying it"""
