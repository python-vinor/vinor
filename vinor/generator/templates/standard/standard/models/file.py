import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from .db import DBModel


def uniqid():
    return uuid.uuid3(
        uuid.uuid1(),
        uuid.uuid4().hex
    ).hex


class File(DBModel):
    __tablename__ = "files"

    id = Column(String(190), primary_key=True, index=True, default=uniqid)
    mimetype = Column(String(190), default=None)
    path = Column(String(190), default=None)
    name = Column(String(190), default=None)
    extension = Column(String(190), default=None)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
