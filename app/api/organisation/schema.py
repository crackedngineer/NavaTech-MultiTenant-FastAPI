from pydantic import BaseModel


class CreateOrganisationRequestSchema(BaseModel):
    name: str
    host: str
    email: str
    password: str

class OrganisationResponseSchema(BaseModel):
    name: str
    host: str
    admin_email: str