import streamlit as st
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# Load the chain
@st.cache_resource
def build_chain():
    embeddings = OllamaEmbeddings(model="mistral")
    vectorstore = FAISS.load_local(
        "rag_index", embeddings, allow_dangerous_deserialization=True
    )
    llm = ChatOllama(model="mistral", base_url="http://127.0.0.1:11434")
    prompt_template = PromptTemplate(
        template=(
            "Use the following context to answer the question. If the answer is not in the context, say \"I don't know.\"\n\n"
            "{context}\n\nQuestion: {question}\nAnswer:"
        ), input_variables=["context", "question"]
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": prompt_template},
        return_source_documents=True,
    )

st.title("RAG Assistant Playground")
st.write("Ask questions based on your document dataset.")

qa_chain = build_chain()
user_query = st.text_input("Your question:")

if user_query:
    with st.spinner("Thinking..."):
        response = qa_chain.invoke({"query": user_query})
        answer = response["result"]
        st.markdown(f"**Answer:** {answer}")
