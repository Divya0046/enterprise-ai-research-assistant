from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.config import CHUNK_SIZE, CHUNK_OVERLAP
from pathlib import Path


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
       chunk_size=CHUNK_SIZE,
       chunk_overlap=CHUNK_OVERLAP,
       length_function=len,
    )

    chunks = splitter.split_documents(documents)

    for i, chunk in enumerate(chunks):

        chunk.metadata["chunk_id"] = i + 1

        source = Path(chunk.metadata["source"]).name

        chunk.metadata["document"] = source

    return chunks




    