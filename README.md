# BloomX Chatbot - NLP Service

RAG-based chatbot for the BloomX/DolphinCX self-service bot. Chunks and embeds a markdown knowledge base, retrieves relevant context, and generates responses via Groq LLM.

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv` then `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file with `GROQ_API_KEY=your_key_here`
5. Add your knowledge base as `knowledge_base.md` in the root folder
6. Run `python build_index.py` once

## Run

`uvicorn main:app`

Server runs at http://127.0.0.1:8000

## Testing

FastAPI auto-generates an interactive Swagger UI — no curl or scripts needed.

1. Go to http://127.0.0.1:8000/docs
2. Expand `POST /chat`, click **Try it out**
3. Edit the request body:
   ```json
   {"query": "what is DolphinCX"}
   ```
4. Click **Execute** and view the response below

To reset conversation history, expand `POST /reset` and click **Try it out → Execute** (no body needed).

Alternative: ReDoc (read-only view) is available at http://127.0.0.1:8000/redoc

## API

POST /chat — send a message
POST /reset — clear conversation history

Request: {"query": "your question here"}
Response: {"response": "answer from the bot"}

## Frontend

A standalone chat UI (`dolphincx-chat.html`) is included for talking to the bot without Swagger. It's a single HTML file with no build step or dependencies — just open it in a browser.

### Running it

1. Make sure the backend is running (`uvicorn main:app`) and CORS is enabled — see `main.py`:
   ```python
   from fastapi.middleware.cors import CORSMiddleware

   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```
2. Open `dolphincx-chat.html` directly in a browser (double-click), or serve it locally:
   ```
   python -m http.server 5500
   ```
   then visit http://localhost:5500/dolphincx-chat.html
3. Click the gear icon and confirm the settings match your backend:
   - **Server URL**: `http://127.0.0.1:8000`
   - **Chat endpoint**: `/chat`
   - **Reset endpoint**: `/reset`
   - **Request field name**: `query`

### Features

- Chat stream with session memory — the page sends `credentials: include` so the session cookie your backend sets is preserved across turns
- Reset button clears both the visible conversation and calls `POST /reset`
- Voice layer (Web Speech API, browser-only — no server changes needed):
  - Mic button: speech-to-text, auto-sends once you stop talking
  - Speaker icon: toggles text-to-speech for bot replies
  - Requires Chrome, Edge, or Safari — Firefox doesn't support `SpeechRecognition`
  - Mic access requires the page be served over `https://` or `localhost`; opening via `file://` may block it in some browsers
- Status indicator in the header pings the server root so connection issues are visible at a glance

## Configuring for remote access

By default, both the backend and frontend only work on the same machine (`127.0.0.1`/`localhost`). To let someone else — a teammate, mentor, or another device — reach the bot, you need to do two things: expose the server beyond localhost, and point the frontend at that new address.

### 1. Expose the backend

**Option A — same network (LAN)**

Run uvicorn bound to all interfaces instead of just localhost:
```
uvicorn main:app --host 0.0.0.0 --port 8000
```
Anyone on the same Wi-Fi/network can then reach it at `http://<your-machine's-local-IP>:8000` (find your IP with `ipconfig` on Windows or `ifconfig`/`ip a` on Mac/Linux). You may also need to allow port 8000 through your firewall.

**Option B — public internet (tunnel)**

For access from outside your network without port-forwarding, use a tunneling tool. Two common options:

- **ngrok**:
  ```
  ngrok http 8000
  ```
  This gives you a public URL like `https://abcd1234.ngrok-free.app` that forwards to your local server.

- **Cloudflare Tunnel** (`cloudflared`):
  ```
  cloudflared tunnel --url http://localhost:8000
  ```
  This gives you a public `https://*.trycloudflare.com` URL. (Not currently wired into this project — this is the manual command if you want to try it standalone.)

Either way, keep `uvicorn main:app` running normally on `127.0.0.1:8000` — the tunnel just forwards to it, no `--host 0.0.0.0` needed for this option.

### 2. Update CORS

If you tunnel or expose the server publicly, tighten `allow_origins` from `["*"]` to the actual origin(s) the frontend will be served from, especially if `allow_credentials=True` (required for session cookies to work) — browsers reject wildcard origins combined with credentials in practice. Example:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-tunnel-url.ngrok-free.app", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 3. Point the frontend at the new address

Open `dolphincx-chat.html`, click the gear icon, and set **Server URL** to whatever address you exposed:
- LAN: `http://<local-IP>:8000`
- Tunnel: `https://abcd1234.ngrok-free.app` (or your `trycloudflare.com` URL)

If you're also serving the HTML file itself remotely (not just opening it locally), make sure that origin is included in `allow_origins` too.

### Notes on session cookies over a tunnel

Cookie-based session memory relies on `credentials: include` on the frontend and a matching `Set-Cookie` from the backend. Over HTTPS tunnels this generally works out of the box; over plain HTTP LAN access, some browsers restrict cross-origin cookies more aggressively — if session memory stops working after exposing the server, that's the first thing to check.

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
