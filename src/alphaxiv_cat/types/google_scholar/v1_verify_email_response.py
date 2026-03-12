# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1VerifyEmailResponse"]


class V1VerifyEmailResponse(BaseModel):
    google_scholar_id: str = FieldInfo(alias="googleScholarId")
