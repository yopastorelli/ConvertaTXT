import os
from celery import Celery
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal  # Import da SessionLocal

celery_app = Celery(__name__, broker='redis://localhost:6379/0')  # Ajuste se estiver rodando local

@celery_app.task
def scan_and_process_folder(folder_path: str):
    """Função Celery que percorre a pasta e processa cada arquivo."""
    db: Session = SessionLocal()
    try:
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_extension = file_name.split('.')[-1].lower()
                file_size = os.path.getsize(file_path)
                file_metadata = schemas.FileCreate(
                    name=file_name,
                    path=file_path,
                    file_type=file_extension,
                    file_size=file_size
                )
                crud.create_file(db=db, file=file_metadata)
                process_file(file_path, file_extension)
    finally:
        db.close()

def process_file(file_path: str, file_extension: str):
    if file_extension == 'pdf':
        extract_pdf_text(file_path)
    elif file_extension == 'docx':
        extract_docx_text(file_path)
    elif file_extension == 'xlsx':
        extract_excel_text(file_path)
    elif file_extension in ['jpg', 'jpeg', 'png']:
        extract_image_text(file_path)
    elif file_extension in ['mp4', 'avi']:
        extract_video_info(file_path)
    else:
        # Tipo de arquivo não suportado
        pass

def extract_pdf_text(file_path: str):
    # TODO: Implementar extração de texto para PDF usando pdfminer.six
    pass

def extract_docx_text(file_path: str):
    # TODO: Implementar extração de texto para DOCX usando python-docx
    pass

def extract_excel_text(file_path: str):
    # TODO: Implementar extração de texto para Excel usando openpyxl
    pass

def extract_image_text(file_path: str):
    # TODO: Implementar OCR para extração de texto de imagens usando pytesseract
    pass

def extract_video_info(file_path: str):
    # TODO: Implementar extração de informações de vídeo usando ffmpeg-python
    pass
