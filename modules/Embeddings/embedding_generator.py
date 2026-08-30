from ollama import embed

class EmbeddingGenerator:

    def __init__(self , model_name : str = "nomic-embed-text" ):
        
        self.model_name = model_name


    def generate_embedding(self , text: str) -> list[float]:

        response = embed(
            model = self.model_name,
            input = text
        )

        return response["embeddings"][0]