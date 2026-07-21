from backend.llm.gemini import get_llm
from backend.rag.retriever import get_retriever


def ask_question(question: str):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)
    
    prompt = f"""
You are an Enterprise AI Research Assistant.

Use both the conversation history and the retrieved context to answer the user's question.

If the answer is not available in the context, reply:

"I couldn't find that information."

Context:
{context}

Question:
{question}

Answer:
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    if hasattr(response, "text") and response.text:
        answer = response.text
    elif isinstance(response.content, list):
        answer = "".join(
            item.get("text", "")
            for item in response.content
            if isinstance(item, dict)
        )
    else:
        answer = str(response.content)

    sources = []

    for doc in docs:

        filename = doc.metadata.get("filename", "Unknown")
        
        page = doc.metadata.get("page", 0) + 1

        source = f"{filename} (Page {page})"

        if source not in sources:
            sources.append(source)

    
    return answer, sources