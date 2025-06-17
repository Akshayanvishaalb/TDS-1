'''import requests

resp = requests.post("http://localhost:11434/api/embeddings", json={
    "model": "nomic-embed-text",
    "prompt": "This is a test."
})
print(resp.status_code, resp.text)'''
#**********************************************************************************
''''import os
import pickle

CHUNKS_FOLDER = "chunks"
metadata = {}
current_id = 0

for filename in os.listdir(CHUNKS_FOLDER):
    if filename.endswith(".md"):
        filepath = os.path.join(CHUNKS_FOLDER, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read().strip()
            if text:
                metadata[current_id] = text
                current_id += 1

# Save metadata
with open("metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)
'''
#**************************************************************************************************
'''
import faiss
import numpy as np
import json

# Paths
faiss_index_path = "faiss_index.bin"
metadata_path = "chunk_metadata.json"
npz_output_path = "embeddings.npz"
json_output_path = "embeddings_metadata.json"

def convert_faiss_to_npz():
    try:
        # Load FAISS index
        print("Loading FAISS index...")
        index = faiss.read_index(faiss_index_path)
        
        # Extract all embeddings
        print("Extracting embeddings...")
        embeddings = index.reconstruct_n(0, index.ntotal)
        print(f"Total embeddings: {len(embeddings)}")
        
        # Save to .npz
        print(f"Saving to {npz_output_path}...")
        np.savez_compressed(npz_output_path, embeddings=embeddings)

        # Copy metadata to a new file
        print("Copying metadata...")
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        
        with open(json_output_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        print("✅ Conversion completed successfully.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    convert_faiss_to_npz()
'''

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import faiss
import requests
import json
import os

# === Config ===
OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings/"  # Trailing slash to prevent redirect
FAISS_INDEX_PATH = "faiss_index.bin"
METADATA_PATH = "chunk_metadata.json"
CHUNKS_DIR = "chunks"

# === Load FAISS index and metadata ===
index = faiss.read_index(FAISS_INDEX_PATH)
with open(METADATA_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)

# === Initialize FastAPI ===
app = FastAPI()

# === Request Model ===
class QueryRequest(BaseModel):
    question: str

# === Embedding Function using Ollama ===
def embed_query(text: str) -> np.ndarray:
    response = requests.post(
        OLLAMA_EMBED_URL,
        json={"model": "nomic-embed-text", "prompt": text}
    )
    response.raise_for_status()
    embedding = np.array(response.json()["embedding"], dtype=np.float32)
    return embedding.reshape(1, -1)

# === Main Route ===
@app.post("/query")
def query_api(data: QueryRequest):
    try:
        # 1. Get embedding
        query_vector = embed_query(data.question)

        # 2. Search in FAISS
        distances, indices = index.search(query_vector, k=1)
        idx = indices[0][0]
        distance = distances[0][0]

        if idx < 0 or idx >= len(metadata):
            return {"error": "No valid match found."}

        # 3. Load metadata + content
        result = metadata[idx]
        chunk_path = os.path.join(CHUNKS_DIR, result["file"])
        with open(chunk_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 4. Return result
        return {
            "question": data.question,
            "top_match": {
                "file": result["file"],
                "post_url": result["post_url"],
                "similarity_score": float(1 / (1 + distance)),  # Inverted distance
                "content_preview": content[:300] + "..."
            }
        }

    except Exception as e:
        return {"error": str(e)}
