import pytest

@pytest.mark.xfail(reason = "найден баг в приложении из-за которого тест падает")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason = "баг исправлен, но все еще висит маркировка xfail")
def test_without_bug():
    pass

@pytest.mark.xfail(reason='Внешний сервис временно недоступен')
def test_external_services_is_unavailable():
    assert 1 == 2