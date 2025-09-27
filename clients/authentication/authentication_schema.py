from pydantic import BaseModel, Field

class TokenSchema(BaseModel):
    token_type: str = Field(alias = "tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class loginResponseSchema(BaseModel):
    token: TokenSchema

class loginRequestSchema(BaseModel):
    email: str
    password: str

class refreshRequestSchema(BaseModel):
    refresh_token: str = Field(alias="refreshToken")

