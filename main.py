import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="JARVIS AI Assistant",
    description="JARVIS Backend API hosted on Render",
    version="1.0.0"
)

class PromptRequest(BaseModel):
    user_input: str

@app.get("/")
async def root():
    return {"message": "Welcome to JARVIS AI Core Backend!"}

@app.get("/health")
async def health():
    return {
        "status": "online",
        "assistant": "JARVIS"
    }

@app.post("/chat")
async def chat(request: PromptRequest):
    user_msg = request.user_input
    reply_text = f"JARVIS Received: {user_msg}. I am active and ready for your commands."
    
    return {
        "reply": reply_text,
        "status": "success"
    }
  
