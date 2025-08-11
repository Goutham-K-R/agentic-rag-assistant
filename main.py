from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA

def load_rag_chain():
    """Set up the retrieval + generation pipeline with Ollama and FAISS."""
    embeddings = OllamaEmbeddings(model="mistral")
    vectorstore = FAISS.load_local(
        "rag_index", embeddings, allow_dangerous_deserialization=True
    )
    llm = ChatOllama(model="mistral", base_url="http://127.0.0.1:11434")

    prompt = PromptTemplate(
        template=(
            "Use the following context to answer the question. If the answer is not in the context, say \"I don't know.\"\n\n"
            "{context}\n\nQuestion: {question}\nAnswer:"
        ),
        input_variables=["context", "question"]
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

def main():
    print("Starting your RAG-assisted CLI…")
    qa = load_rag_chain()
    while True:
        q = input("\nAsk a question (or type 'exit'): ").strip()
        if q.lower() == "exit":
            print("Bye! 👋")
            break
        resp = qa.invoke({"query": q})
        print(f"\nAnswer:\n{resp.get('result')}\n")

if __name__ == "__main__":
    main()
