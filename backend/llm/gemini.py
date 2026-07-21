import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from backend.config import GEMINI_MODEL, TEMPERATURE

load_dotenv()


def get_llm():

    return ChatGoogleGenerativeAI(
       model=GEMINI_MODEL,
       temperature=TEMPERATURE,
    )