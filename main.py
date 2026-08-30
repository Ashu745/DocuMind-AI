from modules.retrieval.retriever import Retriever
from modules.generation.generator import Generator


retriever = Retriever()
generator = Generator()

while True:


    query = input("Ask...")
    result_chunks = retriever.retrieve(
        query
    )

    final_chunks = result_chunks["documents"][0]
    sources = result_chunks["metadatas"][0]

    context = "\n\n".join(final_chunks)

    answer = generator.generate(
        context = context,
        question = query
    )


    print(answer)

    print("\nSources:")

    for source in sources:
        print(
            f"- {source['source']} "
            f"(Chunk {source['chunk_number']})"
        )

