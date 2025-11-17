from http import HTTPStatus
import pytest

from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.authentication.authentication_schema import loginRequestSchema, loginResponseSchema
from clients.users.public_users_client import get_public_user_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema
from tests.conftest import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user: UserFixture, authentication_client: AuthenticationClient):
    # инициализируется публичный клиент с помощью фикстур в файле conftest
    # инициализируется аутентификация клиента с помощью фикстур в файле conftest
    # запрос создание пользователя через фикстуры

    # запрос аутентификации пользователя
    request = loginRequestSchema(email = function_user.email,password = function_user.password)
    response = authentication_client.login_api(request)
    response_data = loginResponseSchema.model_validate_json(response.text)
    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)
    # Данная (последняя) строчка кода выполняет валидацию JSON-данных против JSON Schema, полученной из Pydantic модели.



