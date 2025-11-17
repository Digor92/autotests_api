import pytest


@pytest.fixture
def analitics_data(autouse = True):
    print('[AUTOUSE] отправляем данные в сервис аналитики')

@pytest.fixture(scope = 'session')
def settings():
    print('[SESSION] инициализируем настройки автотестов: хосты, порты, данные от БД')

@pytest.fixture(scope = 'class')
def user():
    print('[CLASS] создаем данные вользователя один раз на тестовый класс')


@pytest.fixture(scope = 'function')
def user_client(settings):
    print('[FUNCTION] создаем api-клиент на каждый автотест')
class TestUserFlow:
    def test_user_can_login(self, user, user_client, settings):
        ...

    def test_user_can_create_course(self, user, user_client, settings):
        ...

class TestAccountFlow:
    def test_user_account(self, user, user_client, settings):
        ...


@pytest.fixture
def user_data() -> dict:
    print("создаем пользователя до теста [setup]")
    yield {"username":"test_user", "email":"test@example.ru"}
    print("удаляем данные пользователя после теста [teardown]")


def test_user_email(user_data: dict):
    print(user_data)
    assert user_data["email"] == "test@example.ru"

def test_user_username(user_data: dict):
    print(user_data)
    assert user_data["username"] == "test_user"
