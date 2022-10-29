from typing import List, Optional
from pydantic import BaseModel
from standard.schemas.post_schema import PostResponse


class CategoryBase(BaseModel):
    title: str
    slug: str
    icon: str
    image: str
    description: str
    is_active: bool
    created_at: Optional[str]
    updated_at: Optional[str]


class CategoryCreate(CategoryBase):
    title: str
    slug: Optional[str]
    icon: Optional[str]
    image: Optional[str]
    description: str
    is_active: bool


class CategoryUpdate(CategoryBase):
    title: Optional[str]
    slug: Optional[str]
    icon: Optional[str]
    image: Optional[str]
    description: Optional[str]
    is_active: Optional[bool] = None


class CategoryResponse(CategoryBase):
    id: int
    models: List[PostResponse] = []

    class Config:
        orm_mode = True
