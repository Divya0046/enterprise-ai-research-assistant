# 🤖 Enterprise AI Research Assistant

An enterprise-grade **Retrieval-Augmented Generation (RAG)** application that enables users to upload PDF documents and ask natural language questions. The system performs semantic search using vector embeddings stored in **ChromaDB** and generates context-aware answers using **Google Gemini**.

The project is designed with a modular architecture using **FastAPI**, **LangChain**, **HuggingFace Embeddings**, **ChromaDB**, and **Streamlit**, making it easy to extend with additional AI capabilities in the future.

---

## 🚀 Features

- 📄 Upload one or multiple PDF documents
- ✂️ Intelligent document chunking
- 🧠 Semantic search using HuggingFace embeddings
- 🗄️ ChromaDB vector database
- 🤖 Google Gemini powered answer generation
- ⚡ FastAPI REST API
- 🖥️ Streamlit user interface
- 📚 Source attribution with page numbers
- 📝 Logging and configuration management
- 🐳 Docker support

---

# 🏗️ System Architecture

```text
                     User
                       │
                       ▼
            ┌────────────────────┐
            │    Streamlit UI    │
            └─────────┬──────────┘
                      │
                      ▼
            ┌────────────────────┐
            │    FastAPI API     │
            └─────────┬──────────┘
                      │
         ┌────────────┴────────────┐
         │                         │
         ▼                         ▼
  Upload Document            Ask Question
         │                         │
         ▼                         ▼
     PDF Loader              Retriever
         │                         │
         ▼                         ▼
 Text Splitter           ChromaDB Vector Store
         │                         │
         ▼                         ▼
 HuggingFace Embeddings      Relevant Chunks
         │                         │
         └────────────┬────────────┘
                      ▼
               Prompt Construction
                      │
                      ▼
                Google Gemini
                      │
                      ▼
           Answer + Source Citations
```

### RAG Pipeline

1. User uploads one or more PDF documents.
2. PDFs are parsed using **PyPDFLoader**.
3. Documents are split into overlapping chunks using **RecursiveCharacterTextSplitter**.
4. Each chunk is converted into vector embeddings using **HuggingFace Sentence Transformers**.
5. Embeddings are stored in **ChromaDB**.
6. When a user asks a question, the query is embedded using the same embedding model.
7. ChromaDB retrieves the most semantically relevant chunks.
8. The retrieved context and user query are combined into a prompt.
9. **Google Gemini** generates a context-aware answer.
10. The application returns both the answer and the source document/page references.

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| LLM Framework | LangChain |
| Embedding Model | HuggingFace Sentence Transformers |
| Vector Database | ChromaDB |
| Large Language Model | Google Gemini |
| PDF Processing | PyPDF |
| API Testing | Swagger UI |
| Containerization | Docker |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
enterprise-ai-research-assistant/
│
├── backend/
│   ├── api/                 # FastAPI endpoints
│   ├── ingestion/           # PDF ingestion pipeline
│   ├── llm/                 # Gemini integration
│   ├── loaders/             # PDF loader
│   ├── rag/                 # Retriever and RAG pipeline
│   ├── utils/               # Logger and utilities
│   ├── vectorstore/         # Embeddings and ChromaDB
│   ├── config.py            # Project configuration
│   └── main.py              # FastAPI entry point
│
├── frontend/
│   └── app.py               # Streamlit UI
│
├── documents/               # Sample PDF documents for indexing
│
├── chroma_db/               # Vector database
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Divya0046/enterprise-ai-research-assistant.git
cd enterprise-ai-research-assistant
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

## 3. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```
---

# ▶️ Running the Application

## Step 1 — Ingest Documents

Place your PDF documents inside the `documents/` directory.

Generate embeddings and create the ChromaDB vector database.

```bash
python -m backend.ingestion.ingest
```

---

## Step 2 — Start FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Step 3 — Start Streamlit Frontend

```bash
streamlit run frontend/app.py
```

Open:

```
http://localhost:8501
```

---

# 🐳 Docker

Build the Docker image

```bash
docker build -t enterprise-ai-research-assistant .
```

Run the container

```bash
docker run -p 8000:8000 enterprise-ai-research-assistant
```

---

# 🌐 REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/upload` | Upload one or more PDF documents |
| POST | `/ask` | Ask questions about uploaded documents |
| GET | `/documents` | List indexed documents |
| DELETE | `/documents/{filename}` | Delete a document and rebuild the vector database |

---

# 🚀 Future Enhancements

- LangGraph Agent
- Hybrid Search (BM25 + Vector Search)
- Re-ranking
- Multi-document comparison
- Conversation memory
- Authentication & Authorization
- Cloud deployment (AWS / Azure / GCP)
- CI/CD pipeline

---
# 📸 Screenshots

## Streamlit User Interface

![Streamlit UI](C:\Users\NISHTHA RAI\OneDrive\Desktop\AI Assistant project\enterprise-ai-research-assistant\assets\streamlit.png)
![Streamlit UI](C:\Users\NISHTHA RAI\OneDrive\Desktop\AI Assistant project\enterprise-ai-research-assistant\assets\streamlit2.png)
---

## FastAPI Swagger Documentation

![Swagger API](C:\Users\NISHTHA RAI\OneDrive\Desktop\AI Assistant project\enterprise-ai-research-assistant\assets\swagger.png)

# 👨‍💻 Author

**Divya Rai**

M.Tech – Information Security  
Maulana Azad National Institute of Technology (MANIT), Bhopal

- GitHub: https://github.com/Divya0046
- LinkedIn: https://www.linkedin.com/in/divya-rai-494860223/

---

⭐ If you found this project useful, consider giving it a star.