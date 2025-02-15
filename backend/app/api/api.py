from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, crud, database
import os
import tasks  # Importa o módulo tasks que está na pasta backend

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/convert/")
def convert_folder(folder_path: str, db: Session = Depends(get_db)):
    # Inicia a tarefa de conversão via Celery
    task = tasks.scan_and_process_folder.delay(folder_path)
    return {"message": "Tarefa de conversão iniciada", "task_id": task.id}

@router.get("/files/")
def list_files(db: Session = Depends(get_db)):
    files = db.query(models.File).all()
    return files

@router.get("/files/{file_id}")
def get_file(file_id: int, db: Session = Depends(get_db)):
    file = crud.get_file(db, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")
    return file

@router.get("/files/{file_id}/download")
def download_file(file_id: int, db: Session = Depends(get_db)):
    file = crud.get_file(db, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")
    if not os.path.exists(file.path):
        raise HTTPException(status_code=404, detail="Arquivo convertido não encontrado")
    from fastapi.responses import FileResponse
    return FileResponse(file.path, media_type='text/plain', filename=os.path.basename(file.path))
