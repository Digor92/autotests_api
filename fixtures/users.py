import pytest
from pydantic import BaseModel, EmailStr
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.privat_http_builder import AuthenticationUserSchema
from clients.users.privat_users_client import PrivatUserClient, get_privat_users_client
from clients.users.public_users_client import PublicUsersClient, get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email = self.email, password = self.password)

@pytest.fixture
def public_user_client() -> PublicUsersClient:
    return get_public_user_client()

@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivatUserClient:
    return get_privat_users_client(function_user.authentication_user)
@pytest.fixture
def function_user(public_user_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)

    return UserFixture(request = request, response = response)

