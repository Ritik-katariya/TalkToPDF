from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import shutil
from ..database import get_db
from ..models import Document
from ..utils.pdf_processing import extract_text_from_pdf
import os

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    text_content = extract_text_from_pdf(file_path)
    document = Document(filename=file.filename, text_content=text_content)
    db.add(document)
    db.commit()
    db.refresh(document)
    
    return {"document_id": document.id, "filename": document.filename}
