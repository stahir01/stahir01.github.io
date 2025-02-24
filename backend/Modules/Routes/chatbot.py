from fastapi import APIRouter, HTTPException
from Modules.Services.retriever import retrieve_text
from Modules.Services.llm_inference import Chatbot
from Modules.config import DEEPSEEK_MODEL, HUGGINGFACE_KEY
from typing import Dict, List
from pydantic import BaseModel

router = APIRouter()

chatbot_model = Chatbot(model_name=DEEPSEEK_MODEL, api_token=HUGGINGFACE_KEY)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    conversation: List[Message] 

@router.post("/chat")
async def generate_chat_response(request: ChatRequest) -> Dict:
    """
    Accepts a conversation history, retrieves relevant context from the vector store,
    and generates a new response using the LLM.
    
    The conversation should be an array of messages with roles ("user" or "assistant").
    The assistant will generate a reply based on the last user message.
    """
    conversation = request.conversation
    if not conversation or conversation[-1].role != "user":
        raise HTTPException(status_code=400, detail="The last message must be from the user.")

    # Use the last user message as the current query
    query = conversation[-1].content

    retrieved_docs = retrieve_text("Modules/vector_store/chromadb", query)
    
    context = "\n".join([doc.page_content for doc in retrieved_docs]) if retrieved_docs else ""

    response_text = chatbot_model.generate_text(query, context)
    
    return {"role": "assistant", "content": response_text}
