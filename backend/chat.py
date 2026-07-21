from backend.rag.rag_chain import ask_question


def main():

    print("=" * 50)
    print("Enterprise AI Research Assistant")
    print("Type 'exit' to quit")
    print("=" * 50)

    while True:

        question = input("\nAsk: ")

        if question.lower() == "exit":
            break

        print("\nSearching documents...\n")

        answer, sources = ask_question(question)

        print("Answer:\n")
        print(answer)

        print("\nSources:")

        for source in sources:
            print(f"- {source}")


if __name__ == "__main__":
    main()