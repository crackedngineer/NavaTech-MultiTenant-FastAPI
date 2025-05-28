from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from ...database import get_org_db_session
from .service import create_organisation_service, get_organization_service

from .schema import CreateOrganisationRequestSchema, OrganisationResponseSchema

routes = APIRouter(
    tags=["organisation"],
    prefix="/organisation",
)


@routes.post(
    "/", response_model=OrganisationResponseSchema, status_code=status.HTTP_201_CREATED
)
def create_organisation(organisation: CreateOrganisationRequestSchema):
    """Create a new organisation"""
    try:
        return create_organisation_service(
            name=organisation.name,
            host=organisation.host,
            email=organisation.email,
            password=organisation.password,
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@routes.get(
    "/{name}", response_model=OrganisationResponseSchema, status_code=status.HTTP_200_OK
)
def get_organization(db: Session = Depends(get_org_db_session), name: str = ""):
    try:
        return get_organization_service(name=name)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
