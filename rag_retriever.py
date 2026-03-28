from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load data
with open("knowledge_base.json") as f:
    docs = json.load(f)

texts = [d['text'] for d in docs]
embeddings = model.encode(texts)

# FAISS index
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

def retrieve(query):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k=2)
    return [texts[i] for i in I[0]]