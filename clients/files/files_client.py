from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

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

    def create_file_api(self, request:CreateFileRequestDict):
        """
                Метод создания файла.

                :param request: Словарь с filename, directory, upload_file.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.post('api/v1/files',
                         data = request,
                         file = {'upload_file': open(request['upload_file'], 'rb')}
                         )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")