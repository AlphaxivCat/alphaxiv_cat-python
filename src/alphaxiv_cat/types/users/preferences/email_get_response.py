# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EmailGetResponse", "Data"]


class Data(BaseModel):
    bounced: bool

    direct_notifications: bool = FieldInfo(alias="directNotifications")

    relevant_activity: bool = FieldInfo(alias="relevantActivity")


class EmailGetResponse(BaseModel):
    data: Data
