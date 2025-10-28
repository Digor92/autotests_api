from typing import Any
def assert_status_code(actual: int, expected: int):
    assert actual == expected, (
        'incorrect response status code',
        f'expected status code{expected}',
        f'actual status code{actual}'
    )

def assert_equal(actual: Any,expected: Any, name: str):
    assert actual == expected, (
        f'incorrect value: {name}',
        f'expected value: {expected}',
        f'actual value: {actual}'
    )