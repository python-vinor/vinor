from typing import Optional
from pydantic import BaseModel


class FileBase(BaseModel):
    name: str
    mimetype: str
    path: Optional[str]
    extension: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]


class FileCreate(FileBase):
    pass


class FileResponse(FileBase):
    id: str
    url: Optional[str] = None

    class Config:
        orm_mode = True
