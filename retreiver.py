import faiss
from sentence_transformers import SentenceTransformer
from model_loader import load_model

class SemanticSearch:
    def __init__(self):
        self.model = load_model()
        self.index = faiss.IndexFlatL2(384)
        self.texts = []

    def add_documents(self, docs):
        embeddings = self.model.encode(docs)
        self.index.add(embeddings)
        self.texts.extend(docs)

    def search(self, query, top_k=1):
        query_embedding = self.model.encode([query])
        _, indices = self.index.search(query_embedding, top_k)
        return [self.texts[i] for i in indices[0]]
