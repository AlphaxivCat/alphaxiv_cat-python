# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3KickoffXMentionsSyncParams"]


class V3KickoffXMentionsSyncParams(TypedDict, total=False):
    dry_run: Annotated[bool, PropertyInfo(alias="dryRun")]
    """If true, only logs papers without queuing"""

    limit: int
    """Number of hot papers to sync (default: 500)"""
