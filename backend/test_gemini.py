from backend.llm.gemini import get_llm


def main():
    llm = get_llm()

    response = llm.invoke("Say hello in one sentence.")

    if hasattr(response, "text") and response.text:
        print(response.text)
    else:
        print(response.content)


if __name__ == "__main__":
    main()