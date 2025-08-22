from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

from clients.privat_http_builder import get_privat_http_client, AuthenticationUserDict

class File(TypedDict):
    """
    Описание структуры файла.
    """
    id: str
    url: str
    filename: str
    directory: str

# Добавили описание структуры запроса на создание файла
class CreateFileResponseDict(TypedDict):
    """
    Описание структуры ответа создания файла.
    """
    file: File

class CreateFileRequestDict(TypedDict):
    filename: str
    directory: str
    upload_file: str
class FilesClient(APIClient):
    def get_file_api(self, files_id:str)->Response:
        """
                Метод получения файла.

                :param file_id: Идентификатор файла.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.get(f'api/v1/files/{files_id}')

    def create_file_api(self, request:CreateFileRequestDict) -> Response:
        """
                Метод создания файла.

                :param request: Словарь с filename, directory, upload_file.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.post('api/v1/files',
                         data = request,
                         files = {'upload_file': open(request['upload_file'], 'rb')}
                         )
        # files = {'upload_file': open(request['upload_file'], 'rb')}
        # data = {
        #     'filename': request['filename'],
        #     'directory': request['directory']
        # }
        # return self.post('api/v1/files', data=data, files=files)

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        response = self.create_file_api(request)
        return response.json()


def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    return FilesClient(client = get_privat_http_client(user))

