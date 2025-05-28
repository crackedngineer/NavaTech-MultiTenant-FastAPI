from app.settings import logger
from sqlalchemy.orm import Session
from alembic.config import Config
from alembic.runtime.migration import MigrationContext
from alembic.script import ScriptDirectory
from app.utils import get_password_hash
from ...database.connection import with_org_db, with_default_db
from .controller import (
    get_organization_by_name,
    create_organisation_in_master,
    create_admin_user,
)
from .error import (
    OrganizationAlreadyExistsError,
    AdminUserCreationError,
    MigrationPendingError,
    OrganizationNotFoundError,
)


def create_organisation_service(name: str, host: str, email: str, password: str):
    schema = name.lower().replace(" ", "_").replace("-", "_")

    with with_org_db(schema) as db:
        existing_org = get_organization_by_name(db, name=name)
        if existing_org:
            raise OrganizationAlreadyExistsError(name)

        alembic_config = Config("alembic.ini")
        context = MigrationContext.configure(db.connection())
        script = ScriptDirectory.from_config(alembic_config)
        if context.get_current_revision() != script.get_current_head():
            raise MigrationPendingError()

        hashed_password = get_password_hash(password)

        org = create_organisation_in_master(
            db, name=name, schema=schema, host=host, admin_email=email
        )

        try:
            create_admin_user(db, email, hashed_password)
        except Exception as e:
            logger.error(f"Error inserting admin user into schema {schema}: {e}")
            raise AdminUserCreationError(schema, e)

        return {
            "name": org.name,
            "host": org.host,
            "schema": org.schema,
            "admin_email": org.admin_email,
        }


def get_organization_service(name: str):
    with with_default_db() as db:
        org = get_organization_by_name(db, name=name)
        if not org:
            raise OrganizationNotFoundError(name)
        return org
