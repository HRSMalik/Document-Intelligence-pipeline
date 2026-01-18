import faiss
from sentence_transformers import SentenceTransformer

class SemanticSearch:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.texts = []

    def add_documents(self, docs):
        embeddings = self.model.encode(docs)
        self.index.add(embeddings)
        self.texts.extend(docs)

    def search(self, query, top_k=5):
        query_embedding = self.model.encode([query])
        _, indices = self.index.search(query_embedding, top_k)
        return [self.texts[i] for i in indices[0]]
