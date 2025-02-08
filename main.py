from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import AsyncIterable
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Initialize the Groq chat model
llm = ChatGroq(streaming=True)

# Message history
chat_history = []

# Response schema
class ChatResponse(BaseModel):
    success: bool
    message: str
    data: dict

async def chat_stream(prompt: str) -> AsyncIterable[str]:
    """Streams chatbot responses."""
    global chat_history
    chat_history.append(HumanMessage(content=prompt))
    
    async for chunk in llm.astream(chat_history):
        yield chunk.content
    
    chat_history.append(AIMessage(content=chunk.content))

@app.post("/chat", response_model=ChatResponse)
async def chat(prompt: str):
    """Handles chatbot messages with streaming."""
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    
    return StreamingResponse(
        chat_stream(prompt),
        media_type="text/event-stream"
    )
