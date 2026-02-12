
import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
from tools.fakers import fake

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    last_name: str = Field(alias="lastName")
    @computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self)->str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    # # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    # динамически генеригует значене id
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    #id: str = Field(default_factory=lambda: fake.email())
    title: str = "PlayWrite"
    max_score: int = Field(alias="maxScore", default=1200)
    min_score: int = Field(alias="minScore", default=1100)
    description: str = "PlayWrite"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id = "course id 1",
    title = "Playwrite",
    max_score = 1201,
    min_score = 1101,
    description = "Playwrite",
    previewFile = FileSchema(
            id = "file-id",
            filename = "file.png",
            directory = "course",
            url = "http://localhost:8000/"
    ),
    estimatedTime = "2 week",
    createdByUser = UserSchema(
            id = "user-id",
            email = "dedkov@mail.ru",
            firstName = "igor",
            middleName = "igorevich",
            lastName = "dedkov"
    )
)

print("course base model: ", course_default_model, type(course_default_model))

# из cловаря получили модель
course_dict = {
    "id":"course id 2",
    "title":"Playwrite",
    "maxScore":100,
    "minScore":10,
    "previewFile": {
            "id": "string",
            "filename": "string",
            "directory": "string",
            "url": "https://example.com/"
            },
    "description":"Playwrite",
    "estimatedTime":"2 week",
    "createdByUser": {
            "id": "string",
            "email": "user@example.com",
            "firstName": "string",
            "middleName": "string",
            "lastName": "string"
            }
    }


course_dict_model = CourseSchema(**course_dict)
print("course dict model: ", course_dict_model, type(course_dict_model))

# из json строки получили модель
course_json = """
    {
    "id":"course id 3",
    "title":"Playwrite",
    "maxScore":100,
    "minScore":10,
    "previewFile": {
            "id": "file-id",
            "filename": "file.png",
            "directory": "course",
            "url": "https://example.com/"
            },
    "description":"Playwrite",
    "estimatedTime":"2 week",
    "createdByUser": {
            "id": "user-id",
            "email": "user@gmail.com",
            "firstName": "igor",
            "middleName": "Igorevixh",
            "lastName": "Dedkov"
            }
    }
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print("course json model: ", course_json_model, type(course_json_model))
print("DICT: ", course_json_model.model_dump()) # в dict вернули НЕ правильное написание
print("JSON: ", course_json_model.model_dump_json(by_alias=True)) # в json вернули правильное написание


user = UserSchema(
            id = "user-id",
            email = "d@m.ru",
            firstName = "igor",
            middleName = "igorevich",
            lastName = "dedkov")

print(user.get_username(), user.username)

# поработаем с ошибкой
try:
    file =  FileSchema(
            id = "file-id",
            filename = "file.png",
            directory = "course",
            url = "localhost"
    )
except ValidationError as error:
    print(error)
    print(error.errors())

