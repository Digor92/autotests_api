import allure
from httpx import Response
from clients.api_client import APIClient
from clients.privat_http_builder import get_privat_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema
from tools.routes import APIRoutes


class PrivatUserClient(APIClient):
    """
        Клиент для работы с /api/v1/users
        """

    @allure.step("Get user me")
    def get_user_me_api(self)-> Response:
        """
                Метод получения текущего пользователя.

                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.get(f'{APIRoutes.USERS}/me')

    @allure.step("Get user by id {user_id}")
    def get_user_api(self, id: str)-> Response:
        """
                Метод получения пользователя по идентификатору.

                :param user_id: Идентификатор пользователя.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.get(f'{APIRoutes.USERS}/{id}')

    @allure.step("Update user by id {user_id}")
    def update_user_api(self, id: str, request: UpdateUserRequestSchema):
        """
                Метод обновления пользователя по идентификатору.

                :param user_id: Идентификатор пользователя.
                :param request: Словарь с email, lastName, firstName, middleName.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.patch(f'{APIRoutes.USERS}/{id}', json = request.model_dump(by_alias=True))

    @allure.step("Delete user by id {user_id}")
    def delete_user_api(self, id: str)-> Response:
        """
               Метод удаления пользователя по идентификатору.

               :param user_id: Идентификатор пользователя.
               :return: Ответ от сервера в виде объекта httpx.Response
               """
        return self.delete(f'{APIRoutes.USERS}/{id}')

    # Добавили новый метод для получения json
    def get_user(self, id: str) -> GetUserResponseSchema:
        response = self.get_user_api(id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_privat_users_client(user: AuthenticationUserSchema) -> PrivatUserClient:
    """
        Функция создаёт экземпляр PrivatUserClient с уже настроенным HTTP-клиентом.

        :return: Готовый к использованию PrivatUserClient.
        """
    return PrivatUserClient(client = get_privat_http_client(user))

#client = get_privat_users_client({"email":"dedkov@mail.ru", "password":"12345"})
#client.get_user_api("1")