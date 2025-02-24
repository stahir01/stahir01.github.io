import os
from typing import List, Optional
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from Modules.config import MINI_LM_EMBED, OPENAI_EMBED, OPENAI_KEY

DEFAULT_EMBED_MODEL = OPENAI_EMBED


def retrieve_text(
        vectordb_path: str, 
        query: str, 
        embed_model: Optional[str] = None,
        collection_name: str = "chromadb") -> List[Document]:
    """
    Retrieve text from the vector store based on the query.

    Args:
        vector_db (Chroma): ChromaDB instance.
        query (str): Query string to search for in the vector store.

    Returns:
        List[Document]: Retrieved documents from the vector store.
    """
    if not os.path.exists(vectordb_path):
        raise FileNotFoundError(f"Vector store not found at: {vectordb_path}")
        
    if not query:
        raise ValueError("Query cannot be empty.")
    
    if embed_model is None:
        embed_model = DEFAULT_EMBED_MODEL

    embedding_model = OpenAIEmbeddings(model=embed_model, api_key=OPENAI_KEY)


    vector_db = Chroma(
        collection_name=collection_name,
        embedding_function=embedding_model,
        persist_directory=vectordb_path
        )

    matched_texts = vector_db.similarity_search(query, k=2)  

    return matched_texts
