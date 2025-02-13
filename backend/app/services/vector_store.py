import os
import logging
from typing import List
from langchain.vectorstores import Chroma

# Define the storage path for ChromaDB
VECTOR_DB_PATH = "vector_store/chroma_db"

def store_embeddings(
        embeddings: List[List[float]], 
        text_chunks: List[str], 
        metadata: List[dict], 
        collection_name: str = "chromadb"
    ) -> None:
    """
    Stores precomputed embeddings and corresponding text chunks in ChromaDB.

    Args:
        embeddings (List[List[float]]): List of embedding vectors.
        text_chunks (List[str]): List of text chunks corresponding to embeddings.
        collection_name (str): Name of the ChromaDB collection.
    """

    # Ensure the storage directory exists
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    # Initialize ChromaDB instance
    db = Chroma(
        collection_name=collection_name,
        persist_directory=VECTOR_DB_PATH
    )

    # Store the embeddings and text in ChromaDB
    db.add_texts(texts=text_chunks, metadatas=metadata, embeddings=embeddings)
    db.persist()  # Save to disk

    logging.info(f"✅ Stored {len(text_chunks)} text chunks in ChromaDB (Collection: {collection_name})")
