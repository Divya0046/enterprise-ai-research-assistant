from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from backend.rag.text_splitter import split_documents
from backend.vectorstore.vector_store import create_vector_store


def load_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    return loader.load()


if __name__ == "__main__":

    pdf_path = Path(__file__).resolve().parents[2] / "documents" / "ManitDivyaRairesume.pdf"

    docs = load_pdf(str(pdf_path))

    print(f"Pages: {len(docs)}")

    chunks = split_documents(docs)

    vector_db = create_vector_store(chunks)

    print("Vector database created successfully.")
    print(f"Total Chunks: {len(chunks)}")

    print("\nFirst Chunk:\n")
    for i, chunk in enumerate(chunks):
        print("=" * 60)
        print(f"Chunk {i+1}")
        print("=" * 60)
        print(chunk.page_content)
        print("\nMetadata:")
        print(chunk.metadata)

    print("\nMetadata:\n")
    print(chunks[0].metadata)