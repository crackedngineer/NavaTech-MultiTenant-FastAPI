from sqlalchemy.orm import Session
from ...models.organisation import Organisation


def get_organisation_by_schema(db: Session, schema: str):
    return db.query(Organisation).filter(Organisation.schema == schema).first()

