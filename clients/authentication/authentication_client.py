from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.public_httpx_builder import get_public_http_client

class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str

class loginResponseDict(TypedDict):
    token: Token

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


    # Добавили метод login
    def login(self, request: loginRequestDict) -> loginResponseDict:
        response = self.login_api(request)
        return response.json()





# Добавляем builder для AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
        Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

        :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
