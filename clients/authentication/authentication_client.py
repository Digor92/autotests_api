from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class loginRequestDict(TypedDict):
    email: str
    password: str

class refreshRequestDict(TypedDict):
    refreshToken: str

class AuthenticationClient(APIClient):

    def login_api(self, request: loginRequestDict) -> Response:
        """
                Метод выполняет аутентификацию пользователя.

                :param request: Словарь с email и password.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.post('api/v1/authentication/login', json = request)

    def refresh_api(self, request: refreshRequestDict) -> Response:
        """
                Метод обновляет токен авторизации.

                :param request: Словарь с refreshToken.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.post('api/v1/authentication/refresh', json  = request)

