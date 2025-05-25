# 🧠 IntelliDoc AI

**IntelliDoc AI** is an intelligent document analysis platform that enables users to upload, query, and extract insights from multiple PDFs and scanned images. With a powerful FastAPI backend and an intuitive Streamlit interface, the system supports natural language questions, citation-level responses, and high-level theme synthesis across documents.

---

## 🚀 Features

- 📄 Upload and process 75+ documents (PDFs, scanned images)
- 🔍 Ask questions across all or specific documents
- 📌 Receive answers with precise citations (page, paragraph)
- 🧩 Extract common themes using Gemini Pro
- 🧾 OCR support for scanned PDFs and images via Tesseract
- 💬 Streamlit-based user interface
- 🐳 Docker-ready, cross-platform compatible

---

## 🧠 AI Models Used

| Task                | Model / Provider           |
|---------------------|----------------------------|
| Answering Questions | `llama3-70b-8192` via Groq |
| Theme Extraction    | `Gemini 1.5 Pro` via Google AI Studio |

---

## 🧱 Tech Stack

| Layer     | Technology                        |
|-----------|------------------------------------|
| Backend   | FastAPI, ChromaDB, SentenceTransformers |
| OCR       | PyMuPDF, Tesseract OCR            |
| LLMs      | Groq (LLaMA 3), Gemini Pro        |
| Frontend  | Streamlit                         |
| Deployment| Docker + Docker Compose           |

---

## 📦 Project Structure

```

IntelliDoc-AI/
├── backend/
│   ├── app/               # FastAPI logic
│   ├── Dockerfile         # Backend Docker definition
│   ├── requirements.txt
│   ├── .env.example       # API key template
├── frontend/
│   ├── app.py
│   ├── Dockerfile         # Frontend Docker definition
│   ├── requirements.txt
├── docker-compose.yml     # Compose both services
├── demo/
│   └── demo.mp4           # Demo video of the app
└── README.md

````

---

## 📹 Demo

> 🎬 Watch IntelliDoc AI in action:

https://github.com/user-attachments/assets/041a386a-a28b-4972-a23b-0312318847db

---

## 🚀 Getting Started

### ✅ Clone the Repository

```bash
git clone https://github.com/yourusername/IntelliDoc-AI.git
cd IntelliDoc-AI
````

---

## 🐳 Run with Docker (Recommended)

### 1. Configure API Keys

Copy and configure your `.env`:

```bash
cp backend/.env.example backend/.env
```

Add your actual API keys:

```env
GEMINI_API_KEY=your-gemini-key
GROQ_API_KEY=your-groq-key
```

### 2. Build & Start Containers

```bash
docker-compose up --build
```

### 3. Access the App

* Frontend UI: `http://<your-ip>:8501`
* Backend API Docs: `http://<your-ip>:8000/docs`

---

## ⚙️ Run Locally (Without Docker)

### Backend

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Environment Variables

Located in `backend/.env`. Required for secure access to LLM APIs.

```env
GEMINI_API_KEY=your-gemini-key
GROQ_API_KEY=your-groq-key
```

> ❗ Never commit this file. Use `.env.example` for sharing.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit and push (`git commit -m 'Add your feature'`)
5. Open a pull request

---

## 📎 License

This project is intended for demonstration, education, and evaluation purposes only.

---

## ✍️ Author

**Vivek**
Backend & AI Systems Engineer
[GitHub](https://github.com/vt57299) | [LinkedIn](https://linkedin.com/in/vivek-thakur-7079aa17b)
