# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EmailUpdateParams"]


class EmailUpdateParams(TypedDict, total=False):
    direct_notifications: Annotated[bool, PropertyInfo(alias="directNotifications")]

    relevant_activity: Annotated[bool, PropertyInfo(alias="relevantActivity")]
