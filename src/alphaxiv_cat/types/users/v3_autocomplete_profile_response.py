# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["V3AutocompleteProfileResponse"]


class V3AutocompleteProfileResponse(BaseModel):
    bio: str

    institution: str

    message: str
