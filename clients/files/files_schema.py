from pydantic import  BaseModel, HttpUrl, Field
from tools.fakers import fake

class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str

# Добавили описание структуры запроса на создание файла
class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema

class CreateFileRequestSchema(BaseModel):
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: str

#print(CreateFileRequestSchema(upload_file="./test/file.txt"))