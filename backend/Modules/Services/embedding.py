"""
This module is responsible for:
    - Converting extracted features into vector embeddings.
    - Storing and retrieving embeddings from a vector database.
    - Performing similarity searches or retrieval for relevant information.
"""

import os
from typing import List, Optional, Tuple
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings
from config import (
    OPENAI_API_KEY,
    MINI_LM_EMBED,
    VECTOR_DB_PATH
)

DEFAULT_EMBED_MODEL = MINI_LM_EMBED

# Define default embedding model
DEFAULT_EMBED_MODEL = MINI_LM_EMBED

def generate_embedding(
        docs: List[Document], 
        embed_model: Optional[str] = None
    ) -> Tuple[List[List[float]], List[str], List[dict]]:
    """
    Generate embeddings for a list of text chunks using Hugging Face.

    Args:
        docs (List[Document]): List of documents to embed.
        embed_model (Optional[str]): Name of the Hugging Face embedding model.

    Returns:
        Tuple[List[List[float]], List[str]]: 
        - List of embedding vectors (floats).
        - List of text chunks corresponding to the embeddings.
    """

    if embed_model is None:
        embed_model = DEFAULT_EMBED_MODEL

    embedding_model = HuggingFaceEmbeddings(model_name=embed_model, show_progress=True)

    text_chunks = [doc.page_content for doc in docs]
    metadata = [doc.metadata for doc in documents]

    embeddings = embedding_model.embed_documents(text_chunks)

    return embeddings, text_chunks, metadata
