# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaperGetCrxPaperInfoResponse"]


class PaperGetCrxPaperInfoResponse(BaseModel):
    has_claimed_authorship: bool = FieldInfo(alias="hasClaimedAuthorship")

    num_questions: float = FieldInfo(alias="numQuestions")

    return_version: float = FieldInfo(alias="returnVersion")
