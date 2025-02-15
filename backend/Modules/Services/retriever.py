import os
from typing import List, Optional
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.Modules.config import MINI_LM_EMBED

DEFAULT_EMBED_MODEL = MINI_LM_EMBED


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

    embedding_model = HuggingFaceEmbeddings(model_name=embed_model, show_progress=True)
    

    # Initialize ChromaDB with the same embedding model used for storing
    vector_db = Chroma(
        collection_name=collection_name,
        embedding_function=embedding_model,
        persist_directory=vectordb_path
        )

    # Retrieve relevant documents from the vector store
    matched_texts = vector_db.similarity_search(query, k=7)  

    return matched_texts
