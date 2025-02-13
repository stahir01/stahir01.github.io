from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List


def split_text(pdf_docs: List[str], chunk_size: int = 500, chunk_overlap: int = 20) -> List[Document]:
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
            chunks.append(Document(page_content=chunk, metadata={"page": doc["page"]}))
    
    return chunks
    

