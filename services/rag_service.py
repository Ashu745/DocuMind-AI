from modules.retrieval.retriever import Retriever
from modules.generation.generator import Generator

retriever = Retriever()
generator = Generator()


def ask_question(question):
    result_chunks = retriever.retrieve(
        question
    )

    final_chunks = result_chunks["documents"][0]
    sources = result_chunks["metadatas"][0]

    context = "\n\n".join(final_chunks)

    answer = generator.generate(
        context = context,
        question = question
    )

    for source in sources:
        print(
            f"- {source['source']} "
            f"(Chunk {source['chunk_number']})"
        )

    return answer, sources