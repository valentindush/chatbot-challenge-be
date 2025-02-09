from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import AsyncIterable
from langchain_groq import ChatGroq # we can easily replaced this with langchain openai (but i've utilized all my free tokens... so i used free model)
from langchain.schema import AIMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = ChatGroq(streaming=True)
chat_history = []

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    success: bool
    message: str
    data: dict

async def chat_stream(prompt: str) -> AsyncIterable[str]:
    global chat_history
    chat_history.append(HumanMessage(content=prompt))
    
    full_response = ""
    async for chunk in llm.astream(chat_history):
        content = chunk.content
        full_response += content
        yield content 
    
    chat_history.append(AIMessage(content=full_response))

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")

    return StreamingResponse(
        chat_stream(request.prompt),
        media_type="text/plain"  # Use text/plain instead of SSE
    )