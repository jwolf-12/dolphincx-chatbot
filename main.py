import os
import uuid
from collections import defaultdict
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from rag import retrieve, get_client, collection_exists, COLLECTION_NAME
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.com"],  # replace with your actual frontend origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Connect to the already-built Qdrant index. This is just opening a file store
# — no embedding computation happens here, so startup is fast. If you've
# changed knowledge_base.md, run `python build_index.py` first (with the
# server stopped) to rebuild it.
qdrant_client = get_client()
if not collection_exists(qdrant_client):
    raise RuntimeError(
        f"Qdrant collection '{COLLECTION_NAME}' not found. "
        "Run `python build_index.py` once before starting the server."
    )

# --- Session memory ---
MAX_TURNS = 6  # number of user+assistant turn pairs to keep per session
SESSION_COOKIE_NAME = "dolphincx_session_id"
SESSION_MAX_AGE = 60 * 60 * 24  # 1 day, in seconds

sessions: dict[str, list[dict]] = defaultdict(list)

# how many recent turns to show the rephraser (keep small — this is a cheap/fast call)
REPHRASE_HISTORY_TURNS = 3


class Message(BaseModel):
    query: str


def get_or_create_session_id(request: Request, response: Response) -> str:
    session_id = request.cookies.get(SESSION_COOKIE_NAME)
    if not session_id:
        session_id = str(uuid.uuid4())
        response.set_cookie(
            key=SESSION_COOKIE_NAME,
            value=session_id,
            max_age=SESSION_MAX_AGE,
            httponly=True,
            samesite="none",
            secure=True,
        )
    return session_id


def rephrase_query(query: str, history: list[dict]) -> str:
    """Rewrite the query as a standalone question using recent chat history,
    so retrieval doesn't break on pronouns / follow-ups like 'what about that?'."""
    if not history:
        return query  # nothing to disambiguate against on the first turn

    recent = history[-(REPHRASE_HISTORY_TURNS * 2):]
    history_str = "\n".join(f"{turn['role']}: {turn['content']}" for turn in recent)

    prompt = (
        "Given the conversation history and a follow-up query, rewrite the query "
        "as a standalone question that contains all necessary context and can be "
        "understood without the history. Do not answer the question. If the query "
        "is already standalone, return it unchanged. Return ONLY the rewritten "
        "query text, nothing else.\n\n"
        f"Conversation history:\n{history_str}\n\n"
        f"Follow-up query: {query}\n\n"
        "Standalone query:"
    )

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=100,
        )
        rewritten = completion.choices[0].message.content.strip()
        return rewritten if rewritten else query
    except Exception:
        # if rephrasing fails for any reason, fall back to the raw query
        # rather than breaking the whole /chat request
        return query


@app.post("/chat")
def chat(msg: Message, request: Request, response: Response):
    session_id = get_or_create_session_id(request, response)
    history = sessions[session_id]

    standalone_query = rephrase_query(msg.query, history)

    context = retrieve(standalone_query, qdrant_client)
    context_str = "\n\n".join(context)

    system_prompt = {
        "role": "system",
        "content": (
            "You are a helpful assistant for DolphinCX. Make sure no one realises "
            "you're working with an internal documentation. Keep the answers precise "
            "and follow a guidance tone, ask questions if necessary. Answer only "
            f"based on the following documentation:\n\n{context_str}"
        ),
    }

    messages = [system_prompt] + history + [{"role": "user", "content": msg.query}]

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
    )

    reply = completion.choices[0].message.content

    history.append({"role": "user", "content": msg.query})
    history.append({"role": "assistant", "content": reply})
    sessions[session_id] = history[-(MAX_TURNS * 2):]

    return {"response": reply, "debug_standalone_query": standalone_query}


@app.post("/reset")
def reset(request: Request, response: Response):
    session_id = request.cookies.get(SESSION_COOKIE_NAME)
    if session_id:
        sessions.pop(session_id, None)
        response.delete_cookie(SESSION_COOKIE_NAME)
    return {"status": "reset"}