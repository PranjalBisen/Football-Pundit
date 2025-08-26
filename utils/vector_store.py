import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self, dimension=384, k=5):
        self.dimension = dimension
        self.k = k
        self.index = faiss.IndexFlatL2(dimension)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.data = []  
    
    def add(self, text: str):
        """Add text to FAISS index"""
        embedding = self.model.encode([text])
        self.index.add(np.array(embedding, dtype="float32"))
        self.data.append(text)
    
    def retrieve(self, query: str):
        """Retrieve top-k similar texts"""
        if len(self.data) == 0:
            return []
        embedding = self.model.encode([query])
        distances, indices = self.index.search(
            np.array(embedding, dtype="float32"), self.k
        )
        return [self.data[i] for i in indices[0] if i < len(self.data)]