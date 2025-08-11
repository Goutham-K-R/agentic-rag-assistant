<p align="center">
  <img src="https://img.shields.io/badge/Agentic-RAG_Assistant-blue?style=for-the-badge&logo=readthedocs">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python">
</p>

# 🧠 Agentic RAG Assistant  
**Module 1 | Ready Tensor Agentic AI Developer Certification**  

> Retrieval-Augmented Generation (RAG) Assistant that answers natural language queries from your own curated knowledge base — powered by **LangChain**, **Ollama (Mistral)**, and **FAISS**.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Why This Matters](#why-this-matters)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Usage Examples](#usage-examples)
- [Repository Structure](#repository-structure)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 📖 Overview
The **Agentic RAG Assistant** is a context-aware chatbot that retrieves relevant information from a custom dataset before generating responses.  
This ensures more accurate, grounded, and **domain-specific answers** compared to standard LLM outputs.

---

## 💡 Why This Matters
Large Language Models often “hallucinate” or give outdated answers.  
By combining **retrieval** with **generation**, you can:
- Ground responses in your *own trusted data*
- Ensure factual accuracy
- Easily update the knowledge base without retraining

---

## ✨ Key Features
| Feature | Description |
|---------|-------------|
| 📂 **Custom Knowledge Base** | Load your own documents (`.txt`) for indexing |
| 🔍 **FAISS Vector Search** | Fast & scalable similarity search |
| 🧠 **Ollama Embeddings** | Uses `mistral` for semantic vector generation |
| 💬 **Interactive CLI** | Ask natural language questions from the terminal |
| ⚡ **Modular Design** | Separate ingestion and query pipelines |
| 🖥️ **Optional Streamlit UI** | (Future enhancement) Web-based playground |

---

## 🛠 Tech Stack
- **Python 3.10+**
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.ai/) (`mistral` model)
- [FAISS](https://faiss.ai/) Vector Store
- [Streamlit](https://streamlit.io/) (optional UI)
- [dotenv](https://pypi.org/project/python-dotenv/) for env management

---

## ⚙️ Installation & Setup

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/agentic-rag-assistant.git
cd agentic-rag-assistant


## 2️. Create virtual environment & install dependencies
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
pip install -r requirements.txt


## 3 Run Ollama locally 

ollama serve

make sure you have the mistral model pulled:

ollama pull mistral 

## 4 Prepare your documents
Place .txt files inside:

data/cleaned/

## 5 Ingest documents into FAISS index

python ingest.py

## 6 run the assistant

python main.py

## Usage Examples

Ask a question (or type 'exit' to quit'): What is Retrieval-Augmented Generation?
Answer: Retrieval-Augmented Generation (RAG) is a method in AI where a system retrieves relevant context from a knowledge base and uses it to guide an LLM's response, ensuring more accurate and contextually grounded answers.


## (Optional) If you add Streamlit UI:

streamlit run app.py


** 📂 Repository Structure


agentic-rag-assistant/
│
├── data/
│   └── cleaned/               # Your prepared .txt documents
│
├── utils/
│   └── helpers.py              # Utility functions
│
├── ingest.py                   # Document ingestion & vector indexing
├── main.py                     # Query interface
├── prompt_template.txt         # Custom prompt template
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation
└── LICENSE


📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

🙏 Acknowledgments

- LangChain Community

- Ollama Team

- FAISS by Facebook AI

- Ready Tensor for providing the course framework

