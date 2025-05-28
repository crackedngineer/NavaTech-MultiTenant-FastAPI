from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all models in the application."""

    __abstract__ = True
    metadata = MetaData(
        schema="org_default"
    )  # schema is set to org_default by default rather than public


def get_org_specific_metadata():
    meta = MetaData(schema="org_default")
    for table in Base.metadata.tables.values():
        # Select tables that do not have schema "shared" aka holds data shared among all orgs
        if table.schema != "shared":
            table.tometadata(meta)
    return meta


def get_shared_metadata():
    meta = MetaData()
    for table in Base.metadata.tables.values():
        if table.schema != "org_default":
            table.tometadata(meta)
    return meta
