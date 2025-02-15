from pydantic import BaseModel
from datetime import datetime

class FileBase(BaseModel):
    name: str
    path: str
    file_type: str
    file_size: int
    description: str | None = None

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: int
    created_at: datetime | None = None
    pdf_text: str | None = None
    docx_text: str | None = None
    excel_text: str | None = None
    image_text: str | None = None
    video_info: str | None = None

    class Config:
        orm_mode = True
