import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv


app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="This is the Langhchain server to interact with chatbot"
    )




origins = [
    "§http://localhost:3000"

]



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000) 