from fastapi import APIRouter, HTTPException
from backend.Modules.Services.retriever import retrieve_text
from backend.Modules.Services.llm_inference import Chatbot
from backend.Modules.config import DEEPSEEK_MODEL, HUGGINGFACE_KEY
from typing import Dict

router = APIRouter()

chatbot_model = Chatbot(model_name=DEEPSEEK_MODEL, api_token=HUGGINGFACE_KEY)

@router.get("/retrieve")
async def generate_response(query: str) -> Dict:
    """
    Retrieves relevant information from the vector store and generates a response using the LLM.
    
    Args:
        query (str): The user query.
    
    Returns:
        Dict: AI-generated response with metadata.
    """
    if not query:
        raise HTTPException(status_code=400, detail="❌ Query cannot be empty.")
    
    # Retrieve relevant documents
    retrieved_docs = retrieve_text("backend/Modules/vector_store/chromadb", query)

    if not retrieved_docs:
        return {"answer": "⚠️ No relevant answer found.", "metadata": "N/A"}

    # Merge retrieved content
    retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

    # Generate LLM response
    response = chatbot_model.generate_text(query, retrieved_text)  # ✅ Fixed spelling mistake

    return {"answer": response}
