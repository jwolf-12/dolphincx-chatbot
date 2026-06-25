# DolphinCX Chatbot

RAG-based chatbot for the BloomX/DolphinCX self-service bot. Chunks and embeds a markdown knowledge base, retrieves relevant context, and generates responses via Groq LLM.

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv` then `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file with `GROQ_API_KEY=your_key_here`
5. Add your knowledge base as `knowledge_base.md` in the root folder

## Run

`uvicorn main:app --reload`

Server runs at http://127.0.0.1:8000

## API

POST /chat

Request: {"query": "what is DolphinCX"}
Response: {"response": "DolphinCX is ..."}

## Stack
- FastAPI
- Groq (llama-3.1-8b-instant)
- sentence-transformers (all-MiniLM-L6-v2)
- numpy
