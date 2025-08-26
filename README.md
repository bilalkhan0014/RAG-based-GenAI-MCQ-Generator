# RAG-based-GenAI-MCQ-Generator
This RAG based MCQ and short question generator is ideal for students, educators, and trainers who want to quickly create practice quizzes, assignments or revision material from study content . 

RAG-based GenAI MCQ Generator is an interactive application that automatically generates Multiple Choice Questions (MCQs) and Short Answer Questions from any uploaded GenAI-related PDF. It combines the power of Retrieval-Augmented Generation (RAG) with Azure OpenAI models to create relevant, content-based questions for learning and assessments.

🚀 Tech Stack

Azure OpenAI (GPT-4o) – for question generation
LangChain – for document processing & retrieval
FAISS – for efficient vector search and indexing
PyPDF2 – for PDF text extraction
Streamlit – for an interactive user interface

🎯 Features

Upload a GenAI-related PDF
Extracts text and creates a FAISS-based semantic index

Generates:

✅ 5 Multiple Choice Questions (MCQs) with 4 options and correct answers
✅ 5 Short Answer Questions based on document content

Displays results in a clean Streamlit dashboard
