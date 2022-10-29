from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .db import DBModel


class Category(DBModel):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(190), unique=True, index=True)
    slug = Column(String(190), unique=True, index=True)
    icon = Column(String(190), default=None)
    image = Column(String(190), default=None)
    description = Column(String(190), default=None)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    posts = relationship("Post", back_populates="category")
