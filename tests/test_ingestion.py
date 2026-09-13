from modules.ingestion.chunking.text_chunker import TextChunker

def test_chunk_creation():

    chunker = TextChunker(
        chunk_size=100,
        chunk_overlap=20
    )

    chunks = chunker.create_chunks(
        "Hello world " * 100
    )

    assert len(chunks) > 0