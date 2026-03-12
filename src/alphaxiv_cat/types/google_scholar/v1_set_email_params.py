# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1SetEmailParams"]


class V1SetEmailParams(TypedDict, total=False):
    local_part: Required[Annotated[str, PropertyInfo(alias="localPart")]]
    """Institutional email local-part"""

    verify_account_email: Required[Annotated[bool, PropertyInfo(alias="verifyAccountEmail")]]
    """
    Send verification code to the user's primary email instead of the institutional
    email. Admin only.
    """
