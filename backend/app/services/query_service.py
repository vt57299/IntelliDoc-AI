from app.services.vector_service import search_similar_chunks, get_all_chunks
from app.core.llm import ask_llm, extract_themes
from typing import List

def query_documents(question: str, doc_ids: List[str] = None):
    docs = search_similar_chunks(question, doc_ids)

    context = "\n\n".join([f"[{d['metadata']['doc_id']} - Page {d['metadata']['page']}]: {d['document']}" for d in docs])

    answer = ask_llm(question, context)

    citations = [
        {
            "doc_id": d["metadata"]["doc_id"],
            "page": d["metadata"]["page"],
            "paragraph": d["metadata"].get("paragraph", None),
            "content_snippet": d["document"][:150] + "..."
        } for d in docs
    ]

    return {
        "answer":answer,
        "citations": citations
    }

def synthesize_themes_from_docs():
    chunks = get_all_chunks()

    context = "\n\n".join([
        f"[{chunk['metadata']['doc_id']} - Page {chunk['metadata']['page']}]: {chunk['document']}"
        for chunk in chunks
    ])

    result = extract_themes(context)

    return {
        "themes": result
    }