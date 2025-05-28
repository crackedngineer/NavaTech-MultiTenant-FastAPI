from datetime import timedelta
from ...database.connection import with_org_db
from ...models.user import User
from .controller import get_organisation_by_schema
from app.utils import verify_password, create_access_token


def login_service(schema: str, email: str, password: str):
    with with_org_db(schema) as db:
        user = db.execute(User.__table__.select().where(User.email == email)).first()

        if not user or not verify_password(password, user.hashed_password):
            raise Exception("Incorrect email or password")

        access_token = create_access_token(
            data={"sub": user.email},
        )
        return {"access_token": access_token, "token_type": "bearer"}
