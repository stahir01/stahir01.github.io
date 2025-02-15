import os
import uvicorn
from fastapi import FastAPI
from backend.Modules.Routes.chatbot import router as chatbot_router

app = FastAPI(title="Chatbot API", description="A chatbot using RAG with LLM.")

app.include_router(chatbot_router, tags=["chatbot"], prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the Chatbot API!"}



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000) 