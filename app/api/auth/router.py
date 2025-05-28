from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.orm import Session

from .schema import TokenSchema, LoginRequestSchema
from .service import login_service
from ...database import get_org_db_session

routes = APIRouter(tags=["authentication"], prefix="/organisation/{schema}/auth")


@routes.post("/login", response_model=TokenSchema)
def login(
    admin_in: LoginRequestSchema,
    schema: str,
    db: Session = Depends(get_org_db_session),
):
    try:
        return login_service(schema, admin_in.email, admin_in.password)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
