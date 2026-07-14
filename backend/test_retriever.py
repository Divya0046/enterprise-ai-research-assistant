from backend.rag.retriever import get_retriever

retriever = get_retriever()

query = input("Ask a question: ")

results = retriever.invoke(query)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(results):
    print("=" * 60)
    print(f"Result {i+1}")
    print("=" * 60)
    print(doc.page_content)