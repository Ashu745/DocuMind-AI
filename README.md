# 📄 DocuMind AI

An AI-powered document assistant that allows users to upload PDF documents, perform semantic search, and receive context-aware answers using Retrieval-Augmented Generation (RAG).

## 🚀 Features

* Upload and process PDF documents
* Support for multiple PDF uploads
* Automatic text extraction and chunking
* Vector embeddings generation
* ChromaDB vector storage
* Semantic similarity search
* Retrieval-Augmented Generation (RAG)
* Source attribution for answers
* Conversational chat interface
* Chat history tracking

---

## 🏗️ Architecture

```text
PDF Upload
    ↓
Text Extraction (PyMuPDF)
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
ChromaDB Vector Store
    ↓
Semantic Retrieval
    ↓
LLM Generation
    ↓
Answer + Sources
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Vector Database

* ChromaDB

### PDF Processing

* PyMuPDF

### Text Chunking

* LangChain Text Splitters

### AI Components

* Embedding Model
* Large Language Model (LLM)
* Retrieval-Augmented Generation (RAG)

---

## 📂 Project Structure

```text
DocuMind-AI/
│
├── app.py
├── ingest.py
│
├── services/
│   └── rag_service.py
│
├── modules/
│   ├── ingestion/
│   ├── retrieval/
│   ├── generation/
│   ├── embeddings/
│   └── vector_store/
│
├── data/
│   └── pdfs/
│
├── chromadb/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd DocuMind-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📸 Example Workflow

1. Upload one or more PDF documents.
2. Click **Ingest Documents**.
3. Ask questions about the uploaded documents.
4. Receive AI-generated answers grounded in the document content.
5. View document sources used to generate the response.

---

## 💡 Future Improvements

* Streaming responses
* Conversation-aware retrieval
* Document deletion
* Knowledge base management
* Authentication and user accounts
* Cloud deployment
* Source snippet highlighting

---

## 👨‍💻 Author

Asirbad Pattanaik

Built to explore Retrieval-Augmented Generation, vector databases, semantic search, and AI-powered document intelligence systems.
