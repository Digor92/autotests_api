from clients.api_client import APIClient
from httpx import Response
from clients.public_httpx_builder import get_public_http_client
from clients.authentication.authentication_schema import loginResponseSchema, loginRequestSchema, TokenSchema, refreshRequestSchema

class AuthenticationClient(APIClient):

    def login_api(self, request: loginRequestSchema) -> Response:
        """
                Метод выполняет аутентификацию пользователя.

                :param request: Словарь с email и password.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.post('api/v1/authentication/login', json = request.model_dump(by_alias=True))

    def refresh_api(self, request: refreshRequestSchema) -> Response:
        """
                Метод обновляет токен авторизации.

                :param request: Словарь с refreshToken.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.post('api/v1/authentication/refresh', json  = request.model_dump(by_alias=True))


    # Добавили метод login для получения json
    def login(self, request: loginRequestSchema) -> loginResponseSchema:
        response = self.login_api(request)
        # потенциально этот ретурн хуже
        #return loginResponseSchema(**response.json())

        # этот return лучше
        return loginResponseSchema.model_validate_json(response.text)



# Добавляем builder для AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
        Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

        :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
