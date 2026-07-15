"""
Run this manually whenever knowledge_base.md changes:

    python build_index.py

It (re)builds the Qdrant collection from scratch. main.py never re-embeds
anything at startup — it just opens the collection this script wrote.

IMPORTANT: stop the FastAPI server before running this (local-mode Qdrant
locks the storage directory to one process at a time), then restart the
server afterwards to pick up the new index.
"""
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from rag import load_chunks, embed, get_client, QDRANT_PATH, COLLECTION_NAME, VECTOR_SIZE

MD_PATH = "knowledge_base.md"


def build():
    print(f"Loading chunks from {MD_PATH} ...")
    chunks = load_chunks(MD_PATH)
    print(f"  -> {len(chunks)} chunks")

    print("Embedding chunks ...")
    embeddings = embed(chunks)

    client = get_client()

    print(f"(Re)creating collection '{COLLECTION_NAME}' ...")
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
    )

    points = [
        PointStruct(id=i, vector=embeddings[i].tolist(), payload={"text": chunk})
        for i, chunk in enumerate(chunks)
    ]
    client.upsert(collection_name=COLLECTION_NAME, points=points)

    print(f"Indexed {len(points)} chunks into '{QDRANT_PATH}'. Done.")


if __name__ == "__main__":
    build()