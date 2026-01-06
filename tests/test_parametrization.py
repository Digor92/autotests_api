import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (4, 15), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])  # Параметризируем по операционной системе
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])  # Параметризируем по хосту
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0  # Проверка указана для примера

'''параметризация фикстур'''
@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest):
    return request.param

def test_host(host: str):
    print(f" running test on host: {host}")

# Для тестовых классов параметризация указывается для самого класса
@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    # Параметр "user" передается в качестве аргумента в каждый тестовый метод класса
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    # Аналогично тут передается "user"
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

@pytest.mark.parametrize("phone_number", ["+700001", "+700002", "=700003"],
                         ids = ["user with money on card",
                                "user without money on card",
                                "user with operation is limited"])
def test_identifiers(phone_number: str):
    pass

''' параметризируем последний  тест так чтобы сохранился и номер и логика пользователя по этому номеру'''

users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize(
    "phone_number",
    users.keys(), # Передаем список номеров телефонов
    ids = lambda phone_number: f"{phone_number}, {users[phone_number]}"
    #ids = users.values()
)
def test_identifiers2(phone_number: str):
    pass