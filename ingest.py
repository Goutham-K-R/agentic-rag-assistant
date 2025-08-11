import os
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from utils.helpers import clean_text, safe_filename

# Paths for data input and vector index
DATA_PATH = "data/cleaned"
INDEX_PATH = "rag_index"

def load_documents(path):
    """Load all cleaned text documents from the specified folder."""
    documents = []
    for file_path in Path(path).glob("*.txt"):
        loader = TextLoader(str(file_path), encoding="utf-8")
        documents.extend(loader.load())
    return documents

def main():
    print("🔍 Loading documents...")
    docs = load_documents(DATA_PATH)
    print(f"Loaded {len(docs)} docs. Splitting into chunks...")

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    chunks = splitter.split_documents(docs)
    print(f"Total chunks: {len(chunks)}")

    print("🧠 Creating embeddings (Ollama)...")
    embeddings = OllamaEmbeddings(model="mistral")

    print("📦 Indexing with FAISS...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(INDEX_PATH)
    print(f"✅ Vector store saved to '{INDEX_PATH}'")

if __name__ == "__main__":
    main()
