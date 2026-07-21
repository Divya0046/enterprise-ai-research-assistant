from langchain_chroma import Chroma

from backend.config import CHROMA_DB_PATH, TOP_K
from backend.vectorstore.embeddings import get_embedding_model

_retriever = None


def get_retriever():
    global _retriever

    if _retriever is None:

        embedding_model = get_embedding_model()

        vector_store = Chroma(
            persist_directory=CHROMA_DB_PATH,
            embedding_function=embedding_model,
        )

        _retriever = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": TOP_K},
        )

    return _retriever