import chromadb
from typing import Any
import streamlit as st
class ChromaStore:

    def __init__(self , collection_name : str = "rag_documents"):
        
        self.collection_name = collection_name

        self.client = chromadb.PersistentClient(
            path = "./chromadb"
        )


        self.collection = self.client.get_or_create_collection(
            name = collection_name
        )


    def add_document(self , doc_id : str , text : str , embedding : list[float] , metadata : dict[str , Any]):

        self.collection.add(
            ids = [doc_id],
            documents = [text],
            embeddings = [embedding],
            metadatas = [metadata]
        )

    def get_count(self):
        return self.collection.count()
    

    def search(self , query_embedding: list[float] , top_k = 3):
        
        results = self.collection.query(
            query_embeddings = [query_embedding],
            n_results = top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        return results