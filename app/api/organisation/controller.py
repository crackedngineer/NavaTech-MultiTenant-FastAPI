from app.settings import logger
from sqlalchemy.orm import Session
from sqlalchemy.schema import CreateSchema
from app.models.organisation import Organisation, Status
from app.models.user import User
from app.models.base import get_org_specific_metadata


def create_organisation_in_master(
    db: Session, name: str, schema: str, host: str, admin_email: str
):
    db_org = Organisation(
        name=name,
        schema=schema,
        host=host,
        admin_email=admin_email,
        status=Status.active,
    )
    db.add(db_org)
    db.execute(CreateSchema(schema))
    get_org_specific_metadata().create_all(bind=db.connection())
    db.commit()
    db.refresh(db_org)
    return db_org


def get_organization_by_name(db: Session, name: str):
    return db.query(Organisation).filter(Organisation.name == name).first()


def create_admin_user(db: Session, email: str, password: str):
    new_admin_user = User(email=email, hashed_password=password, is_admin=True)
    db.add(new_admin_user)
    db.commit()
    db.refresh(new_admin_user)
    logger.info("Admin User Created Successfully !")
