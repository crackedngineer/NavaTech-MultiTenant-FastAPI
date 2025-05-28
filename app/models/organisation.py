from enum import Enum
from sqlalchemy import Column, String, Integer, Enum as saEnum
from .base import Base


class Status(Enum):
    active = "active"
    inactive = "inactive"


class Organisation(Base):
    __tablename__ = "organisations"

    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", String(256), nullable=False, index=True)
    schema = Column("schema", String(256), nullable=False, unique=True)
    host = Column("host", String(256), nullable=False, unique=True)
    admin_email = Column("email", String(256), nullable=False)
    status = Column("status", saEnum(Status, inherit_schema=True), nullable=False)

    __table_args__ = ({"schema": "shared"},)

# class MasterAdmin(Base):
#     __tablename__ = "master_admins"
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)