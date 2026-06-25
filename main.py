import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from rag import load_chunks, embed, retrieve
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MD_PATH = "knowledge_base.md"  # rename your markdown file to this
chunks = load_chunks(MD_PATH)
chunk_embeddings = embed(chunks)

class Message(BaseModel):
    query: str

@app.post("/chat")
def chat(msg: Message):
    context = retrieve(msg.query, chunks, chunk_embeddings)
    context_str = "\n\n".join(context)
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful assistant for BloomX. Keep the answers precise and follow a guidance tone, ask questions if necessary. Answer only based on the following documentation:\n\n{context_str}"
            },
            {
                "role": "user",
                "content": msg.query
            }
        ]
    )
    return {"response": response.choices[0].message.content}