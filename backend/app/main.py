# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

from fastapi import FastAPI
from app.api import document, query

app = FastAPI()

app.include_router(document.router)
app.include_router(query.router)

@app.get('/')
def read_root():
    return {"message": "Chatbot backend is running 🚀"}
