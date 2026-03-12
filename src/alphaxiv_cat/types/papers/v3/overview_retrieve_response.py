# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "OverviewRetrieveResponse",
    "Citation",
    "Summary",
    "AITooltips",
    "OverviewSectionTitles",
    "SummarySectionTitles",
]


class Citation(BaseModel):
    alphaxiv_link: Optional[str] = FieldInfo(alias="alphaxivLink", default=None)

    full_citation: str = FieldInfo(alias="fullCitation")

    justification: str

    title: str


class Summary(BaseModel):
    key_insights: List[str] = FieldInfo(alias="keyInsights")

    original_problem: List[str] = FieldInfo(alias="originalProblem")

    results: List[str]

    solution: List[str]

    summary: str


class AITooltips(BaseModel):
    ai_generated_content: str = FieldInfo(alias="aiGeneratedContent")


class OverviewSectionTitles(BaseModel):
    relevant_citations: str = FieldInfo(alias="relevantCitations")

    table_of_contents: str = FieldInfo(alias="tableOfContents")


class SummarySectionTitles(BaseModel):
    abstract: str

    method: str

    problem: str

    results: str

    summary: str

    takeaways: str


class OverviewRetrieveResponse(BaseModel):
    abstract: str

    citations: List[Citation]

    intermediate_report: Optional[str] = FieldInfo(alias="intermediateReport", default=None)

    overview: str

    summary: Summary

    title: str

    ai_tooltips: Optional[AITooltips] = FieldInfo(alias="aiTooltips", default=None)

    overview_section_titles: Optional[OverviewSectionTitles] = FieldInfo(alias="overviewSectionTitles", default=None)

    summary_section_titles: Optional[SummarySectionTitles] = FieldInfo(alias="summarySectionTitles", default=None)
