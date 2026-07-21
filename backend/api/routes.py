from fastapi import APIRouter
from fastapi import UploadFile, File
from pathlib import Path
import shutil
import os
from fastapi import HTTPException
from backend.api.schemas import QuestionRequest
from backend.rag.rag_chain import ask_question
from backend.ingestion.ingest import ingest_documents

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Enterprise AI Research Assistant"
    }

@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    documents_dir = Path("documents")
    documents_dir.mkdir(exist_ok=True)

    file_path = documents_dir / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_documents()

    return {
        "message": "Document uploaded and indexed successfully",
        "filename": file.filename
    }

@router.get("/documents")
def list_documents():

    documents_dir = Path("documents")

    files = [
        file.name
        for file in documents_dir.glob("*.pdf")
    ]

    return {
        "documents": files,
        "count": len(files)
    }

@router.delete("/documents/{filename}")
def delete_document(filename: str):

    file_path = Path("documents") / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    os.remove(file_path)

    ingest_documents()

    return {
        "message": "Document deleted successfully",
        "filename": filename
    }


@router.post("/ask")
def ask(request: QuestionRequest):

    answer, sources = ask_question(request.question)

    return {
        "answer": answer,
        "sources": sources
    }