from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .db import DBModel


class Post(DBModel):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(190), unique=True, index=True)
    slug = Column(String(190), unique=True, index=True)
    image = Column(String(190), default=None)
    content = Column(String(190), default=None)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True,)
    category = relationship("Category", back_populates="posts")
