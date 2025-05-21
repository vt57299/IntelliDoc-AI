from app.config import settings
import json
import os

METADATA_FILE = settings.METADATA_FILE

def save_metadata(doc_id: str, filename: str, pages: int):
    entry = {
        "doc_id": doc_id,
        "filename": filename,
        "pages": pages
    }

    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r") as f:
            data = json.load(f)

    else:
        data = []

    data.append(entry)
    
    with open(METADATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_all_metadata():
    if not os.path.exists(METADATA_FILE):
        return []
    with open(METADATA_FILE, "r") as f:
        return json.load(f)
