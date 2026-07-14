from backend.rag.rag_chain import ask_question


def main():

    print("=" * 50)
    print("Enterprise AI Research Assistant")
    print("Type 'exit' to quit")
    print("=" * 50)

    while True:

        question = input("\nAsk: ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        print("\nSearching documents...")

        answer = ask_question(question)

        print("\nAI:\n")
        print(answer)


if __name__ == "__main__":
    main()