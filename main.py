import streamlit as st
from helper import load_pdf, create_faiss_index, generate_qa

st.title("RAG-based GenAI MCQ Generator")

pdf_file = st.file_uploader("Upload a GenAI-related PDF", type = ["pdf"])

if pdf_file:
    with st.spinner("Processing PDF..."):
        text = load_pdf(pdf_file)
        index = create_faiss_index(text)
        mcqs , shorts = generate_qa(index)

    st.subheader("Multiple Choice Questions")
    st.text_area("MCQs",mcqs,height=250)

    st.subheader("short Answer Questions")
    st.text_area("Short Answers", shorts,height = 250)

    
