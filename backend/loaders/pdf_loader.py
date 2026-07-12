from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from backend.rag.text_splitter import split_documents


def load_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    return loader.load()


if __name__ == "__main__":

    pdf_path = Path(__file__).resolve().parents[2] / "documents" / "ManitDivyaRairesume.pdf"

    docs = load_pdf(str(pdf_path))

    print(f"Pages: {len(docs)}")

    chunks = split_documents(docs)

    print(f"Total Chunks: {len(chunks)}")

    print("\nFirst Chunk:\n")
    print(chunks[0].page_content)

    print("\nMetadata:\n")
    print(chunks[0].metadata)