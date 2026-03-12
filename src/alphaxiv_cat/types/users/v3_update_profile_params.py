# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3UpdateProfileParams"]


class V3UpdateProfileParams(TypedDict, total=False):
    biography: Optional[str]

    bluesky_username: Annotated[Optional[str], PropertyInfo(alias="blueskyUsername")]

    github_username: Annotated[Optional[str], PropertyInfo(alias="githubUsername")]

    institution: Optional[str]

    linkedin_username: Annotated[Optional[str], PropertyInfo(alias="linkedinUsername")]

    location: Optional[str]

    public_email: Annotated[Optional[str], PropertyInfo(alias="publicEmail")]

    real_name: Annotated[str, PropertyInfo(alias="realName")]

    username: str

    x_username: Annotated[Optional[str], PropertyInfo(alias="xUsername")]
