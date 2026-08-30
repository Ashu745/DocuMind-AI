from modules.Embeddings.embedding_generator import EmbeddingGenerator
from modules.vector_store.chroma_store import ChromaStore

class Retriever:

    def __init__(self):

        self.embedding_generator = EmbeddingGenerator()
        self.store = ChromaStore()

    def retrieve(self , query : str , top_k : int = 3):

        query_embedding = self.embedding_generator.generate_embedding(
            query
        )

        results = self.store.search(
            query_embedding = query_embedding,
            top_k = top_k
        )
        
        return results
    
        