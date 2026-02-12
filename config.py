import os
from typing import Self

from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestData(BaseModel):
    image_png_file: FilePath

# универсальный способ передачи переменной окружения для разных окрежений
#config_file = os.getenv("CONFIG_FILE", ".env.local")
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Указываем, из какого файла читать настройки
        # Указываем кодировку файла
        # Указываем разделитель для вложенных переменных
        env_file = ".env",
        env_file_encoding = "utf-8",
        env_nested_delimiter = "."
    )
    test_data: TestData
    http_client: HTTPClientConfig
    allure_results_dir: DirectoryPath  # Добавили новое поле

    # Добавили метод initialize
    @classmethod
    def initialize(cls) -> Self:  # Возвращает экземпляр класса Settings
        allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке
        allure_results_dir.mkdir(exist_ok=True)  # Создаем папку allure-results, если она не существует

        # Передаем allure_results_dir в инициализацию настроек
        return Settings(allure_results_dir=allure_results_dir)

#print(Settings())
#settings = Settings()
# Теперь вызываем метод initialize
settings = Settings.initialize()

