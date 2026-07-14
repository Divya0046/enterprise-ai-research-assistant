from backend.llm.gemini import get_llm
from backend.rag.retriever import get_retriever
from backend.prompts.prompt import RAG_PROMPT

retriever = get_retriever()
llm = get_llm()
def ask_question(question: str):


    docs = retriever.invoke(question)
    print("\n" + "=" * 60)
    print("Retrieved Chunks")
    print("=" * 60)

    for i, doc in enumerate(docs, start=1):
        print(f"\nChunk {i}")
        print("-" * 30)
        print(doc.page_content[:400])
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = RAG_PROMPT.format(
    context=context,
    question=question
)
    

    response = llm.invoke(prompt)

    # Gemini 3.x returns structured content
    if hasattr(response, "text") and response.text:
        return response.text

    # Fallback
    if isinstance(response.content, list):
        return "".join(
            item.get("text", "")
            for item in response.content
            if isinstance(item, dict)
        )

    return str(response.content)