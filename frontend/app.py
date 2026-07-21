import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Enterprise AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise AI Research Assistant")

# -------------------------
# Upload PDF
# -------------------------

st.header("📄 Upload Document")

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            "application/pdf"
        )
    }

    if st.button("Upload"):

        response = requests.post(
            f"{API_URL}/upload",
            files=files
        )

        if response.status_code == 200:
            st.success("Document uploaded successfully.")
        else:
            st.error(response.text)

# -------------------------
# Ask Question
# -------------------------

st.header("💬 Ask Question")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question.strip():

        response = requests.post(
            f"{API_URL}/ask",
            json={
                "question": question
            }
        )

        if response.status_code == 200:

            data = response.json()

            st.subheader("Answer")

            st.write(data["answer"])

            st.subheader("Sources")

            for source in data["sources"]:
                st.write(f"• {source}")

        else:
            st.error(response.text)