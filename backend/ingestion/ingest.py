import os
import shutil
from pathlib import Path


from backend.loaders.pdf_loader import load_pdf
from backend.rag.text_splitter import split_documents
from backend.vectorstore.vector_store import create_vector_store
from backend.utils.logger import logger

def ingest_documents():

    documents_dir = Path("documents")

    all_docs = []

    pdf_files = list(documents_dir.glob("*.pdf"))

    logger.info(f"Loaded {len(pdf_files)} PDF(s)")

    for pdf in pdf_files:
        docs = load_pdf(str(pdf))
        all_docs.extend(docs)

    chunks = split_documents(all_docs)

    logger.info(f"Created {len(chunks)} chunks")

    if len(chunks) == 0:
        print("No documents found. Skipping vector store creation.")
        return

        print("No documents left. Vector database deleted.")
        return

    create_vector_store(chunks)

    logger.info("Vector database created successfully.")

if __name__ == "__main__":
    ingest_documents()