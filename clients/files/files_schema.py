from pydantic import BaseModel, Field, FilePath

from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """

    id: str
    url: str
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """

    filename: str = Field(default_factory=fake.file_name)
    directory: str = Field(default_factory=fake.word)
    upload_file: FilePath


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """

    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """
    Описание структуры запроса получения файла.
    """

    file: FileSchema
