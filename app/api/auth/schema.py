from pydantic import BaseModel, EmailStr, field_validator
from app.utils import validate_password

class TokenSchema(BaseModel):
    access_token: str

class LoginRequestSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password_strength(cls, v: str) -> str:
        return validate_password(v)