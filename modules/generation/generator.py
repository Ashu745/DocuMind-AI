from ollama import chat

class Generator:

    def generate(self , context : str , question : str) -> str:
        
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
        response = chat(
            model = "qwen3:4b",
            messages = [
                {
                    "role" : "user",
                    "content" : prompt
                }
            ]
        )


        return response["message"]["content"]