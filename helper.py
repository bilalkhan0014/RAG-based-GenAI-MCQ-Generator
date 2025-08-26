import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai import AzureChatOpenAI

load_dotenv()
def load_pdf(file):
    pdf = PdfReader(file)
    return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def create_faiss_index(text):
    splitter = CharacterTextSplitter(chunk_size = 1000,chunk_overlap = 150)
    docs = splitter.create_documents([text])
    embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=os.getenv("EMBEDDING_OPENAI_ENDPOINT"),
    openai_api_key=os.getenv("EMBEDDING_OPENAI_API_KEY"),
    openai_api_version=os.getenv("EMBEDDING_OPENAI_API_VERSION"),
    azure_deployment=os.getenv("EMBEDDING_OPENAI_DEPLOYMENT_NAME"),
)
    return FAISS.from_documents(docs,embeddings)

def generate_qa(index):
    llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4o",
    temperature=0.3
)
    retriever = index.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm , retriever = retriever)

    mcq_prompt = "Generate 5 multiple-choice questions with 4 options each and clearly mention the correct answer. Base them only on the content."
    short_q_prompt = "Generate 5 short-answer questions based only on the content."

    mcqs = qa_chain.run(mcq_prompt)
    shorts = qa_chain.run(short_q_prompt)

    return mcqs,shorts
    
