from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict

from clients.files.files_client import File
from clients.privat_http_builder import get_privat_http_client, AuthenticationUserDict
from clients.users.privat_users_client import User


class GetCoursesDict(TypedDict):
    """
        Описание структуры запроса на получение списка курсов.
        """
    userId: str

class CreateCoursesDict(TypedDict):
    """
        Описание структуры запроса на создание курса.
        """
    title: str
    maxScore: None
    minScore: None
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str
class UpdateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class Course(TypedDict):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File  # Вложенная структура файла
    estimatedTime: str
    createdByUser: User  # Вложенная структура пользователя

# Добавили описание структуры запроса на создание курса
class CreateCourseRequestDict(TypedDict):
    """
    Описание структуры ответа создания курса.
    """
    course: Course

class CoursesClient(APIClient):
    def get_courses_api(self, query: GetCoursesDict)->Response:
        """
                Метод получения списка курсов.

                :param query: Словарь с userId.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.get('/api/v1/courses', params = query)

    def create_course_api(self,request: CreateCoursesDict)->Response:
        """
        Метод создания курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/courses', json = request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCoursesDict) -> CreateCourseRequestDict:
        response = self.create_course_api(request)
        return response.json()

def get_course_client(user: AuthenticationUserDict) -> CoursesClient:
    return CoursesClient(client = get_privat_http_client(user))