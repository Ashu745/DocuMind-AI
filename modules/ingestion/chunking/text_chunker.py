from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextChunker:

    def __init__(self , chunk_size: int = 500 , chunk_overlap: int = 100):
        
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def create_chunks(self , text : str ) -> list[str]:
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = self.chunk_size,
            chunk_overlap = self.chunk_overlap
        )

        chunks = splitter.split_text(text)

        return chunks
    