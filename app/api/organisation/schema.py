from pydantic import BaseModel, EmailStr, field_validator
from app.utils import validate_password


class CreateOrganisationRequestSchema(BaseModel):
    name: str
    host: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password_strength(cls, v: str) -> str:
        return validate_password(v)


class OrganisationResponseSchema(BaseModel):
    name: str
    host: str
    schema: str
    admin_email: str
