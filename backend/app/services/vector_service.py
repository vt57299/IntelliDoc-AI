from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import uuid
from typing import List
import re

# Initialize embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="data/vectorstore", settings=Settings(
    persist_directory="backend/data/vectorstore",   # our storage path
    # chroma_db_impl="duckdb+parquet"    # Uses DuckDB (lightweight SQL) + Parquet files for efficient local vector storage
))
collection = chroma_client.get_or_create_collection(name="documents")

# --- CHUNKING LOGIC ---
def chunk_text(text, chunk_size=500, overlap=100):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def chunk_paragraphs(text):
    paragraphs = re.split(r'\n{2,}', text)  # splitting on double newlines
    chunks = []

    for i, para in enumerate(paragraphs):
        para = para.strip()
        if len(para.split()) > 20:  # Skipping very short lines
            chunks.append((i+1, para))  # (para number, text)

    return chunks



# --- EMBED + STORE ---
def embed_and_store(document_text: list, document_id: str):
    for i, page in enumerate(document_text):
        page_text = page["text"]
        para_chunks = chunk_paragraphs(page_text)

        texts = [para for _, para in para_chunks]
        para_numbers = [para_num for para_num, _ in para_chunks]

        embeddings = embedder.encode(texts)
        ids = [f"{document_id}_p{i+1}_para{j}" for j in para_numbers]

        collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids,
            metadatas=[{
                "doc_id":document_id,
                "page": i + 1,
                "paragraph": para_num
            } for para_num in para_numbers]
        )


# def embed_and_store(document_text: list, document_id: str):
#     """
#     Accepts list of page-level text content and stores embeddings in ChromaDB.
#     """
#     for i, page in enumerate(document_text):
#         page_text = page["text"]
#         chunks = chunk_text(page_text)

#         embeddings = embedder.encode(chunks)
#         ids = [f"{document_id}_p{i+1}_c{j}" for j in range(len(chunks))]

#         collection.add(
#             documents=chunks,
#             embeddings=embeddings,
#             ids=ids,
#             metadatas=[{"doc_id": document_id, "page": i + 1, "chunk": j} for j in range(len(chunks))]
#         )


def search_similar_chunks(query: str, doc_ids: List[str], top_k: int = 5):
    embedding = embedder.encode([query])[0]
    # results = collection.query(query_embeddings=[embedding], n_results=top_k, include=['documents', 'metadatas'])

    query_params = {"query_embeddings": [embedding], "n_results": top_k, "include": ['documents', 'metadatas']}
    if doc_ids:
        query_params["where"] = {"doc_id": {"$in": doc_ids}}

    results = collection.query(**query_params)
    
    return [
        {
            "document": doc, 
            "metadata": meta
        }
        for doc, meta in zip(results["documents"][0], results["metadatas"][0])
    ]

def get_all_chunks():
    results = collection.get(include=["documents", "metadatas"])

    return [
        {
            "document": doc,
            "metadata": meta
        } for doc, meta in zip(results['documents'], results['metadatas'])
    ]


