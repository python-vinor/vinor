from typing import Optional
from pydantic import BaseModel


class SettingBase(BaseModel):
    name: str
    key: str
    value: str
    created_at: Optional[str]
    updated_at: Optional[str]


class SettingCreate(SettingBase):
    name: str
    key: Optional[str]
    value: Optional[str]


class SettingUpdate(SettingBase):
    name: Optional[str]
    key: Optional[str]
    value: Optional[str]


class SettingResponse(SettingBase):
    id: int

    class Config:
        orm_mode = True
