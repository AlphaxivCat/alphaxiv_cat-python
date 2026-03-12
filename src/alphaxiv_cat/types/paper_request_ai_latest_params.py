# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaperRequestAILatestParams"]


class PaperRequestAILatestParams(TypedDict, total=False):
    preferred_language: Annotated[
        Literal[
            "am",
            "ar",
            "az",
            "bg",
            "bn",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "et",
            "fa",
            "fi",
            "fr",
            "gu",
            "ha",
            "he",
            "hi",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ka",
            "kn",
            "ko",
            "lt",
            "lv",
            "ml",
            "mr",
            "ms",
            "my",
            "ne",
            "nl",
            "no",
            "pa",
            "pl",
            "pt",
            "ro",
            "ru",
            "si",
            "sk",
            "sl",
            "sr",
            "sv",
            "sw",
            "ta",
            "te",
            "th",
            "tl",
            "tr",
            "uk",
            "ur",
            "uz",
            "vi",
            "yo",
            "zh",
        ],
        PropertyInfo(alias="preferredLanguage"),
    ]
