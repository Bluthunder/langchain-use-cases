from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI

if __name__ == '__main__':
    load_dotenv()

    pdf_path = "C:\\Users\\KAUSHIK\\Downloads\\bellman.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    pdf_document = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="\n")
    docs = text_splitter.split_documents(documents=pdf_document)

    embeddings = OpenAIEmbeddings()
    print(embeddings[0])
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_bellman")

    new_vectorstore = FAISS.load_local("faiss_bellman", embeddings)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(),
                                     chain_type="stuff",
                                     retriever=new_vectorstore.as_retriever())

    res = qa.run("Tell us about mathematical formulations for bellman equation")

    print(res)
