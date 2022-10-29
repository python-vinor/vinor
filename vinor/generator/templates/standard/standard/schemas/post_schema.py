from typing import Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    slug: str
    image: str
    content: str
    is_active: bool
    created_at: Optional[str]
    updated_at: Optional[str]


class PostCreate(PostBase):
    category_id: int


class PostUpdate(PostBase):
    title: Optional[str]
    slug: Optional[str]
    image: Optional[str]
    content: Optional[str]
    category_id: Optional[int]
    is_active: Optional[bool]


class PostResponse(PostBase):
    id: int
    category_id: int

    class Config:
        orm_mode = True
