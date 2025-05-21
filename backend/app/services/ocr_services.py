import pymupdf # PyMuPDF
import pytesseract
from PIL import Image
from io import BytesIO
from app.services.metadata_service import save_metadata
import os

from app.services.vector_service import embed_and_store
import uuid

async def process_document(file):
    filename = file.filename.lower()
    file_bytes = await file.read()

    extracted_pages = []

    # process PDF file
    if filename.endswith(".pdf"):
        extracted_pages = extract_text_from_pdf(file_bytes)
    elif filename.endswith((".png", ".jpg", ".jpeg")):
        extracted_pages = extract_text_from_image(file_bytes)
    else:
        return {"error": "Unsupported file type"}
    
    # generate unique doc ID and store
    document_id = str(uuid.uuid4())[:8]
    embed_and_store(extracted_pages, document_id)    # storing in db
    save_metadata(document_id, file.filename, len(extracted_pages))     # saving metadata

    return {"doc_id": document_id, "pages": len(extracted_pages)}
    
def extract_text_from_pdf(file_bytes):
    doc = pymupdf.open(stream=file_bytes, filetype="pdf")   # open document using stream file data
    extracted_pages = []

    for i, page in enumerate(doc):
        text = page.get_text()
        if not text.strip():
            pix = page.get_pixmap()    # render page to an image
            img = Image.open(BytesIO(pix.tobytes("png")))
            text = pytesseract.image_to_string(img)
        extracted_pages.append({"page": i + 1, "text": text})
    
    return extracted_pages

def extract_text_from_image(file_bytes):
    image = Image.open(BytesIO(file_bytes))
    text = pytesseract.image_to_string(image)
    return [{"page": 1, "text": text}]
