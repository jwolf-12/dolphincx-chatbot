import os
import numpy as np
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from dotenv import load_dotenv

load_dotenv()

model = SentenceTransformer('all-MiniLM-L6-v2')

# Local, on-disk Qdrant — no server to run. Same folder is used by build_index.py
# (to write the index) and main.py (to read it).
QDRANT_PATH = os.getenv("QDRANT_PATH", "./qdrant_storage")
COLLECTION_NAME = "dolphincx_knowledge"
VECTOR_SIZE = 384  # all-MiniLM-L6-v2 output dim


def load_chunks(md_path: str) -> list[str]:
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    chunks = []
    current = []
    for line in content.split('\n'):
        if line.startswith('## ') and current:
            chunks.append('\n'.join(current).strip())
            current = [line]
        else:
            current.append(line)
    if current:
        chunks.append('\n'.join(current).strip())
    return [c for c in chunks if c]


def embed(texts: list[str]) -> np.ndarray:
    return model.encode(texts, convert_to_numpy=True)


def get_client() -> QdrantClient:
    """Opens the local Qdrant store. NOTE: local-mode Qdrant file-locks the
    directory, so only one process (either main.py OR build_index.py, not both
    at once) can hold it open at a time. Stop the FastAPI server before
    running build_index.py, then restart it after."""
    return QdrantClient(path=QDRANT_PATH)


def collection_exists(client: QdrantClient) -> bool:
    return client.collection_exists(COLLECTION_NAME)


def retrieve(query: str, client: QdrantClient, top_k: int = 3) -> list[str]:
    query_emb = model.encode(query, convert_to_numpy=True).tolist()
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_emb,
        limit=top_k,
    ).points
    return [point.payload["text"] for point in results]