# handles embedding logic.
class EmbeddingService:
    def __init__(self, model_type="sentence-transformers/all-mpnet-base-v2"):
        self.model_type = model_type
        print("Using embedding model: " + self.model_type)
        pass

    def embed_text(self, text):
        # implement embedding model logic here,
        # return the embedding vector for storage, or query.
        return f"embedding vector for: {text}"