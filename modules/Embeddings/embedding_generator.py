from ollama import Client


class EmbeddingGenerator:
    def __init__(self, model_name: str = "nomic-embed-text"):
        self.model_name = model_name
        self.client = Client(host = "http://host.docker.internal:11434")

    def generate_embedding(self, text: str) -> list[float]:
        response = self.client.embed(
            model=self.model_name, 
            input=text
        )

        return response["embeddings"][0]
