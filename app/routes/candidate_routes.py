from fastapi import APIRouter, UploadFile, File
import shutil
import uuid

from app.services.parser import parse_pdf
from app.services.embedding import create_embedding
from app.services.llm import extract_cv_information

router = APIRouter()

UPLOAD_FOLDER = "uploads"

@router.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):

    file_id = str(uuid.uuid4())

    file_path = f"{UPLOAD_FOLDER}/{file_id}.pdf"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    cv_text = parse_pdf(file_path)

    info = extract_cv_information(cv_text)

    embedding = create_embedding(cv_text)

    return {
        "cv_text": cv_text,
        "structured_data": info,
        "embedding_length": len(embedding)
    }