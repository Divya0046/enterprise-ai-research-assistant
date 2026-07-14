import shutil
import os

from langchain_chroma import Chroma
from backend.vectorstore.embeddings import get_embedding_model


def create_vector_store(chunks):

    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="./chroma_db",
    )

    return vector_store