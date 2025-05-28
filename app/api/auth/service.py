from datetime import timedelta
from ...database.connection import with_org_db
from ...models.user import User
from .controller import get_organisation_by_schema
from app.utils import verify_password, create_access_token
from .error import AuthenticationError


def login_service(schema: str, email: str, password: str):
    with with_org_db(schema) as db:
        user = db.execute(User.__table__.select().where(User.email == email)).first()

        if not user or not verify_password(password, user.hashed_password):
            raise AuthenticationError()

        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=timedelta(minutes=30)
        )
        return {"access_token": access_token}
