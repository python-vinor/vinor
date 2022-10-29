from typing import Optional

from pydantic import BaseModel


class SubscriptionBase(BaseModel):
    name: str
    email: str
    type: str
    schedule: str
    is_active: bool
    created_at: Optional[str]
    updated_at: Optional[str]


class SubscriptionCreate(SubscriptionBase):
    name: str
    email: str
    type: str
    schedule: str = None
    is_active: bool = True


class SubscriptionUpdate(SubscriptionBase):
    name: Optional[str]
    email: Optional[str]
    type: Optional[str]
    schedule: Optional[str]
    is_active: Optional[bool]


class SubscriptionResponse(SubscriptionBase):
    id: int

    class Config:
        orm_mode = True
