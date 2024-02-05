from pydantic import BaseModel
from enum import Enum
from typing import Optional


class FileType(str, Enum):
    EXTERNAL = "external"
    FILE = "file"


class FileExternal(BaseModel):
    url: str


class FileFile(BaseModel):
    url: str
    expiry_time: Optional[str] = None


class File(BaseModel):
    type: FileType
    external: Optional[FileExternal] = None
    file: Optional[FileFile] = None
