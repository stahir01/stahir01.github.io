from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List

"""
It is a good idea to use a small chunk size for tasks that require a fine-grained view of the text and a larger chunk size 
for tasks that require a more holistic view of the text.

Since we want a more Holistic view as it's better for chatbot Q/A
"""

def split_text(pdf_docs: List[str], chunk_size: int = 100, chunk_overlap: int = 20) -> List[Document]:
    """
    Splits text into chunks for efficient embedding.
    
    - `chunk_size`: Max characters per chunk.
    - `chunk_overlap`: Overlap between chunks for better context retention.
    
    Returns a list of text chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )

    chunks = []
    for page_text in pdf_docs:
        split_chunks = text_splitter.split_text(page_text)
        for chunk in split_chunks:
            chunks.append(Document(page_content=chunk))
    
    return chunks
    

