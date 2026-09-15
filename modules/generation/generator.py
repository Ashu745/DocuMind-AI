from ollama import chat
from ollama import Client


class Generator:

    def __init__(self):
        self.client = Client(host="http://host.docker.internal:11434")

    def generate(self, context: str, question: str) -> str:
        prompt = f"""
You are a helpful AI assistant.

Use the provided context to answer the question.

If the answer is not present in the context, say:
"I could not find the answer in the provided context."


Context:
{context}

Question:
{question}
"""
        response = self.client.chat(
            model="qwen3:4b", messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]
