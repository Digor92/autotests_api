#from httpx import Response
import httpx
from typing import TypedDict
from clients.api_client import APIClient
from clients.public_httpx_builder import get_public_http_client


class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class User(TypedDict):
    """
           Описание структуры пользователя.
           """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
        Описание структуры запроса на создание пользователя.
        """
    user: User


class PublicUsersClient(APIClient):
    """
            Метод создает пользователя.

            :param request: Словарь с email, password, lastName, firstName, middleName.
            :return: Ответ от сервера в виде объекта httpx.Response
            """
    def create_user_api(self, request: CreateUserRequestDict)->httpx.Response:
        return self.post('/api/v1/users', json = request)

    # Добавили новый метод для получения json
    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()



def get_public_user_client() -> PublicUsersClient:
    """

    :rtype: object
    """
    return PublicUsersClient(client=get_public_http_client())