from modules.ingestion.pdf_reader import PDFReader
from modules.ingestion.chunking.text_chunker import TextChunker
from modules.Embeddings.embedding_generator import EmbeddingGenerator
from modules.vector_store.chroma_store import ChromaStore
import os


def ingest_pdf(pdf_path):
    reader = PDFReader()

    chunker = TextChunker(
        chunk_size=500,
        chunk_overlap=100
    )

    generator = EmbeddingGenerator()
    store = ChromaStore()

    pdf_file = os.path.basename(pdf_path)

    print("PROCESSING:", pdf_file)

    text = reader.extract_text(pdf_path)

    chunks = chunker.create_chunks(text)

    for index, chunk in enumerate(chunks):

        embedding = generator.generate_embedding(chunk)

        store.add_document(
            doc_id=f"{pdf_file}_chunk_{index}",
            text=chunk,
            embedding=embedding,
            metadata={
                "source": pdf_file,
                "chunk_number": index
            }
        )

    print("COUNT:", store.get_count())
    print("Ingestion Complete")
    print(f"Total Chunks: {len(chunks)}")

    return len(chunks)