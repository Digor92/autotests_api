from clients.users.public_users_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus

from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user


def test_create_user():
    # инициализируется публичный клиент
    public_user_client = get_public_user_client()
    # инициализируется запрос
    request = CreateUserRequestSchema()
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


    #assert response.status_code == HTTPStatus.OK, 'некорректный статус-код ответа'
    # вместо проверки выше сделаем масштабирование:
    assert_status_code(response.status_code, HTTPStatus.OK )

    # далее заменим 4-е проверки ниже на новую строку через созданный метод
    '''
    assert response_data.user.email == request.email, 'некорректный email пользователя'
    assert response_data.user.last_name == request.last_name, 'некорректный last_name пользователя'
    assert response_data.user.first_name == request.first_name, 'некорректный first_name пользователя'
    assert response_data.user.middle_name == request.middle_name, 'некорректный middle_name пользователя'
    '''


    assert_create_user(request, response_data)

    # validate_json_schema проверяет, соответствует ли синтаксис входной строки формату JSON
    # model_json_schema - возвращает из модели json файл
    validate_json_schema(response.json(), response_data.model_json_schema())


