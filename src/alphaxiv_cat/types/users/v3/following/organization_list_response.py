# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["OrganizationListResponse", "Organization"]


class Organization(BaseModel):
    id: str

    name: str


class OrganizationListResponse(BaseModel):
    organizations: List[Organization]
