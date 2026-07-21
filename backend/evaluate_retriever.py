from backend.rag.retriever import get_retriever

questions = [
    "What is Divya's M.Tech CGPA?",
    "What projects are mentioned in the resume?",
    "What technologies are used in the Enterprise AI Research Assistant?",
    "What experience does Divya have?",
    "What certifications are listed?"
]

retriever = get_retriever()

for question in questions:
    print("=" * 80)
    print("QUESTION:")
    print(question)

    docs = retriever.invoke(question)

    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(docs):
        print(f"Chunk {i+1}")
        print("-" * 40)
        print(doc.page_content[:300])
        print()