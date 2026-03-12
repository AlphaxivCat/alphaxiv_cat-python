# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V3RetrieveGeoTrendsResponse",
    "FrequentCollaboration",
    "TopCountriesByPaperCount",
    "TopCountriesByStar",
    "TopGitHubRepo",
]


class FrequentCollaboration(BaseModel):
    collaboration_count: float = FieldInfo(alias="collaborationCount")

    countries: List[str]


class TopCountriesByPaperCount(BaseModel):
    count: float

    country: str


class TopCountriesByStar(BaseModel):
    country: str

    total_stars: float = FieldInfo(alias="totalStars")


class TopGitHubRepo(BaseModel):
    countries: List[str]

    description: Optional[str] = None

    first_publication_date: str = FieldInfo(alias="firstPublicationDate")

    language: Optional[str] = None

    paper_group_id: str = FieldInfo(alias="paperGroupId")

    stars: float

    stars_daily: float = FieldInfo(alias="starsDaily")

    title: str

    universal_id: str = FieldInfo(alias="universalId")

    url: str


class V3RetrieveGeoTrendsResponse(BaseModel):
    frequent_collaborations: List[FrequentCollaboration] = FieldInfo(alias="frequentCollaborations")

    paper_count_graph: Dict[str, List[float]] = FieldInfo(alias="paperCountGraph")

    paper_stars_graph: Dict[str, List[float]] = FieldInfo(alias="paperStarsGraph")

    top_countries_by_paper_count: List[TopCountriesByPaperCount] = FieldInfo(alias="topCountriesByPaperCount")

    top_countries_by_stars: List[TopCountriesByStar] = FieldInfo(alias="topCountriesByStars")

    top_github_repos: List[TopGitHubRepo] = FieldInfo(alias="topGitHubRepos")

    total_papers_count: float = FieldInfo(alias="totalPapersCount")
