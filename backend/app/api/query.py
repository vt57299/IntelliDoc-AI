from fastapi import APIRouter, Body, Query
from typing import Optional, List
from app.services.query_service import query_documents, synthesize_themes_from_docs

router = APIRouter(prefix="/query", tags=["query"])

@router.post("/")
async def query_endpoint(
    question: str = Body(..., embed=True),
    doc_ids: Optional[List[str]] = Query(None)
):
    return query_documents(question, doc_ids)

@router.get("/themes")
async def extract_themes_endpoint():
    return synthesize_themes_from_docs()