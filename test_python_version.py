import pytest

system_version = "v1.2.0.3"

@pytest.mark.skipif(system_version == "v1.2.0.3",
                    reason = "Тест не может быть запущен на версии системы v1.2.0.3")
def test_system_version_valid():
    pass

@pytest.mark.skipif(system_version == "v1.2.0.4",
                    reason = "Тест не может быть запущен на версии системы v1.2.0.4")
def test_system_version_invalid():
    pass