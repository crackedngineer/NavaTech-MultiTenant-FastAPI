from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from .base import Base


class User(Base):
    __tablename__ = "users"  # This table will be created in each schema
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=True)

    __table_args__ = ({"schema": "org_default"},)
