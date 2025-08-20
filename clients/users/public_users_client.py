#from httpx import Response
import httpx
from typing import TypedDict
from clients.api_client import APIClient

class NewUsersDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
            Метод создает пользователя.

            :param request: Словарь с email, password, lastName, firstName, middleName.
            :return: Ответ от сервера в виде объекта httpx.Response
            """
    def create_user_api(self, request: NewUsersDict)->httpx.Response:
        return self.post('/api/v1/users', json = request)

