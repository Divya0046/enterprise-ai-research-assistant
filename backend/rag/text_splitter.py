from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split LangChain Document objects into smaller chunks.  
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
    )

    chunks = text_splitter.split_documents(documents)

    return chunks
    