# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["V3ProcessNotificationEmailResponse"]


class V3ProcessNotificationEmailResponse(BaseModel):
    message: str

    success: bool
