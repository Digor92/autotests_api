from pydantic import BaseModel, Field
from tools.fakers import fake

class TokenSchema(BaseModel):
    token_type: str = Field(alias = "tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class loginResponseSchema(BaseModel):
    token: TokenSchema

class loginRequestSchema(BaseModel):
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

class refreshRequestSchema(BaseModel):
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)

#print(loginRequestSchema())
#print(loginRequestSchema(email="dedkov@mail.ru", password="qwertY123"))


