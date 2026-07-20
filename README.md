# RAG-with-Chatbot
AI-powered Retrieval-Augmented Generation (RAG) chatbot built with Python, LangChain, FAISS, Hugging Face, and Flask for intelligent document-based question answering.
# 🤖 RAG Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that answers questions from PDF documents using LangChain, FAISS, Hugging Face, and Python.

## 📌 Features

- 📄 Load and process PDF documents
- ✂️ Split documents into text chunks
- 🔍 Semantic search using FAISS
- 🧠 Generate context-aware answers
- 🤖 Hugging Face language model integration
- 💬 Interactive command-line chatbot
- ⚡ Fast and accurate document retrieval

## 🛠️ Tech Stack

- Python
- LangChain
- FAISS
- Hugging Face Transformers
- Sentence Transformers
- PyPDF
- Flask (Optional Web Interface)

## 📁 Project Structure

```
RAG-Chatbot/
│── chatbot.py
│── documents/
│── requirements.txt
│── README.md
```

## 🚀 Installation

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
pip install -r requirements.txt
python chatbot.py
```

## 💡 How It Works

1. Load PDF documents.
2. Split the text into smaller chunks.
3. Convert chunks into embeddings.
4. Store embeddings in a FAISS vector database.
5. Retrieve relevant information based on the user's question.
6. Generate an answer using the retrieved context.

## 📷 Demo

```
You: What is RAG?
Bot: Retrieval-Augmented Generation (RAG) combines information retrieval with language generation to provide accurate, context-aware answers.
```
