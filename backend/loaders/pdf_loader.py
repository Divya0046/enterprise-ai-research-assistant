from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    for doc in docs:
        doc.metadata["filename"] = Path(pdf_path).name
    print(docs[0].metadata)


    return docs