# 🧠 Document Intelligence Chatbot – GenAI Internship Assignment

This project is a production-grade, AI-powered document intelligence system that allows users to upload multiple documents (PDFs and images), ask natural language questions, and extract answers with precise citations and theme summaries.

> 🚀 Built as a part of the Wasserstoff Gen-AI Internship task.

---

## ✨ Features

- 📄 Upload and process 75+ documents (PDFs, scanned images)
- 🔍 Query all or selected documents using natural language
- 📌 Get answers with citations (document → page → paragraph)
- 🧩 Extract common themes across all documents using Gemini Pro
- 📊 Track and view all uploaded documents via clean API or UI
- 💬 Visual interface built using Streamlit (optional)

---

## 🧠 AI Models Used

| Functionality             | Model / Provider           |
|--------------------------|----------------------------|
| Answering Questions      | `llama3-70b-8192` via Groq |
| Theme Extraction         | `Gemini 1.5 Pro` via Google AI Studio |

---

## 🧱 Tech Stack

- 🐍 Python 3.11
- 🚀 FastAPI (Backend API)
- 🧠 ChromaDB (Vector DB)
- 🤖 SentenceTransformers for embeddings
- 🧾 Tesseract OCR + PyMuPDF (for PDFs/images)
- 🧑‍💻 Streamlit (Frontend UI)
- 🐳 Docker & Docker Compose (Deployment)

---

## 📦 Folder Structure

```

chatbot\_theme\_identifier/
├── backend/           # FastAPI app
│   ├── app/           # All backend logic (API, services, core)
│   ├── data/          # OCR output, vector DB, metadata
│   ├── .env           # (Ignored) user-defined API keys
│   └── requirements.txt
├── frontend/          # Streamlit app
│   ├── app.py
│   └── requirements.txt
├── demo/              # Demo video of the app
├── .env.example       # API key template
├── docker-compose.yml
└── README.md

````

---

## ⚙️ Setup (Docker - Recommended)

> 🛑 Make sure you create your `.env` file with API keys before building.

### 1. Create `.env` file

Copy from template:
```bash
cp backend/.env.example backend/.env
````

Then edit `backend/.env` and add your keys:

```env
GEMINI_API_KEY=your-gemini-key
GROQ_API_KEY=your-groq-key
```

### 2. Build and Run

```bash
docker-compose up --build
```

### Access:

* **Frontend UI**: [http://localhost:8501](http://localhost:8501)
* **Backend API docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ⚙️ Setup (Manual / No Docker)

### 1. Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2. Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 API Key Handling

This project requires access to:

* **Gemini API** (via Google AI Studio – no billing required)
* **Groq API** (for LLaMA 3 model inference)

> Keys are loaded securely using `.env` file and not committed to version control.

---

## 🧪 API Endpoints

### `POST /documents/upload`

Upload multiple PDFs/images and extract text + embeddings

### `GET /documents/list`

View metadata of all uploaded documents

### `POST /query`

Ask a question across all or specific documents

**Query Parameters:**

* `doc_ids[]` — (optional) List of specific document IDs to filter

**Response:**

* Answer
* Citations with `doc_id`, `page`, `paragraph`, and snippet

### `GET /query/themes`

Extract themes and topic clusters across all stored documents


## 📎 License

This code was created for academic & project evaluation purposes. Do not reuse any keys or credentials embedded during testing.

---

## ✍️ Author

**Vivek**
Generative AI Application Engineer
[GitHub](https://github.com/vt57299) | [LinkedIn](https://linkedin.com/in/vivek-thakur-7079aa17b)

