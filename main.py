from config import CHROMA_DIR, OPENAI_TOKEN, CHUNK_SIZE, CHUNK_OVERLAP
from langchain_openai import ChatOpenAI

from loaders import load_pdf
from splitter import split_documents
from embeddings import get_embeddings
from vectorstore import build_vectorstore
from retriever import get_retriever
from prompt import get_prompt
from rag_chain import build_rag_chain
from query import ask_question

def main():
    PDF_DIR = "data"
    print(PDF_DIR)

    docs = load_pdf(PDF_DIR)
    split_docs = split_documents(docs, CHUNK_SIZE, CHUNK_OVERLAP)
    embeddings = get_embeddings()
    vectorstore = build_vectorstore(split_docs, embeddings, CHROMA_DIR)
    retriever = get_retriever(vectorstore)
    prompt = get_prompt()

    llm = ChatOpenAI(api_key=OPENAI_TOKEN, model="gpt-4")

    rag_chain = build_rag_chain(retriever, prompt, llm)
    ask_question(rag_chain)

if __name__ == "__main__":
    main()