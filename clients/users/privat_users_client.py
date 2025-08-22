from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

from clients.privat_http_builder import get_privat_http_client, AuthenticationUserDict


class UpdateUserRequest(TypedDict):
    """
       Описание структуры запроса на обновление пользователя.
       """
    email: str|None
    lastName: str|None
    firstName: str|None
    middleName: str|None

class User(TypedDict):
    """
       Описание структуры пользователя.
       """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class GetUserResponseDict(TypedDict):
    user: User
class PrivatUserClient(APIClient):
    """
        Клиент для работы с /api/v1/users
        """
    def get_user_me_api(self)-> Response:
        """
                Метод получения текущего пользователя.

                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.get('api/v1/users/me')

    def get_user_api(self, id: str)-> Response:
        """
                Метод получения пользователя по идентификатору.

                :param user_id: Идентификатор пользователя.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.get(f'api/v1/users/{id}')

    def update_user_api(self, id: str, request: UpdateUserRequest):
        """
                Метод обновления пользователя по идентификатору.

                :param user_id: Идентификатор пользователя.
                :param request: Словарь с email, lastName, firstName, middleName.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.patch(f'api/v1/users/{id}', json = request)
    def delete_user_api(self, id: str)-> Response:
        """
               Метод удаления пользователя по идентификатору.

               :param user_id: Идентификатор пользователя.
               :return: Ответ от сервера в виде объекта httpx.Response
               """
        return self.delete(f'api/v1/users/{id}')

    # Добавили новый метод для получения json
    def get_user(self, id: str) -> GetUserResponseDict:
        response = self.get_user_api(id)
        return response.json()


def get_privat_users_client(user: AuthenticationUserDict) -> PrivatUserClient:
    return PrivatUserClient(client = get_privat_http_client(user))

#client = get_privat_users_client({"email":"dedkov@mail.ru", "password":"12345"})
#client.get_user_api("1")