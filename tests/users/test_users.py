from clients.users.privat_users_client import PrivatUserClient
from clients.users.public_users_client import get_public_user_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
import pytest
from tools.fakers import fake



@pytest.mark.users
@pytest.mark.regression
class TestUsers:
    def test_get_user_me(self, function_user: UserFixture, private_users_client: PrivatUserClient):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "yandex.com"])
    def test_create_user(self, email: str, public_user_client: PublicUsersClient):
        # инициализируется публичный клиент с помощью фикстур в файле conftest
        # инициализируется запрос
        request = CreateUserRequestSchema(email=fake.email(domain=email))
        # request = CreateUserRequestSchema()
        print(request.email)
        # возвращается ответ
        response = public_user_client.create_user_api(request)
        # десеарилизуем текст в модель CreateUserResponseSchema
        '''
        Метод model_validate_json в библиотеке Pydantic для Python проверяет данные JSON на соответствие модели Pydantic. Это
        Проверять, соответствуют ли данные ожидаемым типам и ограничениям модели. Pydantic гарантирует, 
        что поля результирующего экземпляра модели будут соответствовать типам полей, определённым в модели
        '''
        # Инициализируем модель ответа на основе полученного JSON в ответе
        # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # assert response.status_code == HTTPStatus.OK, 'некорректный статус-код ответа'
        # вместо проверки выше сделаем масштабирование:
        assert_status_code(response.status_code, HTTPStatus.OK)

        # далее заменим 4-е проверки ниже на новую строку через созданный метод
        '''
        assert response_data.user.email == request.email, 'некорректный email пользователя'
        assert response_data.user.last_name == request.last_name, 'некорректный last_name пользователя'
        assert response_data.user.first_name == request.first_name, 'некорректный first_name пользователя'
        assert response_data.user.middle_name == request.middle_name, 'некорректный middle_name пользователя'
        '''

        assert_create_user_response(request, response_data)

        # validate_json_schema проверяет, соответствует ли синтаксис входной строки формату JSON
        # model_json_schema - возвращает из модели json файл
        validate_json_schema(response.json(), response_data.model_json_schema())


