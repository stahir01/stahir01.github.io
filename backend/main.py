import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Modules.Routes.chatbot import router as chatbot_router

app = FastAPI(title="Chatbot API", description="A chatbot using RAG with LLM.")

app.include_router(chatbot_router, tags=["chatbot"], prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Chatbot API!"}

if __name__ == '__main__':
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)