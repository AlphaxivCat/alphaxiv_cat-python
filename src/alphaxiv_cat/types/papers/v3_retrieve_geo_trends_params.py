# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V3RetrieveGeoTrendsParams"]


class V3RetrieveGeoTrendsParams(TypedDict, total=False):
    collaboration_limit: Annotated[str, PropertyInfo(alias="collaborationLimit")]

    paper_limit: Annotated[str, PropertyInfo(alias="paperLimit")]

    past_months: Annotated[str, PropertyInfo(alias="pastMonths")]

    repo_limit: Annotated[str, PropertyInfo(alias="repoLimit")]

    top_countries: Annotated[str, PropertyInfo(alias="topCountries")]
