import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



origins = [
    "§http://localhost:3000"

]



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000) 