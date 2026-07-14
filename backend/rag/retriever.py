from langchain_chroma import Chroma
from backend.vectorstore.embeddings import get_embedding_model


def get_retriever():

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding_model,
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 10,
        },
    )

    return retriever