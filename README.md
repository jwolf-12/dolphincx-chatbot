# BloomX Chatbot - NLP Service

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

## Testing

Using curl:

`curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d "{\"query\": \"what is DolphinCX\"}"`

Using Python:

`import requests`
`requests.post("http://127.0.0.1:8000/chat", json={"query": "what is DolphinCX"}).json()`

To reset conversation history:

`curl -X POST http://127.0.0.1:8000/reset`

## API

POST /chat — send a message
POST /reset — clear conversation history

Request: {"query": "your question here"}
Response: {"response": "answer from the bot"}

## Notes
- Knowledge base is chunked by ## headers
- Top 3 most relevant chunks are retrieved per query
- Conversation history is maintained per server session
- Replace GROQ_API_KEY with your own key from console.groq.com

## Stack
- FastAPI
- Groq (llama-3.1-8b-instant)
- sentence-transformers (all-MiniLM-L6-v2)
- numpy