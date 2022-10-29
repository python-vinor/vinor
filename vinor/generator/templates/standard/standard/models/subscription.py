from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func

from .db import DBModel


class Subscription(DBModel):
    """
        type: newletters, new course, discount, ..etc
        schedule: daily, weekly, or cronjob format: * * * * *
    """
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(190))
    email = Column(String(190), index=True)
    type = Column(String(190))
    schedule = Column(String(190), default=None)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
