from fastapi import APIRouter, UploadFile, File
from app.services.ocr_services import process_document
from app.services.metadata_service import load_all_metadata
from typing import List

router = APIRouter(prefix="/documents", tags=["documents"])

# @router.get("/upload")
# async def upload_document(file: UploadFile = File(...)):
#     result = await process_document(file)
#     return {"status": "success", "data": result}

@router.get("/upload")
async def upload_documents(files: List[UploadFile] = File(...)):
    responses = []
    for file in files:
        result = await process_document(file)
        responses.append({
            "filename": file.filename,
            "doc_id": result.get("doc_id", None),
            "pages": result.get("pages", 0),
            "error": result.get("error", None)
        })
    return {"status": "success", "documents": responses}


@router.get("/list")
async def list_document():
    docs = load_all_metadata()
    return {"documents": docs}

