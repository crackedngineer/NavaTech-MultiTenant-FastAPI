from pydantic import BaseModel

class TokenSchema(BaseModel):
    access_token: str

class LoginRequestSchema(BaseModel):
    email: str
    password: str