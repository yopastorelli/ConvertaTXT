from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class File(Base):
    __tablename__ = "files"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)         # Nome do arquivo (anteriormente file_name)
    path = Column(String, index=True, nullable=False)           # Caminho completo do arquivo
    file_type = Column(String, index=True, nullable=False)      # Tipo do arquivo (ex.: pdf, docx, etc.)
    file_size = Column(Integer, nullable=False)                 # Tamanho do arquivo em bytes
    description = Column(String, index=True, nullable=True)
    created_at = Column(DateTime)
    
    # Colunas para armazenar informações extraídas por diferentes ferramentas:
    pdf_text = Column(String, nullable=True)                    # Texto extraído via pdfminer.six
    docx_text = Column(String, nullable=True)                   # Texto extraído via python-docx
    excel_text = Column(String, nullable=True)                  # Texto extraído via openpyxl
    image_text = Column(String, nullable=True)                  # Texto extraído via pytesseract
    video_info = Column(String, nullable=True)                  # Informações extraídas via ffmpeg-python

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
