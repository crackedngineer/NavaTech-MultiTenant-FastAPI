from contextlib import contextmanager
from typing import Optional

from fastapi import Depends, HTTPException, Request
from sqlalchemy import text
from sqlalchemy.orm import Session

from ..models.base import Base
from ..models.organisation import Organisation

from .engine import engine

__all__ = ["get_default_db_session", "get_org_db_session"]


def get_host_from_request(req: Request) -> str:
    return req.url.path.split("/")[3]


def get_default_db_session():
    return with_default_db()


def get_org_db_session(host=Depends(get_host_from_request)):
    # check if org exists in the "shared" schema
    with with_default_db() as db:
        org = db.query(Organisation).filter(Organisation.host == host).one_or_none()

        if org is None:
            raise HTTPException(status_code=404, detail="Organisation not found")

        return with_org_db(schema=org.schema)


@contextmanager
def with_default_db():
    """Get a database connection using the schemas defined in each model"""
    connectable = engine.execution_options()
    try:
        db = Session(autocommit=False, autoflush=False, bind=connectable)
        yield db
    finally:
        db.close()


@contextmanager
def with_org_db(schema: Optional[str]):
    """Get a database connection for the given org schema"""
    if schema:
        schema_translate_map = dict(
            org_default=schema
        )  # Maps org_default schema to the org DB schema
    else:
        schema_translate_map = None

    connectable = engine.execution_options(schema_translate_map=schema_translate_map)

    try:
        db = Session(autocommit=False, autoflush=False, bind=connectable)
        yield db
    finally:
        db.close()
