
# HealthRAG

HealthRAG is a Retrieval-Augmented Generation (RAG) chatbot designed for medical document question-answering, built with Python, LangChain, FAISS, and Hugging Face API.

---

## Overview

HealthRAG is a medical Q&A chatbot that responds to user queries by retrieving relevant information from PDF documents. It is intended for:

- 🩺 **Patients** seeking general medical insights (may contain technical language)
- 👨‍⚕️ **Medical students** for revision, summarization, and context-based querying

> The **quality of answers** depends heavily on the **PDFs provided** as context.

---

## 🎥 Demo

![Demo](HealthRag_demo.gif)

---

## ⚙️ How It Works

1. Users upload one or more PDF files containing medical content
2. The content is split into chunks and converted into embeddings
3. FAISS is used to store the embeddings and retrieve the most relevant context
4. A custom prompt sends the context + user question to a hosted LLM via Hugging Face Router
5. The chatbot responds concisely using only the retrieved context

---

## 🧪 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Y1D1R/HealthRAG.git
cd HealthRAG
```

### 2. Create and configure your `.env`
Create a `.env` file in the root with:
```bash
HF_TOKEN=your_huggingface_access_token
HF_API_TOKEN=your_huggingface_api_token
```
👉 You can get this from https://huggingface.co/settings/tokens

### 3. Install dependencies
```bash
pip install -e .
```

### 4. Add your PDFs
Place your medical `.pdf` files in the `data/` directory.

### 5. Generate the vector store
```bash
python app/components/data_loader.py
```

### 6. Launch the app
```bash
python app/application.py
```
Visit the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🐳 Run with Docker

### 1. Add your PDFs
Place your PDF documents in the local `data/` folder before building the image.

### 2. Create and configure your `.env`
Ensure your `.env` file with API keys is available in the root before the build.

### 3. Build the Docker image
```bash
docker build -t healthrag .
```

> ✅ During the build, the vector store will be automatically generated from the contents of `data/`.

### 4. Run the container
```bash
docker run -p 5000:5000 --name healthrag-container healthrag
```

Then visit the app at: [http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

```
HealthRAG/
├── app/
│   ├── components/       # pdf_loader, embeddings, vector store
│   ├── config/           # API keys, chunk config
│   ├── common/           # Logger, custom exception
│   └── application.py    # Flask web interface
├── templates/            # Frontend HTML
├── static/images/        # Logo
├── data/                 # Your medical PDFs
├── Dockerfile
├── setup.py
├── Jenkinsfile
└── README.md
```

---

## 🧰 Built With

- Python 3.11
- Flask
- LangChain
- Hugging Face Hub & Router
- FAISS (vector store)
- Sentence Transformers (embeddings)
- OpenAI-compatible `openai` Python client

---

## 🛡️ Disclaimer
This chatbot is a proof of concept and **not intended for clinical use**. Its accuracy depends solely on the content of the provided PDFs.

---
