# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SharedCopyResponse"]


class SharedCopyResponse(BaseModel):
    copied_count: float = FieldInfo(alias="copiedCount")

    copied_folders: float = FieldInfo(alias="copiedFolders")

    folder_id: str = FieldInfo(alias="folderId")
