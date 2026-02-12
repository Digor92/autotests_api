from pathlib import Path

from pydantic import BaseModel, HttpUrl, Field, FilePath

#from config import settings
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
    upload_file: FilePath

class GetFileResponseSchema(BaseModel):
    file: FileSchema

file_path = Path("./testdata/files/testQA.png")
print(CreateFileRequestSchema(upload_file=file_path))
