from langchain_huggingface import HuggingFaceEmbeddings

from backend.config import EMBEDDING_MODEL

_embedding_model = None


def get_embedding_model():
    global _embedding_model

    if _embedding_model is None:
        print("Loading embedding model...")
        _embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

    return _embedding_model