from pydantic import  BaseModel, HttpUrl

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
    filename: str
    directory: str
    upload_file: str