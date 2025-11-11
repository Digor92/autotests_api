from http import HTTPStatus
import pytest

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import loginRequestSchema, loginResponseSchema
from clients.users.public_users_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    # инициализируется публичный клиент
    public_users_client = get_public_user_client()
    # инициализируется аутентификация
    authentication_client = get_authentication_client()

    # запрос создание пользователя
    create_user_request = CreateUserRequestSchema()
    public_users_client.create_user_api(create_user_request)

    # запрос аутентификации пользователя
    login_request = loginRequestSchema(
        email = create_user_request.email,
        password = create_user_request.password
    )

    login_response = authentication_client.login_api(login_request)
    login_response_data = loginResponseSchema.model_validate_json(login_response.text)
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
    # Данная строчка кода выполняет валидацию JSON-данных против JSON Schema, полученной из Pydantic модели.
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())


