from typing import List
from langchain.vectorstores import Chroma
from langchain.schema import Document


def retrieve_text(vector_db: Chroma, query: str) -> List[Document]:
    """
    Retrieve text from the vector store based on the query.

    Args:
        vector_db (Chroma): ChromaDB instance.
        query (str): Query string to search for in the vector store.

    Returns:
        List[Document]: Retrieved documents from the vector store.
    """
    if not query:
        raise ValueError("Query cannot be empty.")

    # Retrieve relevant documents from the vector store
    matched_texts = vector_db.similarity_search(query, k=2)  

    return matched_texts
