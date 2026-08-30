import streamlit as st
from ingest import ingest_pdf
from services.rag_service import ask_question
import os

# -------------------------
# Session State
# -------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------
# Title
# -------------------------

st.title("📄 AI Document Assistant")

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.header("📚 Documents")

    pdf_folder = "data/pdfs"

    if os.path.exists(pdf_folder):

        pdf_files = [
            file
            for file in os.listdir(pdf_folder)
            if file.endswith(".pdf")
        ]

        if pdf_files:

            for file in pdf_files:
                st.write(f"✅ {file}")

        else:
            st.info("No documents ingested.")

# -------------------------
# PDF Upload Section
# -------------------------

uploaded_files = st.file_uploader(
    "Upload Your PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

ingest_button = st.button("Ingest Documents")

if uploaded_files and ingest_button:

    ingested_count = 0

    for uploaded_file in uploaded_files:

        save_path = os.path.join(
            "data/pdfs",
            uploaded_file.name
        )

        if os.path.exists(save_path):

            st.warning(
                f"{uploaded_file.name} already exists"
            )

        else:

            with st.spinner(
                f"Ingesting {uploaded_file.name}..."
            ):

                with open(save_path, "wb") as f:
                    f.write(
                        uploaded_file.getbuffer()
                    )

                ingest_pdf(save_path)

            ingested_count += 1

    if ingested_count > 0:

        st.success(
            f"{ingested_count} document(s) ingested successfully!"
        )
        st.rerun()

# -------------------------
# Question Section
# -------------------------

question = st.text_input(
    "Ask about your documents..."
)

ask_button = st.button("Ask")

if ask_button:

    if not question:

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner("Thinking..."):

            answer, sources = ask_question(
                question
            )

        st.session_state.chat_history.append(
            {
                "question": question,
                "answer": answer,
                "sources": sources
            }
        )

# -------------------------
# Chat History
# -------------------------

if st.session_state.chat_history:

    st.subheader("💬 Chat History")

    for chat in reversed(
        st.session_state.chat_history
    ):

        with st.chat_message("user"):
            st.write(
                chat["question"]
            )

        with st.chat_message("assistant"):
            st.write(
                chat["answer"]
            )

        st.markdown("**Sources:**")

        for source in chat["sources"]:

            st.write(
                f"- {source['source']} "
                f"(Chunk {source['chunk_number']})"
            )

        st.divider()