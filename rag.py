import os
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

model = SentenceTransformer('all-MiniLM-L6-v2')

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

def retrieve(query: str, chunks: list[str], chunk_embeddings: np.ndarray, top_k: int = 3) -> list[str]:
    query_emb = model.encode([query], convert_to_numpy=True)
    scores = np.dot(chunk_embeddings, query_emb.T).squeeze()
    top_indices = np.argsort(scores)[::-1][:top_k]
    return [chunks[i] for i in top_indices]