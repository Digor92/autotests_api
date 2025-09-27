from httpx import Response
from clients.api_client import APIClient
from clients.privat_http_builder import get_privat_http_client, AuthenticationUserSchema
from clients.files.files_schema import FileSchema, CreateFileRequestSchema, CreateFileResponseSchema


class FilesClient(APIClient):
    def get_file_api(self, files_id:str)->Response:
        """
                Метод получения файла.

                :param file_id: Идентификатор файла.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.get(f'api/v1/files/{files_id}')

    def create_file_api(self, request:CreateFileRequestSchema) -> Response:
        """
                Метод создания файла.

                :param request: Словарь с filename, directory, upload_file.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.post('api/v1/files',
                         data = request.model_dump(by_alias=True, exclude={'upload_file'}),
                         files = {'upload_file': open(request.upload_file, 'rb')}
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

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    return FilesClient(client = get_privat_http_client(user))

